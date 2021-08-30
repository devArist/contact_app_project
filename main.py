from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy import properties as p


class ContactScreenManager(ScreenManager):
    screen_stack = []

    def push(self, screen_name):
        if not screen_name in self.screen_stack:
            self.screen_stack.append(self.current)
            self.transition.direction = 'left'
            self.current = screen_name

    def pop(self):
        if len(self.screen_stack) > 0:
            screen_name = self.screen_stack[-1]
            del self.screen_stack[-1]
            self.transition.direction = 'right'
            self.current = screen_name


class ContactApp(MDApp):
    manager = p.ObjectProperty(None)
    data = {
        "Django": "language-python",
        "Ruby on rails": 'language-ruby',
        "Laravel": 'language-php'
    }

    def build(self):
        self.manager = ContactScreenManager()
        return self.manager


ContactApp().run()