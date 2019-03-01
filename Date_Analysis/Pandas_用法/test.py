
import numpy as np
import pandas as pd

data_sbuck = pd.read_csv("./starbucks_store_worldwide.csv")
print(data_sbuck.info())
print(data_sbuck.head(1))

# 分组，pandas中根据列名(str)直接分组返回可迭代对象DataFrameGroupBy：每一个元素是一个元组(索引(分组的值),分组后的DataFrame)
# DataFrameGroupBy对象可以：1.可以进行遍历 2.调用聚合方法，如count,sum,mean,median,std,var,min,max

# 1.遍历
grouped = data_sbuck.groupby(by="Country")  # DataFrameGroupBy类型
# for i,j in grouped:
#     print(i,type(i))
#     print("-"*100)
#     print(j,type(j))
#     print("*"*100)

# 2.聚合
# print(grouped.count())  # DataFrame类型
# grouped["Brand"]  # SeriesGroupBy类型
print(grouped["Brand"].count())  # Series类型
country_count = grouped["Brand"].count()

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

