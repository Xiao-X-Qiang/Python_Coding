import pandas as pd
import numpy as np
import string

# 创建DataFrame:二维，Series容器
# pd.Series(data[,index=...,columns=...])
# 方式一：
x_1 = pd.DataFrame(np.arange(24).reshape((4,6)),index=list("abcd"),columns=list("WXYZFG"))

# 方式二
x_2 = pd.DataFrame([[1,2,3],[4,5,6]],index=list("ab"),columns=list("WXY"))
print(x_2)

# 方式三
# pd.DataFrame(dict)
# 3.1 参数是字典
x_3_1 = pd.DataFrame({"name":["xiong","luo","chen"],"age":[22,23,26],"tel":[10086,10010,10000]})
print(x_3_1)

# 3.2 参数是列表
x_3_2 = pd.DataFrame([{"name":"xiong","age":22,"tel":10086},{"name":"luo","age":23,"tel":10086},{"name":"chen","age":26,"tel":10000}])
print(x_3_2)

# DataFrame与Series的关系:DataFrame的单行或单列便是Series
print(type(x_3_1))
print(type(x_3_1.loc[:,"name"]))


# DataFrame的常用属性有：
# obj.shape  # 数组的维度的长度，即(行数、列数)
# obj.dtype  # 列数据类型
# obj.ndim  # 数据维度
# obj.index  # 行标签索引
# obj.columns  # 列标签索引
# obj.values  # 对象值，二维ndarray数组

# DataFrame常用方法：
# obj.drop([],axis=0,1)  # 按标签名删除obj的行(axis=0),或列(axis=1)
# obj.to_dict(orient="records")  # 将二维数据按行转换成字典形式，常用于sklearn特征提取中(字典形式)
# eg:print(x_3_1.drop(index=["a"],inplace=True))

# DataFrame整体情况查看：
# obj.head(num)  # 显示头num行，默认5行
# obj.tail(num)  # 显示尾num行，默认5行
# obj.info()  # 相关信息概览：行数、行索引、列数、列索引、列非空值个数、列类型、内存占用
# obj.describe()  # 相关统计信息：计数、均值、标准差、最大值、四分位数、最小值

# 排序
# obj.sort_value(by=列索引,asscending=False)按某列的值进行排序,默认升序，ascending=True
print(x_3_1.sort_values(by="age",ascending=False))  # 按第二列降序排列
