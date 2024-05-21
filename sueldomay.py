i=int=1
cont=int

sueldo=float
smay =float

ce=int(input("ingrese la cantidad de empleado"))

while (i<=ce):
    sueldo=input("ingrese su sueldo")
    if sueldo > smay:
        smay=sueldo
        cont=i
    i=i+1

print("el empleado con mas sueldo es el ",c, " ganando un total de ",smay)