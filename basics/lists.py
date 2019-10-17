print('--- Lists ---')
l1 = ['h', 'e', 'l', 'l', 'o']
l2 = [1, 2, 3, 'a', 1.0, l1]
print(l2)
print(type(l2))
print('x' in l2)
print('a' in l2)
print(3 in l2)
print()

#retornando um único valor
print(l2[2])
print(l2[5][0])

#retornando vários valores
print(l2[1:4])
print(l2[1:])