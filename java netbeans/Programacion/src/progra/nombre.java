/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package progra;
import java.util.Scanner;
/**
 *
 * @author Pablo
 */
public class nombre {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner N=new Scanner(System.in);
        System.out.println("Ingrese su Nombre: ");
        String Nombre=N.nextLine();
        System.out.println("Bienvenido "+Nombre);
        
    }
    
}
