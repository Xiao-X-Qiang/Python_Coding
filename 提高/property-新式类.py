class Goods(object):
    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property  # # 参数；返回值；装饰符；
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter  # 参数；装饰符
    def price(self, value):
        self.original_price = value

    @price.deleter  # 参数
    def price(self):
        print("--del--")
        del self.original_price

obj = Goods()
print(obj.price)  # 获取商品价格
obj.price = 200   # 修改商品原价
print(obj.price)
del obj.price     # 删除商品原价
