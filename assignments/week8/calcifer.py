import pygame
import random
from sys import exit

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Class Example')
clock = pygame.time.Clock()


class Calcifer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load and size the image
        self.image = pygame.image.load("calcifer.png").convert_alpha()
        self.image.set_colorkey((255, 0, 0))
        self.image = pygame.transform.scale(self.image, (100, 100))

        # Position at the bottom center
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 500  # SCREEN_HEIGHT - 100

        # Movement physics constants
        self.vel_y = -15
        self.vel_x = random.choice([-5, 5])
        self.gravity = 0.6

    def update(self):
        # Apply gravity and move
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        self.rect.x += self.vel_x

        # Bounce off the floor
        if self.rect.y >= 500:
            self.rect.y = 500
            self.vel_y = random.uniform(-18, -12)
            self.vel_x = random.uniform(-6, 6)

            # Bounce off left/right walls
        if self.rect.x <= 0 or self.rect.x >= 700:  # 700 is SCREEN_WIDTH - 100
            self.vel_x *= -1

        # Setup the sprite group and add one Kitty


all_sprites = pygame.sprite.Group()
all_sprites.add(Calcifer())

# Game Loop
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # Game logic
    all_sprites.update()

    # Drawing
    screen.fill((255, 0, 0))  # Cyan background
    all_sprites.draw(screen)
    pygame.display.flip()