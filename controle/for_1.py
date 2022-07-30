# for i in range(10):
#     print(i)
#
# for i in range(1, 11):
#     print(i)

# for i in range(1, 100, 7):  # terceiro param é o passo
#     print(i)

# nums = [1, 2, 3]
# for n in nums:
#     print(n, end=' ')

# texto = 'Texto de teste'
# for letra in texto:
#     print(letra, end=', ')

# for n in {1, 2, 3, 4, 4, 4, 5}:
#     print(n, end=' ')

produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'dect': 0.5
}
# for key in produto:
#     print(key, '==>', produto[key])
for key, value in produto.items():
    print(key, '=>', produto[key])

for key in produto.keys():  # qual diferença desse para o padrão??
    print(key, end=' ')

for value in produto.values():
    print(value, end=' ')



