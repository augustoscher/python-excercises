print('--- Lists ---')
l1 = ['h', 'e', 'l', 'l', 'o']
l2 = [1, 2, 3, 'a', 1.0, l1]
print(l2)
print(type(l2))
print('x' in l2)
print('a' in l2)
print(3 in l2)
print()

# add value
l2.append('oi')

#retornando um único valor
print(l2[2])
print(l2[5][0])

#retornando vários valores
print(l2[1:4])
print(l2[1:])

# filtrando valores
scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 70, scores)
print(list(filtered))
