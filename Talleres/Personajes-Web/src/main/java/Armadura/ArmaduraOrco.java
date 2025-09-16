package Armadura;

public class ArmaduraOrco extends Armadura {

    private int defensa = 37;
    private int peso = 40;

    @Override
    public String armadura() {
        return "Pesada y agresiva, hecha para resistir golpes devastadores. "
                + "Ofrece gran defensa, pero limita la movilidad.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Peso: " + peso;
    }
}
