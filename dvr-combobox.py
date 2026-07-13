import time
import threading
import pyautogui
from pynput import keyboard

pyautogui.PAUSE = 0

pressed = set()

def perform_action(direction):
    time.sleep(0.01)
    pyautogui.keyUp('shift')
    time.sleep(0.01)
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.press(direction)
    time.sleep(0.01)
    pyautogui.press('enter')
    time.sleep(0.01)
    pyautogui.keyDown('shift')

def on_press(key):
    pressed.add(key)
    shift = keyboard.Key.shift in pressed or keyboard.Key.shift_l in pressed or keyboard.Key.shift_r in pressed

    if shift and key == keyboard.Key.up:
        threading.Thread(target=perform_action, args=('up',), daemon=True).start()
    elif shift and key == keyboard.Key.down:
        threading.Thread(target=perform_action, args=('down',), daemon=True).start()

def on_release(key):
    pressed.discard(key)

print("Hold shift, press up or down multiple times...")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()