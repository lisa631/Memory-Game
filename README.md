Ich habe den ersten Entwurf für den Algorthmus geschrieben, ich konnte ihn aber noch nicht austesten. Mein Computer will das gerade noch nicht. Wenn das aber jemand kurz überprüfen und mir eine Rückmeldung geben könnte wäre das super. Datei = "Probe für algorithmus" - für level 1 
ansonsten habe ich jetzt mehrere Boilder hinzugefügt. In der Datei ist noch nicht mitinbegriffen, was passiert, wenn zwei gleiche Paare sich erkennen. 

Heute geschaft: 
- erster Entwurf für den Algorthmus
- Bilder gefunden + hinzugefügt
- Zufallsmechsnismen recherchieren/ mit Buttons integrieren

Nächste Schritte:
- überprüfen ob algorthmus funktioniert
- paare finden erkennung programieren
- sobalt ein Paar gefunden wurde soll es offen bleiben
- counter für die punkte
- Ende
- Timer
- (anpassung für Level 2 und 3)
- Main Page
- Ende (Rangliste)

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

