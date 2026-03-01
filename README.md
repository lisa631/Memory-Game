Ich habe den ersten Entwurf für den Algorthmus geschrieben, ich konnte ihn aber noch nicht austesten. Mein Computer will das gerade noch nicht. Wenn das aber jemand kurz überprüfen und mir eine Rückmeldung geben könnte wäre das super. Datei = "Probe für algorithmus" - für level 1 
ansonsten habe ich jetzt mehrere Boilder hinzugefügt. In der Datei ist noch nicht mitinbegriffen, was passiert, wenn zwei gleiche Paare sich erkennen. 

Also ich habe einige Kleinigkeiten in der Datei "Probe für Algorithmus" geändert, sodass es ausgeführt werden kann. Es werden jetzt 16 Felder angezeigt, zum anklicken, aber das zeitliche Delay von dem anzeigen der Karten nach dem antippen stimmt noch nicht ganz. Zudem sollten wir noch eine Art Blockade hinzufügen, die verhindert, dass man alle Karten gleichzeitig anklicken kann. Ich habe jetzt auch noch versucht, die Anfänge von der Paarbildzuordnung zu etablieren. Wir brauchen ja nur pro Paar ein Foto, was wir zweimal reinmachen, deswegen hab ich die doppelten rausgenommen. - Lisa

Heute geschaft: 
- erster Entwurf für den Algorthmus
- Bilder gefunden + hinzugefügt
- Zufallsmechsnismen recherchieren/ mit Buttons integrieren
- überprüfen ob algorthmus funktioniert

Nächste Schritte:
- paare finden erkennung programieren
- sobalt ein Paar gefunden wurde soll es offen bleiben
- counter für die punkte
- Ende
- Timer
- (anpassung für Level 2 und 3)
- Main Page
- Ende (Rangliste)
- Verhindern, dass mehr als 2 Karten angeklickt werden können

Bildlink Hund: https://www.pngmart.com/files/23/Dog-Emoji-PNG-Pic.png

Bilder einfügen:
import tkinter as tk

root = tk.Tk()
root.title("Bild einfügen")
root.geometry("400x400")

photo = tk.PhotoImage(file="bild.png")  # Nur PNG/GIF
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()

