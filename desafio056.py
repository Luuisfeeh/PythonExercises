velho = 0
nvelho = 0
fem = 0
nfem = 0
media = 0
soma = 0
for c in range(1,5):
    print('-----{}° PESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper()).strip()
    soma += idade
    if sexo == 'F':
        if idade < 20:
            fem += 1
        else:
            nfem += 1
    if c == 1 and sexo in 'M':
        nvelho = nome
        velho = idade
    else:
        if idade > velho and sexo in 'M':
            nvelho = nome
            velho = idade

media = soma / 4
print('A média de idade das pessoas é {:.1f}'.format(media))
print('O {} é o homem mais velho com {} anos.'.format(nvelho,velho))
print('Nessa lista tem {} mulhres com menos de 20 anos.'.format(fem))