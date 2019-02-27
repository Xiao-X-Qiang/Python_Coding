import numpy as np
from matplotlib import pyplot as plt
import random

# numpy生成随机数

# np.random.rand(d1,d2...) 创建(d1,d2...)维度的均匀分布的随机数数组，浮点数，范围0-1
x_a = np.random.rand(2,20)

# np.random.randn(d1,d2...) 创建(d1,d2...)维度的标准正态分布的随机数数组，浮点数，标准正态分布：平均数：0，标准差：1
x_b = np.random.randn(2,20)

# np.random.randint(low,high,(shape)) 从[low,high)中随机选取shape维度的数组
x_c = np.random.randint(2,20,(3,4))

# np.random.uniform(low,high,(shape)) 从[low,high)中选取shape维度的符合均匀分布的数组
x_d = np.random.uniform(2,20,(3,5))

# np.random.normal(mean,std,(shape))  选取shape维度的均值是mean,标准差为std的符合正态分布的数组
x_e = np.random.normal(2,1,(2,20))

# np.random.seed(s) 随机数种子，s:种子值，可以通过设定相同的随机数种子生成相同的随机数

# 该种子值表示当第一次随机生成时数组随机，第二次再次生成时则会与第一次保持一致，
# 即s1、s2在程序执行一次过程中是不同的，但每次执行程序时，s1、s2生成的随机数与程序上次执行时生成的随机数则是相同
# 即设置随机种子数值后，程序内随机，程序间相同
np.random.seed(3)
s1 = np.random.rand(2,3)
s2 = np.random.rand(2,3)



