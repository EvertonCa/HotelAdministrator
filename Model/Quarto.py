import Utilities.LDDE
import Utilities.Fila
import Cliente
import Pedido


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
        valor_total += self.valor_diaria * self.tempo_estadia
        while self.pedidos.top():
            valor_total += self.pedidos.top().valor.preco
            self.pedidos.pop()

        del self.pedidos
        self.tempo_estadia = None
        self.valor_diaria = None
        self.clientes = Utilities.LDDE.LDDE()
        self.pedidos = Utilities.Fila.FilaEncadeada()
        return valor_total

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


# quarto = Quarto(1)
# quarto.definirTempoDeEstadia(3)
# quarto.definirValorDiaria(100)
# cliente = Cliente.Cliente('Nome', 'telefone', 'cpf', 'endereco', 'sexo')
# quarto.adicionaCliente(cliente)
# pedido = Pedido.Pedido('Descricao', 200)
# quarto.adicionaPedido(pedido)
# print(quarto.fazerCheckout())
