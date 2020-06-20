from pynput import keyboard

class Listener:
    def __init__(self):
        self.current = set()
        self.combinations = [
            {keyboard.Key.shift, keyboard.KeyCode(char='v')},
            {keyboard.Key.shift, keyboard.KeyCode(char='V')}
        ]


    def get_flashcard(self):
        print("TEST SCRIPT")

    def on_press(self, key):
        if any([key in COMBO for COMBO in self.combinations]):
            self.current.add(key)
        if any(all(k in self.current for k in COMBO) for COMBO in self.combinations):
            self.get_flashcard()

    def on_release(self, key):
        if any([key in COMBO for COMBO in self.combinations]):
            self.current.remove(key)

    def listen(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
