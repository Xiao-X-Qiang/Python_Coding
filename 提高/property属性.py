class Foo(object):
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)

    # 定义property属性
    @property  # 此关键字，而且必须有一返回值
    def prop(self):
        return self.name


foo_obj = Foo("Xiao")
foo_obj.func()  # 调用实例方法
name = foo_obj.prop  # 调用property属性,实例方法属性化
