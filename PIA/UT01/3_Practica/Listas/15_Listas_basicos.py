# Lista basica
lista = [1, 2, 3, 4, 5]

# Dinamica : Distintos elementos
lista1 = []
lista2 = ["a", 1, True]

print("• Mostrar una lista basica : ")
print(lista)

print("• Unión de 2 listas en una sola")
lista_mezclada = zip(lista, lista2)

for i in lista_mezclada:
    print(i, end=" ")

numeros = [11, 22, 33, 44, 55]
letras = ['aa', 'bb', 'cc', 'dd']

for num, letra in zip(numeros, letras):
    print(num, letra)

print("\n###################")
cont = 0
for num in lista:
    cont += 1
    print(num, end=" ")
    print("• Recorrer una lista basica : ", cont)


print("###################")
lista_caracteres = ["aa", "ba", "ca", "da", "fa", "ga", "ha", "ia"]

for i in lista_caracteres:
    print(i, end=" ")

print("► Convertir listas en tuplas")

# Crear Tupla vacia
tupla = tuple()

print("► Convertir en tupla")
for num, letra in zip(numeros, letras):
    tupla = num, letra
    print(tupla)

# Unir 2 listas y crear una tupla
tupla1 = tuple(lista)
tupla2 = tuple(lista2)

tupla_combinada = tupla1 + tupla2

for elementos in tupla_combinada:
    print(elementos, end=" ")

# Unión de listas
unir_listas = zip(lista, lista_caracteres)
print("\n• De que tipo soy: ", type(unir_listas))

# Recorremos la lista
for i in unir_listas:
    print(i, end=" ")

print("\n▬ Uniendo elementos con 'zip()' para convertirlos en 'dict' #")

# Creamos un dict
unir_listas = zip(lista, lista_caracteres)
diccionario = dict(unir_listas)

# Mostramos el dict
print(diccionario)
