import Utilities.LDDE
import Utilities.Fila


class Quarto:
    def __init__(self, numero, valorEstadia):
        self.numero = numero
        self.valor_estadia = valorEstadia
        self.tempo_estadia = None
        self.clientes = Utilities.LDDE.LDDE()
        self.pedidos = Utilities.Fila.FilaEncadeada()

    def definirTempoDeEstadia(self, tempo):
        self.tempo_estadia = tempo

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


