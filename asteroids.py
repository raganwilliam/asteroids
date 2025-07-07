import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):

        vector = self.position + (self.velocity * dt)

        self.position = vector


    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)


        new_radius = self.radius - ASTEROID_MIN_RADIUS

        pos_asteroid_velocity = self.velocity.rotate(random_angle)
        neg_asteroid_velocity = self.velocity.rotate(-random_angle)

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = 1.2 * pos_asteroid_velocity
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = 1.2 * neg_asteroid_velocity
            

            
        ### self.asteroid_field.spawn(new_radius, old_position, pos_asteroid.velocity)
        ### self.asteroid_field.spawn(new_radius, old_position, neg_asteroid.velocity)
