package Armadura; // Paquete de la armadura

// Clase concreta que representa la armadura usada por los orcos
public class ArmaduraOrco extends Armadura {

    // Defensa física que ofrece la armadura
    private int defensa = 37;

    // Peso de la armadura (afecta la movilidad del portador)
    private int peso = 40;

    // Ruta de la imagen asociada a esta armadura
    private final String img = "images/armadura_orco.png";

    // Descripción de la armadura
    @Override
    public String armadura() {
        return "Pesada y agresiva, hecha para resistir golpes devastadores. "
                + "Ofrece gran defensa, pero limita la movilidad.";
    }

    // Retorna la ruta de la imagen
    @Override
    public String getImg() {
        return img;
    }

    // Retorna las estadísticas principales de la armadura
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Peso: " + peso;
    }
}
