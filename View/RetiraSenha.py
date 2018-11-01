from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from Criador import *


class RetiraSenhaLayout(GridLayout):
    def novaSenha(self, label, preferencial):
        i = int(label) + 1

        if preferencial:
            print(str(i) + " preferencial")
            salvaSenhaPrioritaria(i)
        else:
            print(str(i) + " não preferencial")
            salvaSenhaNormal(i)

        self.display.text = str(i)


class senhaApp(App):

    def build(self):
        return RetiraSenhaLayout()

senhaApp().run()

