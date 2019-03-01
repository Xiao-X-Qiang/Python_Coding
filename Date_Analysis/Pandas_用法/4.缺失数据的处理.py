import pandas as pd
import numpy as np

# 缺失数据的处理
# 缺失数据指的是：NaN、0

data = pd.DataFrame(np.arange(24).reshape((4, 6)), index=list("ABCD"), columns=list("UVWXYZ"))

data.iloc[0, 0] = np.nan
data.iloc[0, -1] = np.nan
data.iloc[-1, 2] = np.nan
data.iloc[1, -2] = 0
print(data.astype(float))

# 1.对于NaN
# 文件或数据库中的数据字段缺失或者为None时，在pandas中表现为NaN
# 推荐在保存数据时，对于没有值的字段，默认缺失或者默认为None
# 判断数据是否为NaN:pd.isnull(obj),pd.notnull(obj)
print(pd.isnull(data.iloc[0]))

# 处理手段：
# 1.1 删除NaN所在的行或列 obj.dropna(axis=[0|1],how=["any"|"all"],[inplace = [True|False]])
# 其中，axis选择行或列，how:含有NaN或全为NaN时删除，默认all，inplace:是否本地替换，默认False
print(data.dropna(axis=0, how="any"))
# 1.2 替换NaN,obj.fillna(data) 将NaN替换为data
print(data.fillna(222))

# 2.对于 0
# 数据中的0有时表示此字段缺失(此时会影响该字段的某些统计信息，如使本字段的平均数偏小)，有时表示真实值，明确何种类型再处理
data[data == 0] = 333
print(data)
