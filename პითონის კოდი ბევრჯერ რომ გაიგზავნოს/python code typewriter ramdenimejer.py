
import pyautogui
import time

i = 0

while i < 20:
    i += 1
    time.sleep(0.0001)
    pyautogui.typewrite("mec momenatre")
    time.sleep(0.0001)
    pyautogui.press('Enter')