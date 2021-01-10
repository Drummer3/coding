from pynput import keyboard

word = 'abc'

def on_press(key):
    try:
        create_words(format(key.char))
    except AttributeError:
        create_words(format(key))


def create_words(symb):
    print(symb)    


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()