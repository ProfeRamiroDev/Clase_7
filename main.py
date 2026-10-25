# REPASO
# Variables, listas, bucles

pollo = "pollo"

# 0, n
# LAs listas son simepre indexadas. Son mutables, son livianas

lista = [ pollo ,10.25,[10,10],True,False  ]
print(lista)
lista.append("banana") # append ( AGREGA ELEMENTOS A LA LISTA, EN LA ULTIMA POS )
print(lista)

# para quitar un elemento uso remove()
lista.remove("banana")
print(lista)


# CICLOS

# WHILE, FOR

# FOR . Uno puede determinar la cantidad de veces que se repita una accion, o puede recorrer
# una estructura determinada ( lista ) y se repetira la cantidad de elementos que esta tenga.

for i in lista:
    # necesito que creen algo que me muestre que elementos existen en la lista.
    print("La lista tiene estos elementos :",i)
    # cualquier tipo de codigo que quiera.
    print("Esto esta fuera del ciclo")




for i in range(41):
    print("NO SE QUE PONER REALMENTE. CADA UNO PONGA LO QUE QUIERA")
    

# Crear un sistema que pida al usuario ingresar elementos en una mochila.

mochila = []

cantidad = input("Cuantos elementos quieres ingresar en la mochila: ")

for i in range(int(cantidad)):
    elem = input("Que elemento quiere ingresar?: ")
    mochila.append(elem)
 
   
   