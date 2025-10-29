# 🎮 Juego Esquiva Bolas

## 👥 Integrantes

- **Juan David Mayorga López** – 20232020116
- **Samuel Andrés Barrera Pulido** – 20232020156
- **Mariam Betin Escobar** – 20232020300

Este es un juego simple desarrollado en **Python**, en el que el jugador controla un cubo que debe esquivar las bolas que caen desde la parte superior de la pantalla.
El objetivo es sobrevivir el mayor tiempo posible sin ser golpeado.

El proyecto implementa los patrones de diseño **Command** y **Chain of Responsibility** para mantener una estructura limpia, modular y fácil de ampliar.

---

## 🧩 Patrones de diseño aplicados

### 🕹️ Command

Permite encapsular los movimientos del jugador como objetos independientes.
Cada tecla presionada se traduce en un comando que el jugador ejecuta, separando la lógica de los controles del código principal.

### 🔗 Chain of Responsibility

Gestiona los eventos y verificaciones (como colisiones y límites) en una cadena ordenada.
Cada manejador tiene una tarea específica y, si no puede resolverla, la pasa al siguiente.

---

## 🧠 Funcionamiento del juego

1. Al iniciar, aparece un cubo (el jugador) en el centro de la pantalla.
2. El jugador puede moverse con las teclas **W, A, S, D**.
3. Las bolas comienzan a caer solo después del primer movimiento.
4. Si el jugador es golpeado por una bola, el juego termina.
5. El jugador no puede salir de los límites de la ventana.

---

## 🏗️ Estructura de clases principal

* `Player`: representa el cubo controlado por el usuario.
* `Enemy`: representa las bolas que caen.
* `Command`: clase abstracta para los comandos del movimiento.
* `MoveRight`, `MoveLeft`, `MoveUp`, `MoveDoen`: comandos concretos.
* `InputHandler`: clase base del patrón Chain of Responsibility.

---

## Requisitos
* Python 3.8 o superior
* Librería Pygame
