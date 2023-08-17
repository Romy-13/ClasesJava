
import java.util.Scanner;


public class Lección2 {

    public static void main(String[] args) {
        //       var condicion = false;
        //     if (condicion) {
        //         System.out.println("condicion verdadera");//condición simple
        //
        //   } else {
        //           System.out.println("condicion falsa");//condición doble

        //       }
        //       var numero = 4;
        //       var numeroTexto = "Número desconocido";
        //       if (numero == 1) {
        //           numeroTexto = "Número uno";
        //       } else if (numero == 2) {
        //           numeroTexto = "Número dos";
        //       } else if (numero == 3) {
        //           numeroTexto = "Número tres";
        //       } else if (numero == 4) {
        //           numeroTexto = "Número cuatro";
        //       } else {
        //           numeroTexto = "Número no encontrado";
        //       }
        //      System.out.println("numeroTexto = " + numeroTexto);
        
        //     Sentencia de control switch:
        Scanner entrada = new Scanner(System.in);
        System.out.println("Dijite un número: ");
        var numero = Integer.parseInt(entrada.nextLine());
        
        var numeroTexto = "Valor desconocido";
        switch (numero) {
            case 1:
                numeroTexto = "Número uno";
                break;
            case 2:
                numeroTexto = "Número dos";
                break;
            case 3:
                numeroTexto = "Número tres";
                break;
            case 4:
                numeroTexto = "Número cuatro";
                break;
            default:
                numeroTexto = "Caso no encontrado";
        }        
        System.out.println("numeroTexto = " + numeroTexto);

        

    }
}
