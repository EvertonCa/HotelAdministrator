import Utilities.Fila


class Gerenciador:
    def __init__(self):
        self._fila = Utilities.Fila.FilaEncadeada()
        self._fila_prioritaria = Utilities.Fila.FilaEncadeada()

    def adicionaNaFila(self, senha):
        self._fila.push(senha)

    def adicionaNaFilaPrioritaria(self, senha):
        self._fila_prioritaria.push(senha)

    def proxFila(self):
        senha = self._fila.top()
        self._fila.pop()
        return senha.valor

    def proxFilaPrioritaria(self):
        senha = self._fila_prioritaria.top()
        self._fila_prioritaria.pop()
        return senha.valor


# geren = Gerenciador()
# geren.adicionaNaFila(5)
# geren.adicionaNaFila(8)
# geren.adicionaNaFila(2)
# geren.adicionaNaFilaPrioritaria(4)
# geren.adicionaNaFilaPrioritaria(9)
# geren._fila.print()
# print(geren.proxFila())
# print(geren.proxFilaPrioritaria())
# print(geren.proxFila())
# print(geren.proxFilaPrioritaria())