

#6-23： 编写一个 属于你自己的日志类，并完成实例调用
#要求如下：
#1：输出格式formatter可配置
#2: 输出到控制台还是文件：可配置
#3：输出级别可配置
#4：输出的文件地址：可配置
import logging
import configparser
class MyLog:
    def __init__(self,config_name):
        cf=configparser.ConfigParser()
        cf.read(config_name,encoding='utf-8')
        self.logger_name = cf.get('LOGCONFIG','logger_name')
        self.logger_level = cf.get('LOGCONFIG','logger_level')
        self.formatter = cf.get('LOGCONFIG','formatter')
        self.formatter_path = cf.get('LOGCONFIG','formatter_path')
        self.state = cf.get('LOGCONFIG','state')

    def log_conf(self):
        mylogger = logging.Logger(self.logger_name,level=self.logger_level)

        try:
            if int(self.state)==1:          #state==1输出到控制台
                mylogger.addHandler(self.log_stream())
            elif int(self.state)==2:    #state==2输出到file文件
                mylogger.addHandler(self.log_file())
            elif int(self.state)==3:    #state==3输出到控制台和file文件
                mylogger.addHandler(self.log_stream())
                mylogger.addHandler(self.log_file())
            else:
                mylogger.warning('没有找到指定的输出类型！')
            return mylogger
        except Exception as e:
            mylogger.exception('错误是：%s'%e)
            raise e


    def log_stream(self):    #输出到控制台
        stream = logging.StreamHandler()
        stream.setLevel(self.logger_level)
        stream.setFormatter(logging.Formatter(self.formatter))
        return stream

    def log_file(self):       #输出到file文件
        file_1 = logging.FileHandler(self.formatter_path,encoding='utf-8')
        file_1.setLevel(self.logger_level)
        file_1.setFormatter(logging.Formatter(self.formatter))
        return file_1

if __name__ == '__main__':
    mylog=MyLog('logger.conf').log_conf()
    mylog.debug('debug调试信息 级别最低')
    mylog.info('info详细信息：数据 进度等')
    mylog.warning('warning警告信息')
    mylog.error('error错误信息')
    mylog.critical('critical致命严重的错误')