# -*- coding:utf-8 -*-
__author__ = 'yang_da'
__date__ = '2017/11/10 下午3:18'

from django import forms
from captcha.fields import CaptchaField

# from users.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=5)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u'验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


