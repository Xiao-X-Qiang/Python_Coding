# 1.实例1
# class human(object):
#
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#
#     def run(self):
#         self.weight -= 0.5
#
#     def eat(self):
#         self.weight += 1
#
#     def __str__(self):
#         return "%s的体重为：%.1f" % (self.name,self.weight)
#
#
#
# xiaoming = human("xiaoming",75.0)
#
# print(xiaoming)
#
# xiaomei = human('xiaomei',45)
#
# print(xiaomei)
#
# xiaoming.run()
# xiaomei.run()
# print(xiaoming)
# print(xiaomei)

#2.实例2

# class HourseIterm(object):
#
#     def __init__(self,name,area):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return "%s的占地面积为 %.2f" % (self.name,self.area)
#
#
# class House(object):
#
#     def __init__(self,house_type,area):
#         self.house_type = house_type
#         self.area = area
#         self.free_area = area
#         self.item_list = []
#
#     def __str__(self):
#         return ("户型：%s \n总面积为：%.2f \n剩余面积为：%.2f\n 家具有：%s "
#                 %(self.house_type,self.area,
#                   self.free_area,self.item_list))
#
#
#     def add_item(self,item):
#         print("要添加%s"%item)
#
#         #1.判断面积
#
#         if item.area > self.free_area:
#             print(" %s 家具太大，实在添不了了"% item.name)
#             return
#         #2.添加家具
#         else:
#             self.item_list.append(item.name)
#         #3.计算剩余面积
#
#         self.free_area -= item.area
#
# bed = HourseIterm('席梦',4)
# chest = HourseIterm("衣柜",2)
#
#
#
# house = House("两室一厅",90)
# print(house)
#
# # house.add_item(bed)
# house.add_item(chest)
#
# print(house)

#实例3

class Gun(object):

    def __init__(self,type):
        self.model = type
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count < 0:
            print("%s 没子弹了..." % self.model)
            return
        else:
            self.bullet_count -= 1
            print("%s 突突..." % self.model)

    def __str__(self):

        return "%s 还有 %d 子弹"%(self.model,self.bullet_count)


class Soldier(object):
    def __init__(self,name):
        self.name = name
        self.gun = None


    def fire(self):
        if self.gun is None:
            print("%s 没有枪..."%self.name)
            return
        print("冲啊...%s"%self.name)
        self.gun.add_bullet(30)
        self.gun.shoot()





ak47 = Gun("ak47")


xusanduo = Soldier("许三多")

xusanduo.gun = ak47

xusanduo.fire()






