from circleshape import *
from constants import *
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = pygame.Vector2(0, 1).rotate(random_angle)
        vector2= pygame.Vector2(0, 1).rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        first_asteroid.velocity = vector1 * 1.2
        second_asteroid.velocity = vector2 * 1.2
