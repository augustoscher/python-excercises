import numpy as np

# Matriz de 10 zeros:
m = np.zeros(10).reshape(1, 10)
print(m)
print()

# Matriz de 10 ones:
m = np.ones(10).reshape(1, 10)
print(m)
print()

# Matriz de 10 cincos:
m = np.linspace(5, 5, 10).reshape(1, 10)
print(m)
print()

# Array de inteiros de 10 a 50
a = np.arange(10, 51)
print(a)
print()

# Array de números pares de 10 a 50
booleanValues = a % 2 == 0
a2 = a[booleanValues]
print(a2)
print()

# Matriz de 3x3 com valores de 0 a 8
m = np.arange(0, 9).reshape(3, 3)
print(m)
print()

# Matriz identidade de 3x3
m = np.eye(3)
print(m)
print()

# Gerar números aleatorios entre 0 e 1 ?
n = np.random.rand(1, 1)
print(n)
print()

# Gerar array de 25 números aleatorios de uma distribuição normal ?
n = np.random.rand(5, 5)
print(n)
print()

# Matriz 10x10 ?
m = np.linspace(0, 1, 100).reshape(10, 10)
print(m)
print()

# Array igualmente espaçado com tamanho 20 de 0 e 1 ?

print()
print(' ----------------------- ')
# Slice array 5x5 ignorando 2 primeiras linhas e 1 coluna
m = np.arange(1, 26).reshape(5, 5)
print(m)
print()

print(m[2:5, 1:5])
print()

# Acessar o elemento de valor 20
print(m[3][4])
print()

# Retornar [2, 7, 12]
print(m[0:3, 1])
print()

# Retornar [21, 22, 23, 24, 24]
print(m[4])
print()

print(m[3:5, 0:5])

print()
print(' ----------------------- ')
# Obter a soma dos valores 
print(m.sum())
print()

# Obter o desvio padrão
print(np.std(m))
print()

# Soma de todas as colunas
print(np.sum(m, axis=0))