import pyautogui, time
time.sleep(10)
f = open("vefxistyaosani", 'r', encoding="utf-8")
for line in f:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
    time.sleep(0.1)
# 
#