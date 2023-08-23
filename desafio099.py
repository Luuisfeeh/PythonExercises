from time import sleep

def maior(* núm):
    cont = maior = 0
    print('-+-'*25)
    print('Analisando os valores...')
    for n in núm:
        print(f'{n} ',end='',flush=True)
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont +=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()