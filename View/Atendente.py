from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import ObjectProperty


class Gerenciador(ScreenManager):
    pass


class Menu(Screen):
    pass


class Cadastrar(Screen):
    sexo = True  # Homem é True e mulher é False

    def homem(self, *args):
        global sexo
        sexo = True

    def mulher(self, *args):
        global sexo
        sexo = False

    def cadastraPessoa(self, nome, telefone, cpf, endeteco):

        print(nome + " " + telefone + " " + cpf + " " + endeteco)
        if sexo:
            print("homem")
        else:
            print("mulher")

        App.get_running_app().root.current = 'menu'
        CustomPopup().call_pops("Pessoa adcionada", "OK")


class CadastrarFuncionario(Screen):
    sexo = True # Homem é True e mulher é False

    def homem(self, *args):
        global sexo
        sexo = True

    def mulher(self, *args):
        global sexo
        sexo = False

    def cadastraFuncionario(self, nome, telefone, cpf, endeteco, usuario, senha):

        print("Funcionario " + nome + " " + telefone + " " + cpf + " " + endeteco + " " + usuario + " " + senha)

        if sexo:
            print("homem")
        else:
            print("mulher")

        App.get_running_app().root.current = 'menu'
        CustomPopup().call_pops("Funcionario adcionado", "OK")


class Senhas(Screen):
    def proximaSenha(self, guiche, prioritaria):
        if prioritaria:
            print("Prioritaria guiche " + guiche)
        else:
            print("Guiche " + guiche)


class Cliente(Screen):
    def buscaNome(self, nome):
        print("Busca o nome "+nome)


class Quartos(Screen):
    def buscaQuarto(self, quarto):
        print("Pesquisar quarto " + quarto)


class Pedidos(Screen):
    def addPedidos(self, pedido):
        print("Adiciona pedido " + pedido)


class CheckOut(Screen):
    def checkout(self):
        print("out")


class PessoaIn(App):
    def __init__(self,id='', **kwargs):
        super().__init__(**kwargs)
        self.ids.default.text = id


class CheckIn(Screen):
    def addPessQuarto(self, qtdPessoas, quarto):
        msgPopUp = CustomPopup()
        if int(qtdPessoas) == 0:
            msgPopUp.call_pops('Nao pode ter 0 pessoas', 'Ok')
            return

        print(qtdPessoas + " " + quarto)
        msgPopUp.call_pops(qtdPessoas + ' pessoas foram adicionadas ao quarto ' + quarto, 'Ok')
        App.get_running_app().root.current = 'menu'

    def qtdPessoas(self, qtdPessoas):
        print(qtdPessoas)
        for i in range(int(qtdPessoas)):
            self.ids.inputNomes.add_widget(PessoaIn(id='pessoa'+str(i)))

class LoginLayout(Screen):

    def verificaLogin(self, login, pswd):

        msgPopUp = CustomPopup()

        if login == "root" and pswd == "toor":
            print("Certo miseravi!")
            App.get_running_app().root.current = 'menu'
        else:
            msgPopUp.call_pops('Errrooou!!', 'Ok')
            print("Errrooou")


class CustomPopup(Popup):
    def call_pops(self, tit, conten):
        cont = Button(text=conten)
        pop = Popup(title=tit, content=cont, size_hint=(None, None), size=(200, 100), auto_dismiss=True)
        pop.open()
        cont.bind(on_press=pop.dismiss)



class Hotel(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Gerenciador()


Hotel().run()

