from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class RetiraSenhaLayout(GridLayout):
    def novaSenha(self, label, preferencial):
        i = int(label) + 1

        if preferencial:
            print(str(i) + " preferencial")
        else:
            print(str(i) + " não preferencial")

        self.display.text = str(i)


class HotelApp(App):

    def build(self):
        return RetiraSenhaLayout()


HotelApp().run()

