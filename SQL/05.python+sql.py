# python DB API访问数据库
from pymysql import connect

# connect-->cursor-->执行sql-->关闭cursor-->关闭connect-->结束
# connect 用以连接数据库
# cursor 用以操作数据库


class Sql_Code(object):
    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user="root", password="root", database="jing_dong", # 打开连接
                            charset="utf8")
        self.cursor = self.conn.cursor()  # 打开游标

    def get_data(self):
        # 1.连接数据库、打开游标、查询、关闭游标及连接
        self.cursor.execute("select * from goods;")  # 执行的结果保存在cusor对象中
        # fetchall() 取一条数据；fetchmany(num) 取num条数据；fetchall() 取所有数据；其中数据是以元组的元组的形式
        result = self.cursor.fetchall()
        print(result)

    def modify_data(self):
        # 2.连接数据库、打开游标、插入[删除、修改]、关闭游标及连接
        self.cursor.execute("insert into goods(name,cate_id) values(%s,2)", [input("请输入要插入的商品名：")])
        self.conn.commit()  # 对于变动数据库数据时，执行execute()后，再执行commit()进行事务提交，方才真正修改数据库；
        # self.conn.rollback()  # 如果不变动数据库，执行该语句，则抛弃execute()所作的修改；

    def __del__(self):
        self.cursor.close()  # 关闭游标
        self.conn.close()  # 关闭连接


def main():
    sql_code = Sql_Code()
    sql_code.modify_data()
    sql_code.get_data()


if __name__ == '__main__':
    main()
