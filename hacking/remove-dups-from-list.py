def remove_duplicated(l):
  return list(dict.fromkeys(l))

arr = [2, 3, 6, 6, 5]
arr = remove_duplicated(arr)
arr.sort(reverse = True)
print(arr)

#-----------------------------
print()
scores = [37.21, 37.21, 37.2, 41, 39]
scores2 = scores[:]

#ordena, remove a nota mais baixa e busca a segunda menor
scores2.sort()
scores2 = scores2[1:]
lowest = scores2[0]

indexes = []
i = 0
for item in scores:
  if item == lowest:
    indexes.append(i)
    i += 1

print(indexes)
for idx in indexes:
  name[idx]