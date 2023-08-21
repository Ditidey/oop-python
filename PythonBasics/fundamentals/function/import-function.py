#you can use function from another files:

# one way
import fun
sum = fun.add(2, 3)

# another way
from fun import*
sum = add(4, 5)

# build in function
# pip install pyautogui
import pyautogui
import time
for i in range(1, 5):
    time.sleep(3)
    pyautogui.write('I love arghya!', interval=0.25)
    pyautogui.press('enter')
