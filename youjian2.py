import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
# from T221.webtest.UnittesT.report import *
from T221.webtest.UnittesT.report import *
import unittest
from HTMLTestRunner import HTMLTestRunner
import os
#============定义发送邮件============
def send_mail(file_new):
    smtpserver = "smtp.qq.com"      #发件服务器
    port = 465                      #端口
    sender = "479270940@qq.com"     #发送端
    psw = "zqlxhtndefkabged"        #密码/授权码
    receiver = "479270940@qq.com"   #接收端

    #=========编辑邮件内容=========
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    #定义发件人，收件人，和邮件标题
    msg = MIMEMultipart()
    msg["from"] = sender    #发件人
    msg["to"] = receiver    #收件人
    msg["subject"] = "自动化测试报告"  #主题

    #正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)    #挂起、固定？

    #附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test1_report.html"'  #定义附件名称
    msg.attach(att)     #挂起

    #=========发送邮件=========
    #连接服务器
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    #发送人登录自己的邮箱
    smtp.login(sender, psw)
    #开始发送邮箱
    smtp.sendmail(sender, receiver, msg.as_string())  #发送
    #关闭SMTP协议
    smtp.quit() #关闭


#----------------------------------------------------------------->>
# 测试套件，构建测试集
suite = unittest.TestSuite()
suite.addTest(Baidu('uest_search'))
# 我们要新建一个用于保存我们测试结果的文件，html
now = time.strftime("%Y-%m-%d-%H-%M-%S")
# 定义文件的名字
filename = './report/' + now + "_result.html"
print(filename)
file = open(filename, "wb")
# 执行我们的报告写入
runner = HTMLTestRunner(stream=file, title="百度搜索测试报告", description="用例执行情况:")
# stream：是指定测试报告文件
# title：指定报告的标题
# description:指定报告的副标题
# 执行我们测试用例
runner.run(suite)
time.sleep(3)
print(file.closed)
# 要进行关闭
file.close()
print(file.closed)
# 执行测试用例
lists = os.listdir('./report')
ff='./report/'+lists[-1]
print(ff)
send_mail(ff)