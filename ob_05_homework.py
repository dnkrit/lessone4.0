import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Класс для ракетки
class Paddle:
    def __init__(self, x, y):
        self.width = 10
        self.height = 100
        self.x = x
        self.y = y
        self.speed = 6

    def move(self, up=True):
        if up:
            self.y -= self.speed
        else:
            self.y += self.speed

        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

# Класс для мяча
class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.x_speed = 4
        self.y_speed = 4

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.y <= 0 or self.y >= HEIGHT:
            self.y_speed = -self.y_speed

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

    def check_collision(self, paddle):
        if paddle.x <= self.x <= paddle.x + paddle.width and paddle.y <= self.y <= paddle.y + paddle.height:
            self.x_speed = -self.x_speed

# Создание объектов
paddle1 = Paddle(30, (HEIGHT - 100) // 2)
paddle2 = Paddle(WIDTH - 40, (HEIGHT - 100) // 2)
ball = Ball()

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.move(up=True)
    if keys[pygame.K_s]:
        paddle1.move(up=False)
    if keys[pygame.K_UP]:
        paddle2.move(up=True)
    if keys[pygame.K_DOWN]:
        paddle2.move(up=False)

    ball.move()
    ball.check_collision(paddle1)
    ball.check_collision(paddle2)

    if ball.x <= 0 or ball.x >= WIDTH:
        ball = Ball()

    screen.fill(BLACK)
    paddle1.draw()
    paddle2.draw()
    ball.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()