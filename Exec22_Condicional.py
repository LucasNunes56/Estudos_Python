#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#    Álcool: até 20 litros, desconto de 3% por litro
#    acima de 20 litros, desconto de 5% por litro
#    Gasolina:
#    até 20 litros, desconto de 4% por litro
#    acima de 20 litros, desconto de 6% por litro
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
#(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
#Sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

comb = input('A - Álcool ou G - Gasolina: ')
l = float(input('Quantos litros: '))

if comb.upper() == 'A':
    tot = l * 1.90
    if l > 20:
        tot = tot + (tot*0.05)
        print(f'R${tot} com 5% de desconto')
    else:
        tot = tot + (tot*0.03)
        print(f'R${tot} com 3% de desconto')
elif comb.upper() == 'G':
    tot = l * 2.50
    if l > 20:
        tot = tot + (tot*0.06)
        print(f'R${tot} com 6% de desconto')
    else:
        tot = tot + (tot*0.04)
        print(f'R${tot} com 4% de desconto')
else:
    print('3RR0')