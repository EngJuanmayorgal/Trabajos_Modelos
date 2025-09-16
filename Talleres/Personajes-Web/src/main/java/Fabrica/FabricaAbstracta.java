package Fabrica;

import Arma.Arma;
import Armadura.Armadura;
import Cuerpos.Cuerpo;
import Monturas.Montura;

public abstract class FabricaAbstracta {

    public abstract void CrearCuerpo();

    public abstract void CrearMontura();

    public abstract void CrearArmadura();

    public abstract void CrearArma();

    public abstract Cuerpo getCuerpo();

    public abstract Montura getMontura();

    public abstract Armadura getArmadura();

    public abstract Arma getArma();


}
