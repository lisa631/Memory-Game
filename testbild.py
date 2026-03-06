from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock


class MemoryCard(BoxLayout):
    def __init__(self, image_source, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.image_source = image_source

        # Einheitliche Kartengröße
        self.card_size = (150, 150)

        # Start mit verdeckter Karte (Button)
        self.card_button = Button(
            text="?",
            font_size=40,
            size_hint=(None, None),
            size=self.card_size
        )
        self.card_button.bind(on_press=self.reveal_card)

        self.add_widget(self.card_button)

    def reveal_card(self, instance):
        # Button entfernen und Bild anzeigen
        self.clear_widgets()
        self.card_image = Image(
            source=self.image_source,
            size_hint=(None, None),
            size=self.card_size,  # gleiche Größe wie Button
            allow_stretch=True,   # Bild wird gestreckt
            keep_ratio=True       # Seitenverhältnis beibehalten
        )
        self.add_widget(self.card_image)

        # Nach 2 Sekunden wieder verdecken
        Clock.schedule_once(self.hide_card, 2)

    def hide_card(self, dt):
        # Bild entfernen und Button zurück
        self.clear_widgets()
        self.add_widget(self.card_button)


class MemoryApp(App):
    def build(self):
        layout = BoxLayout(padding=20, spacing=20)
        layout.add_widget(MemoryCard("pig.jpeg"))
        return layout


if __name__ == "__main__":
    MemoryApp().run()