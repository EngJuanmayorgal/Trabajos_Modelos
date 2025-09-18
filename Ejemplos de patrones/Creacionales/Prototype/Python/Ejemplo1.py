import copy  # importa el módulo copy para realizar copias superficiales y profundas

class Personaje:  # define la clase Personaje
    def __init__(self, nombre, raza):  # constructor que recibe nombre y raza
        self.nombre = nombre  # asigna el nombre al atributo
        self.raza = raza  # asigna la raza al atributo

    def clone(self):  # método que crea un clon superficial
        return copy.copy(self)  # devuelve una copia superficial del objeto

# --- Uso ---
p1 = Personaje("Aragorn", "Humano")  # crea el personaje original
p2 = p1.clone()  # clona el personaje usando copy.copy (shallow)
print(p1 is p2)  # muestra False: p1 y p2 son objetos distintos
print(p1.nombre, p2.nombre)  # imprime los nombres (mismo valor inicial)
