
import pygame

from pygame.locals import *

import time #用于延时，减小CPU的使用率


#注：HeroPlane的bulletList[]中的子弹无限的增多，可能导致内存泄露；另外，循环删除列表时，连续删除相邻位置的元素会出现bug
#解决方法：先记录要删除的元素，然后一个个删除

class HeroPlane(object):

    def __init__(self,screen):
        #设置飞机的位置
        self.x=230
        self.y=600
        #设置要显示内容的窗口
        self.screen=screen

        self.imageName = './feiji/hero.gif'
        self.image = pygame.image.load(self.imageName).convert()

        #用来存储英雄飞机发射的所有子弹
        self.bulletList=[] 

    def display(self):
        #将飞机图片填充到窗口中
        self.screen.blit(self.image,(self.x,self.y))

        # 刷新飞机的同时，调用每一颗子弹的display()方法
        for bullet in self.bulletList:
            bullet.display()
            bullet.move() #修改子弹的位置

        print(len(self.bulletList))


        #删除无效的子弹
        needRemoveList=[]

        for tempbullet in self.bulletList:
            if tempbullet.judgeout():
                needRemoveList.append(tempbullet)

        for tempbullet in needRemoveList:
            self.bulletList.remove(tempbullet)

        # #修改所有子弹的位置 (修改属性，最好使用方法,此处 move() )
        # for bullet in self.bulletList:
        #     bullet.y -= 2

    #键盘按键的处理方法
    def keyhandle(self,keyvalue):
        if keyvalue.type == QUIT:
            print('exit')
            exit()
        elif keyvalue.type == KEYDOWN:
            if keyvalue.key == K_a or event.key == K_LEFT:
                self.moveLeft()
                print('left')
            elif keyvalue.key == K_d or event.key == K_RIGHT:
                self.moveRight()
                print('right')
            elif keyvalue.key == K_SPACE:
                self.sheBullet()
                print('space')


    def moveLeft(self):
        self.x -= 10
    def moveRight(self):
        self.x += 10

    def sheBullet(self):
        newBullet=Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)

class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+41
        self.y = y-16
        self.screen=screen
        self.imageName='./feiji/bullet-3.gif'
        self.image=pygame.image.load(self.imageName).convert()

    #修改子弹的位置，使其移动
    def move(self):
        self.y -= 2

    def display(self):
        # 将子弹图片填充到窗口中
        self.screen.blit(self.image, (self.x, self.y))

    def judgeout(self):
        if self.y < 1:
            return True
        else:
            return False





if __name__=='__main__':

    #1.创建窗口,用来显示内容
    screen=pygame.display.set_mode((480,720),0,32)

    #2.创建一个和窗口大小的图片，用以充当背影
    background=pygame.image.load('./feiji/background.png').convert()

    #创建一个飞机对象
    heroPlane=HeroPlane(screen)
    # x=0
    # y=0



    #3.将背影图片填充到窗口中
    while True:
        screen.blit(background, (0, 0))
        #screen.blit(hero, (x, y))
        heroPlane.display()

        #获取事件，比如键盘等
        for event in pygame.event.get():

            heroPlane.keyhandle(event)

        time.sleep(0.01)
        pygame.display.update()



