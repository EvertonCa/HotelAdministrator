class LES:
    def __init__(self):
        self.tamanho = 0
        self.lista = []

    def insert(self, value):
        i = 0

        self.lista.append(None)

        for i in range(self.tamanho+1):
            if self.lista[i]:
                if self.lista[i] >= value:
                    break

        for j in range(self.tamanho, i, -1):
            self.lista[j] = self.lista[j-1]

        self.lista[i] = value
        self.tamanho += 1

    def search(self, value):
        for i in range(self.tamanho):
            if self.lista[i] == value:
                return i
        return -1

    def remove(self, value):
        index = self.search(value)

        if index == -1:
            return False
        else:
            for j in range(index, self.tamanho-1):
                self.lista[j] = self.lista[j+1]

            self.lista = self.lista[:self.tamanho-1]
            self.tamanho -= 1
            return True

    def print(self):
        print(self.lista)


les = LES()
les.insert(4)
les.print()
les.insert(7)
les.print()
les.insert(2)
les.print()
print(les.search(4))
les.remove(4)
les.print()
