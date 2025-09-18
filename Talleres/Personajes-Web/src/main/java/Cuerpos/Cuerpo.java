package Cuerpos; // Paquete donde se almacenan las clases relacionadas con los cuerpos

// Clase abstracta que define la estructura básica de un cuerpo
public abstract class Cuerpo {

    // Método abstracto que devuelve la descripción del cuerpo
    public abstract String Cuerpo();

    // Método abstracto que devuelve las estadísticas del cuerpo
    public abstract String stats();

    // Método abstracto que devuelve el nombre del cuerpo
    public abstract String getName();   

    // Método abstracto que devuelve la ruta de la imagen del cuerpo
    public abstract String getImg();
}
