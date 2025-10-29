import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Juego")
clock = pygame.time.Clock()

class Command:
    def execute(self, player):
        pass

class MoveUp(Command):
    def execute(self, player):
        player.y -= player.speed

class MoveDown(Command):
    def execute(self, player):
        player.y += player.speed

class MoveLeft(Command):
    def execute(self, player):
        player.x -= player.speed

class MoveRight(Command):
    def execute(self, player):
        player.x += player.speed


class InputHandler:
    # Revisa una tecla y pasa el control si no es la suya.
    def __init__(self, key, command, next_handler=None):
        self.key = key
        self.command = command
        self.next = next_handler

    # Ciclo para el manejador de la tecla
    def handle(self, keys, player):
        moved = False
        if keys[self.key]:
            self.command.execute(player)
            moved = True
        elif self.next:
            moved = self.next.handle(keys, player)
        return moved


class Player:
    # Creacion del jugador en sus respectivas proporciones
    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.size = 30
        self.color = (0, 255, 100)
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def keep_inside(self):
        # Limitar movimiento dentro de los bordes
        if self.x < 0:
            self.x = 0
        if self.x + self.size > WIDTH:
            self.x = WIDTH - self.size
        if self.y < 0:
            self.y = 0
        if self.y + self.size > HEIGHT:
            self.y = HEIGHT - self.size


class Enemy:
    # Creacion de los enemigos (bolas)
    # Posicion y velocidad aleatoria
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-100, -10)
        self.size = random.randint(10, 20)
        self.color = (255, 0, 0)
        self.speed = random.randint(2, 5)

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-100, -10)
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def get_rect(self):
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)


player = Player()
enemies = [Enemy() for _ in range(10)]

# Crear cadena de responsabilidades (letras)
handler_chain = InputHandler(
    pygame.K_w, MoveUp(),
    InputHandler(
        pygame.K_s, MoveDown(),
        InputHandler(
            pygame.K_a, MoveLeft(),
            InputHandler(
                pygame.K_d, MoveRight(), None
            )
        )
    )
)


running = True
game_over = False
started = False  # Control para que las bolas inicien solo tras moverse
font = pygame.font.SysFont(None, 48)

while running:
    screen.fill((30, 30, 40))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Procesar entrada
        moved = handler_chain.handle(keys, player)
        if moved:
            started = True

        player.keep_inside()

        # Actualizar enemigos solo después del primer movimiento
        if started:
            for e in enemies:
                e.update()
                e.draw()

        player.draw()

        # Verificar colisión
        if started:
            player_rect = player.get_rect()
            for e in enemies:
                if player_rect.colliderect(e.get_rect()):
                    game_over = True
                    break
    else:
        text = font.render("GAME OVER", True, (255, 100, 100))
        screen.blit(text, text.get_rect(center=screen.get_rect().center))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
