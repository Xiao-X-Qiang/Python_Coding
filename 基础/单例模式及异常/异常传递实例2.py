def test1():
    try:
        print("1-1")
        file("hello")
        print("1-2")
    except:
        print("error test1")
    print("1-3")


def test2():
    print("2-1")
    test1()
    print("2-2")


def test3():
    print("3-1")
    try:
        test1()
    except:
        print("error")
    else:
        print("normal")
    print("3-2")

test3()
