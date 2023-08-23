nome = str(input('Digite seu nome Completo: '))
nomeI = nome.split()
nomeF = nomeI[len(nomeI)-1]
print('É um prazer te conhecer {}'.format(nome))
print('Seu primeiro nome é {}'.format(nomeI[0]))
print('Seu ultimo nome é {}'.format(nomeF))
