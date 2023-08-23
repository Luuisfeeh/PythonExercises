n1 = count = soma = 0
n1 = int(input('Digite um número [999 para parar]: '))
while n1 != 999:
    count += 1
    soma += n1
    n1 = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles foi {}.'.format(count,soma))