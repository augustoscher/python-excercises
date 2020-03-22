print("-- Strings -- ")
print()

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

print()
nome = 'Teste'
idade = 18
print('Nome: {a}, Idade: {b}'.format(a=nome, b=idade))


def print_full_name(a, b):
    print('Hello {a} {b}! You just delved into python.'.format(a=a, b=b))

print_full_name('Ross', 'Taylor')


a = "this is a string"
a = a.split(" ") # a is converted to a list of strings. 
print(a)

string = ''
for item in a:
    if len(string) > 0:
        string = string +"-"+ item
    else:
        string = string + item
        

print(string)