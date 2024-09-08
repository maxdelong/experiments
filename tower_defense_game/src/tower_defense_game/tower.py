import pygame

class Tower:
    def __init__(self, position, range, damage, cooldown):
        self.position = position  # (x, y) tuple for the tower's position
        self.range = range  # How far the tower can shoot
        self.damage = damage  # How much damage the tower deals
        self.cooldown = cooldown  # Time between shots
        self.last_shot_time = 0  # Keeps track of when the tower last shot

    def can_shoot(self, current_time):
        # Determine if the tower can shoot based on the cooldown
        return current_time - self.last_shot_time >= self.cooldown

    def is_in_range(self, enemy_position):
        # Calculate distance between the tower and the enemy
        dx = self.position[0] - enemy_position[0]
        dy = self.position[1] - enemy_position[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return distance <= self.range

    def shoot(self, enemies, current_time):
        # Check if the tower can shoot
        if self.can_shoot(current_time):
            for enemy in enemies:
                if self.is_in_range(enemy.position):
                    enemy.take_damage(self.damage)
                    self.last_shot_time = current_time
                    break



    def draw(self, screen):
        # Draw the tower (example representation as a circle)
        pygame.draw.circle(screen, (0, 0, 255), self.position, 20)  # Blue circle