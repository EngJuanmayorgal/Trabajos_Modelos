package Monturas;

public class MonturaHumano extends Montura {

    private int velocidad = 41;
    private int resistencia = 49;
    private final String name = "Caballo";
    private final String img = "images/caballo.png";

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
        return "CABALLO: Rapido y confiable, ideal para largas distancias y "
                + "desplazamientos en campo abierto.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Velocidad: " + velocidad
                + "Resistencia: " + resistencia;
    }

}
