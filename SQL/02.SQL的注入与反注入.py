
import pymysql

conn = pymysql.connect(host="localhost", port=3306, database="jing_dong", user="root", password="root", charset="utf8")

cusor = conn.cursor()

# SQL注入
# item_name = input("input the name of goods:")

# 只要where的条件满足要求，都可以被注入，如下面三种方式
# cusor.execute("select * from goods where name = '%s'"% item_name)  # 输入 ' or 2=2 or '  会被注入显示所有商品信息
# cusor.execute("select * from goods where name = \"%s\""% item_name)  # 输入 " or 2=2 or "  会被注入显示所有商品信息
# cusor.execute("select * from goods where name = %s"% item_name)  # 输入 "" or 2=2  也会被注入显示所有商品信息

# -- 当输入 ' or 2=2 or '  时，会显示goods的所有数据，这是因为：
# -- select * from goods where name = ''or 2=2 or''  A or B or C ，A，C虽然不满足，但B(2=2)满足，此时显示所有数据


# SQL反注入，将输入的数据放入列表，使sql语句参数化，conn.cursor.execute()进行sql语句的拼接
item = []
item.append(input("输入商品的名称："))
cusor.execute("select * from goods where name = %s", item)

print(cusor.fetchall())

cusor.close()
conn.close()
