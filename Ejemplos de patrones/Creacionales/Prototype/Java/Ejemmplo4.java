// === Ejemplo 4: Prototype con clon profundo ===
class Arma implements Cloneable {
    String tipo;
    int daño;
    public Arma(String tipo, int daño) { this.tipo = tipo; this.daño = daño; }

    public Arma clone() throws CloneNotSupportedException {
        return (Arma) super.clone();
    }
}

class Personaje implements Cloneable {
    String nombre;
    Arma arma;
    public Personaje(String nombre, Arma arma) { this.nombre = nombre; this.arma = arma; }

    public Personaje clone() throws CloneNotSupportedException {
        Personaje clon = (Personaje) super.clone();
        clon.arma = arma.clone(); // clon profundo
        return clon;
    }
}
