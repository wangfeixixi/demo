# 导入所需要的库

# send_user = "1020301980@qq.com"       # 发件人的邮箱账号
# send_pwd = "wfcp+250"        # 发件人邮箱的密码
# rec_user = "1020301980@qq.com"    #收件人邮箱
#
# def mail():
#     ret = True
#     try:
#         # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#         msg = MIMEText("这是测试邮箱发送内容！", "plain", "utf-8")
#         msg["From"] = formataddr(["FromSMTPQQ", send_user])  # 括号中对应发件人邮箱昵称、发件人邮箱账号
#         msg["To"] = formataddr(["RecSMTP"], rec_user)  # 括号中对应收件人邮箱昵称、收件人邮箱账号
#         msg["Subject"] = "这是邮件的主题"  # 邮件的主题或标题
#
#         server = smtplib.SMTP_SSL("SMTP.qq.com", 446)   # 括号中对应的是发件人邮箱中的SMTP服务器，端口
#         server.login(send_user, send_pwd)  # 括号中对应的是发件人邮箱账号和密码
#         server.sendmail(send_user, rec_user, msg.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()  # 关闭连接
#     except Exception as e:
#         print(e)
#         ret = False
#     return ret
#
# ret = mail()
# if ret:
#     print("邮件发送成功！")
# else:
#     print("邮件发送失败！")
from email.mime.text import MIMEText

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = "2274177609@qq.com"
password = "hngbopubpqxrebcf"
# 输入收件人地址:
to_addr = "Fei.Wang20@geely.com"
# 输入SMTP服务器地址:
smtp_server = "SMTP.qq.com"

import smtplib

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
