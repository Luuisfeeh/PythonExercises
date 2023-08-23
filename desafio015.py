dias = int(input('Por quantos dias você alugou? '))
km = int(input('Quantos km você rodou? '))
valor = (60 * dias) + (0.15 * km)
print('O total a pagar referente ao uso diário e km rodados é de R${:.2f}'.format(valor))