// Definimos el paquete al que pertenece esta clase
package Fabrica;
/**
 * 
 * @author Juan Mayorga, Mariam, Samuel
 */

// Importamos las clases necesarias de los diferentes paquetes
import Arma.Arma;           // Importa la interfaz o clase Arma
import Armadura.Armadura;   // Importa la interfaz o clase Armadura
import Cuerpos.Cuerpo;      // Importa la interfaz o clase Cuerpo
import Monturas.Montura;    // Importa la interfaz o clase Montura

// Declaramos la clase FabricaAbstracta como abstracta
// Esto significa que no se puede instanciar directamente
// y que sirve como base para que otras fábricas concretas la hereden
public abstract class FabricaAbstracta {

    // Método abstracto para crear un objeto de tipo Cuerpo
    // Las fábricas concretas implementarán este método
    public abstract void CrearCuerpo();

    // Método abstracto para crear un objeto de tipo Montura
    public abstract void CrearMontura();

    // Método abstracto para crear un objeto de tipo Armadura
    public abstract void CrearArmadura();

    // Método abstracto para crear un objeto de tipo Arma
    public abstract void CrearArma();

    // Método abstracto que devuelve un objeto de tipo Cuerpo
    // Se usará para obtener el cuerpo creado
    public abstract Cuerpo getCuerpo();

    // Método abstracto que devuelve un objeto de tipo Montura
    public abstract Montura getMontura();

    // Método abstracto que devuelve un objeto de tipo Armadura
    public abstract Armadura getArmadura();

    // Método abstracto que devuelve un objeto de tipo Arma
    public abstract Arma getArma();
}
