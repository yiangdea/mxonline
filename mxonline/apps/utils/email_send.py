# -*- coding:utf-8 -*-
__author__ = 'yang_da'
__date__ = '2017/11/17 下午2:08'

from random import Random

from users.models import EmailVerifyRecord
from django.core.mail import send_mail
from mxonline.settings import EMAIL_FROM


def send_register_email(email, send_type="register"):
    send_code = random_mystr(16)

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕学在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(send_code)

        send_status = send_mail(subject=email_title,
                                message=email_body,
                                from_email=EMAIL_FROM,
                                recipient_list=[email])
        if send_status:
            email_record = EmailVerifyRecord()
            email_record.code = send_code
            email_record.email = email
            email_record.send_type = send_type
            email_record.save()
        else:
            # 没发出去
            pass
        return send_status

    elif send_type == "forget":
        email_title = "慕学在线网注册密码重置链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/reset/{0}".format(send_code)

        send_status = send_mail(subject=email_title,
                                message=email_body,
                                from_email=EMAIL_FROM,
                                recipient_list=[email])
        if send_status:
            email_record = EmailVerifyRecord()
            email_record.code = send_code
            email_record.email = email
            email_record.send_type = send_type
            email_record.save()
        else:
            # 没发出去
            pass
        return send_status


def random_mystr(randomlength=8):
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    length = len(chars) - 1
    random = Random()
    my_str = ''
    for index in range(randomlength):
        my_str += chars[random.randint(0, length)]
    return my_str

