import threading  # para manejar hilos
import datetime  # para manejar fechas y horas

class ThreadSafeLogger:
    _instance = None  # instancia única
    _lock = threading.Lock()  # lock para evitar race conditions
    _initialized = False  # evita re-inicialización

    def __new__(cls, *args, **kwargs):  # controla la creación de la instancia
        with cls._lock:  # asegura que solo un hilo cree la instancia
            if cls._instance is None:  # si no hay instancia
                cls._instance = super().__new__(cls)  # crea la instancia
        return cls._instance  # siempre retorna la misma instancia

    def __init__(self, log_file="thread_safe.log"):  # inicializador
        if not self._initialized:  # solo inicializar la primera vez
            self.log_file = log_file  # archivo de logs
            ThreadSafeLogger._initialized = True  # marca como inicializado

    def write_log(self, level, message):  # método para escribir logs
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # fecha y hora
        log_message = f"[{timestamp}] [{level}] {message}"  # formato del log
        with open(self.log_file, "a", encoding="utf-8") as file:  # abre archivo
            file.write(log_message + "\n")  # escribe log
        print(log_message)  # imprime en consola

# --- Uso con hilos ---
def log_task(name):
    logger = ThreadSafeLogger()  # obtiene la instancia singleton
    logger.write_log("INFO", f"Tarea {name} ejecutada")  # escribe log

# crear varios hilos
threads = [threading.Thread(target=log_task, args=(i,)) for i in range(5)]
for t in threads:
    t.start()  # inicia cada hilo
for t in threads:
    t.join()  # espera a que todos terminen
