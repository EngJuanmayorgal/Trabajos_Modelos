package Arma;

public class ArmaElfo extends Arma {

    private int daño = 26;
    private int precision = 40;
    private int rango = 45;
    private String name = "Arco";
    private final String img ="images/arco.jpg";

    @Override
    public String arma() {
        return "Precisio y letal a larga distancia, excelente para ataques "
                + "sigilosos y estrategias desde lejos.";
    }

    @Override
    public String getImg() {
        return img;
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Daño: " + daño
                + "Presicion: " + precision
                + "Rango: " + rango;
    }

    @Override
    public String getName() {
        return name;
    }
}
