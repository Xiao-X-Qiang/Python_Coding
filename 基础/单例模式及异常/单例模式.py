
class Singleton(object):

    __instance=None
    __first_init=False

# __new__ (cls,*args,**kwargs)方法用于创建实例对象(然后进行实例的初始化，即__init__() )

    def __new__(cls, *args, **kwargs):
        print('--__new__()--')
        if not cls.__instance:
            cls.__instance=object.__new__(cls)
            print(cls.__instance)
        return cls.__instance

    def __init__(self):
        print('--__init()__--')
        print(self)


a=Singleton()
print(a)