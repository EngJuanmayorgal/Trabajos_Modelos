package Arma; // Paquete donde se encuentra la clase Arma

// Clase abstracta Arma que define la estructura general
// para todas las armas específicas (ej: arma de elfo, enano, humano, orco)
public abstract class Arma {

    // Método abstracto que debe ser implementado por las subclases
    // Retorna una descripción del arma
    public abstract String arma();

    // Método abstracto que debe ser implementado por las subclases
    // Retorna las estadísticas específicas del arma
    public abstract String stats();

    // Método abstracto que debe ser implementado por las subclases
    // Devuelve el nombre del arma
    public abstract String getName();

    // Método abstracto que debe ser implementado por las subclases
    // Devuelve la ruta o referencia a la imagen del arma
    public abstract String getImg();
} // Fin de la clase abstracta Arma
