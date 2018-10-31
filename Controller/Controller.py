import Criador
from pathlib import Path


class Senhas():
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self._funcionario = None

    def verificaUserESenha(self):
        avl_funcionarios = Criador.recuperaFuncionarios()

        temp = avl_funcionarios.search(avl_funcionarios.raiz, self._user)
        if temp:
            funcionario = temp.valor
            if funcionario.senha == self._password:
                self._funcionario = funcionario.admin
                return True
        return False

    def ehAdmin(self):
        if self._funcionario is True:
            return True
        else:
            return False


def inicializaPrograma(quantidadeDeQuartos):
    arquivo_funcionarios = Path(Criador.diretorio_files + 'Funcionarios.pkl')
    arquivo_clientes = Path(Criador.diretorio_files + 'Clientes.pkl')
    arquivo_quartos = Path(Criador.diretorio_files + 'Quartos.pkl')
    arquivo_pedidos = Path(Criador.diretorio_files + 'Pedidos.pkl')
    if arquivo_funcionarios.is_file() is False:
        Criador.inicialFuncionario()
        print('Arquivo Funcionarios.pkl criado!')
    if arquivo_clientes.is_file() is False:
        Criador.inicialCliente()
        print('Arquivo Clientes.pkl criado!')
    if arquivo_pedidos.is_file() is False:
        Criador.inicialPedidos()
        print('Arquivo Pedidos.pkl criado!')
    if arquivo_quartos.is_file() is False:
        Criador.iniciaQuartos(quantidadeDeQuartos)
        print('Arquivo Quartos.pkl criado com ' + str(quantidadeDeQuartos) + ' quartos!')


def pesquisaCliente(nome):
    avl_clientes = Criador.recuperaClientes()
    temp = avl_clientes.search(avl_clientes.raiz, nome)
    if temp:
        cliente = temp.valor
        return cliente
    else:
        return None


# senha = Senhas('admin', 'admin')
# print(senha.verificaUserESenha())
# print(senha.ehAdmin())
# inicializaPrograma(3)
