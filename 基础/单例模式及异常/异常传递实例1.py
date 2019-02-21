
# 在异常传递过程中，哪一级对异常做了处理，则从当下继续执行
# 在本例中，test1()异常在test3()中做了处理，则从test3()继续执行

def test1():
    print('--1.1--')
    file(hello)
    print('--1.2--')

def test2():
    print('--2.1--')
    test1()
    print('--2.2--')

def test3():
    try:
        print('--3.1--')
        test1()
        print('--3.2--')
    except Exception as result:
        print('捕获了异常信息是：%s'%result)

test3()
print('hello,world')