

import logging
#日志级别
#debug        调试信息 级别最低
#info         详细信息：数据 进度等
#warning      警告信息
#error        错误信息
#critical     致命严重的错误


formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
fh.setFormatter(formatter)
logger.addHandlerRef(fh)
#创建一个日志收集器
logger=logging.Logger('duolal','DEBUG')  #级别要大写
#收集不同级别的日志，从低到高
logger.debug('duolala')
logger.info('heaven')
logger.warning('花花')
logger.error('华华，吃西瓜')
logger.critical('你很可爱')