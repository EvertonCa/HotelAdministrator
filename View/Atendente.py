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


        self.ids.nome.text = ""
        self.ids.telefone.text = ""
        self.ids.cpf.text = ""
        self.ids.endeteco.text = ""
        self.ids.sexo.text = ""


    def limpaCliete(self):
        self.ids.nome.text = ""
        self.ids.telefone.text = ""
        self.ids.cpf.text = ""
        self.ids.endeteco.text = ""
        self.ids.sexo.text = ""



class Quartos(Screen):
    def buscaQuarto(self, quarto):
        print("Pesquisar quarto " + quarto)
        numero = int(quarto)

        popup = CustomPopup()

        # procura quarto


        popup.call_pops('Quarto: ' + str(numero) +
                        "\nPessoa: ", 'Ok', 0.4, 0.4)



class Pedidos(Screen):
    def addPedidos(self, pedido):
        print("Adiciona pedido " + pedido)


class CheckOut(Screen):
    def checkout(self, quarto):
        popup = CustomPopup()
        try:
            numero = int(quarto)
        except:
            popup.call_pops('Nao foi entrado um quarto valido', 'Ok')
            return

        print("out " + str(numero))
        self.ids.num.text = ""

        App.get_running_app().root.current = 'menu'



class CheckIn(Screen):
    def addPessQuarto(self, nome, quarto):
        popup = CustomPopup()
        if nome is "" or quarto is "":
            popup.call_pops('Nao foi preenchido todos os itens', 'Ok')
            return

        numero = 0

        try:
            numero = int(quarto)
        except:
            popup.call_pops(quarto + " nao eh um numero!", 'Ok')
            return

        # verifica se o quarto existe no hotel
        if numero < 1 or numero > 15:
            popup.call_pops('So existe quartos de 1 a 15', 'Ok')
            return

        # busca se o nome ja foi cadastrado

        # vincula o quarto a pessoa vice versa

        print(nome + " " + quarto)
        popup.call_pops(nome + ' foi adicionadas no quarto ' + quarto, 'Ok')
        self.ids.nomeQuarto.text = ""

        App.get_running_app().root.current = 'menu'

class LoginLayout(Screen):

    def verificaLogin(self, login, pswd):

        msgPopUp = CustomPopup()

        if login == "root" and pswd == "toor":
            print("Certo miseravi!")
            self.ids.loginText.text = ""
            self.ids.passwordText.text = ""
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

    def call_pops(self, tit, conten, x, y):
        cont = Button(text=conten)
        pop = Popup(title=tit, content=cont, size_hint=(x, y), size=(200, 100), auto_dismiss=True)
        pop.open()
        cont.bind(on_press=pop.dismiss)



class Hotel(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Gerenciador()


Hotel().run()

