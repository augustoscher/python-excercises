def find_occurrences(l):
  d = {}
  for item in l:
    d[item] = d[item] + 1 if item in d else 1
  tup = sorted(list(d.items()), key=lambda v: v[1], reverse=True)[0]
  return tup[0]

print(find_occurrences([1, 2, 3, 3, 4, 4, 4, 5, 6, 9, 10, 10, 10, 10, 11]))
print(find_occurrences([1]))
print(find_occurrences([1,1,1,1,2,2,3]))
print(find_occurrences([100,100,2,2,3,4,4,4,4,4,4]))
