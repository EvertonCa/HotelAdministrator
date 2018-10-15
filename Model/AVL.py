import Model.NoArvore

class AVL:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def _altura(self, no):
        if no is None:
            return -1
        else:
            altura_folha_esquerda = self._altura(no.folha_esquerda)
            altura_folha_direita = self._altura(no.folha_direita)
            if altura_folha_esquerda > altura_folha_direita:
                return altura_folha_esquerda + 1
            else:
                return altura_folha_direita + 1

    def _fator_balanceamento(self, no):
        return self._altura(no.folha_esquerda) - self._altura(no.folha_direita)

    def _left(self, no):
        if no.folha_direita is None:
            return None

        nova_raiz = no.folha_direita

        if no.pai is None:
            self.raiz = nova_raiz
            self.raiz.pai = None
        else:
            no_temp = no.pai
            nova_raiz.pai = no_temp
            if no_temp.folha_esquerda and no_temp.folha_esquerda == no:
                no_temp.folha_esquerda = nova_raiz

            elif no_temp.folha_direita and no_temp.folha_direita == no:
                no_temp.folha_direita = nova_raiz

        no.pai = nova_raiz

        if nova_raiz.folha_esquerda:
            no.folha_direita = nova_raiz.folha_esquerda
            no.folha_direita.pai = no

        nova_raiz.folha_esquerda = no

    def _right(self, no):
        if no.folha_esquerda is None:
            return None

        nova_raiz = no.folha_esquerda

        if no.pai is None:
            self.raiz = nova_raiz
            self.raiz.pai = None
        else:
            no_temp = no.pai
            nova_raiz.pai = no_temp
            if no_temp.folha_esquerda and no_temp.folha_esquerda == no:
                no_temp.folha_esquerda = nova_raiz

            elif no_temp.folha_direita and no_temp.folha_direita == no:
                no_temp.folha_direita = nova_raiz

        no.pai = nova_raiz

        if nova_raiz.folha_direita:
            no.folha_esquerda = nova_raiz.folha_direita
            no.folha_esquerda.pai = no

        nova_raiz.folha_direita = no

    def _balanceia(self, no):
        while no:
            if self._fator_balanceamento(no) >= 2:
                if no.folha_direita and self._fator_balanceamento(no.folha_direita) < 0:
                    self._right(no.folha_direita)
                self._left(no)

            elif self._fator_balanceamento(no) <= -2:
                if no.folha_esquerda and self._fator_balanceamento(no.folha_esquerda) > 0:
                    self._left(no.folha_esquerda)
                self._right(no)

            no = no.pai

    def _antes(self, no):
        if no.folha_direita is None:
            return no
        return self._antes(no.folha_direita)

    def _quantosFilhos(self, no):
        return (no.folha_esquerda is not None) + (no.folha_direita is not None)

    def _ponteiroDoPai(self, ponteiro_apagar, novo_ponteiro = None):
        if ponteiro_apagar.pai.folha_esquerda == ponteiro_apagar:
            ponteiro_apagar.pai.folha_esquerda = novo_ponteiro
        else:
            ponteiro_apagar.pai.folha_direita = novo_ponteiro

    def _search(self, no, valor):
        if no is None or no.valor == valor:
            return no
        elif valor > no.valor:
            return self._search(no.folha_direita, valor)
        else:
            return self._search(no.folha_esquerda, valor)

    def remove(self, valor):
        if self._search(self.raiz, valor) is None:
            return False
        else:
            self._remover(self._search(self.raiz, valor))
        return True

    def _remover(self, valor):
        filhos = self._quantosFilhos(valor)

        if filhos == 0:
            self._ponteiroDoPai(valor)
            del valor
        elif filhos == 1:
            f = valor.folha_esquerda
            if f is None:
                f = valor.folha_direita

            self._ponteiroDoPai(valor, f)
            f.pai = valor.pai
            del valor
        else:
            anterior = self._antes(valor.folha_esquerda)
            valor.valor = anterior.valor
            self._remover(anterior)

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
        self._balanceia(novo)
        return True


arvoreAVL = AVL()
arvoreAVL.insert(5)
arvoreAVL.insert(8)
arvoreAVL.insert(2)
arvoreAVL.insert(4)
arvoreAVL.print()
arvoreAVL.insert(41)
arvoreAVL.insert(42)
arvoreAVL.insert(43)
#arvoreAVL.insert(44)
arvoreAVL.print()