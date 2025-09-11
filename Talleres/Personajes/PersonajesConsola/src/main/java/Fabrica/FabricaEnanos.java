package Fabrica;

import Arma.Arma;
import Arma.ArmaEnano;
import Armadura.Armadura;
import Armadura.ArmaduraEnano;
import Cuerpos.Cuerpo;
import Cuerpos.CuerpoEnano;
import Monturas.Montura;
import Monturas.MonturaEnano;

public final class FabricaEnanos extends FabricaAbstracta {

    private Cuerpo cuerpo;
    private Montura montura;
    private Armadura armadura;
    private Arma arma;

    public FabricaEnanos() {
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
        cuerpo = new CuerpoEnano();
    }

    @Override
    public void CrearMontura() {
        montura = new MonturaEnano();
    }

    @Override
    public void CrearArmadura() {
        armadura = new ArmaduraEnano();
    }

    @Override
    public void CrearArma() {
        arma = new ArmaEnano();
    }

}
