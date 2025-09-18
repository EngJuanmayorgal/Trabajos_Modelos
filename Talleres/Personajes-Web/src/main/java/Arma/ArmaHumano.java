package Arma; // Paquete donde está ubicada la clase ArmaHumano

// Clase ArmaHumano que hereda de la clase abstracta Arma
// Representa el arma usada por los humanos (una espada)
public class ArmaHumano extends Arma {

    // Atributo que representa el daño que causa la espada
    private int daño = 36;

    // Atributo que representa la velocidad de ataque de la espada
    private int velocidadAtaque = 40;

    // Nombre del arma, en este caso es "Espada"
    private String name = "Espada";

    // Ruta de la imagen que representa la espada
    private String img = "images/espada.jpg";

    // Sobrescribe el método arma de la clase abstracta Arma
    // Devuelve una descripción general de la espada como arma de los humanos
    @Override
    public String arma() {
        return "Equilibrada y versatil, con daño moderado y buena velocidad "
                + "de ataque. Adaptable a cualquier estilo de combate.";
    }

    // Sobrescribe el método getImg de la clase abstracta Arma
    // Devuelve la ruta de la imagen asociada a la espada
    @Override
    public String getImg() {
        return img;
    }

    // Sobrescribe el método stats de la clase abstracta Arma
    // Devuelve las estadísticas de la espada: daño y velocidad de ataque
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Daño: " + daño
                + "V.Ataque: " + velocidadAtaque;
    }

    // Sobrescribe el método getName de la clase abstracta Arma
    // Devuelve el nombre del arma ("Espada")
    @Override
    public String getName() {
        return name;
    }
} // Fin de la clase ArmaHumano
