#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                   Até 5 Kg               Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#  Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#  porém não há limites para a quantidade de carne por cliente.
#  Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total a compra.
#  Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
#  contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
#  valor do desconto e valor a pagar.

tipo = int(input('Selecione o corte: 1-Filé Duplo, 2-Alcatra, 3-Picanha: '))
qtd = int(input('Quantidade: '))
if tipo == 1:
    print('Filé Duplo')
    if qtd < 5:
        pre = qtd * 4.90
        print(f'{qtd} KG\nR${pre}')
    elif qtd >= 5:
        pre = qtd * 5.80
        print(f'{qtd} KG\nR${pre}')

elif tipo == 2:
    print('Filé Duplo')
    if qtd < 5:
        pre = qtd * 5.90
        print(f'{qtd} KG\nR${pre}')
    elif qtd >= 5:
        pre = qtd * 6.80
        print(f'{qtd} KG\nR${pre}')

elif tipo == 3:
    print('Filé Duplo')
    if qtd < 5:
        pre = qtd * 6.90
        print(f'{qtd} KG\nR${pre}')
    elif qtd >= 5:
        pre = qtd * 7.80
        print(f'{qtd} KG\nR${pre}')

pgt = int(input('Forma de pagamento: 1-Dinheiro, 2-Crédito, 3-Débito, 4-Pix, 5-Cartão Tabajara(5%OFF)'))
if pgt == 5:
    promo = pre - (pre * 0.05)
    print(f'Valor atualizado com Desconto Tabajara. R${promo:.2f}')




