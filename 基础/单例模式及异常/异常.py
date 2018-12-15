

try:
    file('hello.txt')       #可能出现异常的语句

except Exception as result: #捕获的异常及其处理方式：1.单个异常 NameError 2 多个异常 (NameError,FileError)
    print(result)           # 3.所有的异常 Exception  4.保存异常  as variable

else:   # try 语句正常执行结束时执行(只要有异常，无论是否被捕获处理，此时都不会执行)
    print('--else--')

finally:
    print('--finally--')  #任何情况下都会被执行