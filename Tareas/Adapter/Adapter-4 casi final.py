import turtle
import time
import random
import tkinter

# Lista de colores posibles para la serpiente, comida y fondo (excepto black)
COLORS = [
    "red", "green", "blue", "yellow", "purple",
    "orange", "pink", "cyan", "magenta", "lime",
    "turquoise", "gold", "brown", "white", "gray"
]

# Colores posibles para el fondo (sin blanco ni negro)
BACKGROUND_COLORS = [c for c in COLORS if c not in ("white", "black")]

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
    def aplicar(self, game):
        exclude = [game.snake.body_color, game.food.food.color()[0]]
        new_bg = random_different_colors(exclude=exclude, count=1, pool=BACKGROUND_COLORS)[0]
        game.screen.bgcolor(new_bg)
        game.scoreboard.update_decorator("Decorador: Cambio de fondo")

class DecoradorSerpiente(Decorador):
    def aplicar(self, game):
        exclude = [game.screen.bgcolor(), game.food.food.color()[0], "black"]
        new_color = random_different_colors(exclude=exclude, count=1)[0]
        if new_color == "black":
            new_color = "gray"
        game.snake.change_body_color(new_color)
        game.scoreboard.update_decorator("Decorador: Cambio de color de la serpiente")

class DecoradorReducirCuerpo(Decorador):
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

        # En modo teclado la dirección la controla direction; en modo mouse direction puede ser "stop"
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

        # Colocar el nuevo segmento en la posición del último segmento (si existe)
        if self.segments:
            x = self.segments[-1].xcor()
            y = self.segments[-1].ycor()
        else:
            # Si no hay segmentos, colocarlo ligeramente detrás de la cabeza según la dirección
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
                # // modificado: si no hay direction (por ejemplo en modo mouse), colocar el segmento
                # // en la posición actual de la cabeza (temporal) y dejaremos una 'invulnerabilidad' para evitar choque inmediato.
                x, y = hx, hy

        new_segment.goto(x, y)
        self.segments.append(new_segment)

    def change_body_color(self, color):
        if color == "black":
            color = "gray"
        self.body_color = color
        for seg in self.segments:
            seg.color(color)

    def reset(self):
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
# Adapter Pattern
# -------------------
class ControlAdapter:
    def conectar_controles(self, game):
        raise NotImplementedError

class KeyboardAdapter(ControlAdapter):
    def conectar_controles(self, game):
        game.screen.listen()
        game.screen.onkeypress(game.snake.go_up, "Up")
        game.screen.onkeypress(game.snake.go_down, "Down")
        game.screen.onkeypress(game.snake.go_left, "Left")
        game.screen.onkeypress(game.snake.go_right, "Right")
        game.screen.onkeypress(game.clear_game_over_message, "space")

class MouseAdapter(ControlAdapter):  # // nuevo
    def conectar_controles(self, game):
        game.screen.listen()
        game.screen.onkeypress(game.clear_game_over_message, "space")
        self.game = game
        # Iniciar seguimiento continuo del mouse
        self._follow_mouse()

    def _follow_mouse(self):
        try:
            g = self.game
            # Coordenadas del puntero respecto al canvas (tkinter)
            x = g.screen.cv.winfo_pointerx() - g.screen.cv.winfo_rootx()
            y = g.screen.cv.winfo_pointery() - g.screen.cv.winfo_rooty()
            # Ajustar al centro del canvas
            x = x - g.screen.window_width() // 2
            y = g.screen.window_height() // 2 - y

            # Limitar objetivo dentro de los bordes jugables
            max_coord = 280
            x = max(-max_coord, min(max_coord, x))
            y = max(-max_coord, min(max_coord, y))

            head = g.snake.head
            # Mover la cabeza suavemente hacia el puntero
            if not g.scoreboard.game_over_visible:
                dx = x - head.xcor()
                dy = y - head.ycor()
                distancia = (dx**2 + dy**2) ** 0.5
                if distancia > 1:
                    head.setheading(head.towards(x, y))
                    # Paso proporcional, evita saltos grandes
                    paso = min(20, max(6, distancia / 5))
                    head.forward(paso)

            # Seguir llamando cada ~20 ms
            g.screen.ontimer(self._follow_mouse, 20)
        except turtle.Terminator:
            pass

class ControlSelector:  # //
    def __init__(self, screen):
        self.screen = screen
        self.selection = None

    def seleccionar(self):
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.color("white")
        writer.penup()
        writer.goto(0, 50)
        writer.write("Selecciona modo de control:\n\n[F] Flechas\n[M] Mouse",
                     align="center", font=("Courier", 18, "bold"))

        def select_keyboard():
            self.selection = "keyboard"
            writer.clear()

        def select_mouse():
            self.selection = "mouse"
            writer.clear()

        self.screen.listen()
        self.screen.onkeypress(select_keyboard, "f")
        self.screen.onkeypress(select_mouse, "m")

        while self.selection is None:
            self.screen.update()

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
        # Notamos que los listeners directos se configuran desde el adapter seleccionado
        self.screen.onkeypress(self.clear_game_over_message, "space")  # botón general para limpiar game over

        self.control_adapter = None
        self.invulnerable_ticks = 0  # Nuevo: ticks para evitar colisiones justo después de crecer

    def seleccionar_control(self):
        selector = ControlSelector(self.screen)
        selector.seleccionar()
        if selector.selection == "keyboard":
            self.control_adapter = KeyboardAdapter()
            # Asegurar que la serpiente use el movimiento por pasos
            self.snake.direction = "stop"
        elif selector.selection == "mouse":
            self.control_adapter = MouseAdapter()
            # En modo mouse evitamos que direction mueva la cabeza
            self.snake.direction = "stop"

        # Conectar controles via adapter
        self.control_adapter.conectar_controles(self)

    def clear_game_over_message(self):
        # Permite reiniciar el juego si el mensaje de Game Over esta en pantalla
        if self.scoreboard.game_over_visible:
            self.scoreboard.clear_game_over()
            self.snake.reset()
            self.scoreboard.reset()
            self.screen.bgcolor("black")

    def check_collisions(self):
        # Modificacion: si hay invulnerabilidad de frames no chequear colisiones (evita game over justo al comer)
        if self.invulnerable_ticks > 0:
            self.invulnerable_ticks -= 1
            return

        if (
            self.snake.head.xcor() > 280
            or self.snake.head.xcor() < -280
            or self.snake.head.ycor() > 280
            or self.snake.head.ycor() < -280
        ):
            if not self.scoreboard.game_over_visible:
                self.scoreboard.game_over()

        # Modificacion: si el control actual es el MouseAdapter, no chequear colisiones con el cuerpo
        if isinstance(self.control_adapter, MouseAdapter):
            return

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

            # // nuevo: después de crecer, dar unos frames de "invulnerabilidad" para evitar choque inmediato
            # // (especialmente necesario en modo mouse donde la cabeza puede quedar encima del nuevo segmento)
            self.invulnerable_ticks = max(2, int(0.25 / self.delay))

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
                # Mover segmentos y cabeza en cada frame
                self.snake.move()
                self.check_food()
                self.check_collisions()
            self.screen.ontimer(self.update_loop, int(self.delay * 1000))
        except turtle.Terminator:
            print("Ventana cerrada. Saliendo.")

    def run(self):
        # Reinicio del bucle principal del juego
        self.seleccionar_control()  # //
        self.update_loop()
        self.screen.mainloop()

# -------------------
# Punto de entrada
# -------------------
if __name__ == "__main__":
    game = Game()
    game.run()
