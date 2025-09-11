package Fabrica;

import static java.lang.System.exit;
import java.util.Scanner;

public final class Cliente {

    public FabricaAbstracta f;

    public Cliente() {
        Menu();
    }

    public void Menu() {
        Scanner sc = new Scanner(System.in);
        String opcion = "";

        while (true) {
            System.out.println(""
                    + "\nSELECCION DE PERSONAJE: "
                    + "\n1. Humano"
                    + "\n2. Elfo"
                    + "\n3. Orco"
                    + "\n4. Enano"
                    + "\n5. Salir");
            opcion = sc.nextLine();
            try {
                int opc = Integer.parseInt(opcion);
                if (Seleccion(opc)) {
                    System.out.println("Caracteristicas del personaje:");
                    System.out.println("CUERPO: \n" + "    " + f.getCuerpo().Cuerpo());
                    System.out.println("MONTURA: \n" + "    " + f.getMontura().montura());
                    System.out.println("ARMADURA: \n" + "    " + f.getArmadura().armadura());
                    System.out.println("ARMA: \n" + "    " + f.getArma().arma());
                    System.out.println("Continuar??\n1.si");
                    opcion = sc.nextLine();
                    try {
                        opc = Integer.parseInt(opcion);
                        switch (opc) {
                            case 1:
                                Menu();
                                break;
                            default:
                                System.out.println("Opcion incorrecta.\n Adios.");
                                exit(0);
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("Opcion incorrecta.\n Adios.");
                        exit(0);
                    }
                }
            } catch (NumberFormatException e) {
                System.out.println("\nOpcion incorrecta.\n");
            }
        }
    }

    public boolean Seleccion(int opcion) {

        //Segun el caso se da la descripcion del personaje
        switch (opcion) {
            case 1:
                f = new FabricaHumanos();
                break;
            case 2:
                f = new FabricaElfos();
                break;
            case 3:
                f = new FabricaOrcos();
                break;
            case 4:
                f = new FabricaEnanos();
                break;
            case 5:
                System.out.println("Buen dia.");
                exit(0);
                break;
            default:
                System.out.println("\nOpcion incorrecta.\n");
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        new Cliente();
    }
}
