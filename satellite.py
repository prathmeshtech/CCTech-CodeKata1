import numpy as np
import random
import pygame

from assets import *

satellites = ["satellite_image (1).png", "satellite_image (2).png", "satellite_image (3).png", "satellite_image (4).png"]


class Satellite:
    def __init__(self):

        #self.image = pygame.image.load(random.choice(satellites))

        self.image = pygame.image.load("satellite_image (1).png")
        self.mass = random.randint(int(1.00 * 10e24),int(1000 * 10e24))  # unit - kg
 
    def define_initial_position(self):
        
        sx = random.randint(0,1000)     # unit - km
        sy = random.randint(0,800)

        self.position_of_satellite = np.array([sx, sy])

    def define_initial_velocity(self):
        '''fastest manmade satellite is '''

        ux = random.randint(1000,10000)   # unit - km/s
        uy = random.randint(1000,10000)

        self.initial_velocity = np.array([ux, uy])

    def distance_between_satellite_and_planet(self, position_of_planet):

        self.distance = (self.position_of_satellite - position_of_planet)*100000 #unit - km

    def calculate_acceleration_due_to_gravity(self, mass_of_planet):

        Gravitational_constant = 6.67 * 10e-11      #Unit - Nm^2/kg^2
        self.acceleration_due_to_gravity = (Gravitational_constant * mass_of_planet)/ ((self.distance*1000) ** 2) #unit- m/s^2

    def velocity_of_satellite(self, resultant_acceleration_due_to_gravity, t = 1):

        self.new_velocity = self.initial_velocity + resultant_acceleration_due_to_gravity * t 

        self.initial_velocity = self.new_velocity








