

#1. 单纯装饰器，装饰函数japan()
def login(func):
    def inner():


        func()

    return inner

@login   #相当于 inner=japan=login(japan)
def japan():
    print("welcome Japan")



#japan =login(japan)
japan()

# ---------------
#2.装饰器，装饰函数japan(x,y,z),与上述不同在于inner的形参

def login(func):
    def inner(*args):


        func(*args)

    return inner


@login    #相当于 inner=japan=login(japan)
def japan(style):
    print('welcome japan',stype)


japan('Tokyo')

# ---------------
#3.装饰器，装饰函数japan(x,y,z),且login(login_style)自带参数


def login(auto_style):
    if auto_style=='qq':
        def outer(func):
            def inner(*args):
                func(*args)
        return outer


@login('qq')    #相当于outer=login1=login('qq'), inner=japan=login1(japan)
def japan(style):
    print('welcome japan',stype)


japan('Tokyo')  #与情形2不同的是，此时以qq的方式进行登录

