from kivy.app import App  
from kivy.uix.button import Button  
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.label import Label  

box = BoxLayout(orientation='vertical')  
box.add_widget(Button(text='Level 1'))  
box.add_widget(Button(text='Level 2'))  
box.add_widget(Button(text='Level 3'))


MainApp().run()