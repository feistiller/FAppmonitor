# -*- coding: UTF-8 -*-
# 发送邮件的脚本，使用smtplib和configparser进行发送和配置的读取
# 使用m_Log记录活动日志
import smtplib
import email
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import configparser
import m_Log


class mail_send:
    def __init__(self, str):
        # 实例化属性
        self.str = str

    def send(self):
        # 读取配置
        cf = configparser.ConfigParser()
        cf.read('../Config/script_config.config')
        mailAccount = cf.get('MAIL', 'MAIL_ACCOUNT')
        password = cf.get('MAIL', 'MAIL_PASSWORD')
        server = cf.get('MAIL', 'SMTP_SERVER')
        receivers = 'uneedzf@outlook.com'  # 接收邮件，可设置为邮箱
        # 自定义的回复地址（暂时一致）
        replyto = receivers

        # 构建alternative结构
        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header('消息通知').encode()
        msg['From'] = '%s <%s>' % (Header('来自服务器').encode(), mailAccount)
        msg['To'] = receivers
        msg['Reply-to'] = replyto
        msg['Message-id'] = email.utils.make_msgid()
        msg['Date'] = email.utils.formatdate()

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # 构建alternative的text/plain部分
        textplain = MIMEText(self.str, _subtype='plain', _charset='UTF-8')
        msg.attach(textplain)
        # 构建alternative的text/html部分
        # texthtml = MIMEText('自定义HTML超文本部分', _subtype='html', _charset='UTF-8')
        # msg.attach(texthtml)

        # 写日志
        m_Log.logWrite('mail', 'mail_send', 'send:',
                       mailAccount + '-' + password + '-' + server + '-' + receivers)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(server, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mailAccount, password)
            smtpObj.sendmail(mailAccount, receivers, msg.as_string())
            smtpObj.quit()
            m_Log.logWrite('mail', 'mail_send', 'send:', "success")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
            m_Log.logWrite('mail', 'mail_send', 'send:', "error")
