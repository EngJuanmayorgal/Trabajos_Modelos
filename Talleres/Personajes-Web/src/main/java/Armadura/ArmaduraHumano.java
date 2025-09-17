package Armadura;

public class ArmaduraHumano extends Armadura {

    private int defensa = 35;
    private int material = 39;
    private final String img = "images/armadura_humano.png";

    @Override
    public String armadura() {
        return "Equilirada y funcional, ofrece buena dfensa y durabilidad, "
                + "sin destacar en ninguna caracteristic externa,";
    }

    @Override
    public String getImg() {
        return img;
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Material: " + material;
    }
}
