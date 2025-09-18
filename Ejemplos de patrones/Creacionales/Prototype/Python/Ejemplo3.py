import copy  # import de copy para clonación

class Arma:  # clase Arma que será un objeto compuesto dentro de Personaje
    def __init__(self, tipo, danio):  # constructor arma con tipo y daño
        self.tipo = tipo  # guarda el tipo de arma
        self.danio = danio  # guarda el daño del arma

class Personaje:  # clase Personaje que contiene una Arma
    def __init__(self, nombre, arma):  # constructor con nombre y referencia a Arma
        self.nombre = nombre  # guarda el nombre
        self.arma = arma  # guarda la referencia al objeto Arma

    def clone(self):  # clon superficial
        return copy.copy(self)  # copy.copy copia el objeto pero comparte los subobjetos

# --- Uso ---
espada = Arma("Espada", 50)  # crea una instancia de Arma
p1 = Personaje("Boromir", espada)  # crea personaje con referencia a la espada
p2 = p1.clone()  # clona el personaje (arma compartida por shallow copy)
p2.arma.danio = 80  # modifica el daño del arma desde el clon
print(p1.arma.danio)  # imprime 80 -> demuestra que arma es compartida (shallow)
