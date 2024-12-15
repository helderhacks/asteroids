import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # game loop starts.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # iterate through updatable objects.
        for obj in updatable:
            # .update() them.
            obj.update(dt)
            for asteroid in asteroids:
                if asteroid.collision_detect(player):
                    print("Game over!")
                    sys.exit()
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collision_detect(shot):
                        asteroid.split()
                        shot.kill()


        screen.fill("black")

        # iterate through drawable objects.
        for obj in drawable:
            # .draw() them.
            obj.draw(screen)

        pygame.display.flip()

        dt = time.tick(60) / 1000
if __name__ == "__main__":
  main()
