

import logging
from logging import handlers


# 过滤filter
class IgnorBackupLogFilter(logging.Filter):
    #'忽略带db backup的日志'
    def filter(self, record): #固定写法
        return 'db backup' not in record.getMessage()

#1.生成logger对象
logger=logging.getLogger('chat.gui')
logger.setLevel(logging.INFO)

#1.1 把filter对象绑定到logger对象
logger.addFilter(IgnorBackupLogFilter())

#2.生成Handler对象
ch=logging.StreamHandler()

#fh=logging.FileHandler('web.log')
fh=handlers.RotatingFileHandler('web.log',maxBytes=10,backupCount=3)

#2.1 handler对象绑定对logger对象

logger.addHandler(ch)
logger.addHandler(fh)

#3.生成formatter对象

file_formatter=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
console_formatter= logging.Formatter('%(asctime)s-%(name)s-%(lineno)s-%(levelname)s-%(message)s')
#3.1 formatter对象绑定hander对象

ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

logger.warning('this is waring')
logger.error('this is error db backup')

#全局的默认lever为warning
#如果logger设置lever，Handler设置lever,先logger过滤，后handler过滤(类似于先loogger发送至handler对象)



