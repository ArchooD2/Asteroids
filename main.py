import pygame
from constants import SCREEN_SIZE
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)
    print(SCREEN_SIZE)
    print(f"Screen width: {SCREEN_SIZE[0]}, Screen height: {SCREEN_SIZE[1]}")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            pass
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        log_state()
        dt = clock.tick(60) /1000
        


if __name__ == "__main__":
    main()
