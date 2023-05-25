#Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))
n3 = int(input('3° Número: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'{n1} maior \n{n3} menor')
    elif n3> n2:
        print((f'{n1} maior \n{n2} menor')
elif n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'{n2} maior \n{n3} menor')
    elif n3 > n1:
        print(f'{n2} maior \n{n1} menor')
elif n3 > n1 and n3 > n2:
    if n1 > n2:
        print(f'{n3} maior \n{n2} menor')
    elif n2 > n1:
        print(f'{n3} maior \n{n1} menor')
    else:
else: