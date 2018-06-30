


#发送邮件,每个邮箱有自己对应得邮箱服务器
#1.组装内容，email.mime.text
#2.发送邮件

#email里面的MIMEText 负责构造邮件
#邮件一般包含：邮件正文内容 from to subject cc抄送附件等信息

#smtplib: 负责发送邮件
#发送邮件一般需要：登录用户名/密码（一般授权密码)、邮件服务器、端口

#引入模块：
from email.mime.text import MIMEText
import smtplib

'''构造邮件内容
content：发送内容
from：发送方
to：收件方
usename：登录用户名
password：登录密码'''

#发送邮件
msg=MIMEText('小樱的测试报告','plain','utf-8')  #组装发送邮件内容
s=smtplib.SMTP_SSL('smtp.qq.com',465)    #指定发送邮件的服务器  SMTP_SSL表示邮箱有加密
s.login('327318711@qq.com','megkkwkwrtsjbhbb')  #登录邮箱
s.sendmail('327318711@qq.com','123816120@qq.com',msg.as_string())   #准备发送
s.quit()    #退出服务器

