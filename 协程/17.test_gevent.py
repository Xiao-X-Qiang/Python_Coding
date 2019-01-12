import gevent
import time
from gevent import monkey

monkey.patch_all()


def print1(num):
    pass


def main():
    ge_list = []

    for i in range(10):
        ge1 = gevent.spawn(print1, i)
        ge_list.append(ge1)

    print(ge_list)


if __name__ == "__main__":
    main()
