viagem = float(input('Quantos KM você precisa percorrer? '))

if viagem <= 200:
    valor = viagem * 0.5
    print('Sua viagem deu R${:.2f}'.format(valor))
else:
    valor = viagem * 0.45
    print('Com a promoção, sua viagem ficará R${:.2f}'.format(valor))
print('Qual será a forma de pagamento?')
