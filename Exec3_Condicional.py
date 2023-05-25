#Faça um Programa que leia três números inteiros e mostre o maior deles.

n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))
n3 = int(input('3° Número: '))

if n1 > n2 and n1 > n3:
    print(f'{n1}')
elif n2 > n1 and n2 > n3:
    print(f'{n2}')
elif n3 > n1 and n3 > n2:
    print(f'{n3}')
else:
    print('3RR0')
