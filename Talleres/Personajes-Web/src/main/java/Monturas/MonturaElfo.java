package Monturas;

public class MonturaElfo extends Montura {

    private int velocidad = 43;
    private int sigilo = 48;
    private final String name = "Ciervo";
    private final String img = "images/ciervo.jpeg";

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getImg() {
        return img;
    }

    @Override
    public String montura() {
        return "CIERVO: Silencioso y agil, con gran velocidad y sigilo. "
                + "Perfecto para exploracion y emboscadas. ";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Velocidad: " + velocidad
                + "Sigilo: " + sigilo;
    }

}
