import math
from datetime import datetime, time
from math import cos, sin

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle, Ellipse, Color, Line, Rotate
from kivy.metrics import dp
from kivy.properties import Clock, ObjectProperty, StringProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget



class TimeWidget(Widget):
    now = datetime.now()
    second_angle = NumericProperty(defaultvalue=-int(now.strftime("%S"))*6)
    minute_angle = NumericProperty(defaultvalue=-int(now.strftime("%M")) * 6)
    hour_angle = NumericProperty(defaultvalue=-int(now.strftime("%H")) * 30 - (float(now.strftime("%M"))/60)*30)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.time_rotating, 1)
    def time_rotating(self, dt):
        self.now = datetime.now()
        self.second_angle = -int(self.now.strftime("%S"))*6
        self.minute_angle = -int(self.now.strftime("%M")) * 6
        self.hour_angle = -int(self.now.strftime("%H")) * 30 - (float(self.now.strftime("%M"))/60)*30


class ClockWidget(Widget):
    numbers_labels = []
    alarm_time = StringProperty("")
    sound = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_numbers()
        self.set_back_ground()
        Clock.schedule_interval(self.check_alarm, 1)
        self.closed_button = Button(text="Ok!", pos=(0, 200), on_press=self.end_sound)
    def check_alarm(self, dt):
        try:
            help = datetime.strptime(self.alarm_time, "%H:%M:%S")
            if help == datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S"):
                self.sound = SoundLoader.load('sound/ringtone.mp3')
                if self.sound:
                    self.sound.loop = True
                    self.sound.play()
                self.add_widget(self.closed_button)
        except ValueError:
            pass
    def end_sound(instance, sound):
        instance.sound.stop()
        instance.remove_widget(instance.closed_button)
    def set_back_ground(self):
        with self.canvas.before:
            self.back = Rectangle(pos=(0, 0), size=(2000, 2000))
    def set_numbers(self):
        for i in range(12):
            number = i
            if i == 0:
                number = 12
            if number == 10:
                number = "X"
            elif number == 11:
                number = "XI"
            elif number == 12:
                number = "XII"
            number_label = Label(text=str(number), font_size=53, color=(0, 0, 0, 1), font_name="house-lannister-font/HouseLannisterFontDemo-ZVplz.ttf")
            self.numbers_labels.append(number_label)
            self.add_widget(number_label)
    def on_size(self, *args):
        for i in range(12):
            number = i
            if i == 0:
                number = 12
            self.numbers_labels[number % 12].pos = self.center_x - self.numbers_labels[number % 12].width/2 + dp(170)*sin(30*(number % 12)/180*math.pi), self.center_y - \
                                                   self.numbers_labels[number % 12].height/2 + dp(170)*cos(30*(number % 12)/180*math.pi)
    def change_alarm(self):
        self.time_input = self.ids.time_input
        try:
            help = datetime.strptime(self.time_input.text, "%H:%M:%S")
            self.alarm_time = self.time_input.text
        except ValueError:
            self.alarm_time = "Wrong!"



class MyApp(App):
    pass

if __name__ == "__main__":
    MyApp().run()