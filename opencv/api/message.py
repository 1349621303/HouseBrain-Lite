# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMe(file):

    # 服务器地址
    smtpserver = 'smtp.163.com'
    # 发送账号
    user = '17742566640@163.com'
    # 发送密码
    password = '18774370611'
    # 收件人
    receivers  = '2892211452@qq.com'
    # 邮件标题
    subject = '宿舍卫生问题，请您查验'
    # 获取附件信息
    with open('name.txt','rb',)as f:
        body = f.read().decode()
    message = MIMEMultipart()
    # 发送地址
    message['From'] = user
    # 接受地址
    message['To'] =  receivers
    # 邮件标题
    message['subject'] =subject
    # 正文内容
    body = MIMEText(body, 'html', 'utf-8')
    message.attach(body)
    # 传当前目录中的name.txt文件
    att = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'    # 死格式
    # filename 表示附件的名称
    att["Content-Disposition"] = 'attachment; filename="name.txt"'
    message.attach(att)
    smtp = smtplib.SMTP()
    # 连接服务器
    smtp.connect(smtpserver)
    # 登录邮箱账号
    smtp.login(user,password)
    # 发送账号信息
    smtp.sendmail(user,receivers,message.as_string())
    # 关闭
    smtp.quit()

if __name__ =="__main__":
    sendMe()
