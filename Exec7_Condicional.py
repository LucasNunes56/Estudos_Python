# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

x = input('Por obséquio, meu nobre jovem, em que período estudaste? \n(M - Matutino), (V - Vespertino) ou (N - Noturno): ')

if x.upper() == 'M':
    print('Bom dia!')
elif x.upper() == 'V':
    print('Boa tarde!')
elif x.upper() == 'N':
    print('Boa noite!')
else:
    print('3RR0')