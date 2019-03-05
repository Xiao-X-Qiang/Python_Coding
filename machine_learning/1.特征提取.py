from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba


# 特征的提取

# 1.对字典数据进行特征值化
# sklearn.feature_extraction.DictVectorizer().fit_transform(X)
def dictvec():
    """
    字典的数据抽取：将字典中的一些类别信息，分别转换成特征(one-hot编码)，数值类型则不需要转换
    :return:None

    """
    dict_1 = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]

    dictvec = DictVectorizer(sparse=False)  # 实例化对象,且转化为DataFrame矩阵
    data = dictvec.fit_transform(dict_1)  # 字典特征值化
    print(dictvec.get_feature_names())  # 返回类别名称
    print(data)  # 实例化时默认sparse参数时，输出sparse矩阵，不用DataFrame矩阵是为了节约内存
    return None


# 2.对文本数据进行特征值化
# 2.1 英文数据
# sklearn.feature_extraction.text.CountVectorizer().fit_transform() 对频数(count)统计
def strvec():
    data = ["life is too short,i use python", "hello world,this is python"]
    strvec = CountVectorizer()
    data_1 = strvec.fit_transform(data)
    print(strvec.get_feature_names())  # 对于单个字母或中文不统计，单个字母表示不了语义
    print(data_1.toarray())  # toarray()将sparse矩阵转为ndarray矩阵


# 2.2 中文数据
# 先分词，再特征值化
def hanzivec():
    hanzivec = CountVectorizer()
    data = ["这是一个美丽富饶的地方","我是一个兵，来自老百姓"]
    data_1 = [jieba.cut(i) for i in data]  # 生成迭代对象列表
    data_2 = [" ".join(i) for i in data_1]  # 对每个迭代对象以空格进行拼接，最终形成字符串列表
    data_3 = hanzivec.fit_transform(data_2)  # 中文特征值化，单个中文不统计
    print(hanzivec.get_feature_names())
    print(type(data_3.toarray()))  # toarray()将sparse矩阵转为ndarray矩阵

# 2.3 tf-idf
# tf:term frequency 词频
# idf:inverse document frequency 逆文本频率, idf=log(总文件数目/包含该词语的文件数目)
# tf*idf 使得：某一特定文件内的高词语词频，及该词语在整个文件集合中的低文件词频，可以产生高权重的tf-idf，从而保留重要的词语

# sklearn.feature_extraction.text.TfidfVectorizer().fit_transform()
def hanzivec_1():
    hanzivec = TfidfVectorizer()
    data = ["这是一个美丽富饶的地方","我是一个兵，来自老百姓"]
    data_1 = [jieba.cut(i) for i in data]  # 生成迭代对象列表
    data_2 = [" ".join(i) for i in data_1]  # 对每个迭代对象以空格进行拼接，最终形成字符串列表
    data_3 = hanzivec.fit_transform(data_2)  # 中文特征值化，单个中文不统计
    print(hanzivec.get_feature_names())
    print(data_3.toarray())  # toarray()将sparse矩阵转为ndarray矩阵


if __name__ == '__main__':
    # dictvec()  # 字典特征值化
    # strvec()  # 英文特征值化
    # hanzivec()  # 中文特征值化
    # hanzivec_1()  # tf-idf特征值化
    pass