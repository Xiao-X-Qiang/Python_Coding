

import numpy as np
import pandas as pd

data_sbuck = pd.read_csv("./starbucks_store_worldwide.csv")
print(data_sbuck.info())
print(data_sbuck.head(1))

# 分组，pandas中数据(DataFrame)根据列名(str)直接分组返回可迭代对象DataFrameGroupBy：每一个元素是一个元组(索引(分组的值),分组后的DataFrame)
# DataFrameGroupBy对象可以：1.可以进行遍历 2.调用聚合方法，如count,sum,mean,median,std,var,min,max

# 1.遍历
grouped = data_sbuck.groupby(by="Country")  # DataFrameGroupBy类型
for i,j in grouped:
    print(i,type(i))
    print("-"*100)
    print(j,type(j))
    print("*"*100)


# 2.聚合
# grouped  # DataFrameGroupBy类型
# grouped.count()  # DataFrame类型
# grouped["Brand"]  # SeriesGroupBy类型
# grouped["Brand"].count()  # Series类型

country_count = grouped["Brand"].count() # Series类型

# 星巴克在美国和中国的数量
print(country_count[["CN","US"]])  # Series切片

# 星巴克在中国各省份的数量又是如何呢？先国家分再按省份分组
china_data = data_sbuck[data_sbuck["Country"] == "CN"]
grouped1 = china_data.groupby(by="State/Province").count()["Brand"]  # DataFrameGroupBy-->DataFrame-->Series
grouped1_ = china_data.groupby(by="State/Province").count()[["Brand"]]  # DataFrameGroupBy-->DataFrame-->DataFrame
grouped2 = china_data.groupby(by="State/Province")["Brand"].count()  # DataFrameGroupBy-->SeriesGroupBy-->Series
print(grouped1,type(grouped1))


# 索引和复合索引

# 按国家和省份同时分组,且返回DataFrame类型
# obj.[""]-->Series 与 obj.[[""]]-->DataFrame 注意区分
# DataFrame-->DataFrameGroupBy-->DataFrame
grouped_1 = data_sbuck[["Brand"]].groupby(by=[data_sbuck["Country"],data_sbuck["State/Province"]]).count()
# Series-->SeriesGroupBy-->Series
grouped_2 = data_sbuck["Brand"].groupby(by=[data_sbuck["Country"],data_sbuck["State/Province"]]).count()
# DataFrameGroupBy-->DataFrame-->DataFrame
grouped_3 = data_sbuck.groupby(by=[data_sbuck["Country"],data_sbuck["State/Province"]]).count()[["Brand"]]
# DataFrameGroupBy-->DataFrameGroupBy-->DataFrame
grouped_4 = data_sbuck.groupby(by=[data_sbuck["Country"],data_sbuck["State/Province"]])[["Brand"]].count()

# 与之前使用一个分组的条件相比，当前的返回结果的前两列是什么呢?  是索引，两个索引即复合索引
# 复合索引的操作有：
# 获取index: obj.index
# 指定index: obj.index = ["x","y"]
# 指定某列作为index：obj.set_index("x",drop=False)  将obj的x列作为标签索引，且x列不从当前数组中删除(drop=False)--默认会删除x(drop=True)
# 返回index的唯一值：obj.index.unique()

# 1.Series复合索引
a = pd.DataFrame({'a': range(7),'b': range(7, 0, -1),'c': ['one','one','one','two','two','two', 'two'],'d': list("hjklmno")})
# 1.1 指定列为其索引
a_1 = a.set_index(["c","d"])["a"]  # Series类型，其中标签索引c在前，d在后
print(a_1)  # a:DateFrame,a_1:Series

# 1.2 根据索引值取值
print(a_1.loc["one"]["j"])  # Series复合索引中，先取"one"索引(Series类型)，再取"j"索引
print(a_1["one","j"])  # 等同于上式，同时引用复合标签索引

# 1.3 当Series是如下形式(Series类型--无列标签)时，只想取one标签索引下的值时，如何呢？  交换复合索引obj.swaplevel()
# d  c
# h  one    0
# j  one    1
# k  one    2
# l  two    3
# m  two    4
# n  two    5
# o  two    6

# level:复合索引的层次关系 obj.index.levels
a_2 = a.set_index(["d","c"])["a"]  # Series类型，其中标签索引d在前，c在后
print(a_2.swaplevel()["one"])  # 交换复合索引的位置后，取标签索引"one"

# 2.DataFrame复合索引
a = pd.DataFrame({'a': range(7),'b': range(7, 0, -1),'c': ['one','one','one','two','two','two', 'two'],'d': list("hjklmno")})
# 2.1 指定列为其索引
a_1 = a.set_index(["c","d"])[["a"]]  # DataFrame类型，其中标签索引c在前，d在后
print(a_1)  # a:DateFrame,a_1:DataFrame

# 2.2 根据索引值取值
print(a_1.loc["one"].loc["h"])  # a:DateFrame,a_1:DataFrame,a_1.loc["one"]:DataFrame

# 2.3 与Series类似，当数组是如下形式(DataFrame类型——有列标签)时，只想取one标签下的值时，如何呢？  交换复合索引obj.swaplevel()
#        a
# d c
# h one  0
# j one  1
# k one  2
# l two  3
# m two  4
# n two  5
# o two  6

# level:复合索引的层次关系 obj.index.levels
a_2 = a.set_index(["d","c"])[["a"]]  # DataFrame类型，其中标签索引d在前，c在后
print(a_2.swaplevel().loc["one"])  # 交换复合索引的位置后，取标签索引"one"




