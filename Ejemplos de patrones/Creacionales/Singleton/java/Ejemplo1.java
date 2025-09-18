// Singleton básico
class Singleton {
    private static Singleton instance; // instancia única

    private Singleton() {} // constructor privado evita instanciación externa

    public static Singleton getInstance() {
        if (instance == null) { // si no existe instancia
            instance = new Singleton(); // crea la instancia
        }
        return instance; // devuelve siempre la misma instancia
    }
}

// Uso
public class Main {
    public static void main(String[] args) {
        Singleton s1 = Singleton.getInstance(); // obtiene la instancia
        Singleton s2 = Singleton.getInstance(); // misma instancia
        System.out.println(s1 == s2); // true
    }
}
