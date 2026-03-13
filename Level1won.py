from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from level2 import ZweiterScreen()  # Modul importieren
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class MenuScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        Builder.load_file('main.kv')
        sm = Manager()
        # Screens zum Manager hinzufügen
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SubScreen(name='other'))
        return sm
        #btn = Button(text="Funktion ausführen")
        #btn.bind(on_press=self.on_button_click)
        #layout.add_widget(btn)
        #return layout

    #def on_button_click(self, instance):
        #level2.Subscreen(Screen)  # Funktion aufrufen

if __name__ == '__main__':
    MyApp().run()