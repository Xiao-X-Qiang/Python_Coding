import pygame

if __name__=='__main__':
    screen=pygame.display.set_mode((480,890),0,32)
    bgImageFile='./feiji/background.png'
    background=pygame.image.load(bgImageFile).convert()
