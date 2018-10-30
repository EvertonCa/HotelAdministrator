import Utilities.No


class FilaEncadeada:
    def __init__(self, tamanho_da_fila=0, ultimo_no=None, primeiro_no=None):
        self.tamanho_da_fila = tamanho_da_fila
        self.ultimo_no = ultimo_no
        self.primeiro_no = primeiro_no

    def push(self, value):
        novo = Utilities.No.No(value)

        if novo is None:
            return False

        if self.ultimo_no is not None:
            self.ultimo_no.proximo = novo
            self.ultimo_no = novo
        else:
            self.primeiro_no = novo
            self.ultimo_no = novo

        return True

    def pop(self):
        if self.primeiro_no is None:
            return False

        else:
            self.primeiro_no = self.primeiro_no.proximo

        return True

    def top(self):
        if self.primeiro_no is None:
            return None

        else:
            return self.primeiro_no

    def print(self):
        aux = self.primeiro_no
        while aux:
            print(aux.valor, end=" ", flush=True)
            aux = aux.proximo
        print("")


# fila = FilaEncadeada()
# fila.push(4)
# fila.push(8)
# fila.push(1)
# fila.push(10)
# fila.push(5)
# fila.push(3)
# fila.print()
# fila.pop()
# fila.print()
# fila.pop()
# fila.print()
