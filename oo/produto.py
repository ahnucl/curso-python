
class Produto:
    def __init__(self, nome, preco=1.99, desc=0.0):
        self.nome = nome
        self.__preco = preco
        self.desc = desc

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    @property
    def preco_final(self):
        return self.preco * (1 - self.desc)


p1 = Produto('Caneta', 5.99, 0.1)
p2 = Produto('Caderno', 14, 0.5)

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)

p2.preco = 20.90
print(p2.nome, p2.preco, p2.desc, p2.preco_final)