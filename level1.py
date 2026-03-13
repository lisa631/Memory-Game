import random
from kivy.app import App
import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from kivy.core.window import Window

def main():
    try:
        start_time = time.perf_counter()
        time.sleep(2.5)
        end_time = time.perf_counter()  
        elapsed = end_time - start_time
        print(f"Elapsed time: {elapsed:.6f} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")

# Klickbares Bild
class ImageButton(ButtonBehavior, Image):
    def __init__(self, index, game, **kwargs):
        super().__init__(**kwargs)
        Window.fullscreen = 'auto'
        self.index = index
        self.game = game
        self.is_matched = False
        self.is_revealed = False
        self.source = "blau.jpeg"  # Rückseite der Karte
        # 🔹 Bild strecken
        self.allow_stretch = True
        self.keep_ratio = False
        padding = 30
        spacing = 30

    def on_press(self):
        if not self.is_revealed and not self.is_matched:
            self.game.reveal_card(self.index)

class MemoryGame(App):
    def build(self):
        self.layout = GridLayout(cols=4, spacing=5, padding=5)

        # 🔹 HIER deine 8 Bilddateien eintragen
        base_images = [
            "dog.jpeg",
            "cat.jpeg",
            "cow.jpeg",
            "bear.jpeg",
            "elefant.jpeg",
            "fox.jpeg",
            "koala.jpeg",
            "lama.jpeg"
        ]

        # 2× jede Datei für Paare
        self.images = base_images * 2

        self.buttons = []
        self.first_choice = None
        self.second_choice = None
        self.locked = False
        self.new_round()
        return self.layout

    def new_round(self):
        """Startet eine neue Runde mit gemischten Bildern."""
        random.shuffle(self.images)
        self.layout.clear_widgets()
        self.buttons.clear()
        self.first_choice = None
        self.second_choice = None
        self.locked = False

        for i in range(16):
            btn = ImageButton(index=i, game=self)
            self.buttons.append(btn)
            self.layout.add_widget(btn)

    def reveal_card(self, index):
        """Zeigt eine Karte und prüft auf Paar."""
        
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
        """Prüft, ob zwei Karten ein Paar sind."""
        first_btn = self.buttons[self.first_choice]
        second_btn = self.buttons[self.second_choice]

        if self.images[self.first_choice] == self.images[self.second_choice]:
            # Paar gefunden
            first_btn.is_matched = True
            second_btn.is_matched = True
            self.first_choice = None
            self.second_choice = None
        else:
            # Kein Paar → kurz anzeigen, dann wieder verdecken
            self.locked = True
            Clock.schedule_once(self.hide_cards, 1)

    def hide_cards(self, dt):
        """Deckt Karten wieder zu."""
        self.buttons[self.first_choice].source = "blau.jpeg"
        self.buttons[self.second_choice].source = "blau.jpeg"
        self.buttons[self.first_choice].is_revealed = False
        self.buttons[self.second_choice].is_revealed = False
        self.first_choice = None
        self.second_choice = None
        self.locked = False

if __name__ == "__main__":
    MemoryGame().run()