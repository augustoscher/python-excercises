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