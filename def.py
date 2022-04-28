def say_hello(name):
    print('hello', name)

name = 'chamso'

say_hello('mohammed')
say_hello(name)
say_hello('anis')
say_hello('achraf')
print('--------------------------------------------')
names = ['malek', 'anis', 'achraf', 'chamso']
for item in names:
    say_hello(item)

    if item == 'achraf':
        break

print("-"*20)
for item in names:

    if item == 'anis':
        continue
    say_hello(item)



