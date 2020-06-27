import pyperclip
from pynput import keyboard
from client import Client

class Listener:
    def __init__(self):
        self.client = Client()
        self.current = set()
        self.combinations = [
            {keyboard.Key.shift, keyboard.KeyCode(char='v')},
            {keyboard.Key.shift, keyboard.KeyCode(char='V')}
        ]


    def get_flashcard(self):
        clipboard_content = pyperclip.paste()
        return str(clipboard_content)
    
    def translate(self):
        phrase = self.get_flashcard()
        self.client.translate(phrase)

    def on_press(self, key):
        if any([key in COMBO for COMBO in self.combinations]):
            self.current.add(key)
        if any(all(k in self.current for k in COMBO) for COMBO in self.combinations):
            self.translate()

    def on_release(self, key):
        if any([key in COMBO for COMBO in self.combinations]):
            self.current.remove(key)

    def listen(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


if __name__ == '__main__':
    listener = Listener()
    listener.listen()
