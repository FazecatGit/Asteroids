import pygame
from circleshape import CircleShape
from constants import *
import random
from player import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
          
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate (random_angle) * 1.2
        velocity2 = self.velocity.rotate (-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = velocity1
        b2 = Asteroid(self.position.x, self.position.y, new_radius,)
        b2.velocity = velocity2



          