import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 现在我们有2015到2017年25万条911的紧急电话的数据，1.请统计出出这些数据中不同类型的紧急情况的次数，2.如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，应该怎么做呢？

data = pd.read_csv("./911.csv")
# data = data[0:200]
# 1.请统计出出这些数据中不同类型的紧急情况的次数、
# 1.1 方法一、使用字符串离散化的方法构造全0数组并进行赋值
data_cate_list_temp = [ i.split(":")[0] for i in data["title"].tolist()]
data_cate_list = list(set(data_cate_list_temp))

# 全0数组并按列进行赋值
data_cate = pd.DataFrame(np.zeros((data.shape[0],len(data_cate_list))),columns=data_cate_list)
for i in data_cate_list:  # 按列进行选取并赋值只需要3次，而按行却要近25万次，提高效率使用列选取
    data_cate.loc[data["title"].str.contains(i),i] = 1  # 列为标签索引，使用.loc选择行列
print(data_cate.sum(axis=0))

# 1.2 方法二、直接在原有数据的添加单列，其值为情况类型，然后进行分组(再聚合统计)
cate_list_column = pd.DataFrame(data_cate_list_temp,columns=["cate"])
data_1 = data.join(cate_list_column)

# 分组聚合后统计
data_total = data_1.groupby(by="cate").count()["title"]
print(data_total)

# 如果想统计出不同月份不同类型紧急电话的次数的变化情况，也可以利用以上的方法解决，也可以使用时间序列来解决：

# 时间序列：针对时间上的操作，常使用的方法主要有：pd.data_range()、pd.to_datatime()、obj.resample()、pd.PeriodIndex()
# 1.pd.date_range():生成特定范围和频率的一组时间序列DatatimeIndex
# pd.date_range(start=None,end=None,periods=None,freq="D"),其中start:开始时间,end:结束时间,periods:索引个数,freq:频率单位
time_index = pd.date_range(start="20180101",end="20181001",freq="M")  # 20180101至20181001每月最后一个日历日
time_index_1 = pd.date_range(start="20180101",periods=20,freq="H")  # 20180101当天的20个时间标签索引，每个索引间隔一小时，
print(time_index)

# 2.pd.to_datetime(time,format=xx)  其中，time:待转化的时间字符串，format:待转化的时间字符串的时间格式
x_1 = pd.to_datetime("2019年3月1日",format=("%Y年%m月%d日"))
print(x_1)

# 3.obj.resample("D")  obj(时间序列必须为标签索引)按天进行重采样，相当于分组 -- DatatimeIndex必须设为标签索引
# 重采样：指的是将时间序列从一个频率转化为另一个频率进行处理的过程，高频-->低频为降采样，反之为升采样
data["timeStamp"] = pd.to_datetime(data["timeStamp"])   # 将"timeStamp"列数据类型进行转化，Series-->Timestamp时间序列
data = data.set_index("timeStamp")
x_2 = data.resample("M").count()

# 4.pd.PeriodIndex(...) 生成时间段PeriodIndex，pd.date_range(...) 生成时间戳DatetimeIndex，
# pd.PeriodIndex(year=data["year"],month=data["month"],day=data["day"],hour=data["hour"],freq="H")  # 将多列字符合并为时间段

data = pd.read_csv("./PM2.5/BeijingPM20100101_20151231.csv")
# print(data.info())
# print(data.head())

# 生成时间段PeriodIndex
datatime = pd.PeriodIndex(year=data["year"],month=data["month"],day=data["day"],hour=data["hour"],freq="H")

# eg1:绘图统计出911数据中不同月份不同类型的电话的次数的变化情况
# 不同类型(类型bool表)-->不同月份(时间序列)
# 时间字符串-->时间序列-->设其为标签索引-->区分类别-->以月为单位重采样
data = pd.read_csv("./911.csv")
data_cate_list_temp = [i.split(":")[0] for i in data["title"].tolist()]
cate_list_column = pd.DataFrame(data_cate_list_temp,columns=["cate"])
data_1 = data.join(cate_list_column)  # 在数组最后添加类别列，以建立标签索引

# 修改时间字符串为时间序列并将其设为其标签索引
data_1["timeStamp"] = pd.to_datetime(data_1["timeStamp"])
data_2 = data_1.set_index("timeStamp")

# 多个类别进行循环，每一类别显示其不同月份：
plt.figure(figsize=(20,8),dpi=80)
for i in set(data_cate_list_temp):
    data_result = data_2[data_2["cate"] == i].resample("M").count()["title"]
    _x = data_result.index
    _y = data_result.values
    plt.plot(_x,_y,label=i)

plt.legend(loc="best")
plt.show()


# eg1_1:统计出911数据中不同月份电话次数的变化情况
# 另一种方式：建立复合索引，以"cate","timeStamp"建立双层索引,然后重采样时间序列并统计显示
data = pd.read_csv("./911.csv")
data_cate_list_temp = [i.split(":")[0] for i in data["title"].tolist()]
cate_list_column = pd.DataFrame(data_cate_list_temp,columns=["cate"])
data_1 = data.join(cate_list_column)

# 修改时间序列为其标签索引
data_1["timeStamp"] = pd.to_datetime(data_1["timeStamp"])
plt.figure(figsize=(20,8),dpi=80)
data_3 = data_1.set_index(["timeStamp","cate"])
for i in set(data_cate_list_temp):
    data_result = data_3.swaplevel().loc[i].resample("M").count()["title"]
    _x = data_result.index
    _y = data_result.values
    plt.plot(_x, _y, label=i)
plt.legend(loc="best")
plt.show()

