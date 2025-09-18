import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

// Logger avanzado con carpeta
class AdvancedLogger {
    private static AdvancedLogger instance;
    private String logFile;

    private AdvancedLogger() { // constructor privado
        File dir = new File("logs"); // carpeta logs
        if (!dir.exists()) {
            dir.mkdir(); // crea carpeta si no existe
        }
        logFile = "logs/app.log"; // ruta completa del archivo
    }

    public static AdvancedLogger getInstance() {
        if (instance == null) {
            instance = new AdvancedLogger();
        }
        return instance;
    }

    public void writeLog(String level, String message) {
        String timestamp = LocalDateTime.now()
                .format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        String logMessage = "[" + timestamp + "] [" + level + "] " + message;
        try (FileWriter fw = new FileWriter(logFile, true)) {
            fw.write(logMessage + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(logMessage);
    }
}

// Uso
public class Main {
    public static void main(String[] args) {
        AdvancedLogger logger = AdvancedLogger.getInstance();
        logger.writeLog("INFO", "Aplicación iniciada");
        logger.writeLog("ERROR", "Ocurrió un fallo");
    }
}
