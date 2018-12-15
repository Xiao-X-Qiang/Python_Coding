import multiprocessing
import os, time, random


def work(msg):
    time.sleep(1)
    t_start = time.time()
    print("%s 开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%.2f" % (t_stop - t_start))


def main():
   pool = multiprocessing.Pool(2)
   for i in range(5):
       pool.apply_async(work, (i, ))

   pool.close()
   #pool.join()
   print('执行结束')


if __name__ == "__main__":
    main()
