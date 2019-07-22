print""
print "Bienvenido a control de Gastos de Paseo"
i=1
while i==1:
		N=raw_input("Ingrese su nombre: ")
		print"Bienvenido ", N
		D=float(input("Ingrese la cantidad de dinero que tiene para Gastar: Q."))
		print"""                Gastos
	* Brazalete Q.50.00 c/u	
	* 5 Comidas Q.------ c/u
	* Noche de hospedaje 
	  Nacional= Q.500.00 c/u Extranjero= Q.1200.00 c/u"""
		print""
		CU=int(input("Ingrese la cantidad de usuarios que iran al paseo : "))
		NA=int(input("Indique si es Nacional = 1 / Extranjero = 2 : "))
		DC=int(input("Cuanto desea Gastar en cada comida: Q."))
		B=50*CU
		CT=DC*5
		C=CT*CU
		Nac=0
		if NA==1:
			Nac=500*CU
		elif NA==2:
			Nac==1200*CU
		else:
			print"No coincide: "
			NA=int(input("Indique si es Nacional = 1 / Extranjero = 2 "))
		T=B+C+Nac
		A=D-T
		Tc=A/CU
		print N, "Su cuenta es :"
		print""
		print" CUENTA "
		print" Brazalete = Q.", B
		print" 5 Comidas = Q.", C
		print" Hospedaje = Q.", Nac
		print" Total = Q.", T
		print" Dinero Sobrante = Q.", A
		print" Le Tocaria a cada uno : Q.", Tc 
		print"" 	
		if D<T:
			print "Lo sentimos, El dinero no es suficiente"
		else:
			print "Que tenga un buen viaje ", N	
			print""		