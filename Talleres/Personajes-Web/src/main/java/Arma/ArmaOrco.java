package Arma; // El paquete donde se encuentra esta clase

// Clase concreta que representa un arma utilizada por los orcos
// Extiende de la clase abstracta Arma
public class ArmaOrco extends Arma {

    // Atributo que indica el daño que puede causar el arma
    private int daño = 36;

    // Atributo que indica el peso del arma, influye en la velocidad de uso
    private int peso = 42;

    // Nombre del arma que se mostrará en la descripción
    private String name = "MazaOrca"; 

    // Ruta de la imagen que representa gráficamente al arma
    private final String img = "images/maza.jpg";

    // Método que devuelve una descripción general del arma orca
    @Override
    public String arma() {
        return "Arma pesada y destructiva, capaz de aplastar cualquier defensa. "
                + "Su lentitud se compensa con el gran tamaño que influye.";
    }

    // Método que retorna la ruta de la imagen del arma
    @Override
    public String getImg() {
        return img;
    }

    // Método que devuelve las estadísticas del arma
    // Muestra el daño y el peso
    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Daño: " + daño
                + " Peso: " + peso;
    }

    // Método que retorna el nombre del arma
    @Override
    public String getName() {
        return name;
    }
}
