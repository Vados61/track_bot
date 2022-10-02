import keyboard
import pyautogui
import pyperclip
import time

delay = 2

time.sleep(delay)
with open('track_list.txt', 'rt', encoding='utf_8') as text:
    for line in text:
        pyperclip.copy(line)
        keyboard.press_and_release('ctrl + v')
        pyautogui.press('enter')
