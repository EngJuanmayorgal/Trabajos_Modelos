// Definimos el paquete donde se encuentra la clase
package Fabrica;
/**
 * 
 * @author Juan Mayorga, Mariam, Samuel
 */
// Importamos las interfaces y clases necesarias para construir el personaje Orco
import Arma.Arma;                   // Importa la interfaz o clase Arma
import Arma.ArmaOrco;               // Importa la implementación concreta del arma de los orcos
import Armadura.Armadura;           // Importa la interfaz o clase Armadura
import Armadura.ArmaduraOrco;       // Importa la implementación concreta de la armadura de los orcos
import Cuerpos.Cuerpo;              // Importa la interfaz o clase Cuerpo
import Cuerpos.CuerpoOrco;          // Importa la implementación concreta del cuerpo de los orcos
import Monturas.Montura;            // Importa la interfaz o clase Montura
import Monturas.MonturaOrco;        // Importa la implementación concreta de la montura de los orcos

// Declaramos la clase FabricaOrcos como final
// Esto significa que no puede ser heredada por otra clase
// Además, hereda de FabricaAbstracta, por lo que debe implementar todos sus métodos abstractos
public final class FabricaOrcos extends FabricaAbstracta {

    // Atributos privados que representan las partes del personaje Orco
    private Cuerpo cuerpo;        // Guarda el cuerpo del orco
    private Montura montura;      // Guarda la montura del orco
    private Armadura armadura;    // Guarda la armadura del orco
    private Arma arma;            // Guarda el arma del orco

    // Constructor de la clase FabricaOrcos
    // Al crear un objeto, automáticamente se construyen todas las partes del orco
    public FabricaOrcos() {
        CrearArma();       // Crea el arma del orco
        CrearArmadura();   // Crea la armadura del orco
        CrearCuerpo();     // Crea el cuerpo del orco
        CrearMontura();    // Crea la montura del orco
    }

    // Método que devuelve el cuerpo del orco creado
    @Override
    public Cuerpo getCuerpo() {
        return cuerpo;
    }

    // Método que devuelve la montura del orco creada
    @Override
    public Montura getMontura() {
        return montura;
    }

    // Método que devuelve la armadura del orco creada
    @Override
    public Armadura getArmadura() {
        return armadura;
    }

    // Método que devuelve el arma del orco creada
    @Override
    public Arma getArma() {
        return arma;
    }

    // Método que crea un cuerpo específico para el orco
    @Override
    public void CrearCuerpo() {
        cuerpo = new CuerpoOrco();   // Se asigna un objeto CuerpoOrco al atributo cuerpo
    }

    // Método que crea una montura específica para el orco
    @Override
    public void CrearMontura() {
        montura = new MonturaOrco(); // Se asigna un objeto MonturaOrco al atributo montura
    }

    // Método que crea una armadura específica para el orco
    @Override
    public void CrearArmadura() {
        armadura = new ArmaduraOrco(); // Se asigna un objeto ArmaduraOrco al atributo armadura
    }

    // Método que crea un arma específica para el orco
    @Override
    public void CrearArma() {
        arma = new ArmaOrco();         // Se asigna un objeto ArmaOrco al atributo arma
    }
}
