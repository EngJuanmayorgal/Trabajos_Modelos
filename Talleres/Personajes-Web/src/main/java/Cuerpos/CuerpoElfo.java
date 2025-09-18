package Cuerpos; // Paquete donde se encuentran las clases de cuerpos

// Clase concreta que representa el cuerpo de un Elfo, hereda de Cuerpo
public class CuerpoElfo extends Cuerpo {

    // Atributo que representa la destreza del elfo
    private int destreza = 17;

    // Atributo que representa la magia del elfo
    private int magia = 18;

    // Atributo que representa la velocidad del elfo
    private int velocidad = 20;

    // Nombre representativo del cuerpo elfo
    private final String name="Elfo";

    // Ruta de la imagen asociada al cuerpo elfo
    private final String img ="images/elfo.png";

    // Método que devuelve el nombre del cuerpo elfo
    @Override
    public String getName() {
        return name;
    }

    // Método que devuelve la ruta de la imagen del elfo
    @Override
    public String getImg() {
        return img;
    }
    
    // Método que devuelve la descripción del cuerpo elfo
    @Override
    public String Cuerpo() {
        return "Agil y veloz, con una afinidad natural hacia la magia. "
                + "Fisicamente menos resistente pero con muy buenas "
                + "destrezas.";
    }

    // Método que devuelve las estadísticas del elfo en formato de texto
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Destreza: " + destreza
                + "\nMagia: " + magia
                + "\nInteligencia: " + velocidad;
    }

}
