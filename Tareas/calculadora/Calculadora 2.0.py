from abc import ABC, abstractmethod  # Importa soporte para clases y métodos abstractos

# Clase Padre de la calculadora
class Calculadora:
    def __init__(self, n1: int, n2: int):  # Constructor, recibe dos números en decimal
        self.n1 = n1  # Guarda primer número
        self.n2 = n2  # Guarda segundo número

    def sumar(self) -> int:  # Método que suma n1 + n2
        return self.n1 + self.n2

    def restar(self) -> int:  # Método que resta n1 - n2
        return self.n1 - self.n2

# Interfaz/Clase abstracta para conversores de base
class Conversor(ABC):
    @abstractmethod
    def convertir(self, numero: str) -> int:  # Convierte string de la base a decimal
        pass

    @abstractmethod
    def representar(self, numero: int) -> str:  # Convierte decimal a string en la base
        pass

# Conversor General que unifica todas las bases
class ConversorGeneral(Conversor):
    def __init__(self, base: int):  # Constructor, recibe la base deseada (2,8,10,16)
        self.base = base  # Guarda la base

    def convertir(self, numero: str) -> int:  # Convierte número de string a decimal
        return int(numero, self.base)  # Usa int() de Python con la base

    def representar(self, numero: int) -> str:  # Convierte número decimal a la base deseada
        if self.base == 2:  # Base binaria
            return bin(numero)[2:]  # Quita prefijo '0b'
        elif self.base == 8:  # Base octal
            return oct(numero)[2:]  # Quita prefijo '0o'
        elif self.base == 10:  # Base decimal
            return str(numero)
        elif self.base == 16:  # Base hexadecimal
            return hex(numero)[2:].upper()  # Quita '0x' y pasa a mayúscula
        else:
            raise ValueError("Base no soportada")  # Error si la base no es 2,8,10,16

# Menú principal
def main():
    while True:  # Bucle infinito hasta salir
        print("\n=== CALCULADORA MULTIBASE ===")
        print("1. Operar en Binario")
        print("2. Operar en Octal")
        print("3. Operar en Hexadecimal")
        print("4. Salir")

        opcion = input("Elige una opción: ")  # Lee opción del usuario

        if opcion == "4":  # Salir
            print("¡Hasta luego!")
            break

        # Selección del conversor de salida (base en que se mostrará el resultado)
        if opcion == "1":
            conversor_resultado = ConversorGeneral(2)
        elif opcion == "2":
            conversor_resultado = ConversorGeneral(8)
        elif opcion == "3":
            conversor_resultado = ConversorGeneral(16)
        else:
            print("Opción inválida, intenta de nuevo.")
            continue

        # Menú para elegir la base de entrada (donde el usuario ingresará los números)
        print("\n¿En qué base desea ingresar los números?")
        print("1. Decimal")
        print("2. Binario")
        print("3. Octal")
        print("4. Hexadecimal")

        base_entrada = input("Elige una opción: ")  # Lee opción de base de entrada

        if base_entrada == "1":
            conversor_entrada = ConversorGeneral(10)
        elif base_entrada == "2":
            conversor_entrada = ConversorGeneral(2)
        elif base_entrada == "3":
            conversor_entrada = ConversorGeneral(8)
        elif base_entrada == "4":
            conversor_entrada = ConversorGeneral(16)
        else:
            print("Opción inválida, regresando al menú principal.")
            continue

        # Menú para elegir operación
        print("\n¿Qué operación desea realizar?")
        print("1. Suma")
        print("2. Resta")

        operacion = input("Elige una opción: ")

        try:
            n1 = input("Ingresa el primer número: ")  # Pide primer número en la base de entrada
            n2 = input("Ingresa el segundo número: ")  # Pide segundo número

            n1_decimal = conversor_entrada.convertir(n1)  # Convierte primer número a decimal
            n2_decimal = conversor_entrada.convertir(n2)  # Convierte segundo número a decimal

            calc = Calculadora(n1_decimal, n2_decimal)  # Crea objeto calculadora con los dos números

            if operacion == "1":  # Suma
                resultado = calc.sumar()
            elif operacion == "2":  # Resta
                resultado = calc.restar()
            else:
                print("Operación inválida.")
                continue

            # Muestra resultado en la base elegida
            print(f"Resultado en la base de operación elegida: {conversor_resultado.representar(resultado)}")

        except ValueError:  # Captura errores de conversión de base
            print("Error: el número ingresado no es válido en esta base.")

# Punto de entrada
if __name__ == "__main__":
    main()
