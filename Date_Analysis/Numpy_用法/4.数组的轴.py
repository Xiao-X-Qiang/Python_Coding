import numpy as np
import random

# 对于数组形状的理解
# obj.shape指的数据在相应维度上的长度，len(obj.shape)表数据的维度，obj.ndim表数据的维度，numpy.ndim(obj)表数据的维度
# x_7.shape = (2,3,4) 其中 2 表示 x_7 在axis=0轴上的长度，相应3表示x_7在axis=1轴上的长度...

x_7 = np.arange(24).reshape((2, 3, 4))
print(x_7.shape)

# x_7[0][2] 表示axis=0上的第1个元素中的axis=1上的第3个元素
print(x_7[0][2])


# 轴 = 维度
# 维度：len(obj.shape)表数据的维度，obj.ndim表数据的维度，numpy.ndim(obj)表数据的维度
# 维度的长度：obj.shape指的数据在相应维度上的长度

x_8 = np.arange(24).reshape((2, 3, 4))
x_8_1 = x_8.sum(axis=0)  # 按数组的第一个维度相加  x_8.shape = (2,3,4) x_8_1.shape = (3,4)
print(x_8_1)

print("*"*20)
x_8_2 = x_8.sum(axis=1)  # 按数组的第二个维度相加
print(x_8_2)

x_8_3 = x_8[0][1][3]  # 第一维度(axis=0)的第1个[0]元素中的第二个维度(axis=1)的第2个[1]的元素中的第三个维度(axis=2)的第4个[3]元素
print(x_8_3)