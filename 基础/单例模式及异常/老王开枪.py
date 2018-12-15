

class Ren:

    def __init__(self,name):
        self.name=name
        self.xueliang=100
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
        self.xueliang-=shashangli

    def __str__(self):
        return '当前血量为：'+str(self.xueliang)


class Qiang:

    def __init__(self):
        self.danjia=None

    def lianjiedanjia(self,danjia):
        self.danjia=danjia


    def __str__(self):
        if not self.danjia:
            return '当前无弹夹'
        else:
            return '当前有弹夹'

    def she(self,diren):
        zidan=self.danjia.chuzidan()

        if zidan:
            zidan.shanghai(diren)


class Danjia:

    def __init__(self,rongliang):
        self.rongliang=rongliang
        self.rongnalist=[]

    def __str__(self):
        return "当前子弹数量为："+str(len(self.rongnalist))+'/'+str(self.rongliang)


    def baocunzidan(self,zidan):
        if len(self.rongnalist)<self.rongliang:
            self.rongnalist.append(zidan)

    def chuzidan(self):
        if len(self.rongnalist)>0:
            temp=self.rongnalist[-1]
            self.rongnalist.pop()
        else:
            print('没子弹了...')

        return temp
class Zidan:

    def __init__(self,shashangli):
        self.shashangli=shashangli


    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)



laowang=Ren('老王')

danjia=Danjia(20)

print(danjia)

zidan=Zidan(10)

i=0
while i<5:
    laowang.anzidan(danjia, zidan)
    i+=1

print(danjia)

qiang=Qiang()
print(qiang)

laowang.andanjia(qiang,danjia)
print(qiang)


laowang.naqiang(qiang)


diren=Ren('diren')
print(diren)

laowang.kaiqiang(diren)

print(diren)

laowang.kaiqiang(diren)

print(diren)




