#temperaturas
repetir='S'

while repetir=='S' or repetir=='s':
	print('Ingrese la temperatura en Grados celsius')
	c=float(input('Ingrese la temperatura en Grados celsius: '))
	print('Presione 1 si desea Grados Fahrenheit')
	print('Presione 2 si desea Grados Rankine')
	print('Presione 3 si desea Grados Kelvin')
	num=int(input('Ingrese la opión: '))

	if num==1:
		f=round(((5/9)*c) +32,1)
		print(c, 'Grados celsius es equivalente a',f,'Grados Fahrenheit')

	if num==2:
		r=round((c*1.8)+491.67,1)
		print(c, 'Grados celsius es equivalente a',r,'Grados Rankine ')
	if num==3:
		k=round(c+273.15,1)
		print(c, 'Grados celsius es equivalente a',k,'Grados Kelvin')
	repetir=input('Desea continuas S/N?')