import turtle  # Librería para gráficos con tortuga
import time  # Librería para manejar pausas de tiempo
import random  # Librería para generar números aleatorios

# Paleta de colores posibles para la serpiente, comida y fondo (excepto black)
COLORS = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "orange",
    "pink",
    "cyan",
    "magenta",
    "lime",
    "turquoise",
    "gold",
    "brown",
    "white",
    "gray",
]

# Colores posibles para el fondo (sin blanco ni negro)
BACKGROUND_COLORS = [c for c in COLORS if c not in ("white", "black")]


# -------------------
# Función utilitaria para escoger colores aleatorios
# -------------------
def random_different_colors(exclude=None, count=1, pool=None):
    pool = pool or COLORS  # si no dan pool, usar COLORS
    pool = [c for c in pool if c != "black"]  # eliminar negro siempre
    exclude = exclude or []  # lista de colores a excluir
    available = [c for c in pool if c not in exclude]  # lista de válidos

    # si no hay colores válidos, usar toda la pool
    if not available:
        available = [c for c in pool if c not in exclude] or pool[:]

    # si count >= len(available), devolver todos
    if count >= len(available):
        return random.sample(available, len(available))

    return random.sample(available, count)  # escoger 'count' colores


# -------------------
# Decoradores
# -------------------
class Decorador:
    def aplicar(self, game):
        raise NotImplementedError  # método abstracto, se implementa en hijos


class DecoradorFondo(Decorador):
    def aplicar(self, game):
        # Cambia el fondo evitando color de serpiente y comida
        exclude = [game.snake.body_color, game.food.food.color()[0]]
        new_bg = random_different_colors(
            exclude=exclude, count=1, pool=BACKGROUND_COLORS
        )[0]
        game.screen.bgcolor(new_bg)


class DecoradorSerpiente(Decorador):
    def aplicar(self, game):
        # Cambia el color del cuerpo de la serpiente evitando fondo y comida
        exclude = [game.screen.bgcolor(), game.food.food.color()[0], "black"]
        new_color = random_different_colors(exclude=exclude, count=1)[0]
        if new_color == "black":  # por seguridad
            new_color = "gray"
        game.snake.change_body_color(new_color)


class DecoradorReducirCuerpo(Decorador):
    def aplicar(self, game):
        # Elimina todos los segmentos (reset visual del cuerpo)
        for seg in game.snake.segments:
            seg.goto(1000, 1000)  # manda fuera de pantalla
        game.snake.segments.clear()


# -------------------
# Clase Snake (la serpiente)
# -------------------
class Snake:
    def __init__(self):
        self.head = turtle.Turtle()  # cabeza
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("white")  # cabeza siempre blanca
        self.head.penup()  # no dibujar líneas
        self.head.goto(0, 0)  # posición inicial en centro
        self.direction = "stop"  # dirección inicial
        self.segments = []  # lista de segmentos del cuerpo
        self.body_color = "gray"  # color inicial del cuerpo

    def move(self):
        # mover los segmentos del cuerpo de atrás hacia adelante
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        # primer segmento sigue la cabeza
        if len(self.segments) > 0:
            self.segments[0].goto(self.head.xcor(), self.head.ycor())

        # mover cabeza según dirección
        if self.direction == "up":  # Arriba
            self.head.sety(self.head.ycor() + 20)
        elif self.direction == "down":  # Abajo
            self.head.sety(self.head.ycor() - 20)
        elif self.direction == "left":  # Izquierda
            self.head.setx(self.head.xcor() - 20)
        elif self.direction == "right":  # Derecha
            self.head.setx(self.head.xcor() + 20)

    def grow(self):
        # Crear nuevo segmento del cuerpo
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        color_to_use = self.body_color if self.body_color != "black" else "gray"
        new_segment.color(color_to_use)
        new_segment.penup()

        # Posicionar nuevo segmento detrás del último
        if self.segments:
            x = self.segments[-1].xcor()
            y = self.segments[-1].ycor()
        else:
            hx, hy = self.head.xcor(), self.head.ycor()
            # coloca el primer segmento detrás de la cabeza según dirección
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
        if color == "black":  # seguridad extra
            color = "gray"
        self.body_color = color
        for seg in self.segments:
            seg.color(color)

    def reset(self):
        # Reinicia la serpiente despues de algun choque
        time.sleep(1)
        self.head.goto(0, 0)
        self.direction = "stop"
        for seg in self.segments:
            seg.goto(1000, 1000)  # manda los segmentos fuera
        self.segments.clear()
        self.body_color = "gray"

    # Métodos de control de dirección (evitan giros 180°)
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
# Clase Food (la comida)
# -------------------
class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.penup()
        self.refresh(exclude_colors=[])

    def refresh(self, exclude_colors=None):
        exclude_colors = exclude_colors or []
        # Genera posición aleatoria dentro del área
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.food.goto(x, y)

        # color aleatorio que no coincida con los excluidos
        new_color = random_different_colors(exclude=exclude_colors, count=1)[0]
        if new_color == "black":
            new_color = "gold"
        self.food.color(new_color)

    def distance(self, snake_head):
        return self.food.distance(snake_head)


