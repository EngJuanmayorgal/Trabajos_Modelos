package Cuerpos; // Paquete donde se agrupan las clases de cuerpos

/**
 * Clase que representa el cuerpo de un Orco.
 * Autor: Juan Mayorga, Mariam, Samuel
 */

public class CuerpoOrco extends Cuerpo { // Clase concreta que extiende de Cuerpo

    // Atributo que almacena la fuerza del orco
    private final int fuerza = 20;

    // Atributo que almacena la resistencia del orco
    private final int resistencia = 20;

    // Atributo que almacena la brutalidad del orco
    private final int brutalidad = 20;

    // Nombre representativo del cuerpo
    private final String name = "Orco";

    // Ruta de la imagen asociada al cuerpo
    private final String img = "images/orco.png";

    // Método que devuelve la ruta/identificador de la imagen
    @Override
    public String getImg() {
        // Retorna la ruta de la imagen
        return img;
    }

    // Método que devuelve el nombre del cuerpo
    @Override
    public String getName() {
        // Retorna el nombre
        return name;
    }

    // Método que devuelve la descripción textual del cuerpo
    @Override
    public String Cuerpo() {
        // Retorna la descripción del orco tal cual está en el código original
        return "Robusto y brutal, con gran fuerza y resistenci. Poco preciso "
                + "y lento, pero imparable en combate fisico.";
    }

    // Método que devuelve las estadísticas formateadas del cuerpo
    @Override
    public String stats() {
        // Construye y retorna las estadísticas usando los atributos definidos arriba
        return "\nEstadisticas:\n"
                + "Destreza: " + fuerza
                + "\nMagia: " + resistencia
                + "\nInteligencia: " + brutalidad;
    }
}
