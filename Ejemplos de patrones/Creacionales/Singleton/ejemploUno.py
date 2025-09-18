class Singleton:
    _instance = None  # Atributo de clase para guardar la única instancia

    def __new__(cls, *args, **kwargs):  
        # __new__ controla la creación de la instancia
        if cls._instance is None:           # Si no existe, se crea
            cls._instance = super().__new__(cls)
        return cls._instance                # Siempre retorna la misma instancia

# --- Uso ---
s1 = Singleton()   # Se crea la instancia por primera vez
s2 = Singleton()   # No crea una nueva, reutiliza la misma

print(s1 is s2)    # True -> Ambas referencias apuntan al mismo objeto
