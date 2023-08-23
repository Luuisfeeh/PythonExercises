valor = int(input('Qual valor você deseja sacar? '))
valCed = 50
valortotal = valor
totCed = 0
while True:
    if valortotal >= valCed:
        valortotal -= valCed
        totCed += 1
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R${valCed}')
        if valCed == 50:
            valCed = 20
        elif valCed == 20:
            valCed = 10
        elif valCed == 10:
            valCed = 1
        totCed = 0
        if valortotal == 0:
            break
