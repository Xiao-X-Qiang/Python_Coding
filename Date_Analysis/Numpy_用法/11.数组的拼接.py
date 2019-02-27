import numpy as np
from matplotlib import pyplot as plt
import random

# 进行数据的拼接

# vertically adv.垂直地;直立地；
# horizontally adv.水平地；

x_a = np.arange(12).reshape((3,4))
x_b = np.arange(20,32).reshape((3,4))

# 1.数组的拼接
# 1.1 垂直拼接
x_v = np.vstack((x_a,x_b))
print(x_v)

# 1.2 水平拼接
x_h = np.hstack((x_a,x_b))
print(x_h)


# 2.数组的行列交换
x_a[[2,0],:] = x_a[[0,2],:]  # 交换x_a 的第1、3行
print(x_a)

x_b[:,[3,1]] = x_b[:,[1,3]]  # 交换x_b的第2、4列
print(x_b)

