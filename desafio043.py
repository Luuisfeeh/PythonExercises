print(' /-\ ' * 10)
print('               VAMOS CALCULAR SEU IMC')
print(' /-\ ' * 10)

altura = float(input('Qual é a sua altura?(m) '))
peso = float(input('Quanto você pesa?(kg) '))
imc = peso / (altura**2)

print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você é classificado como MAGREZA e tem 0 de OBESIDADE')
elif 18.5 <= imc <= 24.9:
    print('Você é classificado como NORMAL e tem 0 de OBESIDADE')
elif 25 <= imc <= 29.9:
    print('Você é classificado como SOBREPESO e tem 1 de OBESIDADE')
elif 30 <= imc <= 39.9:
    print('Você é classificado como OBESIDADE e tem 2 de OBESIDADE')
else:
    print('Você é classificado como OBESIDADE GRAVE e tem 3 de OBESIDADE')