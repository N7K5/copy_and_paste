
from pynput.keyboard import Key, Controller
import time

import web

link= "https://raw.githubusercontent.com/N7K5/copy_and_paste/main/copy.txt"

src= "copy.txt"

auto_braces= [
    "{", 
    "(",
    "["
]






keyboard = Controller()

# keyboard.press(Key.alt)
# keyboard.press(Key.tab)
# keyboard.release(Key.tab)
# time.sleep(.2)
# keyboard.release(Key.alt)

time.sleep(3)


def main():
    chars= web.web_to_chars(link)

    for c in chars:
        if c=="\t":
            keyboard.press(Key.space)
            keyboard.release(Key.space)
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif c=="\n":
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        elif c in auto_braces:
            keyboard.press(c)
            keyboard.release(c)
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        else:
            keyboard.press(c)
            keyboard.release(c)
        time.sleep(.01)


main()