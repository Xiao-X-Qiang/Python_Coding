



import time

# 秒数-->2018-01-01 10：01：01
time.time() #秒数

time.localtime()    #struct_time
time.gmtime()   #struct_time

time.strftime('%Y-$m-%d %H:%M:%S',time.localtime())

#2018-01-01 10：01：01-->秒数

temp=time.strptime('2018-01-01 10:01:01','%Y-%m-%d %H:%M:%S')   #struct_time

time.mktime(temp)


