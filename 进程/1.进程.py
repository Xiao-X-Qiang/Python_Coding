
import multiprocessing
import time


def hello(name, age, **kwargs):
    while True:
        time.sleep(1)
        print(name, age, kwargs)


def main():

    p1 = multiprocessing.Process(target=hello, args=("xiaoming", 12), kwargs={"m": 30})  # 创建子进程对象
    p1.start()  # 创建子进程并运行
    while True:
        time.sleep(1)
        print("--main--")


if __name__ == "__main__":
    main()
