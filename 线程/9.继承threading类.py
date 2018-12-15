
import time
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(2):
            time.sleep(1)
            print("I'm"+self.name + "@" + str(i))


def main():
    for i in range(5):
        # 创建线程对象
        t1 = MyThread()
        # 线程开始执行
        t1.start()
        # 打印线程对象
        print(threading.enumerate())


if __name__ == "__main__":
    main()
