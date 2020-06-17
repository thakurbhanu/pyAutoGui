import pyautogui

list_of_apps = ['youtube music', 'whatsapp', 'github', 'brave', 'file explorer', 'android studio', 'windows terminal',
                'microsoft edge']


def name_timer(nm):
    if nm == 'file explorer':
        pyautogui.sleep(.5)
        pyautogui.hotkey('altleft', 'd')
        pyautogui.sleep(.5)
        pyautogui.typewrite('E:')
        pyautogui.sleep(.5)
        pyautogui.press('enter')
        pyautogui.sleep(2)

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
