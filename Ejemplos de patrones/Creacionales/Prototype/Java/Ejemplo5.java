// === Ejemplo 5: Prototype Registry ===
import java.util.HashMap;
import java.util.Map;

interface Prototype extends Cloneable {
    Prototype clone() throws CloneNotSupportedException;
}

class Hechizo implements Prototype {
    String nombre;
    int poder;
    public Hechizo(String nombre, int poder) { this.nombre = nombre; this.poder = poder; }

    public Prototype clone() throws CloneNotSupportedException {
        return (Hechizo) super.clone();
    }
}

class PrototypeRegistry {
    private Map<String, Prototype> prototypes = new HashMap<>();

    public void register(String key, Prototype prototype) {
        prototypes.put(key, prototype);
    }

    public Prototype clone(String key) throws CloneNotSupportedException {
        return prototypes.get(key).clone();
    }
}
