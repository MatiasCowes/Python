n=int(input("ingrese la cantidad de temperaturas"))
media=float
cont=0
num=int
suma=0
temp=[n]
i=1
for i in range(n):
    num=int(input("ingrese la temperatura"))
    temp.append(num)
    suma=suma+temp[i]
media=suma/n

for i in range(n):
    if temp[i]>=media:
        cont=cont+1
        
print("la media es de ",media)
print("los que superaron la media son ",cont)