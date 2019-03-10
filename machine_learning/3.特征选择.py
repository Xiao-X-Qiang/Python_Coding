from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import jieba
import numpy as np

# 特征选择：
# 即单纯从提取到的所有特征中选择部分特征作为训练集特征，特征在选择前和选择后可以改变值(eg:PCA)、或不改变值(eg:直接选择特征)
# 特征选择的主要方法有：
# 1.Filter(过滤式):VarianceThreshold 2.Embedded(嵌入式):正则化、决策树 3.Wrapper(包裹式) 4.其它方法：eg:神经网络

# 1.Filter：VarianceThreshold
# 1.1 根据方差对特征直接选择
# sklearn.feature_selection.VarianceThreshold(threshold=0.1).fit_transform(X) 不高于方差的特征将被剔除
def vthreshold():
    data = [[0,2,0,3],[0,1,4,3],[0,1,1,3]]
    vthreshold = VarianceThreshold(threshold=0.0)
    data_1 = vthreshold.fit_transform(data)
    print(data)
    print("*"*30)
    print(data_1)

# 1.2 PCA降维
# 目的：维度空间转换，尽可能降低原数据的维数且损失较少量信息
# 可以降维的根本缘由在于：高维度时特征之间的相关性也较强

# sklearn.decomposition.PCA(n_components=None).fit_transpose(X)
# 其中，n_components:小数[0,1]或整数(降至多少维数，不常用)

def pca():
    data = [[1,2,1,5,3],[5,7,4,9,2],[2,4,1,10,6],[5,6,7,4,2]]
    pca = PCA(n_components=0.93)
    data_1 = pca.fit_transform(data)
    print(data)
    print("*"*30)
    print(data_1)

# 2.Embedded(嵌入式):正则化、决策树  --> 待定

# 3.Wrapper(包裹式)  --> 待定
#
# 4.其它方法：eg:神经网络  --> 待定


if __name__ == '__main__':
    # vthreshold()  # 根据方差直接对特征进行选择
    pca()  # 主成分分析
