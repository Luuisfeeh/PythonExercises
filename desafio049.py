n1 = int(input('Me diga um número que deseja vê a tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n1, c , n1*c))