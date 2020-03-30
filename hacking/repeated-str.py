# It counts the number of "a" in a full string, and in the last, 
# potentially partial string, and calculates the total amount of "a" based on that.
# "a" count of full string * number of string repeats + "a" count of last string.

def repeatedStr(s, n):
  print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))


repeatedStr('aba', 10)