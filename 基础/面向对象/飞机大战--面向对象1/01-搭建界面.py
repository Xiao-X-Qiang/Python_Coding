
import pygame

from pygame.locals import *

if __name__=='__main__':

    #1.创建窗口,用来显示内容
    screen=pygame.display.set_mode((480,890),0,32)

    #2.创建一个和窗口大小的图片，用以充当背影
    background=pygame.image.load('./feiji/background.png').convert()

    #3.将背影图片填充到窗口中
    while True:
        screen.blit(background, (0, 0))
        pygame.display.update()



