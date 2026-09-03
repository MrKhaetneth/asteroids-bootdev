import random

import pygame

from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            color = "white", 
            center = self.position,
            radius = self.radius,
            width = LINE_WIDTH
        )
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = v1 * 1.2
            ast2.velocity = v2 * 1.2
        