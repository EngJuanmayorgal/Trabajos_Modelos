package Servlets;

import Fabrica.FabricaAbstracta;
import Fabrica.FabricaElfos;
import Fabrica.FabricaEnanos;
import Fabrica.FabricaHumanos;
import Fabrica.FabricaOrcos;

public class Pool {

    private static FabricaAbstracta f;
    public static Pool instancia;

    public Pool() {
    }

    public static Pool getInstancia(String pers) {
        if (instancia == null) {
            instancia = new Pool();
            Escoger(pers);
        }
        return instancia;
    }

    private static void Escoger(String pers) {
        if ("humano".equalsIgnoreCase(pers)) {
            f = new FabricaHumanos();
        } else if ("elfo".equalsIgnoreCase(pers)) {
            f = new FabricaElfos();
        } else if ("enano".equalsIgnoreCase(pers)) {
            f = new FabricaEnanos();
        } else if ("orco".equalsIgnoreCase(pers)) {
            f = new FabricaOrcos();
        }
    }

    public FabricaAbstracta getF() {
        return f;
    }

    public static void reiniciarInstancia() {
        instancia = null;
    }
}
