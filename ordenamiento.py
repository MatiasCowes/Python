numel=int(input("ingrese la cantidad de elementos"))
i=int
numele=[]
for i in range(numel):
    ele=int(input("ingrese un numero"))
    numele.append(ele)

numele.sort()
print(numele)