package Arma; // Paquete donde está ubicada la clase ArmaElfo

// Clase ArmaElfo que hereda de la clase abstracta Arma
// Representa el arma usada por los elfos (un arco)
public class ArmaElfo extends Arma {

    // Atributo que representa el daño que causa el arco
    private int daño = 26;

    // Atributo que representa la precisión del arco
    private int precision = 40;

    // Atributo que representa el rango de alcance del arco
    private int rango = 45;

    // Nombre del arma, en este caso es "Arco"
    private String name = "Arco";

    // Ruta de la imagen que representa el arma
    private final String img = "images/arco.jpg";

    // Sobrescribe el método arma de la clase abstracta Arma
    // Devuelve una descripción general del arco como arma de los elfos
    @Override
    public String arma() {
        return "Precisio y letal a larga distancia, excelente para ataques "
                + "sigilosos y estrategias desde lejos.";
    }

    // Sobrescribe el método getImg de la clase abstracta Arma
    // Retorna la ruta de la imagen del arco
    @Override
    public String getImg() {
        return img;
    }

    // Sobrescribe el método stats de la clase abstracta Arma
    // Devuelve las estadísticas del arco: daño, precisión y rango
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Daño: " + daño
                + "Presicion: " + precision
                + "Rango: " + rango;
    }

    // Sobrescribe el método getName de la clase abstracta Arma
    // Retorna el nombre del arma ("Arco")
    @Override
    public String getName() {
        return name;
    }
} // Fin de la clase ArmaElfo

