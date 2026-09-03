import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state, log_event
from player import Player
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Grouping 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    # Player object
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    dt = 0.0
    clock = pygame.time.Clock()
    
    # Drawing game
    while True:
        log_state()
        for event in pygame.event.get():
            # Making the close button on window actually work
            if event.type == pygame.QUIT: 
                return 
        
        dt = clock.tick(60) / 1000
        
        screen.fill("black") # Black background screen
        
        for thing in drawable:
            thing.draw(screen) # Draw player sprite on screen
        updatable.update(dt) # Update rotation and position
        
        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for bullet in shots:
                if ast.collides_with(bullet):
                    log_event("asteroid_shot")
                    bullet.kill()
                    ast.split()
        
        pygame.display.flip() # Render

if __name__ == "__main__":
    main()
