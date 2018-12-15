#
# class Singleton(object):
#     __instance=None
#     __first_init=False
#
# #—__new__(cls,*args,**kwargs)方法用于创建实例对象（然后再进行实例的初始化，即__init__()）
#     def __new__(cls,*args,**kwargs):
#         print('---__new__---')
#         if not cls.__instance:
#             cls.__instance=object.__new__(cls)
#             print(cls.__instance)
#         return cls.__instance
#
#     def __init__(self):
#         print('---__init__---')
#         print(self)
#
# sing=Singleton()
# print(sing)
# print('===================')
# sing2=Singleton()
# print(sing2)


class Singleton(object):
    __instances=None

    @classmethod
    def __new__(self, *args, **kwargs):
        if not self.__instances:
            self.__instances=object.__new__(self)
        return self.__instances

    def __init__(self):
        pass


sing=Singleton()
print(sing)

sing2=Singleton()
print(sing2)

#
# class A(object):
#     __name='类属性'
#
#     @classmethod
#     def test(cls):
#         print(cls.__name)
#
#
# class B(A):
#     pass

#
# try:
#     file('hello.txt')
#
# except Exception as result:
#     print('hello,world')
#
# finally:
#     print('this is finally')



