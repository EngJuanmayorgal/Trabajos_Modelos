package Monturas; // Paquete donde se encuentra la clase Montura
/**
 * 
 * @author Juan Mayorga, Mariam, Samuel
 */

// Clase abstracta que servirá como base para todas las monturas (ej: montura de orco, humano, etc.)
public abstract class Montura {

    // Método abstracto que debe ser implementado por las subclases para describir la montura
    public abstract String montura();

    // Método abstracto que debe ser implementado por las subclases para retornar estadísticas de la montura
    public abstract String stats();

    // Método abstracto que debe devolver el nombre de la montura
    public abstract String getName();

    // Método abstracto que debe devolver la ruta o nombre de la imagen de la montura
    public abstract String getImg();
}
