print "***********************************************************"
print "************ Bienvenido a nuestro supermercado ************"
print "***********************************************************"
print "**** Este es el listado de productos que le ofrecemos: ****"
print "***********************************************************"

Suma = 0
Total = []
Total_Suma = []


print "-------------------------1. Arroz--------------------------"
print "-------------------------2. Frijol-------------------------"
print "-------------------------3. Aceite-------------------------"
print "-------------------------4. Jugos--------------------------"
print "-------------------------5. Galletas-----------------------"

print ""
Compra = input("______Ingrese el numero del producto que desee comprar:_____ ")



if Compra == 1:
	Numero1 = input("_____Ingrese la cantidad de arroz que desee comprar:_____ ")
	Valor1 = Numero1 * 3.00
	Total.append(Valor1)
	print Valor1
	print ""
elif Compra == 2:
	Numero2 = input("_____Ingrese el numero de elementos que desee comprar:_____ ")
	Valor2 = Numero2 * 2.50
	Total.append(Valor2)
	print Valor2
	print ""
elif Compra == 3:
	Numero3 = input("______Ingrese el numero de elementos que desee comprar:_____ ")
	Valor3 = Numero3 * 8.00
	Total.append(Valor3)
	print Valor3
	print ""
elif Compra == 4:
	Numero4 = input("_____Ingrese el numero de jugos que desee comprar:_____ ")
	Valor4 = Numero4 * 4.00
	Total.append(Valor4)
	print Valor4
	print ""
elif Compra == 5:
	Numero5 = input("_____Ingrese el numero de galletas que desee comprar:_____ ")
	Valor5 = Numero5 * 5.00
	Total.append(Valor5)
	print Valor5
	print ""
else:
	print "Lo sentimos//////   :(   este producto no existe.///// "
	print Total
	print ""

while Compra != 0:
	Compra = input("_____Ingrese el numero del siguiente producto:_____ ")
	if Compra == 1:
		Numero6 = input("_____Ingrese el numero de elementos que desee comprar:_____ ")
		Valor6 = Numero6 * 3.00
		Total.append(Valor6)
		print Valor6
		print ""
	elif Compra == 2:
		Numero7 = input("_____Ingrese el numero de elementos que desee comprar:_____ ")
		Valor7 = Numero7 * 2.50
		Total.append(Valor7)
		print Valor7
		print ""
	elif Compra == 3:
		Numero8 = input("_____Ingrese el numero de elementos que desee comprar:_____ ")
		Valor8 = Numero8 * 8.00
		Total.append(Valor8)
		print Valor8
		print ""
	elif Compra == 4:
		Numero9 = input("_____Ingrese el numero de jugos que desee comprar:_____ ")
		Valor9 = Numero9 * 4.00
		Total.append(Valor9)
		print Valor9
		print ""
	elif Compra == 5:
		Numero10 = input("_____Ingrese el numero de galletas que desee comprar:_____")
		Valor10 = Numero10 * 5.00
		Total.append(Valor10)
		print Valor10
		print ""
	elif Compra == 0:
		for s in Total:
			Suma += int(s)
			Total_Suma.append(Suma)
		print Total_Suma
		print "$$$$$$$$ OJO LA ULTIMA CANTIDAD ES SU TOTAL. $$$$$$$$"
	else:
		print "&&&&&&&&Lo sentimos   :(   este producto no existe.&&&&&&&&"
		print Total
		print ""