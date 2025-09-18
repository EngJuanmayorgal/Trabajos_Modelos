// Definimos el paquete donde se encuentra la clase
package Fabrica;

// Importamos las interfaces y clases necesarias para construir el personaje Elfo
import Arma.Arma;                 // Importa la interfaz o clase Arma
import Arma.ArmaElfo;             // Importa la implementación concreta del arma de los elfos
import Armadura.Armadura;         // Importa la interfaz o clase Armadura
import Armadura.ArmaduraElfo;     // Importa la implementación concreta de la armadura de los elfos
import Cuerpos.Cuerpo;            // Importa la interfaz o clase Cuerpo
import Cuerpos.CuerpoElfo;        // Importa la implementación concreta del cuerpo de los elfos
import Monturas.Montura;          // Importa la interfaz o clase Montura
import Monturas.MonturaElfo;      // Importa la implementación concreta de la montura de los elfos

// Declaramos la clase FabricaElfos como final
// Esto significa que no podrá ser heredada por otra clase
// Además, extiende de FabricaAbstracta, por lo que debe implementar todos sus métodos abstractos
public final class FabricaElfos extends FabricaAbstracta {

    // Atributos privados que almacenan las partes del personaje Elfo
    private Cuerpo cuerpo;        // Guarda el cuerpo del elfo
    private Montura montura;      // Guarda la montura del elfo
    private Armadura armadura;    // Guarda la armadura del elfo
    private Arma arma;            // Guarda el arma del elfo

    // Constructor de la clase FabricaElfos
    // Al instanciar un objeto, automáticamente se crean todas las partes del personaje Elfo
    public FabricaElfos() {
        CrearArma();       // Crea el arma del elfo
        CrearArmadura();   // Crea la armadura del elfo
        CrearCuerpo();     // Crea el cuerpo del elfo
        CrearMontura();    // Crea la montura del elfo
    }

    // Método que devuelve el cuerpo del elfo creado
    @Override
    public Cuerpo getCuerpo() {
        return cuerpo;
    }

    // Método que devuelve la montura del elfo creada
    @Override
    public Montura getMontura() {
        return montura;
    }

    // Método que devuelve la armadura del elfo creada
    @Override
    public Armadura getArmadura() {
        return armadura;
    }

    // Método que devuelve el arma del elfo creada
    @Override
    public Arma getArma() {
        return arma;
    }

    // Método que crea un cuerpo específico para el elfo
    @Override
    public void CrearCuerpo() {
        cuerpo = new CuerpoElfo();   // Asigna un nuevo objeto CuerpoElfo al atributo cuerpo
    }

    // Método que crea una montura específica para el elfo
    @Override
    public void CrearMontura() {
        montura = new MonturaElfo(); // Asigna un nuevo objeto MonturaElfo al atributo montura
    }

    // Método que crea una armadura específica para el elfo
    @Override
    public void CrearArmadura() {
        armadura = new ArmaduraElfo(); // Asigna un nuevo objeto ArmaduraElfo al atributo armadura
    }

    // Método que crea un arma específica para el elfo
    @Override
    public void CrearArma() {
        arma = new ArmaElfo();        // Asigna un nuevo objeto ArmaElfo al atributo arma
    }
}
