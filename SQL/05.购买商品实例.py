
from pymysql import connect


class JD(object):

    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user="root", password="root", database="jing_dong", charset="utf8")
        self.cusor = self.conn.cursor()

    def __del__(self):
        self.cusor.close()
        self.conn.close()

    def register(self):
        info = list()
        info.append(input("input your name :"))
        info.append(input("input your address :"))
        info.append(input("input your tel :"))
        info.append(input("input your passwd :"))
        self.cusor.execute("insert into customers values(default,%s,%s,%s,%s)", info)
        self.conn.commit()

    def login(self):
            info = list()
            info.append(input("input your name:"))
            info.append(input("input your passwd:"))

            self.cusor.execute("select * from customers where name=%s and passwd=%s", info)
            if len(self.cusor.fetchall()) == 1:
                return 1
            else:
                print("name or passwd error,please try again")

    def show_all_items(self):
        self.cusor.execute("select * from goods;")
        for temp in self.cusor:
            print(temp)

    def show_cates(self):
        self.cusor.execute("select name from goods_cates;")
        for temp in self.cusor:
            print(temp)

    def show_brands(self):
        self.cusor.execute("select name from goods_brands;")
        for temp in self.cusor:
            print(temp)

    def add_brands(self):
        item_brand = input("请输入品牌名称：")
        self.cusor.execute("""insert into goods_brands values(default, '%s');""" % item_brand)
        self.conn.commit()

    def show_info_by_name(self):
        name = input("请输入商品名：")
        # sql = """select * from goods_brands where name = "%s";"""%name
        # self.cusor.execute(sql)
        # print(self.cusor.fetchall())
        params = [name]
        sql = "select * from goods_brands where name = %s;"
        self.cusor.execute(sql, [name])
        print(self.cusor.fetchall())

    def exit_1(self):
        exit()

    @staticmethod
    def show_menu_regi_log():
        print("-----京东----")
        print("0:注册")
        print("1.登陆")
        return input("input your choice:")

    @staticmethod
    def show_meau():
        print("-----京东-----")
        print("1.查看所有信息：")
        print("2.查询分类信息：")
        print("3.查询品牌信息：")
        print("4.添加品牌信息：")
        print("5.根据商品名查询信息：")
        print("6.退出")
        return input("请选择：")

    def run(self):
        while True:
            choice1 = self.show_menu_regi_log()

            if choice1 == "0":
                self.register()
            if choice1 == "1":
                result = self.login()
                if result == 1:
                    break
        while True:
            choice = self.show_meau()
            if choice == "1":
                self.show_all_items()
            elif choice == "2":
                self.show_cates()
            elif choice == "3":
                self.show_brands()
            elif choice == "4":
                self.add_brands()
            elif choice == "5":
                self.show_info_by_name()
            elif choice == "6":
                self.exit_1()
            else:
                print("输入有误，请重新输入")


def main():

    jd = JD()
    jd.run()


if __name__ == "__main__":
    main()