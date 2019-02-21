

import time

import threading

def main():

    g_list = [1,2,3]

    def test1(name):
        i = 0
        while True:
            time.sleep(1)
            print("test1",name)
            g_list = 2
            i += 1

    def test2():
        while True:
            time.sleep(1)
            print("test2")

    t1 = threading.Thread(target=test1,args=["11",])
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

    print(threading.enumerate())




if __name__ == '__main__':
    main()