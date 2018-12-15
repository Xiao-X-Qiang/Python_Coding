


import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load('./feiji/background.png').convert()

screen.blit(screen, (0, 0))

pygame.display.update()

while True:
    pass

pygame.quit()