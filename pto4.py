l=[]

print('Ingrese cinco numeros reales')
n1=float(input('Ingrese el primer numero: '))
l.append(n1)
n2=float(input('Ingrese el segundo numero: '))
l.append(n2)
n3=float(input('Ingrese el tercer numero: '))
l.append(n3)
n4=float(input('Ingrese el cuarto numero: '))
l.append(n4)
n5=float(input('Ingrese el quinto numero: '))
l.append(n5)
mayor=max(l)
menor=min(l)
prom=sum(l)/len(l)

print('El numero mayor es: ', mayor)
print('El numero menor es: ', menor)
print('El promedio de los numeros es: ', prom)




