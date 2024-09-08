import pygame

class Enemy:
    def __init__(self, position, health, speed):
        self.position = position  # (x, y) tuple for the enemy's position
        self.health = health  # The health points of the enemy
        self.speed = speed  # How fast the enemy moves
        self.alive = True  # Track if the enemy is still alive

    def move(self, target_position):
        # Move the enemy towards the target position
        if self.position[0] < target_position[0]:
            self.position = (self.position[0] + self.speed, self.position[1])
        elif self.position[0] > target_position[0]:
            self.position = (self.position[0] - self.speed, self.position[1])
        
        if self.position[1] < target_position[1]:
            self.position = (self.position[0], self.position[1] + self.speed)
        elif self.position[1] > target_position[1]:
            self.position = (self.position[0], self.position[1] - self.speed)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def draw(self, screen):
        # Draw the enemy (example representation as a red rectangle)
        pygame.draw.rect(screen, (255, 0, 0), (*self.position, 20, 20))  # Red rectangle