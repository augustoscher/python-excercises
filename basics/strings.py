
def change_capitalization(s):
  lst = list(map(lambda c: c.lower() if c.capitalize() == c else c.capitalize(), s))
  res = ''.join(lst)
  print(res)

change_capitalization('HackerRank')
change_capitalization('hackerRank')

# ============

def mutate_string(string, position, character):
  lst = list(string)
  lst[position] = character 
  print(''.join(lst)) 

mutate_string("xuxuxu", 1, 'a')


# ============
def count_substring(string, sub_string):
  subs = 0
  for i in range(0, len(string)):
    part = string[i:len(sub_string)+i]
    if part == sub_string:
      subs +=1
  print(subs)

count_substring('BCDCDC','CDC')


# ============
# check if string has any chars of:
s = "231a"
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))



width = 20
print('HackerRank'.rjust(width,'-'))
