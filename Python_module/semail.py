#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText


def send_email(subject, content):
    _user = "user@qq.com"
    _pwd = "passwd"
    _to = "touser@qq.com"

    msg = MIMEText('<html><h1 style="text-align: center;">%s</h1></html>' % content, 'html', 'utf-8')
    msg["Subject"] = subject
    msg["From"] = _user
    msg["To"] = _to

    try:
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        return True
    except smtplib.SMTPException:
        return False