# -------------------
# Clase Scoreboard (marcador)
# -------------------
class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.writer = turtle.Turtle()  # tortuga para escribir texto
        self.writer.speed(0)
        self.writer.color("white")
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.goto(0, 260)  # posición superior
        self.update()

        # tortuga adicional para el cartel de GAME OVER
        self.game_over_writer = turtle.Turtle()
        self.game_over_writer.speed(0)
        self.game_over_writer.color("red")
        self.game_over_writer.penup()
        self.game_over_writer.hideturtle()

    def update(self):
        # Actualizacion del puntaje
        self.writer.clear()
        self.writer.write(
            f"Score: {self.score}     High Score: {self.high_score}",
            align="center",
            font=("courier", 24, "normal"),
        )

    def increase(self):
        # Aumenta el puntaje
        self.score += 10

        # Actualiza el record (si es necesario)
        if self.score > self.high_score:
            self.high_score = self.score
        self.update()

    def reset(self):
        # Reinicia el puntaje
        self.score = 0
        self.update()

    def game_over(self):
        self.game_over_writer.goto(0, 0)
        self.game_over_writer.write(
            "GAME OVER",
            align="center",
            font=("courier", 36, "bold"),
        )


# -------------------
# Clase Game (bucle principal del juego)
# -------------------
class Game:

    def __init__(self):
        self.delay = 0.1
        self.screen = turtle.Screen()
        self.screen.title("Snake con Decoradores y Colores (corregido)")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)  # desactivar animación automática

        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()

        # Diccionario de decoradores aplicables
        self.decoradores = {
            3: DecoradorFondo(),
            4: DecoradorSerpiente(),
            5: DecoradorReducirCuerpo(),
        }

        # Controles de teclado
        self.screen.listen()
        self.screen.onkeypress(self.snake.go_up, "Up")
        self.screen.onkeypress(self.snake.go_down, "Down")
        self.screen.onkeypress(self.snake.go_left, "Left")
        self.screen.onkeypress(self.snake.go_right, "Right")

    def check_collisions(self):
        # Colisión con paredes
        if (
            self.snake.head.xcor() > 280
            or self.snake.head.xcor() < -280
            or self.snake.head.ycor() > 280
            or self.snake.head.ycor() < -280
        ):
            self.snake.reset()
            self.scoreboard.reset()
            self.screen.bgcolor("black")
            self.scoreboard.game_over()

        # Colisión con el propio cuerpo
        for segment in self.snake.segments:
            if segment.distance(self.snake.head) < 20:
                self.snake.reset()
                self.scoreboard.reset()
                self.screen.bgcolor("black")
                self.scoreboard.game_over()
                break

    def check_food(self):
        # Si la cabeza está cerca de la comida
        if self.food.distance(self.snake.head) < 20:
            self.snake.grow()  # crecer
            self.scoreboard.increase()  # subir puntaje

            # Tirar dado para aplicar decoradores
            roll = random.randint(0, 5)
            if roll in self.decoradores:
                self.decoradores[roll].aplicar(self)

            # refrescar comida con colores válidos
            self.food.refresh(
                exclude_colors=[self.snake.body_color, self.screen.bgcolor()]
            )

    def update_loop(self):
        try:
            self.screen.update()  # refrescar pantalla
            self.snake.move()  # mover serpiente
            self.check_food()  # verificar comida
            self.check_collisions()  # verificar colisiones
            # programar siguiente frame
            self.screen.ontimer(self.update_loop, int(self.delay * 1000))
        except turtle.Terminator:
            print("Ventana cerrada. Saliendo.")

    def run(self):
        self.update_loop()
        self.screen.mainloop()  # iniciar bucle principal


# -------------------
# Punto de entrada
# -------------------
if __name__ == "__main__":
    game = Game()
    game.run()
