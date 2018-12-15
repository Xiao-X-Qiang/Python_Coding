import pygame

import plane_sprites as ps


class PlaneGame(object):
    """飞机大战主动游戏"""
    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(ps.SCREEN_RECT.size)

        # 2.创建时钟
        self.clock = pygame.time.Clock()

        # 3.调用私有方法创建精灵组
        self.__creat_sprites()

        # 4.设置定时器事件 -- 创建敌机
        pygame.time.set_timer(ps.CREAT_ENEMY_EVENT, 1000)

        # 5.设置英雄飞机发射子弹事件
        pygame.time.set_timer(ps.HERO_FIRE_EVENT, 500)

    def star_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新频率
            self.__set_clock()

            # 2.事件监听
            self.__event_handler()

            # 3.碰撞检测
            self.__check_collide()

            # 4.更新、绘制精灵组
            self.__update_sprites()

            # 5.更新显示
            pygame.display.update()

    def __creat_sprites(self):
        # 创建背影精灵和精灵组
        bg1 = ps.BackGround()
        bg2 = ps.BackGround(True)
        # bg2.rect.y = -bg2.rect.height

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵及精灵组
        self.hero = ps.Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == ps.CREAT_ENEMY_EVENT:
                # 1.创建敌机精灵
                enemy = ps.Enemy()

                # 2.添加至敌机精灵组
                self.enemy_group.add(enemy)

            elif event.type == ps.HERO_FIRE_EVENT:
                self.hero.fire()
            # 键盘事件 方法一：
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
        # 键盘事件，方法二：
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键的索引值 1
        if keys_pressed[pygame.K_RIGHT]:
            # print('向右移动')
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):

        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)


        # 2.敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies):
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    def __set_clock(self):
        self.clock.tick(ps.FRAME_PER_SEC)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 游戏开始
    game.star_game()


