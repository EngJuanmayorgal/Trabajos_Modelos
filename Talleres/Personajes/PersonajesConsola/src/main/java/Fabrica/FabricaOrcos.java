package Fabrica;

import Arma.Arma;
import Arma.ArmaOrco;
import Armadura.Armadura;
import Armadura.ArmaduraOrco;
import Cuerpos.Cuerpo;
import Cuerpos.CuerpoOrco;
import Monturas.Montura;
import Monturas.MonturaOrco;

public final class FabricaOrcos extends FabricaAbstracta {

    private Cuerpo cuerpo;
    private Montura montura;
    private Armadura armadura;
    private Arma arma;

    public FabricaOrcos() {
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
        cuerpo = new CuerpoOrco();
    }

    @Override
    public void CrearMontura() {
        montura = new MonturaOrco();
    }

    @Override
    public void CrearArmadura() {
        armadura = new ArmaduraOrco();
    }

    @Override
    public void CrearArma() {
        arma = new ArmaOrco();
    }

}
