import threading
g_num = 0
mutex = threading.Lock()

def sum1(num):
    global g_num
    mutex.acquire()  # 上锁
    for i in range(num):
        g_num += 1
    mutex.release()  # 解锁
    print("sum1:g_num is :%d" % g_num)

def sum2(num):
    global g_num
    mutex.acquire()  # 上锁
    for i in range(num):
        g_num += 1
    mutex.release()  # 解锁
    print("sum2:g_num is :%d" % g_num)

def main():
    t1 = threading.Thread(target=sum1, args=(1000000,))
    t2 = threading.Thread(target=sum2, args=(1000000,))
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()