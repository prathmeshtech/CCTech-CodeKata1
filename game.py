import pygame
import sys
import os

'''
Variables
'''
#making planets

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        #self.images = pygame.transform.scale(img, (50, 30))
        img = pygame.image.load("planet.png")
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

worldx = 1240
worldy = 720
fps = 40  # frame rate
ani = 4   # animation cycles
main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

# put Python classes and functions here
'''
Setup
'''
# main window
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load("stage.jpg")
backdropbox = world.get_rect()

#define planet
player = Player()   # spawn player

player.rect.x = 100   # go to x
player.rect.y = 100   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)


'''
Main Loop
'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)






