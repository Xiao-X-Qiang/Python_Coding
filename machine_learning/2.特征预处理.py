from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
import jieba
import numpy as np


# 特征的预处理
# sklearn.preprocessing
# 通过特定的统计方法(或数学方法)将数据转换成算法要求的数据

# 数值型数据：标准缩放：1.归一化 2.标准化 3.缺失值
# 类别型数据：one-hot编码--特征提取
# 时间类型：时间的切分

# 1. 归一化
# 归一化：通过对原始数据进行变换将数据映射到(默认为[0,1])特定的区间范围内
# 为何需归一化？各特征的权重相等
# 弊端：容易受异常点影响，只适合于传统精确小数据场景，应用范围有限
#
# 计算方式：x_1 = (x-min)/(max-min)  x_2 = mi + x_1*(mx-mi)  其中：max:特征最大值，min:特征最小值，mx,mi 映射到[mi,mx]区间上，默认[0,1]
#
# sklearn.preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform()

def scaler():
    sc = MinMaxScaler(feature_range=(1,2))  # 实例化，并指定映射区间[1,2]
    data = [[2,3,1,4],[4,5,6,2],[7,8,3,1]]  # 数量必须是二维形式的，列表或ndarray
    data_1 = sc.fit_transform(data)  # fit_transform() 归一化
    print(data_1)

# 2. 标准化
# 为了减小可能的异常值对数据特征的影响，便应运而生对数据的标准化 -- 由于样本数量比较多，相对于归一化，影响的程度较小
# 标准化：通过对原始数据进行变换将数据映射到均值为0，标准差为1的区间范围内

# 计算方式：x_1 = (x-mean)/std,作用于每一列，其中，mean:特征均值，std:特征标准差
#
# sklearn.preprocessing.StandardScaler().fit_transform()

def sscaler():
    ssc = StandardScaler()
    data = [[2,3,1,4],[4,5,6,2],[7,8,3,1]]
    data_1 = ssc.fit_transform(data)
    print(data_1)

# 3. 缺失值
# 对于缺失值的处理，通常两种：
# 1.删除：如果特征列或样本行缺失达到一定比例，建议放弃该列或该行
# 2.插补：通过特征列的平均值、中位数等填充(通常是对列进行操作，对行取均值无意义)
# 另：通常在pandas中对异常值nan(必须是np.nan,且为float类型)进行处理，sklearn虽然也可以处理

# sklearn.preprocessing.Imputer(missing_values="NaN",strategy="mean",axis=0).fit_transform()
def im():
    im = Imputer(missing_values="NaN",strategy="mean",axis=0)
    data = np.array([[np.nan,3,1,4],[4,5,np.nan,2],[7,8,3,1]]).astype("float")
    data_1 = im.fit_transform(data)
    print(data)
    print("*"*20)
    print(data_1)

if __name__ == '__main__':
    # scaler()  # 归一化
    # sscaler()  # 标准化
    im()  # 对缺失值处理
    pass
