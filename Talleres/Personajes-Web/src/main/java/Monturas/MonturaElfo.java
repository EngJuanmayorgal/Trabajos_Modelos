package Monturas; // Paquete donde está ubicada la clase MonturaElfo
/**
 * 
 * @author Juan Mayorga, Mariam, Samuel
 */

// Clase MonturaElfo que hereda de la clase abstracta Montura
public class MonturaElfo extends Montura {

    // Atributo que representa la velocidad de la montura
    private int velocidad = 43;

    // Atributo que representa el sigilo de la montura
    private int sigilo = 48;

    // Atributo constante que guarda el nombre de la montura
    private final String name = "Ciervo";

    // Atributo constante que guarda la ruta de la imagen de la montura
    private final String img = "images/ciervo.jpeg";

    // Sobrescribe el método getName de la clase abstracta Montura
    // Retorna el nombre de la montura (en este caso "Ciervo")
    @Override
    public String getName() {
        return name;
    }

    // Sobrescribe el método getImg de la clase abstracta Montura
    // Retorna la ruta de la imagen asociada a la montura
    @Override
    public String getImg() {
        return img;
    }

    // Sobrescribe el método montura de la clase abstracta Montura
    // Retorna una descripción detallada de la montura del elfo
    @Override
    public String montura() {
        return "CIERVO: Silencioso y agil, con gran velocidad y sigilo. "
                + "Perfecto para exploracion y emboscadas. ";
    }

    // Sobrescribe el método stats de la clase abstracta Montura
    // Retorna un texto con las estadísticas de la montura (velocidad y sigilo)
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Velocidad: " + velocidad
                + "Sigilo: " + sigilo;
    }

} // Fin de la clase MonturaElfo
