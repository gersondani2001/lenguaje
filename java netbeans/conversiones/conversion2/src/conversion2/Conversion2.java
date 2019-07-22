/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package conversion2;
import java.util.Scanner;
/**
 *
 * @author Pablo
 */
public class Conversion2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner Numero=new Scanner(System.in);
        System.out.println("Ingrese su Cantidad en Grados Fahrenheit : ");
        Double CantidadEnFahrenheit=Numero.nextDouble();
        Double ResultadoEnCelcius=(CantidadEnFahrenheit-32)*5/9;
        System.out.println(CantidadEnFahrenheit+" F° es igual a = "+ResultadoEnCelcius+" C°");
    }
    }
    
}
