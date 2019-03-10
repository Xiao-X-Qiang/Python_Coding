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
from sklearn.ensemble import RandomForestClassifier
import sklearn




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


# 算法模型的评估
# 1 准确率  反映预测结果的准确性
# 2 精确率和召回率
# 混淆矩阵，针对的二分类结果，eg:真实：是猫，不是猫，预测：是猫，不是猫，所以有2*2的混淆矩阵；有多少类别，就有多少混淆矩阵、精确率、召回率、F1-score
# 精确率：反映是否查得准，对预测正样本的区分能力，即预测为正例的样本中正则结果为正例的比例
# 召回率反映是否查得全，对正样本的区分能力，即真实为正例的样本中预测结果为正例的比例
# 3 F1-score，反映模型的稳健性

# sklearn.metrics.classification_report(y_true,y_pred,target_names=None)  # 分类算法的评估报告
# y_true:真实目标值
# y_pred:预估器预测的目标值
# target_names:目标值类别名称
# return:目标值类别名，精确率，召回率，F1-score，真实为正预测为正的个数

# 实例参考Knn算法、朴素贝叶斯算法


# 1.2 朴素贝叶斯算法
# 朴素贝叶斯的思想基础是这样的：对于给出的待分类项，求解在此项出现的条件下各个类别出现的概率，哪个最大，就认为此待分类项属于哪个类别
# 理论基础：1.各特征值间不相关，即相互独立；2.贝叶斯公式

# 数学基础，p(a|b) = p(ab)/p(b) = (p(b|a)p(a))/p(b), 其中：b:各特征值，a:所属类别，p(a|b)：测试集所属类别
# 分母：p(b):测试集中特征值的概率
# 分子：p(a):训练集中各类别的概率，p(b|a)：训练集中各特征值的概率
# 从以上可知，当一个测试样本需要确定其所属哪一类别时，只需要计算分子在各类别的值即可，哪一值大即属哪一类别
# 测试集用以确定分子计算时所需哪些特征

# 拉普拉斯平滑系数：
# P(a|b) = (Ni + alpha)/(N + alpha*m) 其中，Ni为某一特征值的频数，N为所有特征值的频数，m为特征值的个数
# 该系数是避免某些特征值在某类训练集中频率为0而使得整个结果为0的情形出现

# 注意点：
# sklearn.naive_bayes.MultinomialNB(alpha=1.0)
# alpha:拉普拉斯平滑系数，一般取1.0；在某些文章中，某些关键词的出现频率为0，此时便需要拉普拉斯系数进行修正处理

# 优点：源于古典数学理论，有稳定的分类效率；对缺失数据不太敏感，算法也简单，常用于文本分类；分类快，准确度高；
# 缺点：需要知道先验概率p(b|a),其源于数据独立的假设，而一般实际上并不满足，应用受限

def naive_bayes():
    # 1 加载数据
    news = fetch_20newsgroups()
    # 2 分割数据为训练集与测试集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)
    # 3 特征提取
    tf = TfidfVectorizer()
    x_train = tf.fit_transform(x_train)  # 以训练集中的词的列表进行每篇文章重要性统计，['a','b','c']
    print(tf.get_feature_names())
    print(x_train.toarray())
    x_test = tf.transform(x_test)  # 测试集中要以训练集中词为基准进行重要性统计，因而直接使用transform()
    # 4 朴素贝叶斯算法
    mlt = MultinomialNB(alpha=1.0)
    mlt.fit(x_train, y_train)
    predict = mlt.predict(x_test)
    score = mlt.score(x_test, y_test)
    report = classification_report(y_test, predict, target_names=news.target_names)
    print("预测值为：", predict)  # 预测值
    print("准确率为：", score)  # 准确率
    print("评估报告：", report)  # 评估报告


if __name__ == '__main__':
    naive_bayes()  # 朴素贝叶斯算法