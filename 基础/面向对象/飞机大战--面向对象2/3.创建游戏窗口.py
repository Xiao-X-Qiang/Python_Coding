

import pygame

pygame.init()

#创建游戏主窗口
screen = pygame.display.set_mode((480,700))


#游戏循环，注意：游戏窗口不需要重复创建
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()




pygame.quit()