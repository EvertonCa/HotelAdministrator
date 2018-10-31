from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
from Controller import *
from Criador import *
from Model.Funcionarios import *
from Model.Cliente import *
from Model.Pedido import *
from Model.Quarto import *



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

        if nome is "" or telefone is "" or cpf is "" or endeteco is "":
            CustomPopup().call_pops("Nao foi preenchido todos os itens", "OK", 0.25, 0.25)
            return

        if sexo:
            genero = "masculino"
        else:
            genero = "feminino"


#        salvaCliente(Cliente(nome, telefone, cpf, endeteco, genero))

        App.get_running_app().root.current = 'menu'
        CustomPopup().call_pops("Pessoa adcionada", "OK", 0.25, 0.25)


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


class Senha(Screen):
    def proximaSenha(self, guiche, prioritaria):
        if prioritaria:
            print("Prioritaria guiche " + guiche)
        else:
            print("Guiche " + guiche)


class Clientes(Screen):
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


        try:
            numero = int(quarto)
        except:
            popup.call_pops(quarto + " nao eh um numero!", 'Ok')
            return

        # verifica se o quarto existe no hotel
        if numero < 1 or numero > 20:
            popup.call_pops('So existe quartos de 1 a 20', 'Ok')
            return

        cliente = pesquisaCliente(nome)

        if cliente is None:
            popup.call_pops("Cliente nao cadastrado", 'Ok')
            return

        # vincula o quarto a pessoa


        print(nome + " " + quarto)
        popup.call_pops(nome + ' foi adicionadas no quarto ' + quarto, 'Ok')
        self.ids.nomeQuarto.text = ""

        App.get_running_app().root.current = 'menu'

class LoginLayout(Screen):
    def verificaLogin(self, login, pswd):
        msgPopUp = CustomPopup()

        senha.setUser(login)
        senha.setPassword(pswd)

        if senha.verificaUserESenha() is True:
            print("Certo miseravi!")
            self.ids.loginText.text = ""
            self.ids.passwordText.text = ""
            App.get_running_app().root.current = 'menu'
        else:
            msgPopUp.call_pops('Errrooou!!', 'Ok', 0.25, 0.25)
            print("Errrooou")


class CustomPopup(Popup):
    def call_pops(self, tit, conten, x=None, y=None):
        cont = Button(text=conten)
        pop = Popup(title=tit, content=cont, size_hint=(x, y), size=(200, 100), auto_dismiss=True)
        pop.open()
        cont.bind(on_press=pop.dismiss)



class Hotel(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Gerenciador()


inicializaPrograma(20)
senha = Senhas('bla', 'bla')

Hotel().run()

#print(Criador.diretorio_atual)

