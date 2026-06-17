from circleshape import CircleShape
from constants import LINE_WIDTH
import random
import pygame

class Particle(CircleShape):
    def __init__(self, x, y, radius, lifetime=1.0):
        super().__init__(x, y, radius)
        self.lifetime = lifetime
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
    