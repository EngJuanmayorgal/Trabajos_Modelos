import datetime  # importa el módulo para manejar fechas y horas

class Logger:  # define la clase Logger
    _instance = None  # guarda la única instancia del singleton
    _initialized = False  # bandera para evitar re-inicializar en __init__

    def __new__(cls, *args, **kwargs):  # controla la creación de la instancia
        if cls._instance is None:  # si aún no existe la instancia
            cls._instance = super().__new__(cls)  # crea la instancia y la guarda
        return cls._instance  # siempre devuelve la misma instancia

    def __init__(self, log_file="app.log"):  # inicializador (se ejecuta en cada llamada)
        if not self._initialized:  # solo inicializar la primera vez
            self.log_file = log_file  # establece el nombre del archivo de logs
            Logger._initialized = True  # marca que ya fue inicializado

    def write_log(self, level, message):  # método para escribir una línea de log
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # obtiene fecha y hora formateada
        log_message = f"[{timestamp}] [{level}] {message}"  # construye la línea de log con formato
        with open(self.log_file, "a", encoding="utf-8") as file:  # abre el archivo en modo append
            file.write(log_message + "\n")  # escribe la línea en el archivo
        print(log_message)  # imprime la línea en consola (útil en desarrollo)

# --- Ejemplo de uso ---
logger1 = Logger()  # crea u obtiene la instancia singleton
logger2 = Logger()  # obtiene la misma instancia que logger1

logger1.write_log("INFO", "Inicio de la aplicación")  # escribe un log de nivel INFO
logger2.write_log("WARNING", "Conexión lenta detectada")  # escribe un log de nivel WARNING
logger1.write_log("ERROR", "No se pudo abrir el archivo de configuración")  # escribe un log de nivel ERROR

print(logger1 is logger2)  # verifica que logger1 y logger2 son la misma instancia (debería imprimir True)
