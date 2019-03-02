import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# eg1:现在我们有北上广、深圳、和沈阳5个城市空气质量数据，请绘制出5个城市的PM2.5随时间的变化情况
# 注意：这组数据中的时间结构，并不是字符串
# pd.PeriodIndex(...) 生成时间段PeriodIndex，pd.date_range(...) 生成时间戳DatetimeIndex，-- PeriodIndex必须设为标签索引
# pd.PeriodIndex(year=data["year"],month=data["month"],day=data["day"],hour=data["hour"],freq="H")  # 将多列字符合并为时间段

data = pd.read_csv("./PM2.5/BeijingPM20100101_20151231.csv")
# print(data.info())
# print(data.head())

# 生成时间段PeriodIndex
datatime = pd.PeriodIndex(year=data["year"],month=data["month"],day=data["day"],hour=data["hour"],freq="H")

# 添加datatime列
data["datatime"] = datatime

# 将PeriodIndex设置为标签索引
data.set_index("datatime",inplace=True)

data = data.resample("7D").mean()

# 取数据列，并作异常处理
data_1 = data["PM_US Post"].dropna()

plt.figure(figsize=(20,8),dpi=80)
_x = data_1.index
_x = [i.strftime("%Y%m%d") for i in _x]
_y = data_1.values

plt.plot(range(len(_x)),_y)
plt.xticks(range(0,len(_x),15),list(_x)[::15],rotation=45)
plt.show()





