package Monturas; // Paquete donde está ubicada la clase MonturaEnano
/**
 * 
 * @author Juan Mayorga, Mariam, Samuel
 */

// Clase MonturaEnano que hereda de la clase abstracta Montura
public class MonturaEnano extends Montura {

    // Atributo que representa la habilidad de escalada de la montura
    private int escalada = 49;

    // Atributo que representa la resistencia de la montura
    private int resistencia = 39;

    // Atributo constante que guarda el nombre de la montura
    private final String name = "Cabra";

    // Atributo constante que guarda la ruta de la imagen de la montura
    private final String img = "images/cabra.jpeg";

    // Sobrescribe el método getName de la clase abstracta Montura
    // Retorna el nombre de la montura (en este caso "Cabra")
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
    // Retorna una descripción de la cabra como montura enana
    @Override
    public String montura() {
        return "CABRA: Especialista en terrenosdificiles, con gran resistencia "
                + "y capacidad de escalada. Ideal para montañas y pasos rocosos.";
    }

    // Sobrescribe el método stats de la clase abstracta Montura
    // Retorna un texto con las estadísticas de la montura (escalada y resistencia)
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Escalada: " + escalada
                + "Resistencia: " + resistencia;
    }
} // Fin de la clase MonturaEnano
