import Criador
from pathlib import Path


class Senhas():
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self._funcionario = None

    def verificaUserESenha(self):
        funcionarios = Criador.recuperaFuncionarios()
        for funcionario in range (funcionarios.tamanho):
            if self._user == funcionarios.at(funcionario).usuario:
                if self._password == funcionarios.at(funcionario).senha:
                    self._funcionario = funcionarios.at(funcionario)
                    return True
            return False

    def ehAdmin(self):
        if self._funcionario.admin is True:
            return True
        else:
            return False


def inicializaPrograma():
    arquivo_funcionarios = Path(Criador.diretorio_files + 'Funcionarios.pkl')
    arquivo_clientes = Path(Criador.diretorio_files + 'Clientes.pkl')
    if arquivo_funcionarios.is_file() is False:
        Criador.inicialFuncionario()
        print('Arquivo Funcionarios.pkl criado!')
    if arquivo_clientes.is_file() is False:
        Criador.inicialCliente()
        print('Arquivo Clientes.pkl criado!')


# senha = Senhas('admin', 'admin')
# print(senha.verificaUserESenha())
# print(senha.ehAdmin())
# inicializaPrograma()
