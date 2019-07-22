#aqui es para q ingrese el numero
N=input("ingrese el numero que desea saber la tabla: ")
while N:
	if N:
		M=1
		while M<11:
			print N, "x", M, "=", N*M
			M+=1	
		N=False	
		N=input("ingrese el numero que desea saber la tabla: ")
	else:
	    print"Error"
	    N=input("ingrese el numero que desea saber la tabla: ")	
