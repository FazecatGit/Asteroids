import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH /2 , SCREEN_HEIGHT/ 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill((0, 0, 0)) #bgd game

        player.draw(screen) # player

        pygame.display.flip() #bgd
    
        dt = clock.tick(60) / 1000 #fps

        player.update(dt)
        player.move(dt)


if __name__ == "__main__":
    main()
