print('--' *10)
print('LOJINHA DO AMIGO')
print('--' *10)

valor = float(input('Qual o valor do produto? R$ '))

# a vista ou pix tem 10% de desconto
# 2x no cartão preço normal
# 3x ou mais 20% de jutos
# a vista no cartão 5%
print('FORMAS DE PAGAMENTO \n [1] Á vista em dinheiro/pix \n [2] Á vista no cartão \n '
      '[3] 2x no cartão \n [4] 3x ou mais no cartão')
escolha = int(input('Qual forma de pagamento? '))

if escolha == 1:
    desconto = valor -(10/100 * valor)
    print('Com essa forma de pagamento o valor de R${}, fica de R${}'.format(valor,desconto))
elif escolha == 2:
    desconto = valor - (5/100 * valor)
    print('Com essa forma de pagamento o valor de R${}, fica de R${}'.format(valor,desconto))
elif escolha == 3:
    parcelas = valor / 2
    print('Com essa forma de pagamento o valor R${} não tem desconto, mas as parcelas ficam de R${}'
          .format(valor,parcelas))
elif escolha == 4:
    parcelas = int(input('Quantas parcelas você deseja? '))
    if parcelas >= 3:
        juros = valor + (20/100 * valor)
        parcela = juros / parcelas
        print('Com essa forma de pagamento o valor de R${} fica R${} e parcelado em {}x fica R${}'
          .format(valor,juros,parcelas,parcela))
    elif parcelas < 3:
        print('Infelizmente essa não é a opção de menos que 3 parcelas')
else:
    print('O pagamento foi cancelado por opção inválida.')
print('AGRADECEMOS SUA COMPRA :3')