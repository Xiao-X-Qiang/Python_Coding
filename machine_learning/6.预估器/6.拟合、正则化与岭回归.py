from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib
import sklearn

# 欠拟合与过拟合
# 1.欠拟合
# 在训练数据集上不能获得更好的拟合，在训练集之外的数据集上也不能很好地拟合数据，此时认为出现了欠拟合现象，即模型过于简单
# 判断：模型在训练集和测试集上都不能获得较好的拟合
# 原因：学习的数据特征过少
# 解决方法：增加数据的特征数量

# 2.过拟合
# 在训练集上能够获得比其他假设更好的拟合，但在训练集之外的其它数据集上却不能很好的拟合数据，此时认为出现了过拟合现象，即模型过于复杂
# 判断：模型很好拟合训练集，却不能很好地拟合测试集
# 原因：训练集的特征过多，存在嘈杂特征，模型因尝试兼顾各个训练数据点而过于复杂
# 解决方法：1.进行特征选择，消除关联性大的特征(难做) 2.正则化


# 特征选择：
# 即单纯从提取到的所有特征中选择部分特征作为训练集特征，特征在选择前和选择后可以改变值(eg:PCA)、或不改变值(eg:直接选择特征)
# 特征选择的主要方法有：
# 1.Filter(过滤式):VarianceThreshold
# 2.Embedded(嵌入式):正则化、决策树、神经网络
# 3.Wrapper(包裹式)

# 正则化：
# 在线性回归的损失函数后加了惩罚项，惩罚因子调节收敛的速度，避免过度学习过拟合的问题

#  算法          策略(损失函数)           优化
# 线性回归       误差平方和(即最小二乘法)   正规方程求解或梯度下降学习求解
# 岭回归         误差平方和(有惩罚项)      正规方程求解或梯度下降学习求解

# 岭回归：
# 相对于线性回归：岭回归肯定有解(损失函数有惩罚项)；拟合的曲线更为合适(正则化损失函数)
# 线性回归的最小二乘法：w = (X.^T*X).^(-1)*X.^T*y
# 岭回归中的的最小二乘法：w = (X.^T*X+alpha*I).^(-1)*X.^T*y  其中，I为单位阵，alpha*I使得(X.^T*X+alpha*I)的逆阵肯定存在


# 加正则化后的岭回归：
# sklearn.linear_model.Ridge(alpha=1.0)
# alpha：正则化力度
# coef_:回归系数
# 特点：得到的回归系数更真实、稳定，在存在病态数据的数据集中也有一定的鲁棒性

# 模型的保存与加载
# 模型的保存
# from sklearn.externals import joblib
# joblib.dump(estimator,"./estimator_complete.pkl")  # 将训练好的模型对象estimator保存至当前目录的estimator_complete.pkl文件中

# 模型的加载
# from sklearn.externals import joblib
# model = joblib.load("./estimator_complete.pkl")  # 加载已经训练好的模型estimator_complete.pkl

def ridge():
    # 读取并分割数据
    data = load_boston()
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25)

    # 标准化(与分类问题有所不同，目标值也要标准化，在最终显示时，可用obj.inverse_transform()反标准化)
    std1 = StandardScaler()
    std2 = StandardScaler()

    # 对特征值标准化 -- fit_transform()及transform()的使用可参考 "0.0.训练集、测试集的特征工程.py"
    x_train = std1.fit_transform(x_train)
    x_test = std1.transform(x_test)

    # 对目标值标准化
    y_train = std2.fit_transform(y_train.reshape((-1, 1)))  # 由一维变二维,算法要求的格式
    # y_test = std2.transform(y_test.reshape((-1, 1)))  # 同上

    # 预估器
    ridge = Ridge()
    ridge.fit(x_train,y_train)  # 训练模型
    joblib.dump(ridge,"./ridge_complete.pkl")  # 保存训练好的模型ridge保存至文件ridge_complete.pkl文件中

    model = joblib.load("./ridge_complete.pkl")  # 从文件ridge_complete.pkl中加载已经训练好的模型
    result = ridge.predict(x_test)
    result_inverse = std2.inverse_transform(result)
    print("预测结果为：",result_inverse)
    print("预测的结果均方误差为：",mean_squared_error(y_test,result_inverse))


if __name__ == '__main__':
    ridge()
    pass

