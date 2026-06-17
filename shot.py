from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, SHOT_RADIUS, PLAYER_SHOT_SPEED
class Shot(CircleShape):
    def __init__(self, x: float, y: float, rotation: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOT_SPEED
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt