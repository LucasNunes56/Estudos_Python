#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

#      Média de Aproveitamento  Conceito
#      Entre 9.0 e 10.0                      A
#      Entre 7.5 e 9.0                        B
#      Entre 6.0 e 7.5                        C
#      Entre 4.0 e 6.0                        D
#      Entre 4.0 e zero                      E
# O algoritmo deve mostrar na tela as notas, a média,o conceito correspondente e a mensagem “APROVADO”
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1+n2)/2

if med >=9 and med <= 10:
    print(f'Sua nota foi {med}, Aprovado nota A')
elif med >= 7.5 and med < 9 :
    print(f'Sua nota foi {med}, Aprovado nota B')
elif med >= 6 and med < 7.5:
    print(f'Sua nota foi {med}, Aprovado nota C')
elif med >= 4 and med < 6:
    print(f'Sua nota foi {med}, Reprovado nota D')
elif med >= 0 and med < 4:
    print(f'Sua nota foi {med}, Reprovado nota E')
else:
    print('3RR0')