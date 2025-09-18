package Fabrica;

// Importamos el método exit de la clase System para poder salir del programa en cualquier momento
import static java.lang.System.exit;
// Importamos la clase Scanner para leer datos ingresados por el usuario desde consola
import java.util.Scanner;

// Declaramos la clase Cliente como final, lo que significa que no puede ser heredada
public final class Cliente {

    // Atributo de tipo FabricaAbstracta, que será la referencia a la fábrica concreta seleccionada
    public FabricaAbstracta f;

    // Constructor de la clase Cliente
    public Cliente() {
        // Llamamos al método Menu() al crear un objeto Cliente
        Menu();
    }

    // Método Menu: se encarga de mostrar opciones al usuario y gestionar la interacción
    public void Menu() {
        // Creamos un objeto Scanner para leer la entrada del usuario desde consola
        Scanner sc = new Scanner(System.in);
        // Variable para guardar la opción ingresada por el usuario
        String opcion = "";

        // Bucle infinito para mantener el menú en ejecución hasta que se elija salir
        while (true) {
            // Mostramos en pantalla las opciones del menú
            System.out.println(""
                    + "\nSELECCION DE PERSONAJE: "
                    + "\n1. Humano"
                    + "\n2. Elfo"
                    + "\n3. Orco"
                    + "\n4. Enano"
                    + "\n5. Salir");
            // Leemos la opción ingresada como texto
            opcion = sc.nextLine();
            try {
                // Convertimos la opción a número entero
                int opc = Integer.parseInt(opcion);
                // Llamamos al método Seleccion con la opción
                if (Seleccion(opc)) {
                    // Si se seleccionó correctamente, mostramos las características del personaje
                    System.out.println("Caracteristicas del personaje:");
                    // Obtenemos y mostramos el cuerpo del personaje
                    System.out.println("CUERPO: \n" + "    " + f.getCuerpo().Cuerpo());
                    // Obtenemos y mostramos la montura del personaje
                    System.out.println("MONTURA: \n" + "    " + f.getMontura().montura());
                    // Obtenemos y mostramos la armadura del personaje
                    System.out.println("ARMADURA: \n" + "    " + f.getArmadura().armadura());
                    // Obtenemos y mostramos el arma del personaje
                    System.out.println("ARMA: \n" + "    " + f.getArma().arma());

                    // Preguntamos al usuario si desea continuar
                    System.out.println("Continuar??\n1.si");
                    // Leemos la nueva opción
                    opcion = sc.nextLine();
                    try {
                        // Convertimos la opción a número entero
                        opc = Integer.parseInt(opcion);
                        // Evaluamos la respuesta del usuario
                        switch (opc) {
                            case 1:
                                // Si eligió "1", volvemos a mostrar el menú
                                Menu();
                                break;
                            default:
                                // Si no ingresó "1", se considera incorrecto y el programa finaliza
                                System.out.println("Opcion incorrecta.\n Adios.");
                                exit(0);
                        }
                    } catch (NumberFormatException e) {
                        // Si el usuario no ingresó un número, mostramos error y salimos del programa
                        System.out.println("Opcion incorrecta.\n Adios.");
                        exit(0);
                    }
                }
            } catch (NumberFormatException e) {
                // Si el usuario no ingresó un número al principio, mostramos error
                System.out.println("\nOpcion incorrecta.\n");
            }
        }
    }

    // Método Seleccion: según la opción elegida, asigna la fábrica correspondiente
    public boolean Seleccion(int opcion) {

        // Según el caso, se crea una fábrica concreta
        switch (opcion) {
            case 1:
                // Si se eligió "1", asignamos una fábrica de humanos
                f = new FabricaHumanos();
                break;
            case 2:
                // Si se eligió "2", asignamos una fábrica de elfos
                f = new FabricaElfos();
                break;
            case 3:
                // Si se eligió "3", asignamos una fábrica de orcos
                f = new FabricaOrcos();
                break;
            case 4:
                // Si se eligió "4", asignamos una fábrica de enanos
                f = new FabricaEnanos();
                break;
            case 5:
                // Si se eligió "5", mostramos mensaje de despedida y salimos del programa
                System.out.println("Buen dia.");
                exit(0);
                break;
            default:
                // Si la opción no corresponde a ninguna válida, mostramos error
                System.out.println("\nOpcion incorrecta.\n");
                return false;
        }
        // Retornamos true si la selección fue válida
        return true;
    }

    // Método main: punto de entrada del programa
    public static void main(String[] args) {
        // Creamos un nuevo objeto Cliente, lo que automáticamente ejecuta el menú
        new Cliente();
    }
}

