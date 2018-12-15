import time
from greenlet import greenlet


def work1():
    while True:
        print("---work1---")
        gr2.switch()
        print("---work1-switch---")
        time.sleep(1)


def work2():
    while True:
        print("---work2---")
        gr1.switch()
        print("---work2-switch---")
        time.sleep(1)


if __name__ == "__main__":
    gr1 = greenlet(work1)
    print(gr1)
    gr2 = greenlet(work2)
    gr1.switch()
