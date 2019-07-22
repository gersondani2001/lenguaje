/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tabla;
import java.util.Scanner;
/**
 *
 * @author Pablo
 */
public class Tabla {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner X=new Scanner(System.in);
        System.out.println("Ingrese Numero: ");
        double numero=X.nextDouble();
        for(int c=0;c<=10;c++){
            double total=numero*c;
            System.out.println(numero+" x "+c+" = "+total);
        }
    }
    
}
