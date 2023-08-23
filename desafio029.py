velo = int(input('Me diga sua velocidade: '))
multa = (velo - 80) * 7

if velo > 80 :
    print('VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE!!(80km/h)')
    print('Você terá que pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um ótima dia e uma boa viagem!')