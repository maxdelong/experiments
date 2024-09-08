import pygame
import sys
from tower_defense_game.tower import Tower
from tower_defense_game.enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tower Defense Game")

# Main game loop
def main():
    clock = pygame.time.Clock()
    tower = Tower((400, 300), range=150, damage=20, cooldown=500)
    enemies = [Enemy((50, 50), health=100, speed=2)]
    target_position = (750, 550)

    while True:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 100, 0))

        # Update and draw enemies
        for enemy in enemies:
            enemy.move(target_position)
            if enemy.alive:
                enemy.draw(screen)
            else:
                enemies.remove(enemy)

        # Tower attacks enemies
        tower.shoot(enemies, current_time)

        # Draw tower
        tower.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()