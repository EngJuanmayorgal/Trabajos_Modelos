import copy  # importa copy para deepcopy

class Arma:  # clase Arma
    def __init__(self, tipo, danio):  # constructor arma
        self.tipo = tipo  # tipo de arma
        self.danio = danio  # daño de arma

class Personaje:  # clase Personaje con un objeto Arma
    def __init__(self, nombre, arma):  # constructor con nombre y arma
        self.nombre = nombre  # guarda nombre
        self.arma = arma  # guarda referencia a arma

    def clone(self):  # clon profundo
        return copy.deepcopy(self)  # deepcopy clona el objeto y sus subobjetos recursivamente

# --- Uso ---
espada = Arma("Espada", 50)  # crea arma original
p1 = Personaje("Gimli", espada)  # personaje con arma original
p2 = p1.clone()  # clona profundamente (arma independiente)
p2.arma.danio = 80  # modifica el daño en el clon
print(p1.arma.danio)  # imprime 50 -> el original NO se ve afectado por el cambio en el clon
