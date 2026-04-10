import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

SERVER = "https://messenger-6n21.onrender.com"

class ChatApp(App):
    def build(self):
        self.name = "User"

        layout = BoxLayout(orientation='vertical')

        self.chat = Label(text="Чат...\n", size_hint_y=8)
        layout.add_widget(self.chat)

        self.input = TextInput(size_hint_y=1, multiline=False)
        layout.add_widget(self.input)

        send = Button(text="Отправить", size_hint_y=1)
        send.bind(on_press=self.send)
        layout.add_widget(send)

        Clock.schedule_interval(self.load, 2)

        return layout

    def send(self, instance):
        text = self.input.text
        if text:
            requests.post(SERVER + "/send", json={
                "name": self.name,
                "text": text
            })
            self.input.text = ""

    def load(self, dt):
        try:
            r = requests.get(SERVER + "/messages")
            msgs = r.json()

            self.chat.text = ""
            for m in msgs:
                self.chat.text += f"{m['name']}: {m['text']}\n"
        except:
            self.chat.text = "Ошибка сервера"

ChatApp().run()
