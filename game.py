import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Арканоид")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Классы
class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - 30
        self.speed = 7

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_speed = 3
        self.y_speed = 3

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x <= 0 or self.x >= WIDTH:
            self.x_speed = -self.x_speed
        if self.y <= 0:
            self.y_speed = -self.y_speed

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    def check_collision(self, paddle):
        if self.y + self.radius >= paddle.y and paddle.x <= self.x <= paddle.x + paddle.width:
            self.y_speed = -self.y_speed

class Brick:
    def __init__(self, x, y):
        self.width = 75
        self.height = 30
        self.x = x
        self.y = y
        self.hit = False

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    def check_collision(self, ball):
        if not self.hit and self.x <= ball.x <= self.x + self.width and self.y <= ball.y <= self.y + self.height:
            self.hit = True
            ball.y_speed = -ball.y_speed
            return True
        return False

# Создание объектов
paddle = Paddle()
ball = Ball()
bricks = [Brick(x*80 + 10, y*40 + 10) for x in range(9) for y in range(5)]

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("left")
    if keys[pygame.K_RIGHT]:
        paddle.move("right")

    ball.move()
    ball.check_collision(paddle)
    for brick in bricks:
        if brick.check_collision(ball):
            break

    screen.fill(BLACK)
    paddle.draw()
    ball.draw()
    for brick in bricks:
        if not brick.hit:
            brick.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()