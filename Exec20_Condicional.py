# Faça um Programa que leia um número e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

#    par ou ímpar;
#    positivo ou negativo;
#    inteiro ou decimal.

print('Digite um número e depois diga qual operação deseja fazer:')
n1 = float(input('Digite o número: '))
print('Qual a operação desejada?\n1- Par ou ímpar;\n2- Positivo ou negativo;\n3- Inteiro ou decimal')
x = input(': ')


if x == '1':
    if n1%2==0:
        print(f'{n1} É par')
    elif n1%2!=0:
        print(f'{n1} É ímpar')
    else:
        print('3RR0')
elif x == '2':
    if n1 > 0:
        print(f'{n1} É positivo')
    elif n1 < 0:
        print(f'{n1} É negativo')
    elif n1 == 0:
        print('Zero não é positivo nem negativo')
    else:
        print('3RR0')
    print('')
elif x == '3':
    if n1==round(n1):
        print(f'{n1} É Inteiro')
    elif n1!=round(n1):
        print(f'{n1} É Decimal')
    else:
        print('3RR0')
else:
    print('3RR0!!!')