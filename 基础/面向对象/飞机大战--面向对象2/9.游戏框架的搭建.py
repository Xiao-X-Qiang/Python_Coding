

import pygame

import plane_sprites as ps

pygame.init()

# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700))


# 1.加载图像数据
bg = pygame.image.load('./images/background.png')
hero = pygame.image.load('./images/me1.png')

# 2.blit绘制图像
screen.blit(bg, (0, 0))
screen.blit(hero, (150, 300))

# 3.更新屏幕的显示
#pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)





# 1.创建敌机的精灵
enemy = ps.GameSprite("./images/enemy1.png")
enemy1 = ps.GameSprite("./images/enemy1.png",2)

# 2.创建敌机的精灵组
enemy_group = pygame.sprite.Group(*(enemy, enemy1))





# 游戏循环，注意：游戏窗口不需要重复创建
while True:
    # 刷新帧率
    clock.tick(60)

    # 游戏事件监听
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:

            # 卸载所有的模块
            pygame.quit()

            # 退出系统
            print("退出游戏")
            exit()

    # 2.修改飞机的位置
    hero_rect.y -= 2
    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))  # 重绘背影，遮挡之前的图像，以免残影
    screen.blit(hero,hero_rect)


    # 让精灵组调用两个方法
    # update:让组中所有的精灵更新位置
    enemy_group.update()

    # draw:在screen上绘制所有的精灵
    enemy_group.draw(screen)



    # 4.调用update方法更新显示
    pygame.display.update()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
