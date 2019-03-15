
import sklearn
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# kmeans分类算法
# 针对对象：无监督数据(通常在实际情况中，分数的个数会根据实际业务有大致范围)

# sklearn.cluster.KMeans(n_clusters=xx)
# n_clusters:分为几类

# 聚类评判标准：轮廓系数 每个样本的轮廓系数的平均值
# 取值范围[-1,1],越接近于1，聚类效果越好；即类间距离最大化，类内距离最小化

# sklearn.metrics.silhouette_score(X,labels=)
# X：特征值
# labels:被聚类标记的目标值

def kmeans():
    """
    使用聚类算法对用户进行分类
    """
    pass
    # 获取数据
    prior = pd.read_csv("/Users/xiaoqiang/Downloads/Data/instacart-market-basket-analysis/order_products__prior.csv")
    products = pd.read_csv("/Users/xiaoqiang/Downloads/Data/instacart-market-basket-analysis/products.csv")
    orders = pd.read_csv("/Users/xiaoqiang/Downloads/Data/instacart-market-basket-analysis/orders.csv")
    aisles = pd.read_csv("/Users/xiaoqiang/Downloads/Data/instacart-market-basket-analysis/aisles.csv")

    _merge = pd.merge(prior,products,on=["product_id","product_id"])
    _merge = pd.merge(_merge,orders,on=["order_id","order_id"])
    _merge = pd.merge(_merge,aisles,on=["aisle_id","aisle_id"])

    # 交叉表
    cross = pd.crosstab(index=_merge["user_id"],columns=_merge["aisle_id"])

    # 取其前1000样本(数据量太大，取前N项)
    cross_1 = cross.loc[:1000,:]

    # 预估器，将数据分为4类
    km = KMeans(n_clusters=4)
    km.fit(cross_1)

    predict = km.predict(cross_1)  # 预测结果

    # 轮廓系数
    score = silhouette_score(cross_1,predict)
    print("轮廓系数为：",score)

    # 绘图
    plt.figure(figsize=(10,10),dpi=80)
    color_list = ["yellow","orange","blue","red"]
    colors = [ color_list[i] for i in predict]
    plt.scatter(cross_1.iloc[:,4],cross_1.iloc[:,13],color=colors)  # 只能取其两列进行绘图
    plt.show()



if __name__ == '__main__':
    kmeans()
    pass

