n1 = int(input('Primeiro valor: '))
n2 = int(input('Segunda valor: '))
n3 = int(input('Terceiro valor: '))
menor = n1
#Verificando o menor valor
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
#Verificando o maior valor
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
