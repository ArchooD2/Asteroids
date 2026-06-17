from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_KINDS
import random
import pygame
from logger import log_event
from particle import Particle

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self) -> None:
        log_event("asteroid_split")
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
        # create particles
        for _ in range(10):
            particle = Particle(self.position.x, self.position.y, new_radius / 10, lifetime=random.uniform(1.0, 2.0))
            particle.velocity = self.velocity.rotate(random.uniform(0, 360)) * random.uniform(0.5, 1.5)