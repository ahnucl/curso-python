from functools import reduce

notas = [6.4, 7.2, 5.8, 8.4]

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
#
# print(notas)


def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc


# def mais_um_meio(nota):
#     return nota + 1.5


notas_finais = map(somar_nota(1.5), notas)  # map não é montado na hora
notas_finais2 = map(somar_nota(1.6), notas)
print(list(notas_finais))
print(list(notas_finais2))

def somar(a, b):
    return a + b


total = reduce(somar, notas, 0)
print(total)