package Monturas;

public class MonturaEnano extends Montura {

    private int escalada = 49;
    private int resistencia = 39;
    private final String name = "Cabra";
    private final String img="";

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
        return "CABRA: Especialista en terrenosdificiles, con gran resistencia "
                + "y capacidad de escalada. Ideal para montañas y pasos rocosos.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Escalada: " + escalada
                + "Resistencia: " + resistencia;
    }
}
