import pyautogui # package - 1
import time # package -2
count = 0
while count < 500:
    time.sleep(0.5) # delay time
    pyautogui.typewrite('hi') # write the message here
    time.sleep(0.3)
    pyautogui.press('enter') # the key will press
    count += 1
    