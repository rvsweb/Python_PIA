# Crear un diccionario básico
diccionario = {}
diccionario = {'uno': 1, 'two': 2, 'three': 3}

diccionario1 = {}
diccionario1['one'] = 1
diccionario1['two'] = 2
diccionario1['three'] = 3

print(type(diccionario))
print(diccionario)
print("Valor de un elemento: ", diccionario['uno'])

print(type(diccionario1))
print(diccionario1)
print("Valor de un elemento: ", diccionario1['one'])
print(len(diccionario1))
print("Aumentar en 1 el valor: ", diccionario1['one'] + 1)
del (diccionario1['one'])
print(diccionario1)
respuesta = 'three' in diccionario1
print(respuesta)
respuesta = 'four' in diccionario1
print(respuesta)
respuesta = 'four' in diccionario1
print(respuesta)

diccionario_base = dict(one=1, two=2, three=3)
print("Diccionario base: ", diccionario_base)

# Copia
diccionario_copia = diccionario_base.copy()
diccionario_copia['one'] = 1000
print("Diccionario mixto: ", diccionario_copia)

# Actualización
diccionario_reemplazo = {
    "cuatro": 4, "cinco": 5, "seis": 6, "siete": 7}
diccionario_copia.update(diccionario_reemplazo)
print(diccionario_copia)

# Recorrer 'keys' diccionario
print('Recorrer llaves')
for llave in diccionario_copia.keys():
    print(llave, end=" ")

# Recorrer 'values' diccionario
print('Recorrer valores')
for valor in diccionario_copia.values():
    print(valor, end=" ")

# Recorrer 'llaves y valores' del diccionario
for llave, valor in diccionario_reemplazo.items():
    print(f'{llave} => {valor}')

# Limpiar diccionario
diccionario_copia.clear()
print("\nDiccionario mixto: ", diccionario_copia)
