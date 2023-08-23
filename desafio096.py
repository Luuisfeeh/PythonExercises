def area(m1,m2):
    a = m1 * m2
    print(f'A área de um terreno {m1} x {m2} é de {a}m².')


#Programa Principal
print('  Controle de Terrenos')
print('=='*16)
m1 = float(input('Largura (m): '))
m2 = float(input('Comprimento (m): '))
area(m1,m2)