import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOOGLE_KEY = KeyCode(char="l")
#można tutaj zmienić klawisz pod którym włącza się klikanie ponieważ program działa przez cały czas
#jeżeli chce się całkowicie wyłączyć cały program należy "kill terminal"
klilkanie = False
myszka = Controller()

def klik():
    while True:
        if klilkanie:
            myszka.click(Button.left, 1)
        time.sleep(0.01)

def toggle_event(key):
    if key == TOOGLE_KEY:
        global klilkanie
        klilkanie = not klilkanie

click_thread = threading.Thread(target=klik)
click_thread.start()

with Listener(on_press = toggle_event) as listener:
    listener.join()