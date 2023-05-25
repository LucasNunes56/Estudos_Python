# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa
#que calculará os reajustes.Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento.

sal = float(input('Digite o salário: R$'))

if sal <= 280:
    au = sal * 0.20
    print(f'Salário pré reajuste R${sal}\n20% de aumento\nSalário novo R${au + sal}')
elif sal > 280 and sal <= 700:
    au = sal * 0.15
    print(f'Salário pré reajuste R${sal}\n15% de aumento\nSalário novo R${au + sal}')
elif sal > 700 and sal <= 1500:
    au = sal * 0.10
    print(f'Salário pré reajuste R${sal}\n10% de aumento\nSalário novo R${au + sal}')
elif sal >1500:
    au = sal * 0.05
    print(f'Salário pré reajuste R${sal}\n5% de aumento\nSalário novo R${au + sal}')
else:
    print('3RR0')