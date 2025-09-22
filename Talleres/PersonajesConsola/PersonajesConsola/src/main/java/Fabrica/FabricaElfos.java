package Fabrica;

import Arma.Arma;
import Arma.ArmaElfo;
import Armadura.Armadura;
import Armadura.ArmaduraElfo;
import Cuerpos.Cuerpo;
import Cuerpos.CuerpoElfo;
import Monturas.Montura;
import Monturas.MonturaElfo;

public final class FabricaElfos extends FabricaAbstracta {

    private Cuerpo cuerpo;
    private Montura montura;
    private Armadura armadura;
    private Arma arma;

    public FabricaElfos() {
        CrearArma();
        CrearArmadura();
        CrearCuerpo();
        CrearMontura();
    }

    @Override
    public Cuerpo getCuerpo() {
        return cuerpo;
    }

    @Override
    public Montura getMontura() {
        return montura;
    }

    @Override
    public Armadura getArmadura() {
        return armadura;
    }

    @Override
    public Arma getArma() {
        return arma;
    }

    @Override
    public void CrearCuerpo() {
        cuerpo = new CuerpoElfo();
    }

    @Override
    public void CrearMontura() {
        montura = new MonturaElfo();
    }

    @Override
    public void CrearArmadura() {
        armadura = new ArmaduraElfo();
    }

    @Override
    public void CrearArma() {
        arma = new ArmaElfo();
    }

}
