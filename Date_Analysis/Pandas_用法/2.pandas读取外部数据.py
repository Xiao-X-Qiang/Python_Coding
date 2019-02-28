import pandas as pd
from pymysql import connect
from pymongo import MongoClient
import string

# 读取本地文件
# 第一列
data_1 = pd.read_csv("./dogNames2.csv")
print(data_1)

# 读取mysql
my_conn = connect(host="localhost",user="root",password="root",port=3306,database="jing_dong",charset="utf8")
sql_query = "select * from goods;"
data_2 = pd.read_sql(sql_query,my_conn)
print(data_2)

# 读取Mongodb
client = MongoClient()
collections = client["test1"]["stu"]
data_3 = list(collections.find())
print(pd.Series(data_3))

