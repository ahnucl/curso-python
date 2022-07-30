a = 'valor'  # Verdadeiro

a = 0           # Falso
a = -1          # Verdadeiro
a = -0.00001    # Verdadeiro
a = ''          # Falso
a = ' '         # Verdadeiro
a = []          # Falso
a = {}          # Falso


if a:
    print('Existe!')
else:
    print('não existe ou zero ou vazio')
