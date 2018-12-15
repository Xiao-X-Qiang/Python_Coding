

def creat_num(all_num):
    a, b = 0, 1
    current_num = 0
    while  current_num < all_num:
        ret3 = yield a
        print("ret3:", ret3)
        a, b = b, a+b
        current_num += 1


obj = creat_num(4)  # 创建生成器对象

ret1 = next(obj)
print("ret1:", ret1)

ret2 = obj.send("hello,world")  # obj.send([None|msg]):唤醒obj生成器对象，类似于next(obj)，但不同的是同时传递了参数
print("ret2:", ret2)