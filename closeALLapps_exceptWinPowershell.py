import pyautogui


pyautogui.sleep(2)

for x in range(30):
    pyautogui.sleep(.2)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(.2)
    pyautogui.hotkey('alt', 'f4')

# ..........................................................................................................
