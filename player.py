import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.color = "white"
        self.speed = 200
        self.rotation = 0
        self.rotation_speed = 180  
        self.shoot_timer = 0 
  
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle())

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= self.rotation_speed * dt  # Rotate counterclockwise
            
        if keys[pygame.K_d]:
            self.rotation += self.rotation_speed * dt  # Rotate clockwise
            
        if keys[pygame.K_w]:
            self.move_forward(dt)
        if keys[pygame.K_s]:
            self.move_backward(dt)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        self.shoot_timer -= dt    
        self.velocity *= 0.99
        self.position += self.velocity * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1)
        shot_velocity = forward.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        #shot_velocity = forward * PLAYER_SHOOT_SPEED
        new_shot = Shot(position=pygame.Vector2(self.position), velocity=shot_velocity)
        
    def move_forward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * self.speed * dt
        
    def move_backward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity -= forward * self.speed * dt

    def rotate_left(self, dt):
        self.rotation_speed -= 180 * dt

    def rotate_right(self, dt):
        self.rotation_speed += 180 * dt 

    def stop(self):
        self.velocity = pygame.Vector2(0, 0)
        self.rotation_speed = 0 

    def accelerate(self, dt):
        self.move_forward(dt)

    def decelerate(self, dt):
        self.move_backward(dt)          