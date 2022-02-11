import pygame
import sys
import os


#making planets
class Planet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        # self.images = pygame.transform.scale(img, (50, 30))
        img = pygame.image.load("planet.png")
        img = pygame.transform.scale(img, (150, 150))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

#making Satellite
class Satellite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load("sat.png")
        img = pygame.transform.scale(img, (90, 70))
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
backdrop = pygame.image.load("st.jpg")
backdropbox = world.get_rect()

#define planet
planet1 = Planet()   # spawn player
planet1.rect.x = 400   # go to x
planet1.rect.y = 500   # go to y
planet1_list = pygame.sprite.Group()
planet1_list.add(planet1)

#define Satellite
satellite1 = Satellite()   # spawn player
satellite1.rect.x = 100   # go to x
satellite1.rect.y = 100   # go to y
satellite1_list = pygame.sprite.Group()
satellite1_list.add(satellite1)


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
    planet1_list.draw(world)
    satellite1_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)






