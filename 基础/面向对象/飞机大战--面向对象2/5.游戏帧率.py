

import pygame


pygame.init()

# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700), 0, 32)


# 1.加载图像数据
bg = pygame.image.load('./images/background.png')
hero = pygame.image.load('./images/me1.png')

# 2.blit绘制图像
screen.blit(bg, (0, 0))
screen.blit(hero, (100, 100))

# 3.更新屏幕的显示
pygame.display.update()


# 创建时钟对象
clock = pygame.time.Clock()

# 游戏循环，注意：游戏窗口不需要重复创建

while True:
    # 刷新帧率
    clock.tick(60)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()

