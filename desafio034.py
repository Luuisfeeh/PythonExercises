s = float(input('Qual o seu salário? '))

if s <= 1250:
    aumento = s + (15/100 * s)

else:
    aumento = s + (10/100 * s )
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s,aumento))