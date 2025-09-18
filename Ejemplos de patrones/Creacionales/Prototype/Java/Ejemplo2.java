// === Ejemplo 2: Prototype con modificación tras clonar ===
class Personaje implements Cloneable {
    String nombre;
    String raza;

    public Personaje(String nombre, String raza) {
        this.nombre = nombre;
        this.raza = raza;
    }

    public Personaje clone(String nuevoNombre) throws CloneNotSupportedException {
        Personaje clon = (Personaje) super.clone();
        clon.nombre = nuevoNombre;
        return clon;
    }
}
