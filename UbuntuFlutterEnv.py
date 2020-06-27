import pyautogui

print('Creating Android Development Environment... [ any errors are handled as exceptions and can are printed in this console')
pyautogui.sleep(7)

#.........................................................................................................................................................


list_of_apps = ['youtube music', 'whatsapp', 'github', 'gitkraken', 'firefox','files', 'android studio',
                'terminal',
                'microsoft edge']




def name_timer(nm):



    if nm == 'files':
        pyautogui.sleep(1)
        pyautogui.hotkey('ctrlleft', 'f')
        pyautogui.sleep(1)
        pyautogui.typewrite('FlutterAngela')
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(2)

    elif nm == 'whatsapp':
        pyautogui.sleep(3)

    elif nm == 'android studio':
        pyautogui.sleep(6)

    elif nm == 'terminal':
        pyautogui.sleep(2)
        pyautogui.typewrite('flutter emulator --launch pixel')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(12)

    else:
        pyautogui.sleep(2)



#............................................................................................................................................................


for name in list_of_apps:

    pyautogui.hotkey('winleft', 'pagedown')
    pyautogui.sleep(1)

    pyautogui.press('winleft')
    pyautogui.sleep(1)
    pyautogui.typewrite(name)

    pyautogui.sleep(1)
    pyautogui.press('enter')

    pyautogui.sleep(1)
    name_timer(name)

    # name_timer(name)

pyautogui.press('win')
pyautogui.sleep(1)
pyautogui.typewrite('gitkraken')

pyautogui.sleep(1)
pyautogui.press('enter')
