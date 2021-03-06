import numpy as np
import random

# 此索引和切片的局限性在于：必须是二维数组，切片过程可参考 obj[x][j][z] 轴进行理解

x_1 = np.arange(17*7).reshape((17,7))
x_1_1 = np.arange(12).reshape((3,4))
print(x_1)
# 取第5行
print(x_1[4])

# 取连续多行--取第10行至第13行
print(x_1[9:13])
# print(x_1[9:13,:])  # 等同于上式

# 也可使用bool索引进行选取
print(x_1_1[:,[True,False,True,False]])  # 选取x_1_1 的第1、3列；此种用法可结合bool索引快速选择，可参考10.numpy小实例2

# 取不连续的多行--取第10、12、14行
print(x_1[[9,11,13]])
# print(x_1[[9,11,13],:])  # 等同于上式，默认取所有列

# 取第3列
print(x_1[:,2])

# 取连续多列 -- 取第4列至第6列
print(x_1[:,3:6])

# 取不连续多列 -- 取第4、6列
print(x_1[:,[3,5]])

# 某行、某列的值  -- 取第4行、第6列
print(x_1[3,5])

# 取连续多行和连续多列的值 -- 取第3至6行、4至6列
print(x_1[2:6,3:6])

# 取多行、多列的交叉点  -- 取第3行4列、第5行7列
print(x_1[[2,4],[3,6]])  # x_1[行,列]

# 在连续取行(或列)时，也可加上步长
# 取第4至10行,步长为2，第3至6列
print(x_1[3:10:2,2:6])