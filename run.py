import pygame
import random
import numpy as np

from satellite import *
from planet import *

pygame.init()

'''the distance between earth and sun is 150 million km
taking this distance in account the screen size is kept at 1 : 100,000 ratio)
'''
screen = pygame.display.set_mode((1500, 800)) 
pygame.display.set_caption("Bitches of Gravity")

background = pygame.image.load("beautiful-milky-way-night-sky.jpg")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

planet_list = [Planet() for i in range(1,random.randint(2,10))]

for planet in planet_list:
    planet.define_position_of_planet()

satellites_list = [Satellite() for i in range(1,random.randint(2,10))]

velocity_list = []
for satellite in satellites_list:
    distance_list = []
    acceleration_list = []

    resultant = np.array([0.0,0.0]) 

    satellite.define_initial_velocity()
    velocity_list.append(satellite.initial_velocity) 
    

    satellite.define_initial_position()
    for planet in planet_list:
        satellite.distance_between_satellite_and_planet(planet.position_of_planet)
        satellite.calculate_acceleration_due_to_gravity(planet.mass)
        distance_list.append(satellite.distance)
        acceleration_list.append(satellite.acceleration_due_to_gravity)
    
    for g in acceleration_list:
        resultant += g
    print('\n')
    print(resultant)
    print('\n')
    print(distance_list)
    print('\n')
print(velocity_list)


velocity = 0.05

clock = pygame.time.Clock()


#game loop
running = True
while running:
    dt = clock.tick(30)   # * 0.01 * 30

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for planet in planet_list:
       screen.blit(planet.image, (planet.position_of_planet[0], planet.position_of_planet[1]))
    
    #screen.blit(planet.image, (planet.position_of_planet[0], planet.position_of_planet[1]))

    for satellite in satellites_list:
        screen.blit(satellite.image, (satellite.position_of_satellite[0], satellite.position_of_satellite[1]))
    
    for satellite in satellites_list:
        satellite.position_of_satellite += int(velocity * dt)


    pygame.display.update()
