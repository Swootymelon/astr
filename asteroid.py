import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS

class Asteroid(CircleShape):
    def __init__(self, position=None, velocity=None, radius=20):
        self.velocity = velocity
        super().__init__(position, velocity, radius)
        self.velocity = velocity
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-180, 180)  # Degrees per second
        self.color = "white"
    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt 

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
        
            split_angle = random.uniform(20, 50)
            
            # Create two new velocity vectors
            vel1 = self.velocity.rotate(split_angle) * 1.2
            vel2 = self.velocity.rotate(-split_angle) * 1.2
            
            # Calculate new radius
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # Create two new smaller asteroids
            Asteroid(position=self.position, velocity=vel1, radius=new_radius)
            Asteroid(position=self.position, velocity=vel2, radius=new_radius)
        self.kill()
        return     
