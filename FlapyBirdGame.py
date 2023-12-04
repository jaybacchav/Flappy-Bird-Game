import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 50, 50
PIPE_WIDTH = 70
GRAVITY = 0.25
BIRD_SPEED = 5
JUMP_AMOUNT = 7

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load('C:/Users/com/Downloads/Bird.png')
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))
pipe_img = pygame.image.load('C:/Users/com/Downloads/Pipe.png')

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0    
        self.img = bird_img

    def jump(self):
        self.velocity = -JUMP_AMOUNT

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        win.blit(self.img, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.top = random.randint(50, 400)
        self.bottom = self.top + 150
        self.x = WIDTH
        self.width = PIPE_WIDTH
        self.passed = False

    def move(self):
        self.x -= BIRD_SPEED

    def draw(self):
        win.blit(pipe_img, (self.x, 0), (0, 0, self.width, self.top))
        win.blit(pipe_img, (self.x, self.bottom), (0, self.top + 150, self.width, HEIGHT - self.bottom))

# Game loop
def game():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.move()

        # Check collisions
        for pipe in pipes:
            if bird.x + bird_img.get_width() > pipe.x and bird.x < pipe.x + pipe.width:
                if bird.y < pipe.top or bird.y + bird_img.get_height() > pipe.bottom:
                    running = False

                if not pipe.passed:
                    pipe.passed = True
                    score += 1

            if pipe.x + pipe.width < 0:
                pipes.remove(pipe)

            pipe.move()

        if bird.y > HEIGHT or bird.y < 0:
            running = False

        if pipes[-1].x < WIDTH - 200:
            pipes.append(Pipe())

        win.fill(WHITE)
        bird.draw()
        for pipe in pipes:
            pipe.draw()

        pygame.display.update()

    pygame.quit()
    quit()

game()
