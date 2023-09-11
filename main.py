import pyautogui
import time

time.sleep(20)
def cls():
    pyautogui.press('2')
    pyautogui.press('enter')
    pyautogui.keyDown('ctrl')
    pyautogui.press('right')
    pyautogui.keyUp('ctrl') 
    time.sleep(1.5)

for x in range(449):
    cls()


