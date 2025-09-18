package Arma; // Paquete donde está ubicada la clase ArmaEnano

// Clase ArmaEnano que hereda de la clase abstracta Arma
// Representa el arma usada por los enanos (un hacha)
public class ArmaEnano extends Arma {

    // Atributo que representa el daño que causa el hacha
    private int daño = 26;

    // Atributo que representa la probabilidad o poder de golpe crítico del hacha
    private int critico = 41;

    // Nombre del arma, en este caso es "Hacha enana."
    private String name = "Hacha enana.";

    // Ruta de la imagen que representa el arma
    private final String img = "images/hacha.jpg";

    // Sobrescribe el método arma de la clase abstracta Arma
    // Devuelve una descripción general del hacha como arma de los enanos
    @Override
    public String arma() {
        return "Forjada con maestria, combina fuerza y preciion. Ideal para "
                + "combates cercanos  cortes contundentes";
    }

    // Sobrescribe el método getImg de la clase abstracta Arma
    // Devuelve la ruta de la imagen asociada al hacha
    @Override
    public String getImg() {
        return img;
    }

    // Sobrescribe el método stats de la clase abstracta Arma
    // Devuelve las estadísticas del hacha: daño y crítico
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Daño: " + daño
                + "Critico: " + critico;
    }

    // Sobrescribe el método getName de la clase abstracta Arma
    // Devuelve el nombre del arma ("Hacha enana.")
    @Override
    public String getName() {
        return name;
    }

} // Fin de la clase ArmaEnano
