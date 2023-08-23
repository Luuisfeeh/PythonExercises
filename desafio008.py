metros = float(input('Diga uma distanância em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = int(metros * 10)
cm = int(metros * 100)
mm = int(metros * 1000)
print('A medida de {}m corresponde a '.format(metros))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
