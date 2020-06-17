import pyautogui

# ..........................................................................................................

print('Closing ALL virtual environments !... [ Ctrl + C to abort]')

pyautogui.sleep(2)

for i in range(10):
    pyautogui.hotkey('winleft', 'ctrlleft', 'f4')
    pyautogui.sleep(.2)

# ..........................................................................................................


