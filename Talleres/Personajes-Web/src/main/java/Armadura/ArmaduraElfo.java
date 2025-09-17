package Armadura;

public class ArmaduraElfo extends Armadura {

    private int defensa = 20;
    private int resistenciaMagica = 32;
    private final String img ="images/armadura_elfo.png";

    @Override

    public String armadura() {
        return "Ligera y elegante, brinda resistencia magica y fleibilidad "
                + "en combate, aunque menos protectora fisicamente.";
    }
 @Override
    public String getImg() {
        return img;
    }
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Resistencia magica: " + resistenciaMagica;
    }

}
