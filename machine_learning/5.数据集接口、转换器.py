from sklearn.datasets import load_iris,fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn

# 数据集
# 1.scikit-learn中数据集获取接口
# 1.1 sklearn.datasets.load_*()，获取小规模数据集，数据包含在datasets中

# 1.2 sklearn.datasets.fetch_*(data_home=None,subset="..")，获取大规模数据集且从网络获取
# data_home指定数据集的下载目录，默认~/scikit_learn_data/下
# subset:"train"或"test"或"all"

# data_source = load_*() 或 data_source = fetch_*()中：
# data_source数据类型：返回的数据集的数据类型是datasets.base.Bunch(类字典格式)，其中：
# data:特征数据数组，是[n_samples*n_features]的二维numpy.ndarray数组
# target:标签数组，是n_samples的一维numpy.ndarray数组
# DESCR:数据描述
# feature_names:特征名，新闻数据、手写数字、回归数据没有
# target_names:标签名，回归数据集没有
# 访问形式可以如下：result.data  或 result["data"] 或 result.get("data")  其中，result类字典格式


def loads_():
   iris = load_iris()
   print(iris["data"])
   print(iris["target"])
   print(iris.get("feature_names"),iris.get("target_names"))

def fetch_():
    news = fetch_20newsgroups(data_home=None,subset="train")
    print(news["data"])
    print(news.get("target"))


# 2 scikit-learn中数据的分割接口
# sklearn.model_selection.train_test_split()  用于分割数据，其中：
# x:数据集的特征值
# y:数据集的目标值
# test_size:测试集的大小，一般为float,eg:0.25,即测试集占数据集的25%
# random_state 随机种子，不同的随机种子产生不同的随机采样结果，相同的种子采样结果相同

# return 训练集特征值，测试集特征值，训练集目标值，测试集目标值(默认随机采样)

def split_iris():
    data = load_iris()
    x_train,x_test,y_train,y_test = train_test_split(data["data"],data["target"],test_size=0.25)
    print(y_test)

# 转换器
# 转换器：数据的处理过程
# 转换器:obj.fit(),obj.transform(),obj.fit_transform()三种形式的区别有：
# obj.fit(X) 对于输入数据X不作处理，只计算一些方法计算统计参数(视object而定)保存在object中
# obj.transform(X) 结合obj.fit(X)使用，使用obj.fix(X)的统计参数(均值、方差等)对X作相应的操作
# obj.fit_transform(X) 结合了fit()与transform()，作统计参数并作用于数据X,推荐使用
# 注：当obj.fit(X) 然后 obj.transform(Y)时，会以obj.fix(X)的统计结果作用于Y,千万注意

# 一般对数据的训练集和测试集上，使用fit_transform()对训练集进行预处理，使用transform()以训练集的相关统计参数(均值和方差等)
# 对测试集进行处理，使得train_data,test_data的处理方式相同


def fit_transform_():
    scalar = StandardScaler()
    data = scalar.fit_transform([[1,2,3],[3,4,5]])

    ss = StandardScaler()
    data_1 = scalar.fit([[7,1,3],[3,4,3]])
    data_2 = scalar.transform([[1,2,3],[3,4,5]])  # 与data不同，原因在于fit()返回的数据的统计不同，并作用于data和data_2
    print(data_2)
    print(data)


if __name__ == '__main__':
    # loads_()  # load_*() 加载数据
    # fetch_()  # fetch_* 加载数据
    # split_iris()  # 对鸢尾花数据分割
    fit_transform_()  # fit_transform()的使用
    pass


