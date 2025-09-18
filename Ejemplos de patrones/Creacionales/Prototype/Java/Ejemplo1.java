// === Ejemplo 1: Prototype básico ===
class Personaje implements Cloneable {
    String nombre;
    String raza;

    public Personaje(String nombre, String raza) {
        this.nombre = nombre;
        this.raza = raza;
    }

    public Personaje clone() throws CloneNotSupportedException {
        return (Personaje) super.clone(); // clon superficial
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Personaje p1 = new Personaje("Aragorn", "Humano");
        Personaje p2 = p1.clone();
        System.out.println(p1 == p2); // false
    }
}
