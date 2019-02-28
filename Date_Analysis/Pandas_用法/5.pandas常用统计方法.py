import pandas as pd
import numpy as np
import string
from matplotlib import pyplot as plt

# 对DataFrame进行切片后的数据(数据类型是DataFrame或Series).values后(数据类型numpy.ndarray)可以直接使用numpy中的方法进行有关统计
# DataFrame --> Series后也可以使用numpy中的部分统计方法,但推荐 Series-->numpy.ndarry后再使用统计方法


# print(type(data)) DataFrame数据类型
data = pd.DataFrame([[1,2,3],[4,5,6]],index=list("ab"),columns=list("ABC"))

# prite(type(data_1))  Series数据类型
data_1 = data["B"]

# print(type(data_2))  numpy.ndarray数据类型
data_2 = data[1:2].values

# eg:√现在我们有一组从2006年到2016年1000部最流行的电影数据，我们想知道这些电影数据中评分的平均分，导演的人数等信息
file_path = "./IMDB-Movie-Data.csv"
data_x = pd.read_csv(file_path)
print(data_x.info())
print(data_x.head(1))

# 评分的平均分
# DataFrame-->Series-->numpy.ndarray.mean()
data_rate_mean = data_x["Rating"].values.mean().round(4)
print(data_rate_mean)

# 导演信息
# 将 DataFrame-->Series-->list-->set 得到不重复的导演个数
data_director = set(data_x["Director"].tolist())
print(len(data_director))

# 演员信息
# DataFrame-->Series-->list
data_actor_temp = [i.split(", ") for i in data_x["Actors"].tolist()]
data_actor = [i for j in data_actor_temp for i in j]
print(len(set(data_actor)))

# 对于这一组电影数据，如果我们想rating，runtime的分布情况，应该如何呈现数据？
data_rate = data_x["Rating"].values
print(np.max(data_rate),np.min(data_rate))
plt.figure(figsize=(20,8),dpi=80)
plt.hist(data_rate,[1.9 + 0.5*i for i in range(20)])
plt.xticks([1.9 + 0.5*i for i in range(20)])

plt.show()

# 对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
# 思路：重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，就让0变为1
gen_list = data_x["Genre"].str.split(",").tolist()