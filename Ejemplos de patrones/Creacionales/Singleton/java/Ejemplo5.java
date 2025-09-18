import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

// Logger seguro para múltiples hilos
class ThreadSafeLogger {
    private static ThreadSafeLogger instance;
    private static final Object lock = new Object(); // lock para sincronizar
    private String logFile = "thread_safe.log";

    private ThreadSafeLogger() {} // constructor privado

    public static ThreadSafeLogger getInstance() {
        if (instance == null) {
            synchronized (lock) { // asegura solo un hilo crea la instancia
                if (instance == null) {
                    instance = new ThreadSafeLogger();
                }
            }
        }
        return instance;
    }

    public void writeLog(String level, String message) {
        String timestamp = LocalDateTime.now()
                .format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        String logMessage = "[" + timestamp + "] [" + level + "] " + message;
        synchronized (lock) { // bloquea escritura para hilos
            try (FileWriter fw = new FileWriter(logFile, true)) {
                fw.write(logMessage + "\n");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        System.out.println(logMessage);
    }
}

// Uso con hilos
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Runnable task = () -> {
            ThreadSafeLogger logger = ThreadSafeLogger.getInstance();
            logger.writeLog("INFO", "Tarea ejecutada en hilo " + Thread.currentThread().getName());
        };

        Thread[] threads = new Thread[5];
        for (int i = 0; i < threads.length; i++) {
            threads[i] = new Thread(task, "Hilo-" + i);
            threads[i].start();
        }
        for (Thread t : threads) {
            t.join();
        }
    }
}
