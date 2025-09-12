package Cuerpos;

public class CuerpoElfo extends Cuerpo {

    private int destreza = 17;
    private int magia = 18;
    private int velocidad = 20;
    private final String name="Elfo";

    @Override
    public String getName() {
        return name;
    }
    

    @Override
    public String Cuerpo() {
        return "Agil y veloz, con una afinidad natural hacia la magia. "
                + "Fisicamente menos resistente pero con muy buenas "
                + "destrezas.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Destreza: " + destreza
                + "Magia: " + magia
                + "Inteligencia: " + velocidad;
    }

}
