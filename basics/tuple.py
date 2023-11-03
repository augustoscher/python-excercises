print('--- Tuple ---')
#tuples are immutable
t = (1, 3, 5, 6)
print(t)
print(type(t))
print(t[2])
print()

# adding values to tuple
t = t + (7,)
print(t)

# appending values to tuple
tuples = (2, 4, 6, 8, 12)
tuples = (*tuples, 15)
print(tuples)

# insert values to the beggining of a tuple
tuples2 = (2, 4, 6, 8, 12)
tuples2 = (0, *tuples2)
print(tuples2)

# add tuple using list
tup = (2, 4, 6, 8)
l = list(tup)
l.append(12)
result = tuple(l)

#returns error if we try to modify some value
#the code below throws error
#t[1] = 'asdj'