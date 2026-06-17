from constants import PLAYER_RADIUS, PLAYER_SHOT_COOLDOWN_SECONDS, LINE_WIDTH, PLAYER_SPEED, PLAYER_MVT_SPEED, PLAYER_SHOT_SPEED
from circleshape import CircleShape
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
    
    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, width=LINE_WIDTH)
    
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_SPEED * dt
    
    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MVT_SPEED * dt
    
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shot_cooldown -= dt
    
    def shoot(self) -> None:
        from shot import Shot
        if self.shot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y, self.rotation)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shot_cooldown = PLAYER_SHOT_COOLDOWN_SECONDS