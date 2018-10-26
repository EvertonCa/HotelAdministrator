import Model.Funcionarios
import Model.Cliente
import Controller.Criador


class Senhas():
    def __init__(self, user, password):
        self._user = user
        self._password = password

    def verificaUserESenha(self):
        funcionarios = Controller.Criador.recuperaFuncionarios()
        for funcionario in funcionarios:
            if self._user == funcionario.usuario:
                if self._password == funcionario.senha:
                    return True
            return False



senha = Senhas('user', 'password')
senha.verificaUserESenha()