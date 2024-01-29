# normal way
list_of_words = []
list_of_sentences = [['The','cat','chases', 'the', 'mouse','.'],['The','dog','barks','.']]
for sentence in list_of_sentences:
  for word in sentence:
    list_of_words.append(word)

print(list_of_words)

# list comprehension
list_of_words2 = [word for sentence in list_of_sentences for word in sentence]
print(list_of_words2)

# list comprehension with if
multiple_of_three = [x for x in range(10) if x % 3 == 0]
print(multiple_of_three)


x = 1
y = 1 
z = 1
n = 2

combinations = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(combinations)
