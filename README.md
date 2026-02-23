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

