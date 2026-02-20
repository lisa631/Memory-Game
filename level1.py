from kivy.app import App  
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.button import Button  
<<<<<<< HEAD
#from kivy.uix.label import Label  

class Level1App(App):  
    def build(self):    

        grid = GridLayout(cols=4)  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))  
        grid.add_widget(Button(text="Memory.io", font_size=20))
        return layout
    

    def button_gedrueckt(self, instance):
        print(instance.text + "wurde gedrückt")
        instance.background_color = (0, 0, 1, 1)

Level1App().run()
=======
from kivy.uix.label import Label  
>>>>>>> 680d0e2f4b0daa9cbb03b94741134f7065c910a1
