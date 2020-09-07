import pyautogui
import time
pyautogui.FAILSAFE = False
for i in range(10):
    time.sleep()
    pyautogui.press('j')
    pyautogui.press('l')
    pyautogui.press('tab')
    pyautogui.press('enter')
print('Done')
