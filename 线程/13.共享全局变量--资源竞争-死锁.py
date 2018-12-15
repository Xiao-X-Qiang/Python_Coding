import threading
g_num = 0
import time
mutex1 = threading.Lock()
mutex2 = threading.Lock()

def sum1(num):
    global g_num
    for i in range(num):
        mutex1.acquire()  # 上锁
        print('mutex1 locked')
        time.sleep(0.01)  # 延时，等待sum2线程上锁mutex2
        mutex2.acquire()
        print("mutex2 locked")
        g_num += 1
        mutex2.release()  # 解锁
        mutex1.release()  # 解锁
    print("sum1:g_num is :%d" % g_num)

def sum2(num):
    global g_num
    for i in range(num):
        mutex2.acquire()  # 上锁
        print("mutex2 locked")
        time.sleep(0.01)  # 延时，等待sum1线程上锁mutex1
        mutex1.acquire()
        print("mutex1 locked")
        g_num += 1
        mutex1.release()  # 解锁
        mutex2.release()  # 解锁
    print("sum2:g_num is :%d" % g_num)

def main():
    t1 = threading.Thread(target=sum1, args=(1000000,))
    t2 = threading.Thread(target=sum2, args=(1000000,))
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()