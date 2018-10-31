from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from GerenciadorDeSenhasDeChama import *


class RetiraSenhaLayout(GridLayout):
    def novaSenha(self, label, preferencial):
        i = int(label) + 1

        if preferencial:
            print(str(i) + " preferencial")
            senhas.adicionaNaFilaPrioritaria(i)
        else:
            print(str(i) + " não preferencial")
            senhas.adicionaNaFila(i)

        self.display.text = str(i)


class senhaApp(App):

    def build(self):
        return RetiraSenhaLayout()

senhas = Gerenciador()
senhaApp().run()

