import Utilities.LDDE
import Utilities.Fila


class Quarto:
    def __init__(self, numero):
        self.numero = numero
        self.valor_diaria = None
        self.tempo_estadia = None
        self.clientes = Utilities.LDDE.LDDE()
        self.pedidos = Utilities.Fila.FilaEncadeada()

    def definirTempoDeEstadia(self, tempo):
        self.tempo_estadia = tempo

    def definirValorDiaria(self, valor):
        self.valor_diaria = valor

    def adicionaCliente(self, cliente):
        self.clientes.insert(cliente)

    def adicionaPedido(self, pedido):
        self.pedidos.push(pedido)

    def fazerCheckout(self):
        del self.clientes
        valor_total = 0
        valor_total += self.valor_estadia * self.tempo_estadia
        while self.pedidos:
            valor_total += self.pedidos.top().preco
            self.pedidos.pop()
        self.tempo_estadia = None
        self.valor_diaria = None

    def __lt__(self, other):
        return self.numero < other

    def __le__(self, other):
        if isinstance(other, Quarto):
            return self.numero <= other.numero
        elif isinstance(other, (int, float, str)):
            return self.numero <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Quarto):
            return self.numero >= other.numero
        elif isinstance(other, (int, float, str)):
            return self.numero >= other
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.numero == other

    def __ne__(self, other):
        return self.numero != other

    def __gt__(self, other):
        return self.numero > other
