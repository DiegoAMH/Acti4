#temperaturas
def gf(n):
	return round(((5/9)*c) +32,1)
def gr(n):
	return round((c*1.8)+491.67,1)
def gk(n):
	return round(c+273.15,1) 

repetir='S'
while repetir=='S' or repetir=='s':
	print('Ingrese la temperatura en Grados celsius')
	c=float(input('Ingrese la temperatura en Grados celsius: '))
	print('Presione 1 si desea Grados Fahrenheit')
	print('Presione 2 si desea Grados Rankine')
	print('Presione 3 si desea Grados Kelvin')
	num=int(input('Ingrese la opión: '))

	if num==1:
		print(c, 'Grados celsius es equivalente a',gf(c),'Grados Fahrenheit')

	if num==2:
		print(c, 'Grados celsius es equivalente a',gr(c),'Grados Rankine ')

	if num==3:
		print(c, 'Grados celsius es equivalente a',gk(c),'Grados Kelvin')
	repetir=input('Desea continuas S/N?')