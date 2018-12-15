

class InputError(Exception):     #继承于异常基类 Exception
    def __init__(self,length,atleast):
        self.length=length
        self.atleast=atleast
        print(type(self))


try:
   raise InputError(1,2)   #raise 搜出异常


except EOFError:
    print('你输入了一个结束标记EOF')

except InputError as result:    #InputError 捕获的自定义异常，result(也为类,print(type(result))绑定到了错误的实例
    print('输入异常，当前的长度为：%s,长度至少应该为:%s'%(result.length,result.atleast))
    print(type(result))

