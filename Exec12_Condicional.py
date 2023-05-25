#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#    Dicas:
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes;

a = float(input('Digite o lado A: '))
b = float(input('Digite o lado B: '))
c = float(input('Digite o lado C: '))

if a == b and a == c:
    print('Equilátero')
elif a == b and b != c or b == c and a != c or a == c and b != a:
    print('Isósceles')
elif a != b and b != c:
    print('Escaleno')
else:
    print('3RR0')