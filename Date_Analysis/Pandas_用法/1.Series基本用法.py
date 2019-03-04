import pandas as pd
import string

# 创建series:一维，带标签的数组
# 方式一：
# pd.Series(data,[index])
x_1 = pd.Series(range(20))

# 方式二：
x_2 = pd.Series([1,2,3,4],index=list("abcd"))   # 或 x_2 = pd.Series([1,2,3,4],list(range(30,34)))

# 方式三
# pd.Series(dict_data[)
# 索引即为字典的键
dict_temp = {"name":"xiaoxiong","age":26,"tel":"17623702666"}
dict_temp1 = dict(name = "xiong",age = 26, tel = "17623702666")
x_3 = pd.Series(dict_temp)
x_3_1 = pd.Series(dict_temp1)

# 注意：
# 当重新为变量指定其它索引时，如果索引存在，则取其值；如果索引不存在，则设其为Nan,数据类型为NaN
x_4 = pd.Series(x_3,index=["name",1,2,3])

# print(type(range(30,34)))

print(x_4)

# Series的索引和切片
# 可视其为字典，有两个索引：标签索引index,以及下标索引，0，1，2...
x_5 = pd.Series({string.ascii_uppercase[i]:i for i in range(10)})
print(x_5)

# 方式一：
print(x_5[4])  # 或 print(x_5["D"])
print(x_5[0:8:2])  # 选取连续的记录，类比于numpy中的切片
print(x_5[[0,3,6]])  # 选择第1、4、6三个不连续的记录
x_5[["A","H"]]  # 选择取第"A"、"H"两条记录

# 方式二：
# 可根据由键值判断的bool索引进行切片
print(x_5[x_5>6])

# 注意：
# 切片时：取单个值，传入下标索引或index;取多个值时，传入下标索引列表或者index列表
print(x_5[4])  # 或 print(x_5["D"])
print(x_5[0:8:2])  # 选取连续的记录，类比于numpy中的切片
print(x_5[[0,3,6]])  # 选择第1、4、6三个不连续的记录

# 如何知道数据的索引及其值呢?
# 键名：obj.index
# 键值：obj.values
print(x_5.index,x_5.values)

# Series对象本质上由两个数组组成：
# 一个数组构成对象的键(标签索引,下标索引)，一个数组构成对象的值(values),对应于键--->值

