from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
from Controller import *
from Criador import *
from Funcionarios import *
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


        salvaCliente(Cliente(nome, telefone, cpf, endeteco, genero))

        App.get_running_app().root.current = 'menu'
        CustomPopup().call_pops("Pessoa adcionada", "OK", 0.25, 0.25)


class CadastrarFuncionario(Screen):
    adm = False

    def adiministrador(self, *args):
        global adm
        adm = True

    def normal(self, *args):
        global adm
        adm = False

    def cadastraFuncionario(self, usuario, senha):

        print("Funcionario " + usuario + " " + senha)

        if usuario is "" or senha is "":
            CustomPopup().call_pops("Preencha tudo!", "Ok", 0.25, 0.25)
            return


        salvaFuncionario(Funcionario(usuario, senha, adm))


        App.get_running_app().root.current = 'menu'
        CustomPopup().call_pops("Funcionario adcionado", "OK", 0.25, 0.25)


class Senha(Screen):
    def proximaSenha(self, guiche, prioritaria):
        if prioritaria:
            print("Prioritaria guiche " + guiche)
        else:
            print("Guiche " + guiche)


class Clientes(Screen):
    def buscaNome(self, nome):
        print("Busca o nome "+nome)

        cliente = pesquisaCliente(nome)

        if cliente is None:
            CustomPopup().call_pops("Nao encontrado", "ok", 0.25, 0.25)
            return

        self.ids.nome.text = str(cliente.nome)
        self.ids.telefone.text = str(cliente.telefone)
        self.ids.cpf.text = str(cliente.cpf)
        self.ids.endeteco.text = str(cliente.endereco)
        self.ids.sexo.text = str(cliente.sexo)


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
        les_quartos = recuperaQuartos()
        quarto = les_quartos.at(numero-1)

        if quarto.valor_diaria is None:
            popup.call_pops("Nao tem ninguem no quarto"+str(quarto.numero), "Ok", 0.25, 0.25)
            return

        mensagem = 'Quarto: ' + str(numero) +\
                   "\nEstadia: " + str(quarto.tempo_estadia) +\
                   "\nDiaria: " + str(quarto.valor_diaria) + "\nPessoas:\n"

        andando = quarto.clientes.primeiro_no

        for i in range(quarto.clientes.tamanho_do_ldde):
            mensagem += str(andando.valor.nome) + "\n"
            andando = andando.proximo


        popup.call_pops(mensagem, 'Ok', 0.5, 0.5)



class Pedidos(Screen):
    def addPedidos(self, pedido, quarto):
        print("Adiciona pedido " + pedido)


class CheckOut(Screen):
    def checkout(self, quarto):
        popup = CustomPopup()

        self.ids.num.text = ""

        try:
            numero = int(quarto)
        except:
            popup.call_pops('Nao foi entrado um quarto valido', 'Ok', 0.25, 0.25)
            return

        les_quartos = recuperaQuartos()

        if les_quartos.at(numero-1).valor_diaria is None or les_quartos.at(numero-1).tempo_estadia is None:
            popup.call_pops("Nao tem ninguem no quarto " + quarto)
            return

        popup.call_pops("Valor total a pagar: " + str(les_quartos.at(numero-1).fazerCheckout()), "Pagar", 0.25, 0.25)

        salvaQuartos(les_quartos)


        App.get_running_app().root.current = 'menu'



class CheckIn(Screen):
    def addPessQuarto(self, nome, quarto, dias, diaria):
        popup = CustomPopup()
        if nome is "" or quarto is "" or dias is "" or diaria is "":
            popup.call_pops('Nao foi preenchido todos os itens', 'Ok', 0.25, 0.25)
            return


        try:
            numero = int(quarto)
            qtdDias = int(dias)
            precoDia = int(diaria)
        except:
            popup.call_pops("Quarto, dias e diaria tem que ser um numero!", 'Ok', 0.25, 0.25)
            return

        # verifica se o quarto existe no hotel
        if numero < 1 or numero > 20:
            popup.call_pops('So existe quartos de 1 a 20', 'Ok', 0.25, 0.25)
            return

        # busca cliente
        cliente = pesquisaCliente(nome)

        if cliente is None:
            popup.call_pops("Cliente nao cadastrado", 'Ok')
            return

        # vincula o quarto a pessoa
        les_quartos = recuperaQuartos()

        les_quartos.at(numero-1).adicionaCliente(cliente)
        les_quartos.at(numero-1).definirValorDiaria(precoDia)
        les_quartos.at(numero-1).definirTempoDeEstadia(qtdDias)

        salvaQuartos(les_quartos)


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

