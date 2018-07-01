

#!-*- encoding:utf-8 -*-
import  os,sys
#1.作业：请写一个类 专门负责配置信息的读写
import os
import configparser
class Conf:

    def __init__(self,file_name,file_path = os.path.dirname(__file__)):
        #file_name :配置文件的名字
        #file_path:配置文件的路径，默认为当前路径上一级
        self.file_name=file_name
        self.file_path=file_path
        self.conf_path=self.file_path+'/'+self.file_name
        self.conf=configparser.ConfigParser()
        self.conf.read(self.conf_path)

    def read_conf(self,db_section,db_option):
        #读取配置文件，传入section，option，返回option中对应得value
        value = self.conf.get(db_section,db_option)
        return value
    def writer_conf(self,db_section,db_option,db_value):
        #新建section，插入option和对应得value
        #修改存在section的option
        #添加以前存在的section的option
        self.conf.add_section(db_section)
        self.conf.set(db_section,db_option,db_value)
        self.conf.write(open(self.conf_path,'w'))
if __name__ == '__main__':
    t=Conf('db.conf')
    print(t.read_conf('DATABASE','config'))
    t.writer_conf('TEST','host','192.168.1.118')

#2.写一个邮件类：请你把DDT测试用例执行完毕之后的HTML报告作为附件发给华华的邮箱： 204893985@qq.com

'''import smtplib
import HTMLTestRunnerNew
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class DoEmail():
    def __init__(self,subject,content,msg_from,msg_passwd,msg_to,file=None,msg_smtp="smtp.qq.com",msg_port=465):
        self.subject=subject  #主题
        self.content=content  #邮件正文的内容
        self.msg_smtp=msg_smtp #QQ邮箱服务器
        self.msg_port=msg_port #端口
        self.msg_from=msg_from #发送人
        self.msg_passwd=msg_passwd #授权码
        self.msg_to=msg_to  #接收人
        self.file=file

    def msg_email(self):
        #创建一个带附件的实例
        msg=MIMEMultipart()
        #创建附件，并获取当前目录下的文件
        if self.file:
            att = MIMEText(open(self.file,'rb').read(),_subtype='html',_charset='gb2312')
            att["Content-Type"] = 'application/octet-stream'
            #这里的filename可以任意写，写什么名字，邮件中显示什么名字，获取的是当前file的文件名
            att["Content-Disposition"] = 'attachment; filename="%s"'%self.file
            msg.attach(att)
            msg.attach(MIMEText(self.content))
            msg['Subject']=self.subject
            msg['From']=self.msg_from
            msg['To']=self.msg_to
            try:
                s=smtplib.SMTP_SSL(self.msg_smtp,self.msg_port)#指定发送邮件的服务器
                s.login(self.msg_from,self.msg_passwd)                  #登录邮箱
                s.sendmail(self.msg_from,self.msg_to,msg.as_string())   #准备发送邮件
                print("邮件发送成功")
            except Exception as e:
                print("邮件发送失败",e)
                raise e
            finally:
                s.quit()                #退出服务器

if __name__ == '__main__':
    send_email=DoEmail("小樱HTTP测试报告","接口测试","327318711@qq.com","yciajonxfasmbhee","204893985@qq.com",file='home_work2018-06-26_01_13_50.html')
    send_email.msg_email()'''
