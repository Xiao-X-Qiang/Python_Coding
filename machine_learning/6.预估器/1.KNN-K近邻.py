from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


# 预估器
# 预估器：算法的具体实现，常用的预估器有：
# 1.用于分类的预估器：
# 1.1 sklearn.neighbors  # k-近邻算法(KNN )
# 1.2 sklearn.naive_bayes  # 贝叶斯算法
# 1.3 sklearn.linear_model.LogisticRegression  # 逻辑回归
# 2.用于回归的预估器：
# 2.1 sklearn.linear_model.LinearRegression  # 线性回归
# 2.2 sklearn.linear_model.Ridge  # 岭回归
# 3.无监督学习：聚类

# 预估器使用方法
# 训练集-->obj.fit()建立模型-->测试集--> 1.pridict(x_test)预测的目标值 或 2.score(x_test,y_test)准确率

# 1.1 KNN 近邻
# k近邻算法中，根据测试集中数据点(测试集)与训练集中数据点距离(欧氏距离、城市距离等等)最近的若干个点的所属类别(n_neighbors)判别测试点的类别
# sklearn.neighbors.KNeighborsClassifier(n_neighbors=xx,algorithm='auto'):n_neighbors k近邻个数，algorithm：搜索近邻算法，一般默认
# 特点：
# 1.K值的选取：k值较小时易受异常点影响，K值较大时易受类别数量的影响(训练集中，爱情片占75%，动作片25%，当k值很大时，很大可能是爱情片)
# 2.性能问题，计算测试集中每一点与训练集中所有数据点的距离

# 优点：无需调参，无需训练，易于理解与实现
# 缺点：1.k值的选取  2.懒惰算法，计算量大，内存开销大

# 应用场景：小数据场景，几千-几万样本，据实际测试而定，应用场景较小


def knn():
    # 1.1 准备数据
    data = load_iris()
    # 1.3 预处理或特征提取(对特征值，而非目标值)
    scaler = StandardScaler()
    data_1 = scaler.fit_transform(data.data)

    # 1.2 分割训练集与数据集
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25)  # 不作标准化处理
    # x_train,x_test,y_train,y_test = train_test_split(data_1,data.target,test_size=0.25)  # 标准化处理

    # 1.3 建立模型
    knn = KNeighborsClassifier(n_neighbors=5)  # 实例化时参数，称为超参数
    knn.fit(x_train, y_train)  # 训练模型
    predict = knn.predict(x_test)  # 对测试集预测结果
    scole = knn.score(x_test, y_test)  # 对测试集预测结果并得出准确率
    print(predict == y_test)
    print(scole)
    print("*" * 30)
    print("测试集大小为：", x_test.shape)
    report = classification_report(y_test, knn.predict(x_test),
                                   target_names=data.target_names)  # 精确率、召回率、f1-score、及真实正例中预测为正例的个数
    print(report)

if __name__ == '__main__':
    knn()  # knn算法