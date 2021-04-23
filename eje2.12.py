lista = []
menor = 99999
indice = 0
for x in range(5):
    val = int(input("Ingrese un numero entero: "))
    lista.append(val)
    if val < menor:
        menor = val
        indice = x
print("La lista ingresada es",lista,"\nEl menor numero es",menor,"y se encuentra en la posicion",indice)