import copy  # importa copy para la operación de clonación

class Personaje:  # define la clase Personaje
    def __init__(self, nombre, raza):  # constructor con nombre y raza
        self.nombre = nombre  # guarda el nombre
        self.raza = raza  # guarda la raza

    def clone(self, nombre=None):  # método clone que acepta un nuevo nombre opcional
        nuevo = copy.copy(self)  # crea una copia superficial del objeto
        if nombre:  # si se pasó un nombre nuevo
            nuevo.nombre = nombre  # cambia el nombre en el clon
        return nuevo  # devuelve el clon (posible modificado)

# --- Uso ---
p1 = Personaje("Legolas", "Elfo")  # personaje base
p2 = p1.clone("Legolas el Guerrero")  # clona y cambia el nombre del clon
print(p1.nombre)  # imprime "Legolas" (original sin cambiar)
print(p2.nombre)  # imprime "Legolas el Guerrero" (clon modificado)
