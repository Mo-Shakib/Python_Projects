import pyautogui
import time
pyautogui.FAILSAFE = False
for i in range(10):
    time.sleep(3)
    pyautogui.press('j')
    # pyautogui.press('l')
    # pyautogui.press('tab')
    # pyautogui.press('enter')
print('Done')
