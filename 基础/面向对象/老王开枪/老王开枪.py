

class Ren:
    def __init__(self,name):
        self.name=name
        self.xue=100
        self.qiang=None

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)
    def naqiang(self,qiang):
        self.qiang=qiang
    def kaiqiang(self,diren):
        self.qiang.she(diren)

    def diaoxue(self,shashangli):
        self.xue-=shashangli

    def __str__(self):
        return self.name+'当前剩余血量为：'+str(self.xue)

    pass

class Qiang:

    def __init__(self):
        self.danjia=None


    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia=danjia

    def __str__(self):
        if self.danjia:
            return "当前有弹夹"
        else:
            return "当前无弹夹"

    def she(self,diren):
        zidan=self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print('没有子弹了，呵呵。。。')

class Danjia:
    def __init__(self,rongliang):
        self.rongliang = rongliang
        self.rongnalist=[]
    def baocunzidan(self,zidan):
        if len(self.rongnalist)<self.rongliang:
            self.rongnalist.append(zidan)
    def __str__(self):
        return "弹夹当前的子弹数量为：%s/%s"%(str(len(self.rongnalist)),str(self.rongliang))

    def chuzidan(self):
        if len(self.rongnalist)>0:
            zidan= self.rongnalist[-1]
            self.rongnalist.pop()
            return zidan
        else:
            return None


class Zidan:

    def __init__(self,shashangli):
        self.shashangli=shashangli
    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)



laowang=Ren('老王')

danjia=Danjia(20)
print(danjia)


i=0
while i<5:
    zidan=Zidan(5)
    laowang.anzidan(danjia,zidan)
    i+=1


print(danjia)


qiang=Qiang()


laowang.andanjia(qiang,danjia)
print(qiang)


diren=Ren('diren')
print(diren)

laowang.naqiang(qiang)

laowang.kaiqiang(diren)

print(diren)
print(danjia)