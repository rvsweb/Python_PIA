import numpy as np

print(np.__version__)

array_2d = np.arange(1, 10).reshape(3, 3)
print(array_2d)

# Crear un array tridimensional
mi_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Mostrar el array
print(mi_array)


# Crear tres matrices
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
matriz3 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])

# Mostrar las dimensiones, el tamaño y la forma de las matrices
for i, matriz in enumerate([matriz1, matriz2, matriz3], start=1):
    print(f"Matriz{i}:")
    print(f"Dimensiones: {matriz.ndim}")
    print(f"Tamaño: {matriz.size}")
    print(f"Forma: {matriz.shape}\n")
