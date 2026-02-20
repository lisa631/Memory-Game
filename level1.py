from kivy.app import App  
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.button import Button  
#from kivy.uix.label import Label  

class Level1App(App):  
    def build(self):    

        layout = GridLayout(cols=4, row=4)   
        def __init__(self, **kwargs):         
            super().__init__(**kwargs)    
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
