package Arma;

public class ArmaEnano extends Arma {

    private int daño = 26;
    private int critico = 41;
    private String name = "Hacha enana.";
    private final String img = "images/hacha.jpg";

    @Override
    public String arma() {
        return "Forjada con maestria, combina fuerza y preciion. Ideal para "
                + "combates cercanos  cortes contundentes";
    }

    @Override
    public String getImg() {
        return img;
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Daño: " + daño
                + "Critico: " + critico;
    }

    @Override
    public String getName() {
        return name;
    }

}
