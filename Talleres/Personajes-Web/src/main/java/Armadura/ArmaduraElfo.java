package Armadura; // El paquete donde está ubicada la clase

// Clase concreta que representa la armadura utilizada por los elfos
// Hereda de la clase abstracta Armadura y proporciona su propia implementación
public class ArmaduraElfo extends Armadura {

    // Atributo que define el nivel de defensa física de la armadura
    private int defensa = 20;

    // Atributo que indica la resistencia mágica de la armadura
    private int resistenciaMagica = 32;

    // Ruta de la imagen asociada a la armadura del elfo
    private final String img ="images/armadura_elfo.png";

    // Implementación del método abstracto armadura()
    // Devuelve una descripción textual de las características de la armadura
    @Override
    public String armadura() {
        return "Ligera y elegante, brinda resistencia magica y fleibilidad "
                + "en combate, aunque menos protectora fisicamente.";
    }

    // Implementación del método abstracto getImg()
    // Devuelve la ruta de la imagen asociada a la armadura
    @Override
    public String getImg() {
        return img;
    }

    // Implementación del método abstracto stats()
    // Devuelve las estadísticas de la armadura: defensa y resistencia mágica
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Defensa: " + defensa
                + "Resistencia magica: " + resistenciaMagica;
    }

}
