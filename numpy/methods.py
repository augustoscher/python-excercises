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

# Funções numpy
array1 = np.arange(1, 11)
print('Raiz quadrada dos elementos')
print(np.sqrt(array1))

print('Exponenciação dos elementos')
print(np.exp(array1))

print('Média dos elementos')
print(np.mean(array1))

print('Desvio padrão')
print(np.std(array1))

print('Seno dos elementos')
print(np.sin(array1))

print('Valor máximo')
print(np.max(array1))

print('Valor minimo')
print(np.min(array1))
