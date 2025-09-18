import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.io.FileWriter;
import java.io.IOException;

// Logger singleton básico
class Logger {
    private static Logger instance; // instancia única
    private String logFile = "app.log"; // archivo de logs
    private Logger() {} // constructor privado

    public static Logger getInstance() {
        if (instance == null) {
            instance = new Logger(); // crea instancia
        }
        return instance; // devuelve la misma instancia
    }

    public void writeLog(String level, String message) {
        String timestamp = LocalDateTime.now()
                .format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")); // fecha
        String logMessage = "[" + timestamp + "] [" + level + "] " + message; // formato
        try (FileWriter fw = new FileWriter(logFile, true)) { // abre archivo en modo append
            fw.write(logMessage + "\n"); // escribe log
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(logMessage); // también imprime en consola
    }
}

// Uso
public class Main {
    public static void main(String[] args) {
        Logger logger1 = Logger.getInstance();
        Logger logger2 = Logger.getInstance();
        logger1.writeLog("INFO", "Aplicación iniciada");
        logger2.writeLog("WARNING", "Conexión lenta");
        System.out.println(logger1 == logger2); // true
    }
}
