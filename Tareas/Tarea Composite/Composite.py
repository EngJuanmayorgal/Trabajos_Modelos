from abc import ABC, abstractmethod

# Interfaz ComponenteBanda
class ComponenteBanda(ABC):
    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar(self):
        pass

    @abstractmethod
    def parar(self):
        pass


# Clase Hoja: Instrumento
class Instrumento(ComponenteBanda):
    def __init__(self, nombre):
        self.nombre = nombre

    def afinar(self):
        print(f"🔧 Afinando el instrumento: {self.nombre}")

    def tocar(self):
        print(f"🎵 Tocando el instrumento: {self.nombre}")

    def parar(self):
        print(f"🛑 Deteniendo el instrumento: {self.nombre}")


# Clase Compuesta: Grupo (Cuerdas, Vientos, Percusión)
class Grupo(ComponenteBanda):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def afinar(self):
        print(f"\n🎸 Afinando grupo de {self.nombre}...")
        for c in self.componentes:
            c.afinar()

    def tocar(self):
        print(f"\n🥁 Tocando grupo de {self.nombre}...")
        for c in self.componentes:
            c.tocar()

    def parar(self):
        print(f"\n🎺 Deteniendo grupo de {self.nombre}...")
        for c in self.componentes:
            c.parar()


# Clase Principal: Banda
class Banda:
    def __init__(self, raiz):
        self.raiz = raiz

    def afinar(self):
        print("\n=== AFINANDO LA BANDA ===")
        self.raiz.afinar()

    def tocar(self):
        print("\n=== TOCANDO LA BANDA ===")
        self.raiz.tocar()

    def parar(self):
        print("\n=== PARANDO LA BANDA ===")
        self.raiz.parar()


# --- Construcción de la banda ---
if __name__ == "__main__":
    # Crear grupos
    cuerdas = Grupo("Cuerdas")
    vientos = Grupo("Vientos")
    percusion = Grupo("Percusión")

    # Agregar instrumentos
    cuerdas.agregar(Instrumento("Guitarra"))
    cuerdas.agregar(Instrumento("Violín"))

    vientos.agregar(Instrumento("Trompeta"))
    vientos.agregar(Instrumento("Flauta"))

    percusion.agregar(Instrumento("Batería"))
    percusion.agregar(Instrumento("Timbal"))

    # Crear grupo raíz (banda completa)
    banda_general = Grupo("Banda Completa")
    banda_general.agregar(cuerdas)
    banda_general.agregar(vientos)
    banda_general.agregar(percusion)

    # Crear la banda principal
    banda = Banda(banda_general)

    # --- Interacción por consola ---
    while True:
        print("\n¿Qué deseas hacer con la banda?")
        print("1. Afinar")
        print("2. Tocar")
        print("3. Parar")
        print("4. Salir")

        opcion = input("👉 Ingresa una opción: ")

        if opcion == "1":
            banda.afinar()
        elif opcion == "2":
            banda.tocar()
        elif opcion == "3":
            banda.parar()
        elif opcion == "4":
            print("\n👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida, intenta nuevamente.")
