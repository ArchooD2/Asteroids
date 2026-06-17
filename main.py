import pygame,sys
from constants import SCREEN_SIZE
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from particle import Particle

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particles = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    Particle.containers = (updatable, drawable, particles)
    AsteroidField.containers = (updatable)
    AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)
    print(SCREEN_SIZE)
    print(f"Screen width: {SCREEN_SIZE[0]}, Screen height: {SCREEN_SIZE[1]}")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        log_state()
        dt = clock.tick(60) /1000
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                running = False
                break

        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    break

if __name__ == "__main__":
    main()
