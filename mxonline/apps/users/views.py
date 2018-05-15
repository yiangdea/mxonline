# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from utils.email_send import send_register_email


# authenticate custom
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user

        except Exception as e:
            return None


class ActiveUserView(View):

    def get(self, request, active_code):
        record_list = EmailVerifyRecord.objects.filter(code=active_code)
        if record_list:
            for rc in record_list:
                user = UserProfile.objects.get(email=rc.email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'msg': u'email已被注册',
                                                         'register_form': register_form})
            user_password = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(user_password)
            user_profile.is_active = False
            user_profile.save()
            
            send_register_email(email=user_name, send_type='register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, 'login.html', {"msg": "用户尚未激活"})
            else:
                return render(request, 'login.html', {"msg": "用户名或密码错误!"})
        else:
            return render(request, 'login.html', {"login_form":login_form})


class ForgetPwdView(View):
    def get(self, request):
        forgetForm = ForgetPwdForm()
        return render(request, "forgetpwd.html", {"forget_form": forgetForm})

    def post(self, request):
        form = ForgetPwdForm(request.POST)
        if form.is_valid():
            email = request.POST.get("email", "")
            send_status = send_register_email(email=email, send_type='forget')
            if send_status:
                return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': form})


class ResetView(View):
    def get(self, request, active_code):
        record_list = EmailVerifyRecord.objects.filter(code=active_code)
        if record_list:
            for rc in record_list:
                return render(request, 'password_reset.html', {"email": rc.email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", '')
            pwd2 = request.POST.get("password2", '')
            email = request.POST.get("email", '')
            if pwd1 == pwd2:
                user_records = UserProfile.objects.filter(email=email)
                if user_records:
                    for user in user_records:
                        user.password = make_password(pwd1)
                        user.save()
                    return render(request, 'login.html')
                else:
                    return render(request, 'password_reset.html', {'email': email,
                                                                   'msg': '账户不存在'})
            else:
                return render(request, 'password_reset.html', {'email': email,
                                                               'msg': '密码不一致'})
        else:
            return render(request, 'password_reset.html', {'modify_form': modify_form})




