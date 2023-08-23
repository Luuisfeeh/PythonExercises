import moeda
valor = float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10, True)}')
print(f'Com desconto de 20%, temos {moeda.diminuir(valor,20, True)}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')