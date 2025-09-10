package Fabrica;

import Arma.Arma;
import Armadura.Armadura;
import Cuerpos.Cuerpo;
import Monturas.Montura;

public abstract class FabricaAbstracta {

    public abstract Cuerpo CrearCuerpo();
    public abstract Montura CrearMontura();
    public abstract Armadura CrearArmadura();
    public abstract Arma CrearArma();
}
