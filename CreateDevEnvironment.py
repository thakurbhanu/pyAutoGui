import pyautogui

print('Creating Android Development Environment... [ any errors are handled as exceptions and can are printed in this console')
pyautogui.sleep(7)

#.........................................................................................................................................................


list_of_apps = ['youtube music', 'whatsapp', 'github desktop', 'firefox','file explorer', 'android studio', 'windows terminal',
                'microsoft edge']


def name_timer(nm):



    if nm == 'file explorer':
        pyautogui.sleep(1)
        pyautogui.hotkey('altleft', 'd')
        pyautogui.sleep(1)
        pyautogui.typewrite('E:')
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(2)

    elif nm == 'whatsapp':
        pyautogui.sleep(3)

    elif nm == 'android studio':
        pyautogui.sleep(6)

    elif nm == 'windows terminal':
        pyautogui.sleep(2)
        pyautogui.typewrite('flutter emulator --launch pixel')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(12)

    else:
        pyautogui.sleep(2)



#............................................................................................................................................................


for name in list_of_apps:

    pyautogui.hotkey('winleft', 'ctrlleft', 'd')
    pyautogui.sleep(1)

    pyautogui.press('win')
    pyautogui.sleep(1)
    pyautogui.typewrite(name)

    pyautogui.sleep(1)
    pyautogui.press('enter')

    pyautogui.sleep(1)
    name_timer(name)

    # name_timer(name)

pyautogui.press('win')
pyautogui.sleep(1)
pyautogui.typewrite('github')

pyautogui.sleep(1)
pyautogui.press('enter')
