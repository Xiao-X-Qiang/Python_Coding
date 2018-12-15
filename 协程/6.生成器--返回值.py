

def creat_num(all_num):
    a, b = 0, 1
    current_num = 0
    while  current_num < all_num:
        yield a
        a, b = b, a+b
        current_num += 1
    return "ok"


obj = creat_num(3)

while True:
    try:
        ret = next(obj)  # 当next()调用生成器时，直至yield方才暂停
        print(ret)       # 如其它条件结束(如本例中 current < all_num不满足)，就会抛出StopIteration异常
    except Exception as result:
        print(result.value)  # 当next()抛出StopIteration异常时，异常的value属性会得到返回值(如果需要的话)
        break
