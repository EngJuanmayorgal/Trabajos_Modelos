package Armadura; // El paquete donde se encuentra la clase

// Clase abstracta que representa el concepto general de una armadura
// Define los métodos que todas las armaduras concretas deben implementar
public abstract class Armadura {

    // Método abstracto que debe devolver una descripción general de la armadura
    public abstract String armadura();

    // Método abstracto que debe devolver las estadísticas específicas de la armadura
    public abstract String stats();

    // Método abstracto que debe devolver la ruta de la imagen asociada a la armadura
    public abstract String getImg();

}
