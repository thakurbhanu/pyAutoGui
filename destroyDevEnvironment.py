import pyautogui

# ..........................................................................................................

print('Closing ALL virtual environments !... [ Ctrl + C to abort]')

pyautogui.sleep(2)

for i in range(10):
    pyautogui.hotkey('winleft', 'ctrlleft', 'f4')
    pyautogui.sleep(.2)

# ..........................................................................................................



print('Closing ALL applications EXCEPT this window !... [ may not work xd]')

pyautogui.sleep(2)

for x in range(15):
    pyautogui.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.sleep(1)
    pyautogui.hotkey('alt', 'f4')

# ..........................................................................................................
