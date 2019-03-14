from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import pandas as pd
from sklearn.feature_extraction import DictVectorizer



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

# 1.3 模型的选择与调优
# 1.3.1 交叉验证
# 作用:使得模型的参数选择结果更可信
# 过程：
# 1.训练集分为训练集与验证集 2.对等N折后，其一作为验证集，其余作为训练集，训练并验证得准确率
# 3.依次轮流作验证集，其余为训练集，训练并验证得准确率 4.对最终的N个准确率求平均值，得出某超参数下的平均准确率
# 5.结合网格搜索后，依次更换M次超参数，进行交叉验证，得出M个平均准确率，选择平均准确率(交叉验证的结果)最高(多次更换超参数)的超参数作为最终的模型参数
#

# 1.3.2 网格搜索
# 作用：结合交叉验证选择相对最优的超参数
# 过程：
# 1.交叉验证对等N折后，其一作为验证集，其余作为训练集，训练并验证得当次M个超参数的准确率
# 2.依次轮流作验证集，其余为训练集，训练并验证最终得M个超参数的N个准确率平均准确率
# 3.取平均准确率最高的超参数作为最终的模型参数

# from sklearn.model_selection import GridSearchCV(estimator,param_grid=None,cv=None)
# estimator:估计器对象
# param_grid:估计器参数，字典形式，eg:{"n_neighbors":[1,3,5,7]}
# cv:几折交叉验证，一般取10折

# 使用方法：
# obj=GridSearchCV()对象-->obj.fit(x_train,y_train)-->obj.best_score_,obj.best_estimator_,obj.cv_results_-->obj.score(x_test,y_test)
# obj.fit(x_train,y_train)：使用训练集进行网格交叉验证
# obj.best_score_:在交叉验证中验证的最好结果，即某超参数下的最高平均准确率
# obj.best_estimator_:最好的参数模型，平均率最高对应的超参数
# obj.cv_results_:每次交叉验证后的验证集的准确率结果
# obj.score:以之前的模型选择结果应用于测试集得准确率

def knngcv():
    # 1.1 准备数据
    data = load_iris()
    # 1.3 预处理或特征提取(对特征值，而非目标值)
    scaler = StandardScaler()
    data_1 = scaler.fit_transform(data.data)

    # 1.2 分割训练集与数据集
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25)  # 不作标准化处理
    # x_train,x_test,y_train,y_test = train_test_split(data_1,data.target,test_size=0.25)  # 标准化处理

    # 1.3 建立模型
    # knn = KNeighborsClassifier(n_neighbors=5)  # 实例化时参数，称为超参数
    knn = KNeighborsClassifier()  # 网格搜索时，要缺省超参数

    # 以训练集为基础进行网格交叉验证寻最优超参数
    gridcv = GridSearchCV(knn, param_grid={"n_neighbors": [1, 3, 5, 7]}, cv=10)  # 实例网格交叉验证对象
    gridcv.fit(x_train, y_train)  # 以训练集为基础(划分为训练集与验证集进行模型选择)进行模型的训练
    print("最好的验证结果：", gridcv.best_score_)
    print("最优的模型选择结果：", gridcv.best_estimator_)
    print("每次交叉的验证结果：", gridcv.cv_results_)

    # 模型选择结果作用于测试集
    predict = gridcv.predict(x_test)  # 以最好的模型结果对测试集进行测试得预测结果
    score = gridcv.score(x_test, y_test)  # 以最好的模型结果对测试集进行测试得预测结果的准确率
    print("测试集上的预测结果为：", predict)
    print("测试集上的准确率为：", score)

    # knn.fit(x_train, y_train)  # 训练模型
    # predict = knn.predict(x_test)  # 对测试集预测结果
    # scole = knn.score(x_test, y_test)  # 对测试集预测结果并得出准确率
    # print(predict == y_test)
    # print(scole)
    # print("*" * 30)
    # print("测试集大小为：", x_test.shape)
    report = classification_report(y_test, predict, target_names=data.target_names)  # 精确率、召回率、f1-score、及真实正例中预测为正例的个数
    print(report)

if __name__ == '__main__':
    knngcv()  # 网络搜索knn