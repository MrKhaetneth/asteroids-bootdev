import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    rotation: int = 0
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shoot_cooldown = 0
    
    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, color = "white", points = self.triangle())
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        initial_dir = pygame.Vector2(0, 1).rotate(self.rotation)
        new_position = initial_dir * PLAYER_SPEED * dt
        self.position += new_position

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            self.shoot_cooldown -= dt
    
    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        else:
            bullet = Shot(self.position.x, self.position.y)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS