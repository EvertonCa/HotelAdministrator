import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador(ScreenManager):
    pass

class LoginLayout(Screen):
    def verificaLogin(self):
        pass


class HotelApp(App):

    def build(self):
        return Gerenciador()

calcApp = HotelApp()
calcApp.run()

