
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np


#  算法          策略(损失函数)           优化
# 线性回归       误差平方和(即最小二乘法)   正规方程求解或梯度下降学习求解
# 岭回归         误差平方和+惩罚项         正规方程求解或梯度下降学习求解
# 逻辑回归       对数似然估计函数          梯度下降学习求解(只能)

# 注意:梯度下降求解时，不能保证求解一定得到全局最优解(得到的是局部最优解)
# 解决方法：1.调整学习率   2.多初始点随机

# 逻辑回归 -- 分类算法
# 逻辑回归是解决 二分类 问题的利器
# 过程可表述为：原始数据-->sigmoid函数转换为0-1范围内-->对数似然估计函数(针对某一类别0或1)也可完整损失函数评估-->损失值越小，预测的准确度越高，sigmoid越接近于1或越接近于0
# 针对1分类时，sigmoid越接近于1时，准确度越高；针对0分类时，sigmoid越接近于0时，准确度越高；总体趋势是，损失函数越小(都是正值)，分类准确度越高
# 哪一类的样本数量少，判定的概率指的便是这个类别，即正例

sklearn.linear_model.LogisticRegression(penalty='l2',C=1.0)
# penalty:l2正则化，同岭回归般解决过拟合问题
# C:正则化力度
# coef_:回归系数

def logicreg():
    """
    逻辑回归二分类进行癌症预测
    :return:
    """
    # 获取数据
    columns_ = ['Sample code number','Clump Thickness', 'Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']
    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",names=columns_)
    print(data.head())
    print(data.info())
    # 数据的预处理(处理缺失值)以及标准化
    data.replace(to_replace="?",value=np.nan,inplace=True)  # 替换
    data.dropna(inplace=True)  # 删除有np.nan的样本

    # 拆分数据
    x_train,x_test,y_train,y_test = train_test_split(data[columns_[1:-1]],data[columns_[-1]],test_size=0.25)

    # 标准化处理,分类问题时目标值不需标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 逻辑回归预估
    logicg = LogisticRegression(penalty="l2",C=1.0)  # 默认参数，正则化，超参数可调优
    logicg.fit(x_train,y_train)  # 建模

    # 回归系数
    print("回归系数：",logicg.coef_)

    # 预测目标
    predict_result = logicg.predict(x_test)

    # 准确率
    print("准确率：",logicg.score(x_test,y_test))

    # 召回率，更注重召回率
    report = classification_report(y_test,predict_result,labels=[2,4],target_names=["良性","亚性"])
    print("分类结果报告：",report)



if __name__ == '__main__':
    logicreg()
    pass

