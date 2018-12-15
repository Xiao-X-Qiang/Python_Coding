
import threading

g_num = 0

def sum1(num):
    global g_num
    for i in range(num):
        g_num += 1

def sum2(num):
    global g_num
    for i in range(num):
        g_num += 1

def main():
    t1 = threading.Thread(target=sum1, args=(1000000,))
    t2 = threading.Thread(target=sum2, args=(1000000,))

    t1.start()
    t2.start()

    print(g_num)

if __name__ == "__main__":
    main()