import Model.NoArvore


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def insert(self, valor):
        novo = Model.NoArvore.No()
        atual = self.raiz
        anterior = None

        while atual:
            anterior = atual

            if valor <= atual.valor:
                atual = atual.folha_esquerda
            else:
                atual = atual.folha_direita

        novo.pai = anterior
        novo.valor = valor

        if anterior:
            if valor <= anterior.valor:
                anterior.folha_esquerda = novo
            else:
                anterior.folha_direita = novo

        else:
            self.raiz = novo

        self.tamanho += 1
        return True

    def antes(self, no):
        if no.folha_direita is None:
            return no
        return self.antes(no.folha_direita)

    def quantosFilhos(self, no):
        return (no.folha_esquerda is not None) + (no.folha_direita is not None)

    def ponteiroDoPai(self, ponteiro_apagar, novo_ponteiro = None):
        if ponteiro_apagar.pai.folha_esquerda == ponteiro_apagar:
            ponteiro_apagar.pai.folha_esquerda = novo_ponteiro
        else:
            ponteiro_apagar.pai.folha_direita = novo_ponteiro

    def search(self, no, valor):
        if no is None or no.valor == valor:
            return no
        elif valor > no.valor:
            return self.search(no.folha_direita, valor)
        else:
            return self.search(no.folha_esquerda, valor)

    def remove(self, valor):
        if self.search(self.raiz, valor) is None:
            return False
        else:
            self.remover(self.search(self.raiz, valor))
        return True

    def remover(self, valor):
        filhos = self.quantosFilhos(valor)

        if filhos == 0:
            self.ponteiroDoPai(valor)
            del valor
        elif filhos == 1:
            f = valor.folha_esquerda
            if f is None:
                f = valor.folha_direita

            self.ponteiroDoPai(valor, f)
            f.pai = valor.pai
            del valor
        else:
            anterior = self.antes(valor.folha_esquerda)
            valor.valor = anterior.valor
            self.remover(anterior)

    def ERD(self, aux):
        if aux:
            self.ERD(aux.folha_esquerda)
            print(aux.valor, end=" ", flush=True)
            self.ERD(aux.folha_direita)
            return True
        return False

    def print(self):
        self.ERD(self.raiz)
        print("")


arvore = ArvoreBinaria()
arvore.insert(5)
arvore.insert(8)
arvore.insert(2)
arvore.insert(9)
arvore.insert(1)
arvore.print()
arvore.remove(1)
arvore.print()
arvore.remove(5)
arvore.print()

arvoreDeString = ArvoreBinaria()
arvoreDeString.insert('a')
arvoreDeString.insert('e')
arvoreDeString.insert('g')
arvoreDeString.insert('b')
arvoreDeString.insert('z')
arvoreDeString.print()
