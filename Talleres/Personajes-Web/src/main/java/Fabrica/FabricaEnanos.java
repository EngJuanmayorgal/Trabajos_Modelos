// Definimos el paquete donde se encuentra la clase
package Fabrica;

// Importamos las interfaces y clases necesarias para construir el personaje Enano
import Arma.Arma;                   // Importa la interfaz o clase Arma
import Arma.ArmaEnano;              // Importa la implementación concreta del arma de los enanos
import Armadura.Armadura;           // Importa la interfaz o clase Armadura
import Armadura.ArmaduraEnano;      // Importa la implementación concreta de la armadura de los enanos
import Cuerpos.Cuerpo;              // Importa la interfaz o clase Cuerpo
import Cuerpos.CuerpoEnano;         // Importa la implementación concreta del cuerpo de los enanos
import Monturas.Montura;            // Importa la interfaz o clase Montura
import Monturas.MonturaEnano;       // Importa la implementación concreta de la montura de los enanos

// Declaramos la clase FabricaEnanos como final
// Esto significa que no puede ser heredada por otra clase
// Además, hereda de FabricaAbstracta, por lo que debe implementar todos sus métodos abstractos
public final class FabricaEnanos extends FabricaAbstracta {

    // Atributos privados que representan las partes del personaje Enano
    private Cuerpo cuerpo;        // Guarda el cuerpo del enano
    private Montura montura;      // Guarda la montura del enano
    private Armadura armadura;    // Guarda la armadura del enano
    private Arma arma;            // Guarda el arma del enano

    // Constructor de la clase FabricaEnanos
    // Al crear un objeto, automáticamente se construyen todas las partes del enano
    public FabricaEnanos() {
        CrearArma();       // Crea el arma del enano
        CrearArmadura();   // Crea la armadura del enano
        CrearCuerpo();     // Crea el cuerpo del enano
        CrearMontura();    // Crea la montura del enano
    }

    // Método que devuelve el cuerpo del enano creado
    @Override
    public Cuerpo getCuerpo() {
        return cuerpo;
    }

    // Método que devuelve la montura del enano creada
    @Override
    public Montura getMontura() {
        return montura;
    }

    // Método que devuelve la armadura del enano creada
    @Override
    public Armadura getArmadura() {
        return armadura;
    }

    // Método que devuelve el arma del enano creada
    @Override
    public Arma getArma() {
        return arma;
    }

    // Método que crea un cuerpo específico para el enano
    @Override
    public void CrearCuerpo() {
        cuerpo = new CuerpoEnano();   // Se asigna un objeto CuerpoEnano al atributo cuerpo
    }

    // Método que crea una montura específica para el enano
    @Override
    public void CrearMontura() {
        montura = new MonturaEnano(); // Se asigna un objeto MonturaEnano al atributo montura
    }

    // Método que crea una armadura específica para el enano
    @Override
    public void CrearArmadura() {
        armadura = new ArmaduraEnano(); // Se asigna un objeto ArmaduraEnano al atributo armadura
    }

    // Método que crea un arma específica para el enano
    @Override
    public void CrearArma() {
        arma = new ArmaEnano();         // Se asigna un objeto ArmaEnano al atributo arma
    }
}
