package Fabrica;

import Arma.Arma;
import Arma.ArmaHumano;
import Armadura.Armadura;
import Armadura.ArmaduraHumano;
import Cuerpos.Cuerpo;
import Cuerpos.CuerpoHumano;
import Monturas.Montura;
import Monturas.MonturaHumano;

public final class FabricaHumanos extends FabricaAbstracta {

    private Cuerpo cuerpo;
    private Montura montura;
    private Armadura armadura;
    private Arma arma;

    public FabricaHumanos() {
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
        cuerpo = new CuerpoHumano();
    }

    @Override
    public void CrearMontura() {
        montura = new MonturaHumano();
    }

    @Override
    public void CrearArmadura() {
        armadura = new ArmaduraHumano();
    }

    @Override
    public void CrearArma() {
        arma = new ArmaHumano();
    }

}
