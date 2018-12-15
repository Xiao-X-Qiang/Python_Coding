import time


def main():
    g1 = work1()
    g2 = work2()
    while True:
        next(g1)
        next(g2)


def work1():
    while True:
        print("---work1---")
        yield
        time.sleep(3)


def work2():
    while True:
        print("---work2---")
        yield
        time.sleep(1)


if __name__ == "__main__":
    main()
