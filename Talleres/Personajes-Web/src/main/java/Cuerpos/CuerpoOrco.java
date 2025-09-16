package Cuerpos;

public class CuerpoOrco extends Cuerpo {

    private int fuerza = 20;
    private int resistencia = 20;
    private int brutalidad = 20;
    private final String name = "Orco";
    private final String img = "images/orco.png";

    @Override
    public String getImg() {
        return img;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String Cuerpo() {
        return "Robusto y brutal, con gran fuerza y resistenci. Poco preciso "
                + "y lento, pero imparable en combate fisico.";
    }

    @Override
    public String stats() {
        return "\nEstadisticas:\n"
                + "Destreza: " + fuerza
                + "Magia: " + resistencia
                + "Inteligencia: " + brutalidad;
    }
}
