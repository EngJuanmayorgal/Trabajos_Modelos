package Monturas; // Paquete donde está ubicada la clase MonturaOrco

// Clase MonturaOrco que extiende de la clase abstracta Montura
public class MonturaOrco extends Montura {

    // Atributo que representa la ferocidad de la montura
    private int ferocidad = 46;

    // Atributo que representa la velocidad de la montura
    private int velocidad = 32;

    // Nombre fijo de la montura (en este caso, un Wargo)
    private final String name = "Wargo";

    // Ruta de la imagen asociada a la montura
    private final String img = "images/wargo.png";

    // Sobrescribe el método getName de la clase abstracta Montura
    // Devuelve el nombre de la montura ("Wargo")
    @Override
    public String getName() {
        return name;
    }

    // Sobrescribe el método getImg de la clase abstracta Montura
    // Devuelve la ruta de la imagen de la montura
    @Override
    public String getImg() {
        return img;
    }

    // Sobrescribe el método montura de la clase abstracta Montura
    // Devuelve una descripción de la montura Wargo con sus características
    @Override
    public String montura() {
        return "WARGO: Bestia feroz, comba fuerza y velocidad. Su erocidad "
                + "lo convierte e un aliado temible en combate.";
    }

    // Sobrescribe el método stats de la clase abstracta Montura
    // Devuelve las estadísticas de la montura (ferocidad y velocidad)
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Ferosidad: " + ferocidad
                + "Velocidad: " + velocidad;
    }
} // Fin de la clase MonturaOrco
