from circleshape import *
import pygame
from constants import *
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def bullet_collides_with(self, other):
        distance = (self.position - other.position).length()
        return distance <= self.radius + other.radius
