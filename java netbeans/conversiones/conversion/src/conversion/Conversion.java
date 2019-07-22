/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package conversion;
import java.util.Scanner;
/**
 *
 * @author Pablo
 */
public class Conversion {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner Numero=new Scanner(System.in);
        System.out.println("Ingrese su Cantidad en Grados Celcius : ");
        Double CantidadEnCelcius=Numero.nextDouble();
        Double ResultadoEnFahrenheit=((9*CantidadEnCelcius)/5)+32;
        System.out.println(CantidadEnCelcius+" C° es igual a = "+ResultadoEnFahrenheit+" F°");
    }
    
}
