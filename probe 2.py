from kivy.app import App  
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.button import Button  
from kivy.uix.label import Label  
from kivy.clock import Clock
import random
from PIL import Image
from kivy.uix.image import Image


bilder = ["bear.jpeg", "cat.jpeg", "cow.jpeg", "dog.jpeg", "elefant.jpeg", "fox.jpeg", "koala.jpeg", "lama.jpeg"] * 2


class GridApp(App):
    def build(self):
        self.counter = 0
        self.aufgedeckte_buttons = []

        grid = GridLayout(cols= 4, padding=20, spacing=10)
        self.rows = 4
        random.shuffle(bilder)
        

        for bild in bilder:
            button = Button(
                background_color=(0, 0, 1, 1))  
                
            button.bild = bild 
            button.offen = False
            button.bind(on_press=self.button_pressed)
            grid.add_widget(button)
                

        return grid
    
    def button_pressed(self, button):

        if button.offen or self.counter ==2:
            return
        
        button.background_color = (0, 0, 1, 0)
        button.offen = True
        self.aufgedeckte_buttons.append(button)
        self.counter += 1

        if self.counter == 2:
            Clock.schedule_once(self.pruefen, 5)

    def pruefen(self, dt):
        for button in self.aufgedeckte_buttons:
            button.background_color = (0, 0, 1, 1)
        b1, b2 = self.aufgedeckte_buttons

        if b1.bild != b2.bild:
            for b in self.aufgedeckte_buttons:
                b.offen = False
        else:
            b1.disabled = True
            b2.disabled = True

        self.aufgedeckte_buttons = []
        self.counter = 0


if __name__ == "__main__":
    GridApp().run()
