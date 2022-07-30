from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]


alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]


# print(alunos)
print(alunos_aprovados)
print(notas_alunos_aprovados)
