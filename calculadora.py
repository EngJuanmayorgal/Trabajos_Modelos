from abc import ABC, abstractmethod

# Clase Padre
class Calculadora:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2

    def sumar(self) -> int:
        return self.n1 + self.n2


# Interfaz
class Conversor(ABC):
    @abstractmethod
    def convertir(self, numero: str) -> int:
        pass

    @abstractmethod
    def representar(self, numero: int) -> str:
        pass


# Clases hijas para conversión
class Binario(Conversor):
    def convertir(self, numero: str) -> int:
        return int(numero, 2)

    def representar(self, numero: int) -> str:
        return bin(numero)[2:]


class Octal(Conversor):
    def convertir(self, numero: str) -> int:
        return int(numero, 8)

    def representar(self, numero: int) -> str:
        return oct(numero)[2:]


class Hexadecimal(Conversor):
    def convertir(self, numero: str) -> int:
        return int(numero, 16)

    def representar(self, numero: int) -> str:
        return hex(numero)[2:].upper()


class Decimal(Conversor):
    def convertir(self, numero: str) -> int:
        return int(numero)

    def representar(self, numero: int) -> str:
        return str(numero)


# Menú principal
def main():
    while True:
        print("\n=== CALCULADORA MULTIBASE ===")
        print("1. Operar en Binario")
        print("2. Operar en Octal")
        print("3. Operar en Hexadecimal")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "4":
            print("¡Hasta luego!")
            break

        if opcion == "1":
            conversor_resultado = Binario()
        elif opcion == "2":
            conversor_resultado = Octal()
        elif opcion == "3":
            conversor_resultado = Hexadecimal()
        else:
            print("Opción inválida, intenta de nuevo.")
            continue

        # Elegir base de entrada
        print("\n¿En qué base desea ingresar los números?")
        print("1. Decimal")
        print("2. Binario")
        print("3. Octal")
        print("4. Hexadecimal")

        base_entrada = input("Elige una opción: ")

        if base_entrada == "1":
            conversor_entrada = Decimal()
        elif base_entrada == "2":
            conversor_entrada = Binario()
        elif base_entrada == "3":
            conversor_entrada = Octal()
        elif base_entrada == "4":
            conversor_entrada = Hexadecimal()
        else:
            print("Opción inválida, regresando al menú principal.")
            continue

        # Pedir números en la base seleccionada
        try:
            n1 = input("Ingresa el primer número: ")
            n2 = input("Ingresa el segundo número: ")

            n1_decimal = conversor_entrada.convertir(n1)
            n2_decimal = conversor_entrada.convertir(n2)

            calc = Calculadora(n1_decimal, n2_decimal)
            resultado = calc.sumar()

            print(f"Resultado en la base de operación elegida: {conversor_resultado.representar(resultado)}")

        except ValueError:
            print("Error: el número ingresado no es válido en esta base.")


if __name__ == "__main__":
    main()