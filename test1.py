


def fas(num):
    a,b = 0,1
    current_num = 0
    while True:
        if current_num <num:
            current_num = yield a
            a,b = b,a+b
            current_num += 1
            print(current_num)
        else:
            print("over")
            break


def main():
    fa = fas(10)

    a = next(fa)
    print(a)

    fa.send(7)

if __name__ == '__main__':
    main()