import numpy as np
import random

# 创建数组,并指定数据类型(可默认，int64),三种
x_1 = np.array([i for i in range(10)], dtype=np.int8)  # 或 dtype="int8" 或 dtype="i1"
x_2 = np.array(range(0, 10, 2))
x_3 = np.arange(10)

print(x_1, x_1.dtype)
print(x_2, x_2.dtype)
print(x_3, x_3.dtype)

# 创建特定类型的数组
x_a = np.zeros((3,4))  # 创建(3,4)型的全0数组
x_b = np.ones((2,3))  # 创建(2,3)型的全1数组
x_c = np.eye(3)  # 创建对角线全1的方阵
print(x_a,x_b,x_c)

# 获取索引的位置
# 获取最大值或最小值的索引位置,如果有相同的值，取索引较小的值
max_index = np.argmax(x_c,axis=0)
min_index = np.argmin(x_c,axis=1)
print(max_index,min_index)

# 修改数据类型
x_1_1 = x_1.astype(dtype=np.int16)
print(x_1_1, x_1_1.dtype)


# 修改浮点型的小数位数
# obj.round(num) 或 np.round(obj,num)
f_1 = [random.random() for i in range(10)]
f_1_1 = np.array(f_1)
f_1_1 = f_1_1.round(2)  # 方式一
f_1_2 = np.round(f_1_1,2)  # 方式二
print(f_1_1)

