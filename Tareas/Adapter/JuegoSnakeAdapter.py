import turtle
import time
import random

# ------------------- Colores -------------------
COLORS = [
    "red", "green", "blue", "yellow", "purple",
    "orange", "pink", "cyan", "magenta", "lime",
    "turquoise", "gold", "brown", "white", "gray"
]
BACKGROUND_COLORS = [c for c in COLORS if c not in ("white", "black")]

def random_different_colors(exclude=None, count=1, pool=None):
    pool = pool or COLORS
    pool = [c for c in pool if c != "black"]
    exclude = exclude or []
    available = [c for c in pool if c not in exclude]
    if not available:
        available = [c for c in pool if c not in exclude] or pool[:]
    if count >= len(available):
        return random.sample(available, len(available))
    return random.sample(available, count)

# ------------------- Decoradores -------------------
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

# ------------------- Snake -------------------
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

# ------------------- Food -------------------
class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.penup()
        self.refresh(exclude_colors=[])

    def refresh(self, exclude_colors=None):
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

# ------------------- Scoreboard -------------------
class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.writer = turtle.Turtle()
        self.writer.speed(0)
        self.writer.color("white")
        self.writer.penup()
        self.writer.hideturtle()
        self.writer.goto(0, 260)
        self.update()
        self.writer_decorador = turtle.Turtle()
        self.writer_decorador.speed(0)
        self.writer_decorador.color("white")
        self.writer_decorador.penup()
        self.writer_decorador.hideturtle()
        self.writer_decorador.goto(0, 230)
        self.game_over_writer = turtle.Turtle()
        self.game_over_writer.speed(0)
        self.game_over_writer.color("red")
        self.game_over_writer.penup()
        self.game_over_writer.hideturtle()
        self.game_over_visible = False

    def update(self):
        self.writer.clear()
        self.writer.write(f"Score: {self.score}     High Score: {self.high_score}",
                          align="center", font=("courier", 24, "normal"))

    def update_decorator(self, message):
        self.writer_decorador.clear()
        self.writer_decorador.write(message, align="center", font=("courier", 16, "italic"))

    def clear_decorator(self):
        self.writer_decorador.clear()

    def increase(self):
        self.score += 10
        if self.score > self.high_score:
            self.high_score = self.score
        self.update()

    def reset(self):
        self.score = 0
        self.update()
        self.clear_decorator()

    def game_over(self):
        self.game_over_writer.goto(0, 0)
        self.game_over_writer.write("GAME OVER", align="center", font=("courier", 36, "bold"))
        self.game_over_visible = True

    def clear_game_over(self):
        self.game_over_writer.clear()
        self.game_over_visible = False

# ------------------- Adapter Pattern -------------------
class ControlAdapter:  # //
    def conectar_controles(self, game):
        raise NotImplementedError

class KeyboardAdapter(ControlAdapter):  # //
    def conectar_controles(self, game):
        game.screen.listen()
        game.screen.onkeypress(game.snake.go_up, "Up")
        game.screen.onkeypress(game.snake.go_down, "Down")
        game.screen.onkeypress(game.snake.go_left, "Left")
        game.screen.onkeypress(game.snake.go_right, "Right")
        game.screen.onkeypress(game.clear_game_over_message, "space")

class MouseAdapter(ControlAdapter):  # //
    def conectar_controles(self, game):
        game.screen.listen()
        game.screen.onkeypress(game.clear_game_over_message, "space")
        game.screen.onscreenclick(lambda x, y: self._move_to_mouse(game, x, y))

    def _move_to_mouse(self, game, x, y):
        game.snake.head.setheading(game.snake.head.towards(x, y))
        game.snake.head.goto(x, y)

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

# ------------------- Game -------------------
class Game:
    def __init__(self):
        self.delay = 0.1
        self.screen = turtle.Screen()
        self.screen.title("Snake con Decoradores y Patrón Adapter")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.decoradores = {
            3: DecoradorFondo(),
            4: DecoradorSerpiente(),
            5: DecoradorReducirCuerpo()
        }
        self.control_adapter = None  # //

    def seleccionar_control(self):  # //
        selector = ControlSelector(self.screen)
        selector.seleccionar()
        if selector.selection == "keyboard":
            self.control_adapter = KeyboardAdapter()
        elif selector.selection == "mouse":
            self.control_adapter = MouseAdapter()
        self.control_adapter.conectar_controles(self)

    def clear_game_over_message(self):
        if self.scoreboard.game_over_visible:
            self.scoreboard.clear_game_over()
            self.snake.reset()
            self.scoreboard.reset()
            self.screen.bgcolor("black")

    def check_collisions(self):
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
        if self.food.distance(self.snake.head) < 20:
            self.snake.grow()
            self.scoreboard.increase()
            roll = random.randint(0, 5)
            if roll in self.decoradores:
                self.decoradores[roll].aplicar(self)
            else:
                self.scoreboard.clear_decorator()
            self.food.refresh(exclude_colors=[self.snake.body_color, self.screen.bgcolor()])

    def update_loop(self):
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
        self.seleccionar_control()  # //
        self.update_loop()
        self.screen.mainloop()

# ------------------- Main -------------------
if __name__ == "__main__":
    game = Game()
    game.run()
