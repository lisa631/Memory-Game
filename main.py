from kivy.app import App  
from kivy.uix.button import Button  
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.label import Label  
import tkinter as tk


class MainApp(App):
    def run_level1():
        script_path = "level1.py"
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=40)

        eins = tk.Button(text="Level 1", background_color=(0, 1, 0, 1), command=run_level1()) 
        zwei = tk.Button(text="Level 2", background_color=(0, 1, 0, 1))
        drei = tk.Button(text="Level 3", background_color=(0, 1, 0, 1))

        layout.add_widget(eins)
        layout.add_widget(zwei)
        layout.add_widget(drei)

        return layout
    
    

MainApp().run()