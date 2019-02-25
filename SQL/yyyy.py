
from pymysql import connect



class SQL_(object):
    def __init__(self):
        self.conn = connect(host="localhost",user="root",password="root",database="jing_dong",port=3306,charset="utf8")
        self.cursor = self.conn.cursor()

    def get_data(self):
        self.cursor.execute("select * from goods;")
        result = self.cursor.fetchall()
        print(result)

    def add_data(self):
        data = []
        while True:
            temp = input("input your message what you want:")
            if temp == "exit":
                break
            data.append(temp)

        self.cursor.execute("insert into goods_brands values(0,%s),(0,%s)",data)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()




def main():
    sql = SQL_()
    # sql.get_data()
    sql.add_data()

if __name__ == '__main__':
    main()