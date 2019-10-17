print('--- Functions ---')

def test():
  print('oi')

def test2(param):
  print(param)

def sum(param, paramb):
  return param + paramb

test()
test2('sou um parametro')
print(sum(5,4))
print()

print('--- Lambda ---')
#function normal
def quadrado(value): return value**2
print(quadrado(2))

my_lambda = lambda param: param**2
print(my_lambda(5))
print()

print('--- Map ---')
s = [1,2,3,4,5]
ls1 = list(map(quadrado, s))
print(ls1)

ls2 = list(map(lambda v: v**3, s))
print(ls2)
print()

print('--- Filter ---')
print(list(filter(lambda v : v >= 3, s)))
ls3 = list(filter(lambda v : v % 2 == 0, s))
print(ls3)



