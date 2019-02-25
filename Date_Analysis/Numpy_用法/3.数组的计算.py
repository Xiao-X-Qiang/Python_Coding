import numpy as np
import random


# 数组的计算
# 1.数组与数字的计算
# 数组中的每一个元素与数字进行相应的计算
x_1 = np.arange(24).reshape((2,4,3))
x_1_1 = x_1 + 3
print(x_1)
print("*"*10)
print(x_1_1)

x_1_2 = x_1 * 2
print(x_1)
print(x_1_2)

# 2.数组1与同型数组2的计算
# 数组1与同型数组2对应位置的元素进行相应的计算

x_2 = np.arange(24).reshape((2,3,4))
x_3 = np.arange(30,54).reshape((2,3,4))
x_4_1 = x_2 + x_3
x_4_2 = x_2 * x_3
x_4_3 = x_2 / x_3
print(x_4_3)

# 3.数组1与不同型数组2的计算
# 广播原则：如果两个数组的后缘维度(即从末尾开始算起的维度)的轴长度相符或其中一方的长度为1，则认为它们是广播兼容的。广播会在缺失和(或)长度为1的维度上进行

# 3.1 轴长度相符
x_5 = np.arange(24).reshape((3,4,2))
x_6 = np.arange(30,38).reshape((4,2))
x_7 = np.arange(2)
x_6_1 = x_5 - x_6   # 三维 - 二维  # x_5.shape = (3,4,2) x_6.shape = (4,2)  轴长度相符
x_7_1 = x_5 - x_7   # 三维 - 一维  # x_5.shape = (3,4,2) x_7.shape = (2,)  轴长度相符
print(x_6_1)
print("*"*20)
print(x_7_1)

# 3.2 其中一方的长度为1  x_8.shape = (4,1) x_5.shape = (3,4,2)  x_8的后缘维度的长度为1，axis=0的维度长度为4，与x_5相应的维度长度相符
x_8 = np.arange(4).reshape((4,1))
x_8_1 = x_5 - x_8
print("x_8_1:",x_8_1)





