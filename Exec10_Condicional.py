#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dia = int(input('Digite o dia da semana [1-Domingo,2-Segunda, 3-Terça, 4-Quarta, 5-Quinta, 6- Sexta, 7- Sábado ]: '))
if dia == 1:
    print('Domingo')
elif dia ==2:
    print('Segunda- Feira')
elif dia == 3:
    print('Terça- Feira')
elif dia == 4:
    print('Quarta- Feira')
elif dia == 5:
    print('Quinta- Feira')
elif dia == 6:
    print('Sexta- Feira')
elif dia == 7:
    print('Sábado')
else:
    print('3RR0')