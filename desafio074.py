from random import randint
lista = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print(f'Essa é a lista de números: ',end='')
for n in lista:
    print(f'{n} ', end='')
print(f'\nO maior número da lista é o {max(lista)}')
print(f'O menor número da lista é o {min(lista)}')
