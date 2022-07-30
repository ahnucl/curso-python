def soma(a, b):
    return a + b


def sub(a, b):
    return a - b



somar = soma
print(somar(1, 3))


def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)


resultado = operacao_aritmetica(soma, 5, 12)
print(resultado)
resultado = operacao_aritmetica(sub, 5, 12)
print(resultado)


def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma

fn = soma_parcial(10)
resultado_final = fn(12)
print(resultado_final)

resultado_final2 = soma_parcial(10)(12)