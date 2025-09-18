package Armadura; // Paquete donde está ubicada la clase

// Clase concreta que representa la armadura utilizada por los humanos
// Extiende de la clase abstracta Armadura e implementa sus métodos
public class ArmaduraHumano extends Armadura {

    // Nivel de defensa física de la armadura
    private int defensa = 35;

    // Tipo o calidad del material con el que está hecha (impacta en resistencia/durabilidad)
    private int material = 39;

    // Ruta de la imagen asociada a la armadura del humano
    private final String img = "images/armadura_humano.png";

    // Implementación del método abstracto armadura()
    // Devuelve una descripción textual de la armadura
    @Override
    public String armadura() {
        return "Equilirada y funcional, ofrece buena dfensa y durabilidad, "
                + "sin destacar en ninguna caracteristic externa,";
    }

    // Implementación del método abstracto getImg()
    // Devuelve la ruta de la imagen de la armadura
    @Override
    public String getImg() {
        return img;
    }

    // Implementación del método abstracto stats()
    // Devuelve las estadísticas principales: defensa y material
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Material: " + material;
    }
}
