import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import string
from matplotlib import pyplot as plt

# 对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
# 思路：重新构造一个全为0的数组，列名为分类，如果某一条数据中分类出现过，就让0变为1
# 如何进行DataFrame数据的字符串的离散化呢？

# eg:√现在我们有一组从2006年到2016年1000部最流行的电影数据：
file_path = "./IMDB-Movie-Data.csv"
data_x = pd.read_csv(file_path)

# 统计分类的列表
list_genre_temp = data_x["Genre"].str.split(",").tolist()  # [[],[],[]]  先分割再列表
# 或者 list_genre_temp = [ i.split(",") for i in data_x["Genre"].tolist() ]  # 先列表再分割
list_genre = set([i for j in list_genre_temp for i in j])  # genre列表，[a,b,...]  不重复的类别
list_genre_x = pd.DataFrame(np.zeros((data_x.shape[0],len(list_genre))),columns=list_genre)  # 类别列表，DataFrame全为0

# 设置类别表
for i in range(list_genre_x.shape[0]):
    list_genre_x.loc[i,list_genre_temp[i]] = 1

# 统计类别数量
sum_genre = list_genre_x.sum(axis=0)
print(type(sum_genre))

# 绘图
plt.figure(figsize=(20,8),dpi=80)

sum_genre_sort = sum_genre.sort_values()
plt.bar(sum_genre_sort.index,sum_genre_sort.values)

plt.grid(alpha=0.4)
plt.show()


