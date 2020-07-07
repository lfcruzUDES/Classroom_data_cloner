from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from fnMenu import FnMenu


class Main(BoxLayout):
    def show_info(self, action):
        try:
            result = action(auto_resp=True, quiet=True)
        except Exception as e:
            self.ids.work_status.text = e
        self.ids.work_status.text = result

    def get_subjects(self):
        self.ids.work_status.text = 'Obteniendo datos de las clases...'
        self.show_info(FnMenu.get_subjects)

    def get_info_files(self):
        self.ids.work_status.text = 'Obteniendo datos de los archivos...'
        self.show_info(FnMenu.get_info_files)

    def make_clones(self):
        self.ids.work_status.text = 'Clonando archivos...'
        self.show_info(FnMenu.make_clones)




class CCCApp(App):
    title = 'UDES Classroom Class Cloner'
    Window.size = 500, 800


if __name__ == '__main__':
    ClassCloner = CCCApp().run()
