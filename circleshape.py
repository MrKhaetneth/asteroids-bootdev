import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def collides_with(self, other: "CircleShape"):
        pos_self = self.position
        pos_oth = other.position
        distance = pos_self.distance_to(pos_oth)
        return distance < (self.radius + other.radius)