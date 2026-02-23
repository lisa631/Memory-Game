from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class GridApp(App):
    def build(self):
       # Set grid size
        self.cols = 4
        self.rows = 4
        grid = GridLayout(cols= self.cols, padding=20, spacing=10)

        for i in range(1, 17):
            grid.add_widget(Button(text=str(i)))


        return grid
    

    def button_gedrueckt(self, instance):
        print(instance.text + "wurde gedrückt")
        instance.background_color = (0, 0, 1, 1)



GridApp().run()
