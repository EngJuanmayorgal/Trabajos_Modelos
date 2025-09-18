import copy  # importa copy para deepcopy

class PrototypeRegistry:  # registro central de prototipos
    def __init__(self):  # constructor del registro
        self._prototypes = {}  # diccionario que guarda prototipos por clave

    def register(self, key, prototype):  # registra un prototipo bajo una clave
        self._prototypes[key] = prototype  # guarda la referencia al objeto prototipo

    def clone(self, key, **attrs):  # clona el prototipo y permite sobrescribir atributos
        original = self._prototypes.get(key)  # obtiene el prototipo original por clave
        if original is None:  # si no existe la clave
            raise KeyError(f"No existe prototipo con clave: {key}")  # lanza error claro
        obj = copy.deepcopy(original)  # clona profundamente el prototipo
        # aplica atributos adicionales/overrides al clon
        for k, v in attrs.items():  # para cada atributo pasado
            setattr(obj, k, v)  # asigna el nuevo valor al clon
        return obj  # devuelve el clon modificado

class Hechizo:  # ejemplo de clase que usaremos como prototipo
    def __init__(self, nombre, poder):  # constructor con nombre y poder
        self.nombre = nombre  # guarda nombre del hechizo
        self.poder = poder  # guarda poder (int) del hechizo

# --- Uso ---
registry = PrototypeRegistry()  # crea registro de prototipos
registry.register("fuego", Hechizo("Bola de fuego", 100))  # registra prototipo fuego
registry.register("hielo", Hechizo("Rayo de hielo", 80))  # registra prototipo hielo

h1 = registry.clone("fuego", poder=120)  # clona "fuego" y sobrescribe el poder a 120
h2 = registry.clone("hielo")  # clona "hielo" sin cambios

print(h1.nombre, h1.poder)  # imprime "Bola de fuego 120"
print(h2.nombre, h2.poder)  # imprime "Rayo de hielo 80"
