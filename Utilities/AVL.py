import Utilities.NoArvore


class AVL:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def _fator_balanceamento(self, no):
        if no.folha_direita:
            altura_direita = no.folha_direita.altura
        else:
            altura_direita = -1
        if no.folha_esquerda:
            altura_esquerda = no.folha_esquerda.altura
        else:
            altura_esquerda = -1

        return altura_direita - altura_esquerda

    def _altura(self, no):
        if no.folha_direita is None and no.folha_esquerda is None:
            no.altura = 0

        elif no.folha_esquerda:
            if no.folha_direita:
                if no.folha_direita.altura > no.folha_esquerda.altura:
                    no.altura = no.folha_direita.altura + 1
                if no.folha_esquerda.altura >= no.folha_direita.altura:
                    no.altura = no.folha_esquerda.altura + 1
            else:
                no.altura = no.folha_esquerda.altura + 1
        elif no.folha_direita:
            no.altura = no.folha_direita.altura + 1

    def _recalcular_altura(self, no):
        while no:
            self._altura(no)
            no = no.pai

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

        if no.folha_direita == nova_raiz:
            no.folha_direita = None
        if no.folha_esquerda == nova_raiz:
            no.folha_esquerda = None

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

        if no.folha_direita == nova_raiz:
            no.folha_direita = None
        if no.folha_esquerda == nova_raiz:
            no.folha_esquerda = None

    def _balanceia(self, no):
        while no:
            fb = self._fator_balanceamento(no)
            if fb >= 2:
                if no.folha_direita and self._fator_balanceamento(no.folha_direita) < 0:
                    temp = no.folha_direita
                    self._right(no.folha_direita)
                    self._recalcular_altura(temp)
                self._left(no)
                self._recalcular_altura(no)

            elif fb <= -2:
                if no.folha_esquerda and self._fator_balanceamento(no.folha_esquerda) > 0:
                    temp = no.folha_esquerda
                    self._left(no.folha_esquerda)
                    self._recalcular_altura(temp)
                self._right(no)
                self._recalcular_altura(no)

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
        a_remover = self._search(self.raiz, valor)
        if a_remover is None:
            return False

        temp = None

        if a_remover.pai:
            temp = a_remover.pai

        self._remover(a_remover)

        if temp is None:
            temp = self.raiz

        self._balanceia(temp)

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

    def _ERD(self, aux):
        if aux:
            self._ERD(aux.folha_esquerda)
            print(aux.valor, end=" ", flush=True)
            self._ERD(aux.folha_direita)
            return True
        return False

    def printERD(self):
        self._ERD(self.raiz)
        print("")

    def _RED(self, aux):
        if aux:
            print(aux.valor, end=" ", flush=True)
            self._RED(aux.folha_esquerda)
            self._RED(aux.folha_direita)
            return True
        return False

    def printRED(self):
        self._RED(self.raiz)
        print("")

    def insert(self, valor):
        novo = Utilities.NoArvore.No()
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
        self._recalcular_altura(novo)
        self._balanceia(novo)
        return True


# arvore2 = AVL()
# arvore2.insert(1)
# arvore2.insert(99)
# arvore2.insert(88)
# arvore2.insert(-5)
# arvore2.insert(0)
# arvore2.insert(-7)
# print(" ------- ERD ------- ")
# arvore2.printERD()
# print(" ------- RED ------- ")
# arvore2.printRED()
#
# arvore2.remove(0)
# print(" ------- ERD ------- ")
# arvore2.printERD()
# print(" ------- RED ------- ")
# arvore2.printRED()