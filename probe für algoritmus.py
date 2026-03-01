from kivy.app import App  
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.button import Button  
from kivy.uix.label import Label  
from kivy.clock import Clock
import random
#from PIL import Image


bilder = ["bear.jpeg", "cat.jpeg", "cow.jpeg", "dog.jpeg", "elefant.jpeg", "fox.jpeg", "koala.jpeg", "lama.jpeg", "bear2.jpeg", "cat2.jpeg", "cow2.jpeg", "dog2.jpeg", "elefant2.jpeg", "fox2.jpeg", "koala2.jpeg", "lama2.jpeg"]


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
            button.bind(on_press=self.button_pressed)
            grid.add_widget(button)
                

        return grid
    
    def button_pressed(self, button):
        
        button.background_color = (0, 0, 1, 0)
        self.aufgedeckte_buttons.append(button)
        self.counter += 1

        if self.counter == 2:
            Clock.schedule_once(self.zuruecksetzen, 5)

    def zuruecksetzen(self, dt):
        for button in self.aufgedeckte_buttons:
            button.background_color = (0, 0, 1, 1)
        self.counter = 0
        self.aufgedeckte_buttons = []

if __name__ == "__main__":
    GridApp().run()
