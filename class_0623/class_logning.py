

import logging
#日志级别   5级别
#debug        调试信息 级别最低
#info         详细信息：数据 进度等
#warning      警告信息
#error        错误信息
#critical     致命严重的错误



#创建一个日志收集器，确定日志的级别
logger=logging.Logger('xiaoxiao','DEBUG')  #级别要大写  'xiaoxiao'创建这个日志收集器的名字

#创建输出渠道 warning级别以上的信息 输出到控制台
ch=logging.StreamHandler()  #添加一个输出渠道，输出到控制台
ch.setLevel('DEBUG')        #输出渠道的级别
logger.addHandler(ch)        #指定日志收集器，，添加一个输出渠道

#创建一个TXT的输出渠道
fh = logging.FileHandler('test_logging.txt',encoding='utf-8')
fh.setLevel('DEBUG')
#输出日志格式  asctime日志时间，levelname日志级别，filename日志收集器的名字
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)   #（fh）追加输入渠道



#收集不同级别的日志，从低到高
logger.debug('duolala')
logger.info('heaven')
logger.warning('花花')
logger.error('华华，吃西瓜')
logger.critical('你很可爱')



#root logger收集日志 ,console headler 输出日志