


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