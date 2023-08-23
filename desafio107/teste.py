import moeda
valor = float(input('Digite um preço: R$'))
print(f'Aumentando 10%, temos R${moeda.aumentar(valor, 10):.1f}')
print(f'Com desconto de 20%, temos R${moeda.diminuir(valor,20):.1f}')
print(f'A metade de R${valor:.1f} é R${moeda.metade(valor):.1f}')
print(f'O dobro de R${valor:.1f} é R${moeda.dobro(valor):.1f}')