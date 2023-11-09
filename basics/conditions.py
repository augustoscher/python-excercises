print ('--- Conditions ----')

nota = 9
resultado = ''

if nota >= 7:
  resultado = 'Aprovado'
elif nota >= 6 and nota < 7:
  resultado = 'Recuperação'
else:
  resultado = 'Reprovado'

print('Resultado: {}'.format(resultado))

sales = 1000
bonus = 50 if sales > 500 else 0
