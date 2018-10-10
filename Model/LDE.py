import Model.No

class LDE:
    def __init__(self, tamanho_do_lde=0, primeiro_no=None):
        self.tamanho_do_lde = tamanho_do_lde
        self.primeiro_no = primeiro_no

    def insert(self, value):
        no_novo = Model.No.No(valor=value)

        no_anterior = None
        no_atual = self.primeiro_no

        while no_atual and value > no_atual.valor:
            no_anterior = no_atual
            no_atual = no_atual.proximo

        no_novo.proximo = no_atual

        if no_anterior is not None:
            no_anterior.proximo = no_novo
        else:
            self.primeiro_no = no_novo

        self.tamanho_do_lde += 1

        return True

    def _search(self, value):
        verificando = self.primeiro_no

        while verificando:
            if verificando.valor == value:
                return verificando

        return None

    def remove(self, value):
        atual = self.primeiro_no
        anterior = None

        while atual:
            if atual.valor == value:
                break

            anterior = atual
            atual = atual.proximo

        if anterior is None:
            self.primeiro_no = atual.proximo
        else:
            anterior.proximo = atual.proximo

        self.tamanho_do_lde -= 1
        return True


    def print(self):
        atual = self.primeiro_no

        while atual:
            print(atual.valor, end=" ", flush=True)
            atual = atual.proximo

        print('')


lde = LDE()
lde.insert(4)
lde.insert(6)
lde.insert(2)
lde.insert(5)
lde.print()
lde.remove(5)
lde.print()
lde.remove(2)
lde.print()
lde.insert(10)
lde.insert(1)
lde.insert(3)
lde.remove(4)
lde.print()
