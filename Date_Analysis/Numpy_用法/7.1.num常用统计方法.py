import numpy as np
import random

# numpy中常用的统计函数
# 如果不指定axis参数，则默认为None,在整个维度上求值
x_4 = np.arange(24).reshape((4,6))
# 求和 obj.sum(axis=None) 或 np.sum(obj,axis=None)
x_4_1 = x_4.sum(axis=0)
x_4_2 = np.sum(x_4,axis=1)
print(x_4_1,x_4_2)

# 均值 obj.mean(axis=None) 或 np.mean(obj,axis=None)
x_4_1 = x_4.mean(axis=0)
x_4_2 = np.mean(x_4,axis=1)
print(x_4_1,x_4_2)

# 中值 np.median(obj,axis=None)
x_4_1 = np.median(x_4,axis=0)
print(x_4_1)

# 最大值、最小值 obj.max(axis=None) 或 np.max(obj,axis=None) obj.min(axis=None) 或 np.min(obj,axis=None)
x_4_1 = x_4.max(axis=0)
x_4_2 = np.max(x_4,axis=1)
print(x_4_1,x_4_2)

# 极值 obj.ptp(axis=None) 或 np.ptp(obj,axis=None)
x_4_1 = x_4.ptp(axis=0)
x_4_2 = np.ptp(x_4,axis=1)
print(x_4_1,x_4_2)

# 标准差 obj.std(axis=None) 或 np.std(obj,axis=None)
x_4_1 = x_4.std(axis=0)
x_4_2 = np.std(x_4,axis=1)
print(x_4_1,x_4_2)