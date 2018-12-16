class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

    # 定义一个属性，当对这个money设置值时调用setMoney,当获取值时调用getMoney
    money = property(getMoney, setMoney)  


a = Money()
a.money = 100  # 调用setMoney方法
print(a.money)  # 调用getMoney方法
