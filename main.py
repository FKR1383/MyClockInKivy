from kivy.app import App
from kivy.graphics import Rectangle, Ellipse, Color, Line, Rotate
from kivy.metrics import dp
from kivy.properties import Clock, ObjectProperty, StringProperty, NumericProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__()



class MyApp(App):
    pass

if __name__ == "__main__":
    MyApp().run()