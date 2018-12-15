# 标准模块
import random

# 第三方模块
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 创建敌机的定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1

# 刷新的帔率
FRAME_PER_SEC = 60


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=3):

        # 调用父类的初始化方法
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        """在垂直方向上运动"""
        self.rect.y += self.speed


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，并指定图片
        super().__init__("./images/enemy1.png")

        # 2.指定敌机的初始随机速度
        self.speed = random.randint(0,3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width- self.rect.width)

    def update(self):
        # 1.调用父类的方法，保持垂直方向飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，移出精灵组
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕，需要从精灵组中删除")
            # kill方法可以将精灵从所有的精灵组中移出，精灵也会被自动销毁
            self.kill()

    def __del__(self):
        # print("敌机挂了...%s"% self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        # 1.调用父类的方法，设置image&speed
        super().__init__("./images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹的精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed

        # 控制英雄不能移动屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")
        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置子弹精灵的位置
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i * 20
            # 3.添加至精灵组
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 调用父类的方法，设置图片及速度
        super().__init__("./images/bullet1.png", -2)

    def update(self, *args):
        # 调用父类的方法，子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁了...")


class BackGround(GameSprite):
    """游戏背影精灵"""

    def __init__(self, is_alt=False):

        # 1.调用父类的方法实现精灵的创建
        super().__init__("./images/background.png")
        # 2.判断是否是交替图像，是的话，设置初始位置
        if is_alt:
           self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类的方法
        super().update()

        # 2.判断是否移动屏幕，如果是，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class HeroPlane(pygame.sprite.Sprite):
    """英雄飞机的位置"""
    def __init__(self, image_name, speed=1, init_location=pygame.Rect(150, 600, 102, 126)):

        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = init_location
        self.speed = speed

    def update(self, *args):
        """垂直方向上运动"""
        self.rect.y -= 5
        if self.rect.y <= -126:
            self.rect.y = 700


