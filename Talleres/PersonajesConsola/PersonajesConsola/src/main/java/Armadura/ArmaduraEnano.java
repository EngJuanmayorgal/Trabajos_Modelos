package Armadura;

public class ArmaduraEnano extends Armadura {

    private int defensa = 34;
    private int durabilidad = 41;
    
    @Override
    public String armadura() {
        return "Forjada con precision, de alta durbilidad. Excelente "
                + "proteccion contra daño fisico y resistencia al desgaste.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Durabilidad: " + durabilidad;
    }
}
