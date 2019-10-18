import numpy as np
print('--- Methods ---')

#reshape faz com que objetos assumam outros formatos
arr = np.random.rand(25)
print(arr)
print(arr.max())
print(arr.min())
print(arr.argmax())
print(arr.shape)
print()

#transforma de um array para uma matriz de 5x5
#retorna um outro objeto
arr2 = arr.reshape((5,5))
print(arr2)
print(arr2.max())
print(arr2.min())
print(arr2.argmax())
print(arr2.shape)

