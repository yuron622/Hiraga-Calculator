import japanize_kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty




class TextWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)

        self.text = ''
        self.hasdot = 0
        self.mode = 0
        self.number1 = 0

    def buttonClickedc(self):
        self.text = ''
        self.hasdot = 0
        self.mode = 0
    def buttonClicked1(self):
        self.text += '1'

    def buttonClicked2(self):
        self.text += '2'

    def buttonClicked3(self):
        self.text += '3'

    def buttonClicked4(self):
        self.text += '4'

    def buttonClicked5(self):
        self.text += '5'
    def buttonClicked6(self):
        self.text += '6'

    def buttonClicked7(self):
        self.text += '7'

    def buttonClicked8(self):
        self.text += '8'

    def buttonClicked9(self):
        self.text += '9'

    def buttonClicked0(self):
        if self.text != '0':
            self.text += '0'

    def buttonClickeddot(self):
        if self.hasdot == 0:
            self.text += '.'
            self.hasdot = 1
    def buttonClickedplus(self):
        self.mode = 1
        self.number1 = float(self.text)
        self.text = ''
        self.hasdot = 0
    def buttonClickedminus(self):
        self.mode = 2
        self.number1 = float(self.text)
        self.text = ''
        self.hasdot = 0
    def buttonClickedtimes(self):
        self.mode = 3
        self.number1 = float(self.text)
        self.text = ''
        self.hasdot = 0
    def buttonClickeddivide(self):
        self.mode = 4
        self.number1 = float(self.text)
        self.text = ''
        self.hasdot = 0
    def buttonClickedequal(self):
        try:
            if self.mode == 1:
                self.text = str(self.number1 + float(self.text))
            if self.mode == 2:
                self.text = str(self.number1 - float(self.text))
            if self.mode == 3:
                self.text = str(self.number1 * float(self.text))
            if self.mode == 4:
                try:
                    self.text = str(self.number1 / float(self.text))
                except ZeroDivisionError:
                    self.text = 'ぜろではわれないよ！'
        except ValueError:
            self.text = 'すうじしかけいさんできないよ！'


class AiuApp(App):
    def __init__(self, **kwargs):
        super(AiuApp, self).__init__(**kwargs)
        self.title = 'Calculator'

    def build(self):
        return TextWidget()

if __name__ == '__main__':
    AiuApp().run()