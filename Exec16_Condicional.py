#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.
# Dica: utilize o operador módulo (resto da divisão): %

n = int(input('Digite o número e veja se é par ou ímpar: '))

if n%2==0:
    print(f'{n} é par')
else:
    print(f'{n} é ímpar')