
import time
import threading


def sing():
    print("唱歌")
    time.sleep(1)


def dance():
    print("跳舞")
    time.sleep(1)


def main():
    # 创建线程对象
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    # 线程开始执行
    t1.start()
    t2.start()
    # 打印线程对象
    print(threading.enumerate())


if __name__ == "__main__":
    main()
