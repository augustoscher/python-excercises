arr = [2, 3, 6, 6, 5]
# remove dups items by using dictionary
d = dict.fromkeys(arr)
# print(d)

#convert back to array
arr = list(d)
arr.sort(reverse = True)

print(arr)
print(arr[1])
