package Cuerpos;

public class CuerpoHumano extends Cuerpo {

    private int fuerza = 10;
    private int agilidad = 18;
    private int inteligencia = 20;
    private final String name = "Humano";
    private final String img = "images/humano.png";

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Fuerza: " + fuerza
                + "Agilidad: " + agilidad
                + "Inteligencia: " + inteligencia;
    }

    @Override
    public String getImg() {
        return img;
    }

    @Override
    public String Cuerpo() {
        return "Equilibrado en todos los aspectos. Un cuerpo versatil "
                + "con gran inteligencia y buena agilidad, aunque "
                + "con una fuerza moderada.";
    }

}
