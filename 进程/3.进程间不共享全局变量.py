
import multiprocessing
import time
import os
g_nums = [11, 22]

def work1():
    """子进程执行的代码"""
    print("in process1 pid = %d,g_nums = %s" % (os.getpid(), str(g_nums)))
    for i in range(2):
        g_nums.append(i)
        time.sleep(1)
        print("in process1 pid = %d,g_nums = %s" % (os.getpid(), str(g_nums)))
def work2():
    """子进程2执行的代码"""
    print("in process1 pid = %d,g_nums = %s" % (os.getpid(), str(g_nums)))

def main():
    p1 = multiprocessing.Process(target=work1)
    p2 = multiprocessing.Process(target=work2)

    p1.start()
    p1.join()  # join()表示：等待p1子进程执行结束

    p2.start()  # p1子进程结束后，p2创建并执行

    g_nums.append(123)
    print("in process1 pid = %d,g_nums = %s" % (os.getpid(), str(g_nums)))

if __name__ == "__main__":
    main()
