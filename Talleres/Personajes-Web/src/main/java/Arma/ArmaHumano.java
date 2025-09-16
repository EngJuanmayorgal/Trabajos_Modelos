package Arma;

public class ArmaHumano extends Arma {

    private int daño = 36;
    private int velocidadAtaque = 40;
    private String name = "Espada";
    private String img="images/espada.jpg";

    @Override
    public String arma() {
        return "Equilibrada y versatil, con daño moderado y buena velocidad "
                + "de ataque. Adaptable a cualquier estilo de combate.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Daño: " + daño
                + "V.Ataque: " + velocidadAtaque;
    }

    @Override
    public String getImg() {
        return img;
    }

    @Override
    public String getName() {
        return name;
    }
}
