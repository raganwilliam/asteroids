import pygame
from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.reload = 0
        
        
    def rotate(self, dt):
        self.rotation = PLAYER_TURN_SPEED * dt + self.rotation

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def shoot(self):
        if self.reload > 0:
            velocity = 0
        else:
            self.bullet = Shot(self.position.x, self.position.y)
            velocity = pygame.Vector2(0,1)
            velocity = velocity.rotate(self.rotation)
            self.bullet.velocity = velocity * PLAYER_SHOOT_SPEED
            self.reload = PLAYER_SHOOT_COOLDOWN


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.reload = max(0, self.reload - dt)
    

    def draw(self, screen):

        pygame.draw.polygon(screen, "white", self.triangle(), 2)