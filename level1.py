from kivy.app import App  
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.button import Button  
from kivy.uix.label import Label  

class MyGridApp(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set grid size
        self.cols = 6
        self.rows = 6
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
    

    def button_gedrueckt(self, instance):
        print(instance.text + "wurde gedrückt")
        instance.background_color = (0, 0, 1, 1)


class GridApp(App):
    def build(self):
        return MyGrid()

MyGridApp().run()
