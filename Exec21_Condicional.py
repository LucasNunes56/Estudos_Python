#. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?"
# O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino".

# Caso contrário, ele será classificado como "Inocente".

p1 = input('Telefonou para a vítima? 1-Sim, 2-Não\n: ')
p2 = input('Esteve no local do crime? 1-Sim, 2-Não\n: ')
p3 = input('Mora perto da vítima? 1-Sim, 2-Não\n: ')
p4 = input('Devia para a vítima? 1-Sim, 2-Não\n: ')
p5 = input('Já trabalhou com a vítima? 1-Sim, 2-Não\n: ')

x = 0

if p1 == '1':
    x = x + 1
elif p1 == '2':
    x = x
if p2 == '1':
    x = x + 1
elif p2 == '2':
    x = x
if p3 == '1':
    x = x + 1
elif p3 == '2':
    x = x
if p4 == '1':
    x = x + 1
elif p4 == '2':
    x = x
if p5 == '1':
    x = x + 1
elif p5 == '2':
    x = x

if x == 5:
    print('ASSASSINO SAFADO')
elif x > 2 and x < 5:
    print('Cúmplice')
elif x == 2:
    print('Suspeito')
elif x == 1:
    print('Inocente')
else:
    print('3RR0')
print(x)
