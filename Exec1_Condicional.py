#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

l = input('Digite uma letra: ')

if l.upper() == 'A' or l.upper() == 'E' or l.upper() == 'I' or l.upper() == 'U':
    print(f'{l} É vogal!')
else:
    print(f'{l} É consoante!')