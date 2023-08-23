import time
print('--'*15)
print('   Cadastro de Idade e Sexo')
print('--'*15)

maiores = homens = mulheres = 0
while True:
    idade = int(input('Quantos anos você tem? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()
    print('--' * 15)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais? [S/N] ')).strip().upper()
        print('--' * 15)
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres += 1
    if resp == 'N':
        print('Agradecemos o uso!')
        break
    else:
        time.sleep(1)
        print('Absorvendo dados...')
        print('--' * 15)

print(f'-Absorvemos e reparamos que possui {maiores} maiores de 18 anos.')
print(f'-Além disso {homens} são do sexo masculino.')
print(f'-Para finalizar são {mulheres} que possue uma idade abaixo dos 20 anos.')