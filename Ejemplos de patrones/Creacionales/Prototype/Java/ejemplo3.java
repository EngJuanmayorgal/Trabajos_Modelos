// === Ejemplo 3: Prototype con composición ===
class Arma {
    String tipo;
    int daño;
    public Arma(String tipo, int daño) { this.tipo = tipo; this.daño = daño; }
}

class Personaje implements Cloneable {
    String nombre;
    Arma arma;
    public Personaje(String nombre, Arma arma) { this.nombre = nombre; this.arma = arma; }

    public Personaje clone() throws CloneNotSupportedException {
        return (Personaje) super.clone(); // clon superficial
    }
}
