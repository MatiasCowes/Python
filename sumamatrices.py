cant=int(input("ingrese la cantidad de columnas y filas"))
a=[cant,cant]
b=[cant,cant]
c=[cant,cant]
numa=int
numb=int
i=int
j=int
for i in range(cant):
    a.append([])
    b.append([])
    c.append([])
    for j in range(cant):
        numa=input("ingrese el numero de a")
        a.append(numa)
        numb=input("ingrese el numero de b")
        b.append(numb)
        c.append(a[i][j]+b[i][j])

print(c)