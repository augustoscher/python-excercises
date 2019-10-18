import numpy as np
print('--- Numpy ---')

l = [1,2,3]
l2 = np.array(l)
print(type(l2))
print(l2)
print(l2[1])
print()

m = [[1,2,3],[4,5,6],[7,8,9]]
m2 = np.array(m)
print(m2)
print(m2[2])
print()

print('--- Arrange ---')
a = np.arange(0,10)
print(a)
print(type(a))

b = np.arange(0, 10, 2)
print(b)
print()

#ndarray de zeros
z = np.zeros(4)
print(type(z))
print(z)
print()

#matriz de zeros
z2 = np.zeros((3,3))
print(type(z2))
print(z2)
print()

#matriz de um
print(np.ones((2,2)))
print()

#matriz identidade
#contem 1 na sua diagonal e zero no rstante
print(np.eye(4))
print()

#linspace é igual ao arange, mas permite
#informar quantos numeros vão aparecer na lista
print(np.linspace(0,10, 3))
print()

#random.rand(5)
#cria numero de zero a 1 seguindo uma
#distribuição uniforme.
print(np.random.rand(3) * 100)
print(np.random.rand(2,2))
print()

print(np.random.randint(0,100, 10))