from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

alunos_aprovados = list(filter(aluno_aprovado, alunos))
# alunos_honra = filter(aluno_honra, alunos)
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
media_aprovados = reduce(somar, notas_alunos_aprovados)/len(notas_alunos_aprovados)


# print(alunos)
print(alunos_aprovados)
print(notas_alunos_aprovados)
# print(list(alunos_honra))
print(media_aprovados)
