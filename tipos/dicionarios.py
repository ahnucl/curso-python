aluno = {
    'nome': 'Pedro',
    'nota': 9.2,
    'ativo': True
}

print(type(aluno))
print(aluno['nome'])
print(len(aluno))

for k in aluno:
    print(k, aluno[k])
