import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def sendString(MyMail):
    ret = True
    mail = MyMail
    try:
        # 输入Email地址和口令:
        from_addr = "2274177609@qq.com"
        password = "hngbopubpqxrebcf"
        # 输入收件人地址:
        # to_addr = "Fei.Wang20@geely.com"

        to_addr = mail.mail_add
        # 输入SMTP服务器地址:
        smtp_server = "SMTP.qq.com"

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        msg = MIMEText(mail.content, "plain", "utf-8")
        msg["From"] = formataddr(["日志系统", from_addr])  # 括号中对应发件人邮箱昵称、发件人邮箱账号
        msg["To"] = formataddr([mail.name, to_addr])  # 括号中对应收件人邮箱昵称、收件人邮箱账号
        msg["Subject"] = "日志系统警告"  # 邮件的主题或标题

        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
    except Exception as e:
        ret = False
        print(e)
    return ret


class MyMail:
    def __init__(self, name, mail_add, content):
        self.name = name
        self.mail_add = mail_add
        self.content = content


# mail = MyMail("bug工程师", "1020301980@qq.com", "加班吧，你的项目出问题了")
mail = MyMail("bug工程师", "Fei.Wang20@geely.com", "尊敬的bug工程师，你的项目出问题了")
string = sendString(mail)
print(string)
