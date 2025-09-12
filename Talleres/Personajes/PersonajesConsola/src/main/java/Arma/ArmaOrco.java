package Arma;

public class ArmaOrco extends Arma {

    private int daño = 36;
    private int peso = 42;
    private String name = "MazaOrca";

    @Override
    public String arma() {
        return "Arma pesada y destructiva, capaz de aplastar cualquier defensa. "
                + "Su lentitud se compensa conel gran tamaño que influye.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Daño: " + daño
                + "Peso: " + peso;
    }

    @Override
    public String getName() {
        return name;
    }
}
