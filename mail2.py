# -*- coding = utf-8 -*-
# @time=2021/2/10 0:39
# @file mail2.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def mail(status):
    from_addr = '1305743207@qq.com'

    password = 'skozeqkfphuobafb'

    to_addr = 'nthqn@sina.com'

    smtp_server = 'smtp.qq.com'

    msg = MIMEText(status, 'plain', 'utf-8')

    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('每日疫情填报情况')

    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, 465)

    server.login(from_addr, password)

    server.sendmail(from_addr, to_addr, msg.as_string())

    server.quit()


