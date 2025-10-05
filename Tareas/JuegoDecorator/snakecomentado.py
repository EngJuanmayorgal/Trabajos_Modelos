import turtle   # Librería para gráficos con tortuga
import time     # Librería para manejar pausas de tiempo
import random   # Librería para generar números aleatorios

# Lista de colores posibles para la serpiente, comida y fondo (excepto black)
COLORS = [
    "red", "green", "blue", "yellow", "purple",
    "orange", "pink", "cyan", "magenta", "lime",
    "turquoise", "gold", "brown", "white", "gray"
]

# Colores posibles para el fondo (sin blanco ni negro)
BACKGROUND_COLORS = [c for c in COLORS if c not in ("white", "black")]

# Función utilitaria para escoger colores aleatorios
def random_different_colors(exclude=None, count=1, pool=None):
    pool = pool or COLORS   # Si no dan pool, usar COLORS
    pool = [c for c in pool if c != "black"]  # Eliminar negro siempre
    exclude = exclude or []  # Lista de colores a excluir
    available = [c for c in pool if c not in exclude]  # Lista de válidos

    if not available:
        available = [c for c in pool if c not in exclude] or pool[:]

    if count >= len(available):
        return random.sample(available, len(available))

    return random.sample(available, count)

# -------------------
# Decoradores
# -------------------
class Decorador:
    def aplicar(self, game):
        raise NotImplementedError

class DecoradorFondo(Decorador):
    # Decorador que cambia el color del fondo
    def aplicar(self, game):
        exclude = [game.snake.body_color, game.food.food.color()[0]]
        new_bg = random_different_colors(exclude=exclude, count=1, pool=BACKGROUND_COLORS)[0]
        game.screen.bgcolor(new_bg)
        game.scoreboard.update_decorator("Decorador: Cambio de fondo")

class DecoradorSerpiente(Decorador):
    # Decorador que cambia el color de la serpiente
    def aplicar(self, game):
        exclude = [game.screen.bgcolor(), game.food.food.color()[0], "black"]
        new_color = random_different_colors(exclude=exclude, count=1)[0]
        if new_color == "black":
            new_color = "gray"
        game.snake.change_body_color(new_color)
        game.scoreboard.update_decorator("Decorador: Cambio de color de la serpiente")

class DecoradorReducirCuerpo(Decorador):
    # Decorador que elimina los segmentos del cuerpo
    def aplicar(self, game):
        for seg in game.snake.segments:
            seg.goto(1000, 1000)
        game.snake.segments.clear()
        game.scoreboard.update_decorator("Decorador: Reducción de cuerpo")

