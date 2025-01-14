import pygame
from circleshape import CircleShape
import random

class Shot(CircleShape):
    def __init__(self, position=None, velocity=None, radius=5):
        self.velocity = pygame.Vector2(velocity)
        super().__init__(position, velocity, radius)
        self.velocity = pygame.Vector2(velocity)
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-180, 180)  # Degrees per second
        self.color = "white"
    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt 

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
