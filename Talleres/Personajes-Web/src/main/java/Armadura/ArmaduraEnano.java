package Armadura; // Paquete donde está ubicada la clase

// Clase concreta que representa la armadura utilizada por los enanos
// Extiende de la clase abstracta Armadura e implementa sus métodos
public class ArmaduraEnano extends Armadura {

    // Nivel de defensa física de la armadura
    private int defensa = 34;

    // Nivel de durabilidad (resistencia al desgaste y golpes)
    private int durabilidad = 41;

    // Ruta de la imagen asociada a la armadura del enano
    private final String img = "images/armadura_enano.png";

    // Implementación del método abstracto armadura()
    // Devuelve una descripción textual de la armadura
    @Override
    public String armadura() {
        return "Forjada con precision, de alta durbilidad. Excelente "
                + "proteccion contra daño fisico y resistencia al desgaste.";
    }

    // Implementación del método abstracto getImg()
    // Devuelve la ruta de la imagen de la armadura
    @Override
    public String getImg() {
        return img;
    }

    // Implementación del método abstracto stats()
    // Devuelve las estadísticas principales: defensa y durabilidad
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Durabilidad: " + durabilidad;
    }
}
