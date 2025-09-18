class Config:
    _instance = None  # guarda la instancia única
    _initialized = False  # evita re-inicialización

    def __new__(cls, *args, **kwargs):  # controla la creación de la instancia
        if cls._instance is None:  # si no existe una instancia
            cls._instance = super().__new__(cls)  # crea la instancia
        return cls._instance  # siempre retorna la misma instancia

    def __init__(self, app_name="MiApp", version="1.0"):  # inicializador
        if not self._initialized:  # solo inicializar la primera vez
            self.app_name = app_name  # guarda nombre de la app
            self.version = version  # guarda versión de la app
            Config._initialized = True  # marca que ya se inicializó

# --- Uso ---
c1 = Config("App1", "2.0")  # crea instancia con parámetros
c2 = Config("App2", "3.0")  # intenta crear otra instancia (será la misma)
print(c1 is c2)  # True -> ambas son la misma instancia
print(c1.app_name, c1.version)  # App1 2.0 -> se mantiene la primera inicialización
print(c2.app_name, c2.version)  # App1 2.0 -> igual, no cambia
