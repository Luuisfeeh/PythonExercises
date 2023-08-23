count = soma = 0
while True:
    n1 = int(input('Digite um valor: '))
    if n1 == 999:
        break
    count += 1
    soma += n1
print(f'Você digitou {count} número e a soma deles é equivalente a {soma}!')