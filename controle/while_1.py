# x = 0
#
# while x != -1:
#     x = float(input('Informe o número ou -1 para sair'))
#
# print('Fim!')

total = 0
nota = 0
qtde = 0

while nota != -1:
    nota = float(input('Informe a nota do aluno ou -1 para sair: '))
    if nota != -1:
        total += nota
        qtde += 1

print(f'Média da turma: {total/qtde}')
