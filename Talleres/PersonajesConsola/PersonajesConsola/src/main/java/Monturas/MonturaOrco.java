package Monturas;

public class MonturaOrco extends Montura {

    private int ferocidad = 46;
    private int velocidad = 32;
    private final String name = "Wargo";

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String montura() {
        return "WARGO: Bestia feroz, comba fuerza y velocidad. Su erocidad "
                + "lo convierte e un aliado temible en combate.";
    }

    public String stats() {
        return "\nEstadisticas:\n"
                + "Ferosidad: " + ferocidad
                + "Velocidad: " + velocidad;
    }
}
