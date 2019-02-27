import numpy as np
import random

# 1.第2、3行修改为4
x_1 = np.arange(4*6).reshape((4,6))
x_1[1:3,:] = 4
print(x_1)

# bool索引 -- 将小于10的数字替换为3
# 通过bool索引修改数组中的数据后得到的数组，与原始数组引用的是同一地址，即是同一个对象
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

# numpy中数据的修改时：
# 1.a = b 引用数据时， 当修改引用a时，引用b也会受影响

# 2.a = b[:,1] 形式时，a是对数据b[:,1]的引用，类似于情形1

# 3.a = b.copy() 时，a与b可看作是浅拷贝的关系，相互间不受影响
