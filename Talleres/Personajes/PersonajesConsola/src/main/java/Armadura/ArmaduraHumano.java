package Armadura;

public class ArmaduraHumano extends Armadura {

    private int defensa = 35;
    private int material = 39;

    @Override
    public String armadura() {
        return "Equilirada y funcional, ofrece buena dfensa y durabilidad, "
                + "sin destacar en ninguna caracteristic externa,";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Material: " + material;
    }
}
