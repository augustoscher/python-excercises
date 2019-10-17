print('--- Iterators ---')
l = [1, 2, 3, 4]
#cria objeto que funciona iterando sobre algum outro
#objeto que é um iterável

for item in l:
  print(item)

print()
#range()
#metodo que permite preencher sequencias
print(type(range(0,1)))
for item in range(0, 10):
  print(item)

print()
#criando lista com base no range
l2 = list(range(0,13))
print(l2)

print()
i = 1
while i < 5:
  print('i: {}'.format(i))
  i = i + 1

print()
out = []
x = [1,2,3,4]

for item in x:
  out.append(item**2)

print(out)

#definição de lista em uma só linha
#list comprehension
print('---list comprehension---')
z = [9,10,11]
#expressão usada para gerar a lista, seguida do for
abc = [item2**2 for item2 in z]

print(abc)

