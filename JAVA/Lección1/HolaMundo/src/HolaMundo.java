
import java.util.Scanner;

public class HolaMundo {

    private static int var;

    public static void main(String[] args) {
        /*  System.out.println("Hola mundo java"); 
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
         */

        //Var - inferencia de tipo en java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //souyv + tab
        //Para ejecutar shift + F6 la tecla para mayús
        //Regla para definir una variable en Java*/

        /*var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //Ejercicio: Caracteres especiales en java
        var nombre = "Natalia";
        System.out.println("\nNueva linea: \n" + nombre);//Diagonal inversa y letra n:salto de linea
        System.out.println("tabulador: \t" + nombre);//Tabulador: espacio para centrar
        System.out.println("\t \t.:MENÚ:.");
        System.out.println("Retroceso: \b"+nombre);//Retroceso:retrocede un espacio o más
        System.out.println("Comillas simples: \'"+nombre+"\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");*/
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 =" + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado; " + titulo2 + " " + usuario2);*/
        /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:" + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte:" + Byte.MAX_VALUE);

        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("valor minimo del short:" + Short.MIN_VALUE);
        System.out.println("valor minimo de short:" + Short.MAX_VALUE);

        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("valor minimo de int:" + Integer.MIN_VALUE);
        System.out.println("valor maximo de int:" + Integer.MAX_VALUE);

        long numEnteroLong = 10;
        System.out.println("numEnteroLong =" + numEnteroLong);
        System.out.println("valor minimo de long:" + Long.MIN_VALUE);
        System.out.println("valor maximo de long:" + Long.MAX_VALUE);

        float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("valor minimo de float:" + Float.MIN_VALUE);
        System.out.println("valor maximo de float:" + Float.MAX_VALUE);

        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("valor minimo de double:" + Double.MIN_VALUE);
        System.out.println("valor maximo de double:" + Double.MAX_VALUE);*/
        
        //Inferencia de tipo var y tipos primitivos
        /*var numEntero = 20;//Las literales sin punto automáticamente son de tipo int
        System.out.println("numEntero = "+ numEntero);
        var numFloat = 10.0F;// Automáticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numdouble = " + numDouble);*/
        
        //Tipos primitivos char
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        var varCaracter1 = '\u0024';
        System.out.println("varCaracter1 = " + varCaracter1);//Indicamos a Java el codigo inicode
        var varDecimal1 = (char)36;//valor entero, le asigna valor int
        System.out.println("varDecimal1 = " + varDecimal1);
        var varCaracterSimbolo1 = '$';//Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int varCaracter = 'b';
        System.out.println("varCaracter = " + varCaracter);*/
        /*
        //Tipos Primitivos tipoa Booleanos
        var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool) {
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
        }
          
        //Algorítmo ¿es mayor de edad?
          var edad = 15;//Literal tener
          var adulto = edad >= 18;//Esta es una expreción boleana
          if (adulto){
              System.out.println("Eres mayor de edad");
          }
          else {
              System.out.println("Eres menor de edad");*/
        
//        /*//Converción de Tipos Primitivos
//        var edad = Integer.parseInt("20");
//        System.out.println("edad = " + edad);
//        var valorPi = Double.parseDouble("3.1416");
//        System.out.println("valorPi = " + valorPi);
//        
//        //Pedir un valor
        var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad: ");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad);*/
        
        //Converción tipo primitivo en Java 2 (convertir un tipo entero a string)
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "Programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        
    }

}  
