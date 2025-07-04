import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #player
    Player.containers = (updateable, drawable)
    #Asteroid
    Asteroid.containers = (asteroids, updateable, drawable)
    #asteroid field
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH /2 , SCREEN_HEIGHT/ 2)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        
        screen.fill((0, 0, 0)) #bgd game

        player.draw(screen) # player



        for game in drawable:
            game.draw(screen)

        pygame.display.flip() #bgd
        dt = clock.tick(60) / 1000 #fps

if __name__ == "__main__":
    main()
