num = int(input('Digite um número: '))
mult = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        mult += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num,mult))
if mult == 2:
    print('Ele é um número PRIMO!')
else:
    print('Ele não é número PRIMO!')
