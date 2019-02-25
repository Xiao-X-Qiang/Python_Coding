import numpy as np
import random


# 数组的形状
# 1.查看数组的形状
x_4 = np.array([i for i in range(10)])
print(x_4.shape)  # 元组长度为1，表示为一维数组
x_5 = np.array([[1,2,3],[4,5,6]])
print(x_5.shape)  # 元组长度为2，表示为二维数组
x_6 = np.array([[[1,2,3,4],[4,5,6,7]],[[7,8,9,10],[10,11,12,13]]])
print(x_6.shape)  # 元组长度为3，表示为三维数组


# 2.改变数组的形状
x_4_1 = x_4.reshape((2,5))  # 一维变二维，reshape((x,y)) 参数(x,y) 元组，x*y == 数据个数
print(x_4_1)
x_5_1 = x_5.reshape((6,))  # 二维变一维，reshape((x,))  参数(x,) 元组，其长度为1
x_5_2 = x_5.flatten()  # 二维变一维
print(x_5_1,x_5_2)
x_6_1 = x_6.reshape((2,8)) # 三维变二维
x_6_2 = x_5.reshape((2,3,1)) # 二维变三维
print(x_6_1,x_6_2)


# 对于数组形状的理解
# obj.shape指的数据在相应维度上的长度，len(obj.shape)表数据的维度，obj.ndim表数据的维度，numpy.ndim(obj)表数据的维度
# x_7.shape = (2,3,4) 其中 2 表示 x_7 在axis=0轴上的长度，相应3表示x_7在axis=1轴上的长度...

x_7 = np.arange(24).reshape((2,3,4))
print(x_7.shape)

# x_7[0][2] 表示axis=0上的第1个元素中的axis=1上的第3个元素
print(x_7[0][2])
