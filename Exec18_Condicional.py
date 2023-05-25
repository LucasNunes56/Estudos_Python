#Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas
#notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade
# de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input('Quanto quer sacar? valor de R$10 a R$600 em notas de 1, 2, 5, 10, 20, 50, 100 e 200\nR$ '))

duz = int(saque / 200)
saque = saque - (duz*200)
cem = int(saque / 100)
saque = saque - (cem*100)
cin = int(saque / 50)
saque = saque - (cin*50)
vin = int(saque / 20)
saque = saque - (vin*20)
dez = int(saque / 10)
saque = saque - (dez*10)
cinco = int(saque / 5)
saque = saque - (cinco*5)
dois = int(saque / 2)
saque = saque - (dois*2)
um = saque

print(f'Notas de R$200: {duz}\nNotas de R$100: {cem}\n'
      f'Notas de R$50: {cin}\nNotas de R$20: {vin}\nNotas de R$10: {dez}\n'
      f'Notas de R$5: {cinco}\nNotas de R$2: {dois}\nNotas de R$1: {um}\n')


