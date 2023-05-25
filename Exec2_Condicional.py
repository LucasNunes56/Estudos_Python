#Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:

#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
me = (n1+n2)/2

if me > 6.99 and me <= 9.99:
    print('APROVADO', me)
elif me < 7:
    print('REPROVADO', me)
elif me >= 10:
    print('APROVADO COM DISTINÇÃO', me)
else:
    print('3RR0')