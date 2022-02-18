import numpy as np
import pygame
import random
from assets import *

class Planet:
    def __init__(self):
        self.image = pygame.image.load("planet.png")

        self.density = random.randint(700, 6000)  # Unit - kg/m^3
        self.radius = random.randint(4500, 140000) # Unit - km

        volume = (4/3)*(3.142)*(self.radius ** 3)
        self.mass = self.density * volume

    def define_position_of_planet(self):

        px = random.randint(0,1000)
        py = random.randint(0,800)

        self.position_of_planet = np.array([px, py])






