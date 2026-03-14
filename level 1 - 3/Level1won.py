from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import subprocess
import sys
import level2


class MyApp(App):
    def build(self):
        layout = BoxLayout()
        btn = Button(text="Level 2", padding=50)
        # Bindet den Klick an die Funktion 'run_level2'
        btn.bind(on_press=self.run_level2)
        layout.add_widget(btn)
        return layout

    def run_level2(self, instance):
        # Öffnet die level2 Datei
        subprocess.Popen([sys.executable, "level2.py"])

if __name__ == '__main__':
    MyApp().run()