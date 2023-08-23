largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
mQuadrado = largura * altura
tinta = mQuadrado / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, mQuadrado))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))