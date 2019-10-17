lst = [1, 2, [3, 4], [5, [100, 200, ['olá']], 23, 11], 3, 7]
print(lst[3][1][2][0])

d = {'k1': [1, 2, 3, {'cafe': ['banana', 'mulher', 'colher', {'alvo': [1, 2, 3, 'olázinho']}]}]}
print(d['k1'][3]['cafe'][3]['alvo'][3])