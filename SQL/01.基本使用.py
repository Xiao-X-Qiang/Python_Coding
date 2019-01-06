

import pymysql

conn = pymysql.connect(host="localhost", port=3306, database="jing_dong", user="root", password="root", charset="utf8")

cusor = conn.cursor()

cusor.execute("select * from goods")

print(cusor.fetchmany(4))

cusor.close()
conn.close()