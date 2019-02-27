import numpy as np
import random

# nan
# 何时出现nan?
# 1.读取本地文件为float时，如有缺失，默认填充nan
# 2.不合适的计算时，如无穷大-无穷大，0/0等情况下

# inf  (包括 inf :正无穷大  -inf :负无穷大 )
# 何时出现inf?
# 1.不合适的计算时，如某数字/0 时，python中直接报错，numpy中显示inf或-inf

x_1 = np.arange(6).reshape((2,3))
x_2 = np.array([0,1,2,3,0,4]).reshape(2,3)

# x_2_1 = x_1 / x_2
# print(x_2_1)

# nan和inf是float数据类型(numpy中)，当一个数组为float型时可添加或修改为nan或inf
# 添加np.nan 或 np.inf

x_3 = np.array([1,2,3,np.nan,np.inf],dtype=float)
print(x_3)

# numpy中的nan注意点：
# 1.两个nan是不相等的,利用此特性，可判断数组中nan的个数
# 1.1 两个nan是不相等的
print(np.nan == np.nan)  # 两个nan不相等

# 1.2 判断数组中nan的个数
# np.count_nonzero()
nan_num = np.count_nonzero(x_3 != x_3)
print(nan_num)

# 或 np.isnan(x_3)判断返回 bool类型
nan_bool = np.isnan(x_3)  # 效果等同于 x_3 != x_3
print(np.count_nonzero(nan_bool))

# 2.nan和任何值计算都为nan
print(np.sum(x_3,0))

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

# 在一组数据中是否可简单地把nan替换为0？
# 一般不可以：替换为0后，替换后的数据的平均值将会变小，一般将其替换为均值(或中值)，或者删除有缺失值的一行记录

# 1.将每一列中的nan替换为该列的均值或中值
x_5 = np.arange(15).reshape((3,5)).astype(np.float)
x_5[2,3:] = np.nan
print(x_5)


def fill_mean_nan(x):
    """
    判断数组中是否有nan,如有，则将当前列中的nan替换为当前列的均值
    :param x: 数组
    :return: 替换nan后的数组
    注意：通过bool索引修改数组中的数据后得到的数组，与原始数组引用的是同一地址，即是同一个对象
    """
    num_col = x.shape[1]
    for i in range(num_col):
        temp = x[:,i]  # 当前的某列
        num_nan = np.count_nonzero(temp != temp)  # 当前列中nan的个数
        if num_nan != 0:  # 当前列中有nan
            temp_no_nan_mean = temp[temp == temp].mean()  # 当前列中非nan的均值
            temp[temp != temp] = temp_no_nan_mean
    return x


print(fill_mean_nan(x_5))
