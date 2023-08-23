casa = float(input('Qual é o valor do imovel? R$'))
salario = float(input('Quanto vc recebe? R$'))
anos = int(input('Em quantos anos vc irá pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * (30/100)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa,anos,prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')