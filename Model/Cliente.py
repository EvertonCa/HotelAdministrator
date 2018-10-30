class Cliente():
    def __init__(self, nome, telefone, cpf, endereco, sexo):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco
        self.sexo = sexo

    def __lt__(self, other):
        return self.nome < other

    def __le__(self, other):
        if isinstance(other, Cliente):
            return self.nome <= other.nome
        elif isinstance(other, (int, float, str)):
            return self.nome <= other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Cliente):
            return self.nome >= other.nome
        elif isinstance(other, (int, float, str)):
            return self.nome >= other
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.nome == other

    def __ne__(self, other):
        return self.nome != other

    def __gt__(self, other):
        return self.nome > other
