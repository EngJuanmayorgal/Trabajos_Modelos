package Cuerpos;

public class CuerpoEnano extends Cuerpo {

    private int fuerza = 18;
    private int resistencia = 20;
    private int precision = 20;
    private final String name = "Enano.";

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String Cuerpo() {
        return "Compacto y resistente, congrean presicion y fuerza "
                + "estable. No tan veloz, pero incansable en la batalla.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Destreza: " + fuerza
                + "Magia: " + resistencia
                + "Inteligencia: " + precision;
    }

}
