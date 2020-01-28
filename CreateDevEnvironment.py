import pyautogui

pyautogui.FAIL_SAFE = True
pyautogui.PAUSE = 1

# ..........................................................................................................

# After automatedesktop.py is clicked, program will run after 3 second delay. ( Just to bring human's focus )
pyautogui.sleep(1)

# ..........................................................................................................

# 1. Create 4 Virtual Desktops.
for i in range(3):
    pyautogui.hotkey('winleft', 'ctrlleft', 'd')
    pyautogui.sleep(.2)

# ..........................................................................................................

# 2. Press enter. Youtube Music will open up. APPS OPENED : 1
pyautogui.hotkey('winleft', '0')
pyautogui.sleep(6)

# ..........................................................................................................

# These 4 lines will open Windows Powershell using Keyboard shortcut Win + x + i
pyautogui.hotkey('winleft', 'ctrlleft', 'left')
pyautogui.hotkey('winleft', 'x')
pyautogui.press('i')

# On same virtual desktop, these lines will open Chrome Browser.
pyautogui.sleep(1)
pyautogui.hotkey('winleft', '4')
pyautogui.sleep(2)

# ..........................................................................................................

pyautogui.hotkey('winleft', 'ctrlleft', 'left')

# This will open PyCharm as it is located on 6th position on taskbar, counting from 1( One ) from left to right
# direction.
pyautogui.hotkey('winleft', '6')
pyautogui.sleep(14)

# ..........................................................................................................

# Will bring control to the original laptop
pyautogui.hotkey('winleft', 'ctrlleft', 'left')
