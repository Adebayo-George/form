from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

Builder.load_file('form.kv')

class MyLayout(Widget):
    email_str = StringProperty()

    def submit(self):
        email_input = self.email_str      
        self.ids.update_label.text = f'Email: {email_input}'

class Form(App):
    def build(self):
        Window.size = (500, 400)
        return MyLayout()

if __name__ == "__main__":
    Form().run()
