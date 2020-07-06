from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RootWidget(BoxLayout):
    pass

class CCC(App):
    title = 'UDES Classroom Class Cloner'
    # Window.size = 530, 600

    def build(self):
        layout = BoxLayout()

        return layout


if __name__ == '__main__':
    CCC().run()
