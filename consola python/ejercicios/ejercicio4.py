#definicion de metodo de salida
import sys
#define el menu
def Menu():
    print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    
Bienvenido a la calculadora
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """
#define la calculadora
def Calculadora():
    Menu()
    opc = int(input("Selecione la operacion que desea realizar : "))
    #crea ciclos o bucles
    while (opc >0 and opc <9):
        if (opc==1):
            print""
            print"xxxxxxxxxxxxxxx Suma: xxxxxxxxxxxxxxxx"
            print""
            a=float(input("Ingrese el primer numero de la Suma : "))
            b=float(input("Ingrese el segundo numero de la Suma : "))
            print a,+b
            print""
            print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """
            opc = int(input("Selecione Operacion: "))
        elif opc==2:
            print""
            print"xxxxxxxxxxxxxxx Resta: xxxxxxxxxxxxxxxx"
            print""

            a=float(input("Ingrese el primer numero de la Resta : "))
            b=float(input("Ingrese el numero que desea Restarle : "))
            print a, "-", b, "=", a-b
            print""
            print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """
            opc = int(input("Selecione Operacion: "))
        elif opc==3:
            print""
            print"xxxxxxxxxxxxx Multiplicacion: xxxxxxxxxxxxxx"
            print""

            a=float(input("Ingrese el primer numero de la Multiplicacion : "))
            b=float(input("Ingrese el segundo numero de la Multiplicacion : "))
            print a, "*", b, "=", a*b
            print""
            print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """
            opc = int(input("Selecione Operacion: "))
        elif opc==4:
            print""
            print"xxxxxxxxxxxxxx Division: xxxxxxxxxxxxxxx"
            print""
            a=float(input("Ingrese el primer numero de la Division : "))
            b=float(input("Ingrese el numero en que lo desea Dividir : "))
            print a, "/", b, "=", a/b
            print""
            print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """
            opc = int(input("Selecione Operacion: "))
        elif opc==5:
            print""
            print"xxxxxxxxxxxxxx Elevacion: xxxxxxxxxxxxxxx"
            print""
            a=int(input("Ingrese el primer numero que desea elevar al cuadrado : "))
            print a,"elevado al cuadrado es = ", a*a
            print""
            print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """
            opc = int(input("Selecione Operacion: "))
        elif opc==6:
            print""
            print"xxxxxxxxxxxxxx Porcentaje: xxxxxxxxxxxxxxx"
            print""
            a=float(input("Ingrese el numero total : "))
            b=float(input("ingrese el numero de porcentaje que le desea sacar : %"))
            c=b/100
            print "El %", b, "de", a, "=", a*c
            print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """ 
            opc = int(input("Selecione Operacion: "))
        elif opc==7:
            print"""
    Integrantes:

    Jose Pablo Angel Morales
    Russel Steven Andre Aguilar Fuentes 
    Jose David Ajqui Arevalo 
    Pablo Andres Canteo Mendez 
    Anderson Chun Morales
    Alexandra Peniel Escobar Cantoral  
    Eldin Joel Escobar Vasquez
    Misley Danely Franco Aguilar
    Samuel David Garcia Ramirez

    Datos:

    4to Baco B
    Programacion
    Liceo Compu-Market
    Grupo numero 1, Calculadora
    prof. Erick
    26/02/2018"""
            print""
            print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """
            opc = int(input("Selecione Operacion: "))  
        elif opc==8:
            print""
            print"Salir"
            print""
            print"--Adios---"
            print""
            sys.exit()
        elif opc==str:
            print""    
            print"ERROR, usted ingreso una letra "
            print""
            print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """ 
            opc = int(input("Selecione Operacion: "))
    else:
        print"ERROR , OPCION NO VALIDA"
        print""
        print"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
A Regresado al menu,vuelva a elejir una Opcion
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Menu de operaciones 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Potencia al cuadrado
6) Porcentaje
7) Informacion Extra
8) Salir  """
        opc = int(input("Selecione Operacion: "))                                                                                                                                                              
Calculadora()









