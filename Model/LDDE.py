import Model.No


class LDDE:
    def __init__(self, tamanho_do_ldde=0, primeiro_no=None, ultimo_no=None):
        self.tamanho_do_ldde = tamanho_do_ldde
        self.primeiro_no = primeiro_no
        self.ultimo_no = ultimo_no

    def insert(self, value):
        novo = Model.No.No(value)

        anterior = None
        atual = self.primeiro_no

        if atual:
            anterior = atual.anterior

        while atual and value > atual.valor:
            anterior = atual
            atual = atual.proximo

        novo.anterior = anterior
        novo.proximo = atual
        proximo = novo.proximo

        if anterior:
            anterior.proximo = novo
        else:
            self.primeiro_no = novo

        if proximo:
            proximo.anterior = novo
        else:
            self.ultimo_no = novo

        self.tamanho_do_ldde += 1
        return True

    def remove(self, valor):
        if self.primeiro_no is None:
            return False

        atual = self.primeiro_no
        anterior = self.primeiro_no.anterior
        proximo = self.primeiro_no.proximo

        while atual and atual.valor != valor:
            anterior = atual
            atual = atual.proximo
            if atual:
                proximo = atual.proximo

        if atual is None:
            return False

        if anterior is None:
            self.primeiro_no = proximo

        else:
            anterior.proximo = proximo

        if proximo is None:
            self.ultimo_no = anterior

        else:
            proximo.anterior = anterior

        self.tamanho_do_ldde -= 1

        return True

    def print(self):
        andando = self.primeiro_no
        for i in range(self.tamanho_do_ldde):
            print(andando.valor, end=" ", flush=True)
            andando = andando.proximo
        print("")


ldde = LDDE()
ldde.insert(6)
ldde.insert(3)
ldde.insert(8)
ldde.insert(5)
ldde.insert(1)
ldde.insert(4)
ldde.print()
ldde.remove(4)
ldde.print()
ldde.remove(6)
ldde.print()
