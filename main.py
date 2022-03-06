
from pynput.keyboard import Key, Controller
import time


src= "copy.txt"

auto_braces= [
    "{", 
    "(",
    "["
]

chars= []

with open(src) as file:
    for line in file:
        for char in line:
            chars.append(char)
file.close()



keyboard = Controller()

# keyboard.press(Key.alt)
# keyboard.press(Key.tab)
# keyboard.release(Key.tab)
# time.sleep(.2)
# keyboard.release(Key.alt)

time.sleep(4)

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
    time.sleep(.02)
