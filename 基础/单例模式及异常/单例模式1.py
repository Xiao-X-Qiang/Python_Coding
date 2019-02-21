

class Car(object):
    def __init__(self,name):
        self.name = name

    def move(self):
        print("move car")

    def __str__(self):
        return "ehllo"

    def __del__(self):
        print("del object")

    Flag = None


class Car1(object):
    def move(self):
        pass

class Audio(Car,Car1):

    new_flag = False  # 记录是否曾实例化
    init_flag = False  # 记录是否曾初始化
    self = None

    # 只实例化一次
    def __new__(cls, *args, **kwargs):
        if not cls.new_flag:
            cls.self = super().__new__(cls)
            cls.new_flag = True
            return cls.self
        return cls.self

    # 只初始化一次
    def __init__(self, name):
        if not self.init_flag:
            self.name = name
            self.init_flag = True






    def move(self):
        super().move()
        print("i am audio")



audio = Audio("Tom")
print(id(audio))
print(audio.name)

print("*"*15)

audio1 = Audio("Jerry")
print(id(audio1))
print(audio1.name)