// Definimos el paquete donde se encuentra la clase
package Fabrica;
/**
 * 
 * @author Juan Mayorga, Mariam, Samuel
 */

// Importamos las interfaces y clases necesarias para construir el personaje Humano
import Arma.Arma;                     // Importa la interfaz o clase Arma
import Arma.ArmaHumano;               // Importa la implementación concreta del arma de los humanos
import Armadura.Armadura;             // Importa la interfaz o clase Armadura
import Armadura.ArmaduraHumano;       // Importa la implementación concreta de la armadura de los humanos
import Cuerpos.Cuerpo;                // Importa la interfaz o clase Cuerpo
import Cuerpos.CuerpoHumano;          // Importa la implementación concreta del cuerpo de los humanos
import Monturas.Montura;              // Importa la interfaz o clase Montura
import Monturas.MonturaHumano;        // Importa la implementación concreta de la montura de los humanos

// Declaramos la clase FabricaHumanos como final
// Esto significa que no puede ser heredada por otra clase
// Además, hereda de FabricaAbstracta, por lo que debe implementar todos sus métodos abstractos
public final class FabricaHumanos extends FabricaAbstracta {

    // Atributos privados que representan las partes del personaje Humano
    private Cuerpo cuerpo;        // Guarda el cuerpo del humano
    private Montura montura;      // Guarda la montura del humano
    private Armadura armadura;    // Guarda la armadura del humano
    private Arma arma;            // Guarda el arma del humano

    // Constructor de la clase FabricaHumanos
    // Al crear un objeto, automáticamente se construyen todas las partes del humano
    public FabricaHumanos() {
        CrearArma();       // Crea el arma del humano
        CrearArmadura();   // Crea la armadura del humano
        CrearCuerpo();     // Crea el cuerpo del humano
        CrearMontura();    // Crea la montura del humano
    }

    // Método que devuelve el cuerpo del humano creado
    @Override
    public Cuerpo getCuerpo() {
        return cuerpo;
    }

    // Método que devuelve la montura del humano creada
    @Override
    public Montura getMontura() {
        return montura;
    }

    // Método que devuelve la armadura del humano creada
    @Override
    public Armadura getArmadura() {
        return armadura;
    }

    // Método que devuelve el arma del humano creada
    @Override
    public Arma getArma() {
        return arma;
    }

    // Método que crea un cuerpo específico para el humano
    @Override
    public void CrearCuerpo() {
        cuerpo = new CuerpoHumano();   // Se asigna un objeto CuerpoHumano al atributo cuerpo
    }

    // Método que crea una montura específica para el humano
    @Override
    public void CrearMontura() {
        montura = new MonturaHumano(); // Se asigna un objeto MonturaHumano al atributo montura
    }

    // Método que crea una armadura específica para el humano
    @Override
    public void CrearArmadura() {
        armadura = new ArmaduraHumano(); // Se asigna un objeto ArmaduraHumano al atributo armadura
    }

    // Método que crea un arma específica para el humano
    @Override
    public void CrearArma() {
        arma = new ArmaHumano();         // Se asigna un objeto ArmaHumano al atributo arma
    }
}
