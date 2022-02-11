
import pygame, sys, pygame.locals#1
pygame.init()#2

window= pygame.display.set_mode((500, 400), 0, 32)#3
pygame.display.set_caption("Paint")#4
BLACK = (0, 0, 0)#5
WHITE = (255, 255, 255)#6
RED = (255, 0, 0)#7
GREEN = (0, 255, 0)#8
BLUE = (0, 0, 255)#9

circle=pygame.Surface((100, 100))#20
circle.fill((0, 0, 0))#21
pygame.draw.circle(circle, GREEN, (50, 50), 25, 0)#22
circle.set_colorkey((0, 0, 0))#23
rects={'circle': circle.get_rect()}# object
rects['circle'].centerx=100#position
rects['circle'].centery=100#position

while True:#29
    for event in pygame.event.get():#30
        if event.type==pygame.locals.QUIT:#31
            pygame.quit()#32
            sys.exit()#33
    for rect in rects:#34
            if rect=='circle':#40
                rects['circle'].centerx=150#41
                rects['circle'].centery=150#42
    window.fill(WHITE)#45
    window.blit(circle, rects['circle'])#49
    pygame.time.Clock().tick(40)#50
    pygame.display.update()#51