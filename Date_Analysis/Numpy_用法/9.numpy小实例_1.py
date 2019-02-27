import numpy as np
from matplotlib import pyplot as plt
import random

# 英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图
data_us = np.loadtxt(fname="./youtube_video_data/US_video_data_numbers.csv",delimiter=",",dtype=np.float)

data_1 = data_us[:,-1]  # 选取data_us最后一列的评论数

data_1 = data_1[data_1<5000]  # 只选择评论数小于5000的数据

plt.figure(figsize=(20,8),dpi=80)

print(np.max(data_1),np.min(data_1))

hist_width = 100

hist_num = (np.max(data_1)-np.min(data_1))//hist_width
hist_num = hist_num.astype(np.int)

plt.hist(data_1,hist_num)

plt.show()