lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze', 'Quatorze','Quinze','Dezeseis','Dezesete','Dezoito','Dezenove','Vinte' )

while True:
    resp = int(input('Digite um número entre 0 e 20: '))
    print('_'*20)
    if 0 <= resp <= 20:
        print(f'Você digitou o número {lista[resp]}!')
        aa = ''
        while aa != 'S' and aa != 'N':
            aa = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if aa == 'N':
            break

    print('Tente novamente.', end='')
