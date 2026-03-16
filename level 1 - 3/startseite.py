from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from level1 import Level1Screen
from level2 import Level2Screen
from level3 import Level3Screen


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation='vertical', padding=50, spacing=20)

        buttons = [
            ("Level 1", "level1"),
            ("Level 2", "level2"),
            ("Level 3", "level3")
        ]

        for text, target in buttons:
            btn = Button(text=text, font_size=20)
            btn.bind(on_press=lambda instance, t=target: self.change_screen(t))
            box.add_widget(btn)

        self.add_widget(box)

    def change_screen(self, screen_name):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = screen_name


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainMenu(name="menu"))
        sm.add_widget(Level1Screen(name="level1"))
        sm.add_widget(Level2Screen(name="level2"))
        sm.add_widget(Level3Screen(name="level3"))

        return sm


if __name__ == "__main__":
    MyApp().run()
