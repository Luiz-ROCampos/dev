from kivy.app import app
from kivy.uix.label import label
from kivy.uix.boxlayout import Boxlayout

class root(app):
    def build(self):
        la = Boxlayout(orientention='vertical')
        lb = label(text='Olá, Mundo!')
        la.add_widget(lb)
        return la
    

if __name__=='__main__':
    root().run()