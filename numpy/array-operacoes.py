import numpy as np
print('--- Operações com Numpy arrays ---')

# Operação vetorizada: Soma cada elemento com o segundo array
array1 = np.arange(0, 20)
print(array1)
print()
print('Soma: ')
array2 = array1 + array1
print(array2)

# Suporta todas as operações
print('Multiplicacao: ')
array3 = array1 * array1
print(array3)
print()

# Operações escalares: Soma 100 a cada elemento 
array4 = array1 + 100
print(array4)
print()

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
