package Armadura;

public class ArmaduraOrco extends Armadura {

    private int defensa = 37;
    private int peso = 40;
    private final String img = "images/armadura_orco.png";

    @Override
    public String armadura() {
        return "Pesada y agresiva, hecha para resistir golpes devastadores. "
                + "Ofrece gran defensa, pero limita la movilidad.";
    }

    @Override
    public String getImg() {
        return img;
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Peso: " + peso;
    }
}
