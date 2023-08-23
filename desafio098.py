from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-+-'*26)
    print(f'Contagem de {i} até {f} de {p} em {p}')


    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont -=p
        print('FIM!')



contador(1,10,1)
contador(10,0,1)
print('-+-'*26)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('INICIO: '))
ffim = int(input('FIM: '))
pa = int(input('PASSOS: '))
contador(ini,ffim,pa)