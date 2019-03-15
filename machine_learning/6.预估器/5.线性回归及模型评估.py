
import sklearn
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# 回归：目标值连续
# 线性(自变量的次数为1)回归：通过一个或多个自变量与因变量之间的映射进行建模的回归分析
# 其中，涉及变量只有一个即一元线性回归，涉及变量不少于2个即多元线性回归


#  算法          策略(损失函数)           优化
# 线性回归       误差平方和(即最小二乘法)   正规方程求解或梯度下降学习求解

# 损失函数 -- 使该目标值最小时的回归系数-->有两种方法求解：正规方程(损失函数求解时,(X.^T*X)逆阵存在时可用该方法)；梯度下降,更通用
# f(...) = (y1 - y1_).^2 + (y2 - y2_).^2...  预测目标值与真实目标值的差的平方和
# 另一形式：f(W) = (X*W-Y).^T*(X*W-Y),其中，W:回归系数，X:测试集，Y:测试集真实目标值

# 线性回归的最小二乘法：w = (X.^T*X).^(-1)*X.^T*y


# 正规方程求解
# sklearn.linear_model.LinearRegression()
# 普通的最小二乘线性回归，返回coef_:回归系数
# 特点：不需学习率；一次运算得出；需计算训练集的逆阵当特征n<1000时可以接受；只适用于线性模型，不适用于逻辑回归等其它模型；不能解决过拟合及其它问题
# 缺点：(X.^T*X)逆阵存在时可用该方法，梯度下降无此限制

# 梯度下降求解
# sklearn.linear_model.SGDRegressor
# 使用SGD最小化线性模型，返回coef_:回归系数
# 特点：需学习率；迭代计算；当特征n很大时也同样适用；适用于多种模型；适用于大规模数据；

# 回归问题模型及其评估
# 使用MSE(mean squared error)均方误差：预测值与真实值的差的平方和的平均值
# sklearn.metrics.mean_absolute_error(y_true,y_pred)
# y_true:标准化前的真实值
# y_pred:标准化前的预测值
# return:浮点结果


def line_lineregression():
    # 读取并分割数据
    data = load_boston()
    x_train,x_test,y_train,y_test = train_test_split(data.data,data.target,test_size=0.25)

    # 标准化(与分类问题有所不同，目标值也要标准化，在最终显示时，可用obj.inverse_transform()反标准化)
    std1 = StandardScaler()
    std2 = StandardScaler()

    # 对特征值标准化 -- fit_transform()及transform()的使用可参考 "0.0.训练集、测试集的特征工程.py"
    x_train = std1.fit_transform(x_train)
    x_test = std1.transform(x_test)

    # 对目标值标准化
    y_train = std2.fit_transform(y_train.reshape((-1,1)))  # 由一维变二维,算法要求的格式
    # y_test = std2.transform(y_test.reshape((-1,1)))  # 同上

    # 实例化预预估器
    lr_1 = LinearRegression()
    sgd_1 = SGDRegressor()  # 学习率默认

    # 1.正规方程求解
    lr_1.fit(x_train,y_train)  # 训练模型
    print(lr_1.coef_)  # 训练得到的模型参数
    result_1 = lr_1.predict(x_test)  # 得到的预测值
    result_1 = std2.inverse_transform(result_1)  # 反标准化
    print("正规求解预测房价为：",result_1)
    print("正规求解均方误差为：",mean_squared_error(y_test,result_1))

    print("*"*30)

    # 2.梯度下降求解
    sgd_1.fit(x_train,y_train)
    print(sgd_1.coef_)
    result_2 = sgd_1.predict(x_test)
    result_2 = std2.inverse_transform(result_2)  # 反标准化
    print("梯度下降求解预测房价为：",result_2)
    print("梯度下降求解均方误差为：", mean_squared_error(y_test, result_2))


if __name__ == '__main__':
    line_lineregression()

    pass
