import os  # para manejar directorios y rutas
import datetime  # para manejar fechas y horas

class AdvancedLogger:
    _instance = None  # instancia única del logger
    _initialized = False  # evita re-inicialización

    def __new__(cls, *args, **kwargs):  # controla la creación de la instancia
        if cls._instance is None:  # si no hay instancia
            cls._instance = super().__new__(cls)  # crea la instancia
        return cls._instance  # siempre devuelve la misma instancia

    def __init__(self, log_dir="logs", log_file="app.log"):  # inicializador
        if not self._initialized:  # solo inicializar la primera vez
            os.makedirs(log_dir, exist_ok=True)  # crea carpeta logs si no existe
            self.log_file = os.path.join(log_dir, log_file)  # ruta completa del archivo
            AdvancedLogger._initialized = True  # marca como inicializado

    def write_log(self, level, message):  # método para escribir logs
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # fecha y hora
        log_message = f"[{timestamp}] [{level}] {message}"  # formato del log
        with open(self.log_file, "a", encoding="utf-8") as file:  # abre archivo en modo append
            file.write(log_message + "\n")  # escribe el log
        print(log_message)  # también muestra en consola

# --- Uso ---
logger = AdvancedLogger()  # crea u obtiene la instancia
logger.write_log("INFO", "Aplicación iniciada")
logger.write_log("ERROR", "Ocurrió un fallo")
