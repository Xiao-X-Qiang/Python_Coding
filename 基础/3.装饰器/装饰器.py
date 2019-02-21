# 1.单纯装饰器，装饰函数baidu()
def login(func):
    def inner():
        print("this is inner")
        func()

    return inner


@login  # inner = baidu = login(baidu)  默认已经执行到此
def baidu():
    print("baidu welcome")


# ****************************


# 2.进阶装饰器，装饰函数tencent(x,y)，与上述不同之处在于inner()的形参 -- 因为tencent()带有形参

def login1(func):
    def inner(*args):
        print("this is inner")
        func(args[0], args[1])

    return inner


@login1  # 相当于 inner = tencent = login1(tencent)  默认已经执行到此
def tencent(x, y):
    print("tencent welcome:", x, y)


# ****************************

# 3.装饰器，装饰函数alibaba(x),且login2(auto_type)自带参数

def login2(auto_type):
    if auto_type == "QQ":
        def outer(func):
            print("this is outer")

            def inner(*args):
                print("this is inner")
                func(args[0])

            return inner

        return outer


@login2("QQ")  # 相当于 outer = login2 = login2(QQ), inner = alibaba = login2(alibaba)  默认已经执行到此,故而控制台才会输出 this is outer
def alibaba(x):
    print("alibaba welcome ", x)


# 情形1
print("*" * 10)
baidu()
print("*" * 10)
# 情形2

tencent(11, 22)
print("*" * 10)
# 情形3
alibaba("qiang")
print("*" * 10)
