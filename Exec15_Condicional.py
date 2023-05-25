#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
print('Digite a data em formato dd/mm/aaaa, a começar pelo dia:')
dd = int(input('dd: '))                                                     #Coleta o dia
mm = int(input('mm: '))                                                     #Coleta o mês
aaaa = int(input('aaaa: '))                                                 #Coleta o ano

if aaaa > 0:                                                                #Testando ano maior que 0
    if (aaaa%4 == 0 and aaaa%100 != 0) or aaaa%400 == 0:                    #Ano bissexto

        if mm < 1 and mm > 12:                                              #Testando se mês existe
            print('Mês inválido')
        else:
            if dd < 1 and dd > 31:                                          #Testando se dia existe
                print('Dia inválido')
            elif dd > 29 and mm == 2:                                       #Tratativa para Fevereiro
                print('Fevereiro, em ano bissexto, tem apenas 29 dias')
            else:
                print(f'A data é a {dd}/{mm}/{aaaa}')                       #Resultado formatado

    elif (aaaa%4 != 0 and aaaa%100 == 0) or aaaa%400 != 0:                  #Ano não bissexto

        if mm < 1 and mm > 12:                                              #Testando se mês existe
            print('Mês inválido')
        else:
            if dd < 1 and dd > 31:                                          #Testando se dia existe
                print('Dia inválido')
            elif dd > 28 and mm == 2:                                       #Tratativa para Fevereiro
                print('Fevereiro, em ano não bissexto, tem apenas 28 dias')
            else:
                print(f'A data é a {dd}/{mm}/{aaaa}')                       #Resultado formatado
    else:
        print('Ano inválido')                                    #Quando o ano não é bissexto e nem não bissexto
else:
    print('Ano inválido')                                                   #Ano negativo
