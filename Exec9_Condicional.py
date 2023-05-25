#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20%
#Imprima na tela as informações, dispostas conforme o exemplo abaixo.
#No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#    Salário Bruto: (5 * 220)        : R$ 1100,00
#    (-) IR (5%)                                : R$   55,00
#    (-) INSS ( 10%)                       : R$  110,00
#    FGTS (11%)                            : R$  121,00
#    Total de descontos                : R$  165,00
#    Salário Liquido                       : R$  935,00

sal = float(input('Digite seu salário por hora: R$'))
qtd = float(input('Digite a quantidade de horas trabalhadas: R$'))

salbru = sal * qtd

if salbru <=900:
    ir = 00
    inss = (salbru * 0.10)
    fgts = (salbru * 0.11)
    tot = ir + inss
    sali = salbru - tot
    print(f'Salário bruto: R${salbru}\nIR: R${ir}\nINSS: R${inss}\nDESCONTOS: R${tot}\nFGTS: R${fgts}\nSalário líquido: R${sali}')
elif salbru > 900 and salbru <= 1500:
    ir = (salbru * 0.05)
    inss = (salbru * 0.10)
    fgts = (salbru * 0.11)
    tot = ir + inss
    sali = salbru - tot
    print(f'Salário bruto: R${salbru}\nIR: R${ir}\nINSS: R${inss}\nDESCONTOS: R${tot}\nFGTS: R${fgts}\nSalário líquido: R${sali}')
elif salbru > 1500 and salbru <= 2500 :
    ir = (salbru * 0.10)
    inss = (salbru * 0.10)
    fgts = (salbru * 0.11)
    tot = ir + inss
    sali = salbru - tot
    print(f'Salário bruto: R${salbru}\nIR: R${ir}\nINSS: R${inss}\nDESCONTOS: R${tot}\nFGTS: R${fgts}\nSalário líquido: R${sali}')
elif salbru > 2500:
    ir = (salbru * 0.20)
    inss = (salbru * 0.10)
    fgts = (salbru * 0.11)
    tot = ir + inss
    sali = salbru - tot
    print(f'Salário bruto: R${salbru}\nIR: R${ir}\nINSS: R${inss}\nDESCONTOS: R${tot}\nFGTS: R${fgts}\nSalário líquido: R${sali}')
else:
    print('3RR0')


