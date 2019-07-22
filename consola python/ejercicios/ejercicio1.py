def Menu():
	#crear menu 
	print""">>>Bienvenido al control de usuario<<<
Menu:
1)Crear cuenta
2)Iniciar sesion
3)Extra
4)Salir"""
#crear contol de usuario
def Control():
    Menu()
    opc = int(input("Selecione la opcion que desea realizar:"))
    while (opc >0 and opc <5):
        if (opc==1):
            print "Crear Usuario"
            No=raw_input("Ingrese su nombre: ")
            print""
            Ap=raw_input("Ingrese su apellido: ")
            print""
            Nick=raw_input("Ingrese su Nickname o Apodo: ")
            print""
            Con=raw_input("Ingrese su contrasena : ")
            print""
            Con3=raw_input("Vuelva a ingresar su contrasena : ")
            print""
            Ed=int(input("Ingrese su edad: "))
            print""
            fecha=raw_input("ingrese el mes en que nacio : ")
            print""
            fecha1=int(input("ingrese el dia en que nacio : "))
            print""
            fecha2=long(input("ingrese el ano en que nacio: " ))
            print""
            Se=raw_input("ingrese su sexo,o especie: ")
            print""
            if Ed<18 or Con!=Con3: 
                print"Error o es menor de edad o no coinciden las contrasenas"
            else:
                print""     
                print"___Felicidades Usted a creado su cuenta___"
                print""
                print""">>>Bienvenido al control de usuario<<<
Menu:
1)Crear cuenta
2)Iniciar sesion
4)Extra
6)Salir"""
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print""
            print"Iniciar sesion"
            Nick2=raw_input("Ingrese su Nickname o Apodo: ")
            Con2=raw_input("Ingrese su Contrasena: ")
            print""
            if Nick2==Nick and Con2==Con:
                print""
                print"Bienvenido Usuario", Nick
                print"*Su Informacion:*"
                print"Nombre= ", No
                print"Apellido= ", Ap
                print"Edad= ", Ed
                print"Nacio el= ", fecha1, "de", fecha, "de", fecha2
                print"sexo= ", Se  
                print""
                print"___Felicidades Usted a Iniciado sesion___"
                print""
                print""">>>Bienvenido al control de usuario<<<    
Menu:
1)Crear cuenta
2)Iniciar sesion
4)Extra
6)Salir"""
            else:
                print""">>>Bienvenido al control de usuario<<<    
Menu:
1)Crear cuenta
2)Iniciar sesion
4)Extra
6)Salir"""
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print""
            print"""
            >>>Integrantes<<<
        	*Stephany Mishel Palencia de leon*
        	*Allan Alexander Ramirez Zet*
        	*Jennifer Gabriela Roquell Gomez*
        	*Pedro Eduardo Velasquez Tol*
        	*Rolman Alexander Requena Pelico*
        	*Luis Anghelo Romero*
        	*Luis Toledo*
                *Karla zipaque*
                *Dayana Elizabeth xiloj*
                *Creditos:Jose Pablo Angel*
                *Control de Usuario***
                *Programacion*
                *4to Baco B*
                *Liceo Mixto Compu-Market*"""
            print""
            print""">>>Bienvenido al control de usuario<<<
Menu:
1)Crear cuenta
2)Iniciar sesion
4)Extra
6)Salir"""
            opc = int(input("Selecione Opcion\n"))
    else:
        print"Error, no existe"
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
Control()
