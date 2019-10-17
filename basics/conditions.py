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