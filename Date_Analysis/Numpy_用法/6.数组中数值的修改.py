import numpy as np
import random

# 1.第2、3行修改为4
x_1 = np.arange(4*6).reshape((4,6))
x_1[1:3,:] = 4
print(x_1)

# bool索引 -- 将小于10的数字替换为3
x_1 = np.arange(4*6).reshape((4,6))
x_1[x_1<3] = 3
print(x_1)

# 三元运算符 -- 将小于10的替换为0，大于10的替换为10
x_1 = np.arange(4*6).reshape((4,6))
x_1_1 = np.where(x_1<10,0,10)
print(x_1_1)

# clip() -- 将小于10的替换为10，大于18的替换为18
x_1 = np.arange(4*6).reshape((4,6))
x_2 = x_1.clip(10,18)
print(x_2)


