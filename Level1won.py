from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
import sys



class MemoryApp(App):
    def build(self):

        layout = BoxLayout(orientation="vertical", size_hint=(1, None), height=50, spacing=20, padding=60)
        
        #file_path = ""
        level2 = Button(text="Level 2", background_color=(0, 0, 1, 1))
        #file_path = os.path.join(os.path.dirname(__file__), "level2.py")
        #level2.bind(on_press=self.open_file) 
        layout.add_widget(level2)
        level2.pack()


        return layout
    
    #def open_file(self, instance):
        #file_path = "level2"
        #try:
        #    if sys.platform.startswith('win'):
         #       os.startfile(file_path)
          #  elif os.name == 'nt':  # Windows
           #     os.startfile(path)
        #except Exception as e:
         #   print(f"Fehler beim Öffnen der Datei: {e}") 

        
        
        
if __name__ == "__main__":
    MemoryApp().run()