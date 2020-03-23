#
# Given an array of integers, find and print the maximum number of integers you can select 
# from the array such that the absolute difference between any two of the chosen integers is less than or equal to 1
#
# Ex:
# a = [1,1,2,2,4,4,5,5,5] -> r1 = [1,1,2,2] and r2 = [4, 4, 5, 5, 5]
# result would be 5 (length of second array)
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
  return max([sum((a.count(i), a.count(i+1))) for i in set(a)])

print(pickingNumbers([4, 6, 5, 3, 3, 1]))