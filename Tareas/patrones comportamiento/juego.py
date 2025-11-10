import pygame
import random
from abc import ABC, abstractmethod

# ================================
#  STRATEGY PATTERN
# ================================
class AttackStrategy(ABC):
    """Interfaz Strategy: define cómo se calcula un ataque."""
    @abstractmethod
    def attack(self, base_damage):
        pass


class AggressiveStrategy(AttackStrategy):
    """Ataque agresivo: más daño + un poco aleatorio."""
    def attack(self, base_damage):
        return int(base_damage * 1.5 + random.randint(0, 3))


class DefensiveStrategy(AttackStrategy):
    """Ataque defensivo: menos daño."""
    def attack(self, base_damage):
        return int(base_damage * 0.8)


class BalancedStrategy(AttackStrategy):
    """Ataque equilibrado: daño base + pequeño aleatorio."""
    def attack(self, base_damage):
        return base_damage + random.randint(0, 2)


# ================================
#  OBSERVER PATTERN
# ================================
class EventManager:
    """Sujeto: Notifica eventos a sus observadores."""
    def __init__(self):
        self._observers = []

    def register(self, obs):
        """Agrega un observador."""
        self._observers.append(obs)

    def notify(self, event_type, **kwargs):
        """Notifica a todos los observadores."""
        for obs in self._observers:
            obs.update(event_type, **kwargs)


class ConsoleLogger:
    """Observador concreto: imprime eventos en consola."""
    def update(self, event_type, **kwargs):
        print(f"[EVENT] {event_type} | {kwargs}")


# ================================
#  ENTITY
# ================================
class Entity:
    """Entidad base: héroe o enemigo."""
    def __init__(self, name, hp, base_damage, strategy=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.base_damage = base_damage
        # Si no pasan estrategia, se usa balanced
        self.strategy = strategy or BalancedStrategy()

    def attack(self, target):
        """Atacar usando la estrategia actual."""
        damage = self.strategy.attack(self.base_damage)
        target.take_damage(damage)
        return damage

    def take_damage(self, dmg):
        """Recibir daño al HP."""
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        """Revisa si sigue vivo."""
        return self.hp > 0

    def toggle_strategy(self):
        """Cambia estrategia cíclicamente: Aggressive → Defensive → Balanced."""
        if isinstance(self.strategy, AggressiveStrategy):
            self.strategy = DefensiveStrategy()
        elif isinstance(self.strategy, DefensiveStrategy):
            self.strategy = BalancedStrategy()
        else:
            self.strategy = AggressiveStrategy()


# ================================
#  TEMPLATE METHOD
# ================================
class GameTemplate:
    """Template Method: define estructura principal del juego."""

    def setup(self):
        raise NotImplementedError

    def main_loop(self):
        raise NotImplementedError

    def end(self):
        raise NotImplementedError

    def run(self):
        """Método plantilla: orden de ejecución fijo."""
        self.setup()
        self.main_loop()
        self.end()


# ================================
#  GAME IMPLEMENTATION
# ================================
WIDTH, HEIGHT = 800, 600

class DungeonGame(GameTemplate):
    """Implementación concreta del juego."""

    def setup(self):
        """Inicialización del juego."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dungeon Game")
        self.clock = pygame.time.Clock()

        # Crear héroe y enemigo
        self.hero = Entity("Hero", 50, 10)
        self.enemy = Entity("Goblin", 40, 8)

        # Observer
        self.event_manager = EventManager()
        self.event_manager.register(ConsoleLogger())

        self.font = pygame.font.SysFont("consolas", 24)

        self.player_turn = True
        self.running = True

    def draw_health_bar(self, x, y, current, max_hp):
        """Dibuja barras de vida."""
        ratio = current / max_hp
        pygame.draw.rect(self.screen, (255, 0, 0), (x, y, 200, 20))          # Fondo rojo
        pygame.draw.rect(self.screen, (0, 255, 0), (x, y, int(200 * ratio), 20))  # HP verde

    def draw(self):
        """Dibuja la escena."""
        self.screen.fill((30, 30, 30))

        # Representación del héroe
        pygame.draw.rect(self.screen, (0, 0, 255), (150, 300, 50, 50))
        self.draw_health_bar(100, 260, self.hero.hp, self.hero.max_hp)

        # Representación del enemigo
        pygame.draw.rect(self.screen, (255, 0, 0), (600, 300, 50, 50))
        self.draw_health_bar(550, 260, self.enemy.hp, self.enemy.max_hp)

        # Texto acciones
        txt = self.font.render(
            "A: Atacar | S: Cambiar estrategia | D: Huir",
            True,
            (255,255,255)
        )
        self.screen.blit(txt, (100, 500))

        pygame.display.flip()

    def main_loop(self):
        """Loop principal del juego."""
        while self.running:

            # ----- Eventos -----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Turno del jugador
                if event.type == pygame.KEYDOWN and self.player_turn:
                    if event.key == pygame.K_a:                     # Atacar
                        damage = self.hero.attack(self.enemy)
                        self.event_manager.notify("hero_attack", damage=damage)
                        self.player_turn = False

                    elif event.key == pygame.K_s:                   # Cambiar estrategia
                        self.hero.toggle_strategy()
                        self.event_manager.notify("hero_change_strategy")
                        self.player_turn = False

                    elif event.key == pygame.K_d:                   # Huir
                        print("Huiste!")
                        self.running = False

            # ----- Turno enemigo -----
            if not self.player_turn and self.enemy.is_alive():
                damage = self.enemy.attack(self.hero)
                self.event_manager.notify("enemy_attack", damage=damage)
                self.player_turn = True

            # ----- Verificar fin de juego -----
            if not self.hero.is_alive():
                print("El héroe murió!")
                self.running = False

            if not self.enemy.is_alive():
                print("¡Ganaste!")
                self.running = False

            # Dibujar
            self.draw()
            self.clock.tick(60)

    def end(self):
        """Salir del juego."""
        pygame.quit()


# ================================
#  MAIN
# ================================
if __name__ == "__main__":
    DungeonGame().run()
