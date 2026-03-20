
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.button import Button


class ImageButton(ButtonBehavior, Image):

    def __init__(self, index, game, **kwargs):
        super().__init__(**kwargs)

        Window.fullscreen = 'auto'

        self.index = index
        self.game = game
        self.is_matched = False
        self.is_revealed = False

        self.source = "Images/blau.jpeg"
        self.allow_stretch = True
        self.keep_ratio = False

    def on_press(self):
        if not self.is_revealed and not self.is_matched:
            self.game.reveal_card(self.index)


class MemoryGame(App):

    def build(self):

        self.layout = GridLayout(cols=4, rows=5, spacing=5, padding=[200, 0, 200, 0])

        base_images = [
            "Images/dog.jpeg",
            "Images/cat.jpeg",
            "Images/cow.jpeg",
            "Images/bear.jpeg",
            "Images/elefant.jpeg",
            "Images/fox.jpeg",
            "Images/koala.jpeg",
            "Images/lama.jpeg",
            "Images/lion.jpeg",
            "Images/monky.jpeg"
        ]

        self.images = base_images * 2

        self.buttons = []
        self.first_choice = None
        self.second_choice = None
        self.locked = False

        self.elapsed_seconds = 0
        self.timer_event = None
        self.score = 0

        self.root_widget = BoxLayout(orientation="vertical", spacing=5, padding=5)

        info_bar = BoxLayout(orientation="horizontal", size_hint=(1, None), height=50)

        self.timer_label = Label(text="Zeit: 0s", font_size=22, bold=True, color=(0.400, 0.698, 1, 1))
        self.score_label = Label(text="Punkte: 0", font_size=22, bold=True, color=(0.400, 0.698, 1, 1))

        info_bar.add_widget(self.timer_label)
        info_bar.add_widget(self.score_label)

        self.root_widget.add_widget(info_bar)
        self.root_widget.add_widget(self.layout)

        self.new_round()

        return self.root_widget



    def new_round(self):

        random.shuffle(self.images)

        self.layout.clear_widgets()
        self.buttons.clear()

        self.first_choice = None
        self.second_choice = None
        self.locked = False

        self.elapsed_seconds = 0
        self.score = 0

        self.update_labels()

        if self.timer_event:
            self.timer_event.cancel()

        self.timer_event = Clock.schedule_interval(self.tick, 1)

        for i in range(20):
            btn = ImageButton(index=i, game=self)
            self.buttons.append(btn)
            self.layout.add_widget(btn)


    def tick(self, dt):

        self.elapsed_seconds += 1
        self.update_labels()


    def update_labels(self):

        self.timer_label.text = f"Zeit: {self.elapsed_seconds}s"
        self.score_label.text = f"Punkte: {self.score}"


    def reveal_card(self, index):

        if self.locked:
            return

        btn = self.buttons[index]

        btn.source = self.images[index]
        btn.is_revealed = True

        if self.first_choice is None:
            self.first_choice = index

        elif self.second_choice is None and index != self.first_choice:
            self.second_choice = index
            self.check_match()


    def check_match(self):

        first_btn = self.buttons[self.first_choice]
        second_btn = self.buttons[self.second_choice]

        if self.images[self.first_choice] == self.images[self.second_choice]:

            first_btn.is_matched = True
            second_btn.is_matched = True

            self.score += 1
            self.update_labels()

            self.first_choice = None
            self.second_choice = None

            if self.score == 12:
                self.game_won()

        else:

            self.locked = True
            Clock.schedule_once(self.hide_cards, 1)


    def hide_cards(self, dt):

        self.buttons[self.first_choice].source = "Images/blau.jpeg"
        self.buttons[self.second_choice].source = "Images/blau.jpeg"

        self.buttons[self.first_choice].is_revealed = False
        self.buttons[self.second_choice].is_revealed = False

        self.first_choice = None
        self.second_choice = None
        self.locked = False


    def game_won(self):

        if self.timer_event:
            self.timer_event.cancel()

        layout = BoxLayout(orientation="vertical", spacing=20, padding=20)

        message = Label(
            text=f"Du hast gewonnen!\n\nZeit: {self.elapsed_seconds}s\nPunkte: {self.score}",
            font_size=24
        )

        restart_button = Button(text="Neues Spiel", size_hint=(1, 0.4))
        restart_button.bind(on_press=self.restart_game)

        layout.add_widget(message)
        layout.add_widget(restart_button)

        self.popup = Popup(
            title="Gewinner",
            content=layout,
            size_hint=(None, None),
            size=(400, 300),
            auto_dismiss=False
        )

        self.popup.open()


    def restart_game(self, instance):

        self.popup.dismiss()
        self.new_round()


if __name__ == "__main__":
    MemoryGame().run()