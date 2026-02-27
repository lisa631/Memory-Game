from kivy.app import App  
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.button import Button  
from kivy.uix.label import Label  
import random
from PIL import Image

a = Image.open("bear.jpeg")
b = Image.open("cat.jpeg")
c = Image.open("cow.jpeg")
d = Image.open("dog.jpeg")
e = Image.open("elefant.jpeg")
f = Image.open("fox.jpeg")
g = Image.open("koala.jpeg")
h = Image.open("lama.jpeg")
i = Image.open("bear2.jpeg")
j = Image.open("cat2.jpeg")
k = Image.open("cow2.jpeg")
l = Image.open("dog2.jpeg")
m = Image.open("elefant2.jpeg")
n = Image.open("fox2.jpeg")
o = Image.open("koala2.jpeg")
p = Image.open("lama2.jpeg")


bilder = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]

button_choice = None
class GridApp(App):
    def build(self):
       # Set grid size
        self.cols = 4
        self.rows = 4
        random.shuffle(bilder)
        grid = GridLayout(cols= self.cols, padding=20, spacing=10)

        for i in range(1, 17):
            button = Button(background_color=(0, 0, 1, 1))
            grid.add_widget(button)

        
        def button_pressed(choice):
            global button_choice
            button_choice = choice
            if button_choice == button:
                button.background_color = (0, 0, 0, 0)
                

        return grid
    

if __name__ == "__main__":
    GridApp().run()
