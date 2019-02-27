import numpy as np
from matplotlib import pyplot as plt
import random

# 体会利用bool索引选取数据的行或列

# 希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改图
data_uk = np.loadtxt(fname="./youtube_video_data/GB_video_data_numbers.csv",delimiter=",",dtype=np.float)

# 根据data_uk第2列的bool索引选取data_uk的行 data[xx,:]选取行，xx:data_uk[:,1]<500000 bool索引
data_1 = data_uk[data_uk[:,1]<500000,:]

data_comment = data_1[:,-1]  # 选取最后一列
data_like = data_1[:,1]  # 选取第2列

plt.figure(figsize=(20,8),dpi=80)
plt.scatter(data_like,data_comment)

plt.show()