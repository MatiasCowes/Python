lim= int(input("ingrese el limite del programa"))


may= -100000000
men = 10000000000
for i in range(0,lim):
    n=int(input("ingrese un numero"))
    if n>may:
        may=n
   
    if n<men:
        men=n
    
print ("el mayor es ",may)
print("el menor es ",men)