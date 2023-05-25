#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
# 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

n = int(input('Digite um número: '))

# Extraindo a unidade
u = n % 10
# Eliminando a unidade de nosso número
n = (n - u)/10
# Extraindo a dezena
d = n % 10
# Eliminando a dezena do número original, fica a centena
n = (n - d)/10
c = n
# Fazendo ser inteiros
d = int(d)
c = int(c)

if c > 1:
    if d >1:
        if u > 1:
            print(f'{c} Centenas, {d} Dezenas, {u} Unidades')
        else:
            print(f'{c} Centenas, {d} Dezenas, {u} Unidade')
    else:
        print(f'{c} Centenas, {d} Dezena, {u} Unidades')
else:
    print(f'{c} Centena, {d} Dezenas, {u} Unidades')