

def main(num):
    a, b = 0, 1
    current_num = 0
    while True:
        if current_num < num:
            # print(a)
            yield a  # 函数体力有关键字yield，表示在执行该函数时，并非调用，而是创建一个生成器对象
            a, b = b, a+b  # 每次调用该对象时，但凡遇到yield关键字时，返回yield后变量，暂时程序；当再次调用该对象时，从此处继续执行
            current_num += 1
        else:
            raise StopIteration  # 遇到StopIteration异常时，for循环结束；自定义的迭代器或生成器时，注意程序的结束条件
        

if __name__ == "__main__":
    generator = main(10)  # 并非调用函数，而是创建一个生成器对象
    print(next(generator))  # 使用next()调用一次该生成器对象(可多次调用)，因为生成器也是迭代器的一种
    for i in generator:  # 生成器也是迭代器，也是可迭代的，也可以使用for进行循环遍历
        print(i)
