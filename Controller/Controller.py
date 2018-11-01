import os
import Criador
from pathlib import Path


diretorio_files = Criador.diretorio_files


class Senhas():
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self._funcionario = None

    def setUser(self, user):
        self._user = user

    def setPassword(self, password):
        self._password = password

    def verificaUserESenha(self):
        avl_funcionarios = Criador.recuperaFuncionarios(diretorio_files)

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


def inicializaPrograma(quantidadeDeQuartos, diretorio=diretorio_files):
    arquivo_funcionarios = Path(diretorio + '/Funcionarios.pkl')
    arquivo_clientes = Path(diretorio + '/Clientes.pkl')
    arquivo_quartos = Path(diretorio + '/Quartos.pkl')
    arquivo_pedidos = Path(diretorio + '/Pedidos.pkl')
    arquivo_senha = Path(diretorio + '/SenhasNormais.pkl')
    if arquivo_funcionarios.is_file() is False:
        Criador.inicialFuncionario(diretorio)
        print('Arquivo Funcionarios.pkl criado!')
    if arquivo_clientes.is_file() is False:
        Criador.inicialCliente(diretorio)
        print('Arquivo Clientes.pkl criado!')
    if arquivo_pedidos.is_file() is False:
        Criador.inicialPedidos(diretorio)
        print('Arquivo Pedidos.pkl criado!')
    if arquivo_quartos.is_file() is False:
        Criador.iniciaQuartos(quantidadeDeQuartos, diretorio)
        print('Arquivo Quartos.pkl criado com ' + str(quantidadeDeQuartos) + ' quartos!')
    if arquivo_senha.is_file() is False:
        Criador.iniciaSenhas(diretorio)
        print('Arquivo SenhasNormais.pkl e SenhasPrioritarias.pkl criados!')


def pesquisaCliente(nome):
    avl_clientes = Criador.recuperaClientes(diretorio_files)
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
