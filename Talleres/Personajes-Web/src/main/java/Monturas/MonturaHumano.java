package Monturas; // Paquete donde está ubicada la clase MonturaHumano

// Clase MonturaHumano que extiende de la clase abstracta Montura
public class MonturaHumano extends Montura {

    // Atributo que representa la velocidad de la montura
    private int velocidad = 41;

    // Atributo que representa la resistencia de la montura
    private int resistencia = 49;

    // Nombre fijo de la montura (un caballo en este caso)
    private final String name = "Caballo";

    // Ruta de la imagen asociada a la montura
    private final String img = "images/caballo.png";

    // Sobrescribe el método getName de la clase abstracta Montura
    // Retorna el nombre de la montura ("Caballo")
    @Override
    public String getName() {
        return name;
    }

    // Sobrescribe el método getImg de la clase abstracta Montura
    // Retorna la ruta de la imagen de la montura
    @Override
    public String getImg() {
        return img;
    }

    // Sobrescribe el método montura de la clase abstracta Montura
    // Retorna una descripción sobre el caballo como montura de los humanos
    @Override
    public String montura() {
        return "CABALLO: Rapido y confiable, ideal para largas distancias y "
                + "desplazamientos en campo abierto.";
    }

    // Sobrescribe el método stats de la clase abstracta Montura
    // Retorna las estadísticas de la montura (velocidad y resistencia)
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Velocidad: " + velocidad
                + "Resistencia: " + resistencia;
    }

} // Fin de la clase MonturaHumano
