import numpy as np
print('--- Indexing and Slice ---')

#nparray de 0 ao 30 de 3 em 3 numeros
arr = np.arange(0, 30, 3)
print(arr)
print(arr[3])
print(arr[2:5])
print(arr[:5])
print(arr[2:])

arr[8:] = 100
print(arr)
print()

#transforma um array em um matriz bi demensional 5x10
arr2 = np.arange(50).reshape((5,10))
print(arr2)
print(arr2.shape)
print()

#primeiro colchete é linha e o segundo e colunas
#pega tudo até a terceira linha e todas as colunas
print(arr2[:3][:])
print()

#gera array de boleanos com base em regra para todos os elementos
v = arr2 > 30
print(v)
print()
#retorna so os itens que são true
print(arr2[v])
print()

#gera um array unidimensional
#transforma em array bidimensional 3x10
array = np.linspace(0,100,30)
array = array.reshape(3,10)
print(array)
print()

print(array[0:2][0:1][0][9])








