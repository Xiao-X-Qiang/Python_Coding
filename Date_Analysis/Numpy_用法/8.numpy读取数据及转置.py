import numpy as np
import random

# 1.数据读取
# np.loadtxt(fname,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False) 其中：
# fname:文件、字符串或产生器，可以是.gz或bz2压缩文件
# dtype:数据类型，可选；csv的字符串以何种数据类型读入数组中，默认np.float
# delimiter:分隔字符串，默认是任何空格
# skiprows:跳过前N行，一般跳过第一行表头
# usecols:读取指定的列、索引、元组类型
# unpack:默认false,按行读入数组中；true时，转置后写入数组中
data = np.loadtxt(fname="./youtube.csv",dtype=float,delimiter=",",usecols=(1,2,4),unpack=True)
print(data)
print(data.shape)
print(type(data))  # numpy.ndarray类型

# 2.数组的转置,3种方式
data = np.arange(12).reshape((3,4))
print(data)
# 2.1 方式一：
data_1 = data.transpose()
print(data_1)

# 2.2 方式二：
data_2 = data.T
print(data_2)

# 2.3 方式三：
data_3 = data.swapaxes(1,0)
print(data_3)

# axis的复数axes