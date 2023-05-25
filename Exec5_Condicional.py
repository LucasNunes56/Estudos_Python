#Faça um programa que pede dois inteiro e armazene em duas variáveis.
# Em seguida, troque o valor das variáveis e exiba na tela.

x = int(input('Digite o valor de A:'))
y = int(input('Agora, digite o valor de B:'))

print(f'A = {x}\nB = {y}')

c = x
x = y
y = c
print(f'Agora: \nA = {x}\nB = {y}')
