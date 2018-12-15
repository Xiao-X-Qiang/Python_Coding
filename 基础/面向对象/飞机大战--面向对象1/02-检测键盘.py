
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

        #获取事件，比如键盘等
        for event in pygame.event.get():

            #判断是否点击了退出按钮
            if event.type == QUIT:
                print('exit')
                exit()
            #判断是否按下了键
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                elif event.key == K_SPACE:
                    print('space')


        pygame.display.update()



