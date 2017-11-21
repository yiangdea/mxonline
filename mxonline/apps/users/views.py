# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm
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
        verify_record = EmailVerifyRecord.objects.get(code=active_code)
        if verify_record is not None:
            user = UserProfile.objects.get(email=verify_record.email)
            user.is_active = True
            user.save()

        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
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
