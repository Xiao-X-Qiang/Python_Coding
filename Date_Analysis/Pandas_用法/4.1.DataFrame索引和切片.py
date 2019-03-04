import pandas as pd
import numpy as np
import string

# pandas索引和切片
# pandas的有两种索引，行索引和列索引(其中，行索引也分为标签索引和下标索引，列索引只有标签索引)
# 索引大致总共有以下几种：
# 1.obj.loc[] 标签索引,取行列(行标签索引不存在时方可使用下标索引)
# 2.obj.iloc[] 下标索引，取行列
# 3.obj[:]取行或obj[""]/obj[["",""]]取列
# 4.obj[bool] 布尔索引取行或列或特定的行列
# 注意：定位数据时，可以以上方式直接获得，也可分步获得，即obj[xx][yy] 由obj[xx]获得行或列，再[yy]进一步获得列或行


# 1.按标签索引进行切片 obj.loc[]，取行列
# 1.1 取某行或某列
data = pd.DataFrame(np.arange(24).reshape((4,6)),index=list("abcd"),columns=list("ABCDEF"))

print(data.loc["a",:])  # 取某行  或 print(data.loc["a"])
print(data.loc[:,"W"])  # 取列

# 1.2 取连续的行或列
print(data.loc["a":,])
print(data.loc[:,"D":])

# 1.3 取不连续的行或列
print(data.loc[["a","d"],:])  # 取第a、d行
print(data.lco[:,["D","E"]])

# 1.4 取行和列的交叉点
print(data.loc[["a","c"],["D","E"]])  # 取第a、c行与第D、E列的交叉点

# 1.5 注意：如果行没有标签索引时，可以使用下标索引取行；如果有标签索引，使用下标索引时会报错
data_1 = pd.DataFrame(np.arange(24).reshape((4,6)),columns=list("ABCDEF"))
print(data_1.loc[3,["A","E"]])

# 2.按下标索引进行切片 obj.iloc[]，取行列
# 2.1 取某行或某列
print(data.iloc[2,:])  # 取第3行 或 print(data.iloc[3])
print(data.iloc[:,2])  # 取第3列

# 2.2 取连续的行或列
print(data.iloc[1:3])
print(data.iloc[:,2:4])

# 2.3 取不连续的行或列
print(data.iloc[[1,3]])  # 取第2、4行
print(data.iloc[:,[2,4]])  # 取第3、5列

# 2.4 取行和列的交叉点
print(data.iloc[[2,3],[3,5]])  # 取第3、4行与第4、6列的交叉点

# 3 直接对DataFrame对象切片，取行或列
# 3.1 对于行切片，只能使用下标索引(即使有标签索引)，且只能取连续的行(bool索引可取不连续特定的行，参考4。pandas的布尔索引)
print(data[1:2])  # 取第2行
print(data[1:3])  # 取第2、3行

# 3.2 对于列切片，只能据标签索引取单列或多列
print(data["D"])  # 取第"D"列
print(data[["D","W"]])  # 取第"D","W"两列

# 4.pandas的布尔索引 -- 不必深究，了解即可
# 使用方法：正常切片，只是将行或列的选择索引替换为bool索引即可
# 4.1 bool索引取不连续的行  -- Series类型的bool索引表
# 使用bool索引(pandas.Series或DataFrame类型时,行索引或列索引名称必须与数组一致)选取特定的行
data_2 = pd.DataFrame(np.arange(24).reshape((4,6)),index=list("abcd"),columns=list("ABCDEF"))
print(data_2[pd.Series([False,True,True,False],index=list("abcd"))])  # 选取第2、3行，行选择时bool的行索引名称与数组一致

# 4.2 bool索引取不连续的列  -- Series类型的bool索引表
print(data_2.loc[:,pd.Series([True,False,True,False,False,False],index=list("ABCDEF"))])  # 取第1、3列，列选择时bool的列索引名称与数组一致

# 4.3 bool索引取特定的值  -- DataFrame类型的bool索引表
print(data_2[data_2<20])  # 取小于20的行列，行列选择时bool的行列索引名称与数组一致


# eg1.找到所有的使用超过800次数的狗的名字 -- bool索引取行
data = pd.read_csv("./dogNames2.csv")
print(data[data["Count_AnimalName"]>800])

# eg2:找到所有的使用次数超过800次且名字字符串长度大于4的狗的名字  -- bool索引取行，只是相与bool类型的真值
index_1 = (data["Row_Labels"].str.len()>4) & (data["Count_AnimalName"]>700)  # 两bool类型的Series对象相与操作
print(data[index_1])

# 数据的另类定位
data_2 = pd.DataFrame(np.arange(24).reshape((4,6)),index=list("abcd"),columns=list("ABCDEF"))
print(data_2["B"][2])  # 可表示为：DateFrame:data_2-->Series：data_2["B"]--> 再索引:data_2["B"].[2]


