

def main():
    num = (x for x in range(1, 2))  # (),而非[]表示一列表生成器
    for i in num:
        print(i)



if __name__ == "__main__":
    main()
