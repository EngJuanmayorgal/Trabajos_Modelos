package Monturas;

public class MonturaElfo extends Montura {

    private int velocidad = 43;
    private int sigilo = 48;
    private final String name = "Ciervo";

    @Override
    public String getName() {
        return name;
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
