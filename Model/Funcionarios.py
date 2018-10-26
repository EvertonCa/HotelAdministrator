class Funcionario():
    def __init__(self, usuario, senha, admin):
        self.usuario = usuario
        self.senha = senha
        self.admin = admin

    def __lt__(self, other):
        return self.usuario < other

    def __le__(self, other):
        if isinstance(other, Funcionario):
            return self.usuario <= other.usuario
        elif isinstance(other, (int, float, str)):
            return self.usuario <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Funcionario):
            return self.usuario >= other.usuario
        elif isinstance(other, (int, float, str)):
            return self.usuario >= other
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.usuario == other

    def __ne__(self, other):
        return self.usuario != other

    def __gt__(self, other):
        return self.usuario > other

