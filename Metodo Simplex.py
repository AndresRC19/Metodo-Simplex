i=0
while i<1:
    Xi=int(input("Digite un número para la cantidad de variables de Z: "))
    if Xi>10:
        print ("El número es muy grande, se permite máximo hasta 10")
        continue
    elif Xi<2:
        print ("El número es muy pequeño, debe ser mínimo de 2 variables")
        continue
    else:
        i=i+1
lista=list(range(Xi))
d=Xi/2
e=int(1)
for i in (range(Xi)):
    y=float(input(f"Digite un valor que corresponda a la variable Z{e}: "))
    lista.append(y)
    del lista[0:1]
    e=e+1
e=int(1)
for i in range(len(lista)):
    print (lista[i],end=f"Z{e} ")
    e=e+1
print()
while i<1
Yi=int(input("Digite la cantidad de inecuaciones (Debe ser un valor positivo): "))
