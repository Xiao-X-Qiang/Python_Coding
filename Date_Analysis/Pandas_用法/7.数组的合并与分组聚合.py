import pandas as pd
import numpy as np


# 数组的合并
# 情形1：行合并：obj1.join(obj2)  默认情况下将行索引相同的数据合并在一起

t1 = pd.DataFrame(np.arange(12).reshape((2,6)),index=list("ab"),columns=list("ABCDEF"))
t2 = pd.DataFrame(np.arange(24).reshape((3,8)),index=list("rta"),columns=list("GHIJKLMN"))

# 行索引相同的合并，以t1为基准
print(t1.join(t2))

# 行索引相同的合并，以t2为基准
print(t2.join(t1))

# 情形2：列合并，obj1.merge(obj2,...) 按照指定的列将数据按照一定的方式进行合并
p1 = pd.DataFrame(np.ones((3,4)),index=list("ABC"),columns=list("MNOP"))
p1.loc[:,"O"] = ["a","b","c"]
print(p1)

p2 = pd.DataFrame(np.zeros((2,5)),index=list("AB"),columns=list("VWXYZ"))
p2.loc[:,"X"] = ["c","d"]
print(p2)

# 2.1 默认情况下，内连接
print(p1.merge(p2,left_on="O",right_on="X"))  # 列名不同时，使用left_on、right_on指定
print(p1.merge(p2,on="a"))  # 当列名相同时，直接使用on,默认内连接

# 2.2 外连接
print(p1.merge(p2,left_on="O",right_on="X",how="outer"))  # 外连接

# 2.3 左连接
print(p1.merge(p2,left_on="O",right_on="X",how="left"))  # 左连接

# 2.4 右连接
print(p1.merge(p2,left_on="O",right_on="X",how="right"))  # 右连接


# 数组的分组聚合
# 情形：现在我们有一组关于全球星巴克店铺的统计数据，如果我想知道美国的星巴克数量和中国的哪个多，或者我想知道中国每个省份星巴克的数量的情况，那么应该怎么办？
data_starbucks = pd.read_csv("./starbucks_store_worldwide.csv")
print(data_starbucks.info())
print(data_starbucks.head(1))



