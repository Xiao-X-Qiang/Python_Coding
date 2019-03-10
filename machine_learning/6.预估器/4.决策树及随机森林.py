from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier



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




# 决策权及随机森林
# 决策树：
# 1.1 信息熵：表示一组数据的信息量的多少，信息熵越大，表示信息量越大，数据的不确定性也就越大
# 计算：H = -(p1logp1 + p2logp2 + ... + p32log32)，其中，p1：表某一类别在总类别中的概率

# 1.2 信息增益：表示数据的某一特征对数据的信息熵的影响程度，其值越大，表示对信息熵的影响越大，数据的不确定性也就越小
# 计算:特征A对训练数据集D的信息增益g(D,A)定义为训练数据集D的信息熵H(D)与特征A给定条件下D的信息条件熵H(D|A)之差，即g(D,A) =H(D)-H(D|A)
# 注：信息增益表示特征A的信息使得D的不确定性减少的程序

# 1.3 常见决策树使用的算法
# ID3:信息增益最大的原则
# C4.5:信息增益比最大的原则
# CART:回归树：平方误差最小，分类树：基尼系数最小，在sklearn中默认该选择

# sklearn.tree.DecisionTreeClassifier(criterion="gini",max_depth=)
# criterion:决策树使用的算法，默认基尼系数
# max_depth:树的深度大小

# 优点：简单理解和实现，且树可视化；需要较少的数据准备，其它算法一般需要数据标准化
# 缺点：生成过于复杂的树(更好地满足训练集)，但可能预测准确率低,即过拟合的现象；不稳定，小的数据变动可能导致完全不同的树

# 改进：对于过拟合的缺点，采用的方法主要有：
# 1.减枝cat算法，实例决策树的参数中 min_samples_split=2,min_samples_leaf=1进行调整
# 2.随机森林

def decision():
    # 读取数据
    data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    print(data.info())  # data基本信息(DataFrame数据类型)

    # 选择特征值与目标值
    x = data[["pclass","age","sex"]]  # 字符串，进行特征提取
    y = data["survived"]  # 数字，不需要特征提取

    # 异常值处理
    x["age"].fillna(x["age"].mean(),inplace=True)

    # 特征提取，特征-->类别-->one_hot编码
    dict = DictVectorizer(sparse=False)
    x = dict.fit_transform(x.to_dict(orient="records"))  # 对训练集特征提取，注意参数 orient="records"

    # 分割数据
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)

    # 实例化决策树
    dec = DecisionTreeClassifier(max_depth=10)
    dec.fit(x_train,y_train)  # 以训练集训练模型

    # 以训练的模型作用于测试集
    print("准确率为：",dec.score(x_test,y_test))

    # 输出决策树至dot文件中，外部环境中dot -Tpng tree.dot -o tree.png转换成png图片
    # dot命令，mac中 brew install graphviz
    export_graphviz(dec,out_file="./tree.dot",feature_names=dict.get_feature_names())

# 随机森林：基于集成学习方法，包含多个决策树分类器，输出的类别由个别树输出的类别中的众数决定
# 集成学习方法，即生成多个分类器/模型，各自独立学习和作出预测
# 构造每颗树的过程：
# 1.训练集表示为：N*M,即N个样本，每个样本M个特征
# 2.从训练集中有放回地抽取N个样本(可能有些是重复的),N*m，即N个样本，每个样本m个特征，且m<<M
# 3.重复步骤2形成一个训练集进行模型的训练

# sklearn.ensemble.RandomForestClassifier(n_estimators=,criterion=,max_depth=,bootstrap=)
# n_estimators:森林中的树木个数,通常选：120，200，300，500，800
# criterion:默认基尼系数进行决策树的建立
# max_depth:决策树的最大深度，通常 5，8，15，25，30
# bootstrap:是否有放回抽样，默认true

# 优点：所有算法中，有较高的准确率；能够有效运行在大数据集上；能够处理高维数据，且不需要降维；能够评估各个特征在分类问题上的重要性；
# 对于缺省值问题也有很好的结果；
# 缺点：参数的选取不好确定，目前只能网格搜索


def randtree():
    # 读取数据
    data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    print(data.info())  # data基本信息(DataFrame数据类型)

    # 选择特征值与目标值
    x = data[["pclass", "age", "sex"]]  # 字符串，进行特征提取
    y = data["survived"]  # 数字，不需要特征提取

    # 异常值处理
    x["age"].fillna(x["age"].mean(), inplace=True)

    # 特征提取，特征-->类别-->one_hot编码
    dict = DictVectorizer(sparse=False)
    x = dict.fit_transform(x.to_dict(orient="records"))  # 对特征进行特征提取，注意参数 orient="records"

    # 分割数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 实例化随机森林
    rf = RandomForestClassifier()

    # 网格交叉验证
    rfcv = GridSearchCV(estimator=rf,param_grid={"n_estimators":[120,200,300],"max_depth":[5,8,15,25,30]},cv=5)

    rfcv.fit(x_train,y_train)  # 训练集训练模型

    print("训练的最优模型为：",rfcv.best_params_)
    print("准确率为：",rfcv.score(x_test,y_test))  # 训练的模型在测试集上的准确率
    pass


if __name__ == '__main__':
    # decision()  # 决策树
    randtree()  # 随机森林

    pass
