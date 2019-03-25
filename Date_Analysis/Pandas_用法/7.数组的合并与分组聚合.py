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
print(p1.merge(p2,left_on="O",right_on="X"))  # 列名不同时，使用left_on、right_on指定，默认内连接
print(pd.merge(p1,p2,on=["O","X"]))  # 效果同上，默认内连接

print(p1.merge(p2,on="a"))  # 当列名相同时，直接使用on,默认内连接

# 2.2 外连接
print(p1.merge(p2,left_on="O",right_on="X",how="outer"))  # 外连接

# 2.3 左连接
print(p1.merge(p2,left_on="O",right_on="X",how="left"))  # 左连接

# 2.4 右连接
print(p1.merge(p2,left_on="O",right_on="X",how="right"))  # 右连接


# 数组的分组聚合
# 情形：现在有一组关于全球星巴克店铺的统计数据，如果想知道美国的和中国的哪个星巴克数量多，或者想知道中国每个省份星巴克的数量时，应该怎么办？
data_sbuck = pd.read_csv("./starbucks_store_worldwide.csv")
print(data_sbuck.info())
print(data_sbuck.head(1))

# 分组：可视结果为单个标签索引，有别于复合索引
# 对于分组后的结果，可视其为将by=xx字段设置为标签索引(单个索引，有别于复合索引)，即 obj.set_index(by=xx)
# pandas中数据(DataFrame)根据列名(str)直接分组返回可迭代对象DataFrameGroupBy：每一个元素是一个元组(索引(分组的值),分组后的DataFrame)
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

# DataFrame-->DataFrameGroupBy-->DataFrame;
# 注意：用于索引的两列，data_sbuck[["Brand"]]数组没有该两列，故而借助于data_sbuck,有别于grouped1、group2的方式
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
# 重置行索引为下标索引：obj.reset_index() 将行标签索引作为列添加至obj中(列标签索引为：index)，行索引变为下标索引

# 1.Series复合索引
a = pd.DataFrame({'a': range(7),'b': range(7, 0, -1),'c': ['one','one','one','two','two','two', 'two'],'d': list("hjklmno")})
# 1.1 指定列为其索引
a_1 = a.set_index(["c","d"])["a"]  # Series类型，其中标签索引c在前，d在后
print(a_1)  # a:DateFrame,a_1:Series

# 1.2 根据索引值取值
print(a_1.loc["one","j"])  # Series复合索引中，先取"one"索引(Series类型)，再取"j"索引
print(a_1.loc["one"])

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

# 交叉表
# pd.crosstab(index=xx,columns=yy)
# 将其列xx作为行索引(去重)，将其yy列作为列索引(去重)，当[xx,yy]存在值时为1，否则为0；
# p1=
#     A   B   C   D   E   F
# a   0   7   2   3   4   5
# b   6   7   8   9  10  11
# c  12  13  14  15  16  17
# d  18  19  20  21  22  17

pd.crosstab(p1["B"],p1["F"])
3*3
#   F  5   11  17
# B
# 7    1   1   0
# 13   0   0   1
# 19   0   0   1

# pd.pivot() 将某列作为行索引(去重)，某列作为列索引(去重)，某列作为对应的值(行列对有重复的，取其平均值)
pd.pivot_table(p1["B"],p1["F"],p1["A"])

