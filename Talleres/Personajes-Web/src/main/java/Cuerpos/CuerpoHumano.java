package Cuerpos; // Paquete donde se agrupan las clases de cuerpos

// Clase concreta que representa el cuerpo de un Humano, extiende de Cuerpo
public class CuerpoHumano extends Cuerpo {

    // Atributo que representa la fuerza del humano
    private final int fuerza = 10;

    // Atributo que representa la agilidad del humano
    private final int agilidad = 18;

    // Atributo que representa la inteligencia del humano
    private final int inteligencia = 20;

    // Nombre representativo del cuerpo humano
    private final String name = "Humano";

    // Ruta de la imagen asociada al cuerpo humano
    private final String img = "images/humano.png";

    // Método que devuelve el nombre del cuerpo humano
    @Override
    public String getName() {
        return name;
    }

    // Método que devuelve las estadísticas del humano en formato de texto
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Fuerza: " + fuerza
                + "\nAgilidad: " + agilidad
                + "\nInteligencia: " + inteligencia;
    }

    // Método que devuelve la ruta de la imagen asociada al humano
    @Override
    public String getImg() {
        return img;
    }

    // Método que devuelve la descripción del cuerpo humano
    @Override
    public String Cuerpo() {
        return "Equilibrado en todos los aspectos. Un cuerpo versatil "
                + "con gran inteligencia y buena agilidad, aunque "
                + "con una fuerza moderada.";
    }
}
