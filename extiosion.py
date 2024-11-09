import pygame
pygame.init()
screen= pygame.display.set_mode((400,500))
turn= False
while not turn:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
pygame.quit()