# -------------------
# Clase Snake
# -------------------
class Snake:
    def __init__(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.goto(0, 0)
        self.direction = "stop"
        self.segments = []
        self.body_color = "gray"

    def move(self):
        # Mueve los segmentos para seguir la cabeza
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        if len(self.segments) > 0:
            self.segments[0].goto(self.head.xcor(), self.head.ycor())

        if self.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.direction == "right":
            self.head.setx(self.head.xcor() + 20)

    def grow(self):
        # Agrega nuevos segmentos al cuerpo
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        color_to_use = self.body_color if self.body_color != "black" else "gray"
        new_segment.color(color_to_use)
        new_segment.penup()

        if self.segments:
            x = self.segments[-1].xcor()
            y = self.segments[-1].ycor()
        else:
            hx, hy = self.head.xcor(), self.head.ycor()
            if self.direction == "up":
                x, y = hx, hy - 20
            elif self.direction == "down":
                x, y = hx, hy + 20
            elif self.direction == "left":
                x, y = hx + 20, hy
            elif self.direction == "right":
                x, y = hx - 20, hy
            else:
                x, y = hx - 20, hy

        new_segment.goto(x, y)
        self.segments.append(new_segment)

    def change_body_color(self, color):
        # Cambia el color del cuerpo
        if color == "black":
            color = "gray"
        self.body_color = color
        for seg in self.segments:
            seg.color(color)

    def reset(self):
        # Reinicia la serpiente al centro de la pantalla
        time.sleep(1)
        self.head.goto(0, 0)
        self.direction = "stop"
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.body_color = "gray"

    # Metodos de direccion evitando ir en las direcciones de 180 grados
    def go_up(self):
        if self.direction != "down":
            self.direction = "up"
    def go_down(self):
        if self.direction != "up":
            self.direction = "down"
    def go_left(self):
        if self.direction != "right":
            self.direction = "left"
    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

# -------------------
# Clase Food
# -------------------
class Food:
    def __init__(self):
        # Crea la comida
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.penup()
        self.refresh(exclude_colors=[])

    def refresh(self, exclude_colors=None):
        # Cambia la posicion y el color de la comida
        exclude_colors = exclude_colors or []
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.food.goto(x, y)

        new_color = random_different_colors(exclude=exclude_colors, count=1)[0]
        if new_color == "black":
            new_color = "gold"
        self.food.color(new_color)

    def distance(self, snake_head):
        return self.food.distance(snake_head)

# -------------------
# Clase Scoreboard
# -------------------
class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0

        # Tortuga para mostrar el puntaje
        self.writer = turtle.Turtle()
        self.writer.speed(0)
        self.writer.color("white")
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.goto(0, 260)
        self.update()

        # Tortuga para mostrar el nombre del decorador usado
        self.writer_decorador = turtle.Turtle()
        self.writer_decorador.speed(0)
        self.writer_decorador.color("white")
        self.writer_decorador.penup()
        self.writer_decorador.hideturtle()
        self.writer_decorador.goto(0, 230)

        # Tortuga pra el mensaje de Game Over
        self.game_over_writer = turtle.Turtle()
        self.game_over_writer.speed(0)
        self.game_over_writer.color("red")
        self.game_over_writer.penup()
        self.game_over_writer.hideturtle()

        self.game_over_visible = False

    def update(self):
        # Actualiza el puntaje 
        self.writer.clear()
        self.writer.write(
            f"Score: {self.score}     High Score: {self.high_score}",
            align="center",
            font=("courier", 24, "normal"),
        )

    def update_decorator(self, message): 
        # Muestra en pantalla el decorador que se usa
        self.writer_decorador.clear()
        self.writer_decorador.write(
            message,
            align="center",
            font=("courier", 16, "italic"),
        )

    def clear_decorator(self):
        # Limpia el texto del decorador actual usado
        self.writer_decorador.clear()

    def increase(self):
        # Suma los puntos correspondientes y actualiza el puntaje de record (si es necesario)
        self.score += 10
        if self.score > self.high_score:
            self.high_score = self.score
        self.update()

    def reset(self):
        # Reinicia el putuntaje despues de chocar sin borrar el record
        self.score = 0
        self.update()
        self.clear_decorator()

    def game_over(self):
        # Hace saltar el mensaje de Game Over
        self.game_over_writer.goto(0, 0)
        self.game_over_writer.write(
            "GAME OVER",
            align="center",
            font=("courier", 36, "bold"),
        )
        self.game_over_visible = True

    def clear_game_over(self):
        # Elimina el mensaje de Game Over
        self.game_over_writer.clear()
        self.game_over_visible = False

# -------------------
# Clase Game
# -------------------
class Game:
    def __init__(self):
        # Configuraciones de la ventana de juego
        self.delay = 0.1
        self.screen = turtle.Screen()
        self.screen.title("Snake con Decoradores y Colores (Game Over con Space)")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

        # Diccionario de los decoradores
        self.decoradores = {
            3: DecoradorFondo(),
            4: DecoradorSerpiente(),
            5: DecoradorReducirCuerpo()
        }

        self.screen.listen()
        self.screen.onkeypress(self.snake.go_up, "Up")
        self.screen.onkeypress(self.snake.go_down, "Down")
        self.screen.onkeypress(self.snake.go_left, "Left")
        self.screen.onkeypress(self.snake.go_right, "Right")
        self.screen.onkeypress(self.clear_game_over_message, "space")

    def clear_game_over_message(self):
        # Permite reiniciar el juego si el mensaje de Game Over esta en pantalla
        if self.scoreboard.game_over_visible:
            self.scoreboard.clear_game_over()
            self.snake.reset()
            self.scoreboard.reset()
            self.screen.bgcolor("black")

    def check_collisions(self):
        # Verificacion de si la serpiente choca con las parades o su mismo cuerpo
        if (
            self.snake.head.xcor() > 280
            or self.snake.head.xcor() < -280
            or self.snake.head.ycor() > 280
            or self.snake.head.ycor() < -280
        ):
            if not self.scoreboard.game_over_visible:
                self.scoreboard.game_over()

        for segment in self.snake.segments:
            if segment.distance(self.snake.head) < 20:
                if not self.scoreboard.game_over_visible:
                    self.scoreboard.game_over()
                break

    def check_food(self):
        # Detecta si la serpiente come
        if self.food.distance(self.snake.head) < 20:
            self.snake.grow()
            self.scoreboard.increase()

            # Aplica un decorador de forma aleatoria
            roll = random.randint(0, 5)
            if roll in self.decoradores:
                self.decoradores[roll].aplicar(self)
            else:
                self.scoreboard.clear_decorator()
            self.food.refresh(exclude_colors=[self.snake.body_color, self.screen.bgcolor()])

    def update_loop(self):
        # Ciclo principal: Actualiza la pantalla y controla los choques
        try:
            self.screen.update()
            if not self.scoreboard.game_over_visible:
                self.snake.move()
                self.check_food()
                self.check_collisions()
            self.screen.ontimer(self.update_loop, int(self.delay * 1000))
        except turtle.Terminator:
            print("Ventana cerrada. Saliendo.")

    def run(self):
        # Reinicio del bucle principal del juego
        self.update_loop()
        self.screen.mainloop()

# -------------------
# Punto de entrada
# -------------------
if __name__ == "__main__":
    game = Game()
    game.run()
