package Cuerpos; // Paquete donde se encuentran las clases de cuerpos

// Clase concreta que representa el cuerpo de un Enano, hereda de Cuerpo
public class CuerpoEnano extends Cuerpo {

    // Atributo que representa la fuerza del enano
    private final int fuerza = 18;

    // Atributo que representa la resistencia del enano
    private final int resistencia = 20;

    // Atributo que representa la precisión del enano
    private final int precision = 20;

    // Nombre representativo del cuerpo enano
    private final String name = "Enano";

    // Ruta de la imagen asociada al cuerpo enano
    private final String img ="images/enano.png";

    // Método que devuelve la ruta de la imagen del enano
    @Override
    public String getImg() {
        return img;
    }

    // Método que devuelve el nombre del cuerpo enano
    @Override
    public String getName() {
        return name;
    }

    // Método que devuelve la descripción del cuerpo enano
    @Override
    public String Cuerpo() {
        return "Compacto y resistente, congrean presicion y fuerza "
                + "estable. No tan veloz, pero incansable en la batalla.";
    }

    // Método que devuelve las estadísticas del enano en formato de texto
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Destreza: " + fuerza
                + "\nMagia: " + resistencia
                + "\nInteligencia: " + precision;
    }

}

