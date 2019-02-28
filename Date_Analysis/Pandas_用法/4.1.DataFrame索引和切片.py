import pandas as pd
import numpy as np
import string

# pandas索引和切片
# 取行或列
# pandas的有两种索引，行索引和列索引(其中，索引也分为字符索引和下标索引)
# 总共有以下几种：
# 1.obj.loc[] 标签索引  2.obj.iloc[] 下标索引  3.obj[:]或obj[""]  4.obj[bool] 布尔索引行
# 注意：定位数据时，可以以上方式直接获得，也可分步获得，即obj[xx][yy] 由obj[xx]获得行或列，再[yy]进一步获得列或行


# 1.按字符索引进行切片 obj.loc[]
# 1.1 取某行或某列
data = pd.DataFrame(np.arange(24).reshape((4,6)),index=list("abcd"),columns=list("ABCDEF"))

print(data.loc["a"])  # 取某行
print(data.loc[:,"W"])  # 取列

# 1.2 取连续的行或列
print(data.loc["a":,])
print(data.loc[:,"D":])

# 1.3 取不连续的行或列
print(data.loc[["a","d"],:])  # 取第a、d行
print(data.lco[:,["D","E"]])

# 1.4 取行和列的交叉点
print(data.loc[["a","c"],["D","E"]])  # 取第a、c行与第D、E列的交叉点


# 2.按下标索引进行切片 obj.iloc[]
# 2.1 取某行或某列
print(data.iloc[2,:])  # 取第3行
print(data.iloc[:,2])  # 取第3列

# 2.2 取连续的行或列
print(data.iloc[1:3])
print(data.iloc[:,2:4])

# 2.3 取不连续的行或列
print(data.iloc[[1,3]])  # 取第2、4行
print(data.iloc[:,[2,4]])  # 取第3、5列

# 2.4 取行和列的交叉点
print(data.iloc[[2,3],[3,5]])  # 取第3、4行与第4、6列的交叉点

# 3 直接对DataFrame对象切片
# 3.1.1 对于行切片，只能使用下标索引，且只能取连续的行
print(data[1:2])  # 取第2行
print(data[1:3])  # 取第2、3行

# 3.1.2 对于行切片，也能使用bool索引(pandas.Series类型,且行标签必须与数组一致)选取特定的行
data_2 = pd.DataFrame(np.arange(24).reshape((4,6)),index=list("abcd"),columns=list("ABCDEF"))
bool_index = pd.Series([False,True,True,False],index=list("abcd"))  # 选取第2、3行
print(data_2[bool_index])

# 3.2 对于列切片，只能据标签索引取单列
print(data["D"])

# 4.pandas的布尔索引
# 可参考 3.1.2 对于行切片...
# eg1.找到所有的使用超过800次数的狗的名字
data = pd.read_csv("./dogNames2.csv")
print(data[data["Count_AnimalName"]>800])

# eg2:找到所有的使用次数超过800次且名字字符串长度大于4的狗的名字
index_1 = (data["Row_Labels"].str.len()>4) & (data["Count_AnimalName"]>700)  # 两bool类型的Series对象相与操作
print(data[index_1])

# 数据的另类定位
data_2 = pd.DataFrame(np.arange(24).reshape((4,6)),index=list("abcd"),columns=list("ABCDEF"))
print(data_2["B"][2])  # 可表示为：DataFrame --> ndarray --> 索引


