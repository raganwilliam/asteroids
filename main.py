import sys
import pygame

from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *


updatable = pygame.sprite.Group()
# all the objects that can be updated

drawable = pygame.sprite.Group()
# all the objects that can be drawn

asteroids = pygame.sprite.Group()
# contains all of the asteroids

shots = pygame.sprite.Group()
# contains all shots

Player.containers = (updatable, drawable)

Asteroid.containers = (asteroids, updatable, drawable)

AsteroidField.containers = (updatable,)

Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    player = Player(x,y)

    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        dt = clock.tick(60)/1000
    
        
        updatable.update(dt)

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision(bullet) == True:
                    asteroid.split()
                    bullet.kill()


        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                sys.exit()



        for render in drawable:
            render.draw(screen)


        pygame.display.flip()



if __name__ == "__main__":
    main()