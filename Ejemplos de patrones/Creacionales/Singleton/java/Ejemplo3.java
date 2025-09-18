// Singleton con parámetros de configuración
class Config {
    private static Config instance;
    private String appName;
    private String version;

    private Config(String appName, String version) { // constructor privado
        this.appName = appName;
        this.version = version;
    }

    public static Config getInstance(String appName, String version) {
        if (instance == null) { // solo inicializa la primera vez
            instance = new Config(appName, version);
        }
        return instance; // siempre retorna la misma instancia
    }

    public String getAppName() { return appName; }
    public String getVersion() { return version; }
}

// Uso
public class Main {
    public static void main(String[] args) {
        Config c1 = Config.getInstance("App1", "2.0");
        Config c2 = Config.getInstance("App2", "3.0"); // ignorado, se mantiene la primera instancia
        System.out.println(c1 == c2); // true
        System.out.println(c1.getAppName() + " " + c1.getVersion()); // App1 2.0
        System.out.println(c2.getAppName() + " " + c2.getVersion()); // App1 2.0
    }
}
