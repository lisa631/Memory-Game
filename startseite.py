# noch nicht fertig
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Buttons mit Ziel-Screens
        buttons = [
            ("Level 1", "level1"),
            ("Level 2", "level2"),
            ("Level 3", "level3")
        ]

        for text, target in buttons:
            btn = Button(text=text, font_size=20)
            # Wichtig: t=target fixiert den Wert pro Button
            btn.bind(on_press=lambda instance, t=target: self.change_screen(t))
            box.add_widget(btn)

        self.add_widget(box)

    def change_screen(self, screen_name):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = screen_name


class LevelScreen(Screen):
    def __init__(self, level_name, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation='vertical', padding=50, spacing=20)
        box.add_widget(Button(text=f"Willkommen bei {level_name}", font_size=24))
        back_btn = Button(text="Zurück", font_size=20)
        back_btn.bind(on_press=lambda instance: self.go_back())
        box.add_widget(back_btn)
        self.add_widget(box)

    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "menu"



if __name__ == "__main__":
    MainMenu().run()