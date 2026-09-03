import pygame

from constants import *
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Grouping 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    # Player object
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
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
        
        pygame.display.flip() # Render

if __name__ == "__main__":
    main()
