import pyautogui
import delaySeconds
import winPressFun

def forFiles():

    pyautogui.hotkey('winleft', 'e')
    pyautogui.sleep(2)
    pyautogui.hotkey('ctrlleft', 'f')
    pyautogui.sleep(2)
    pyautogui.typewrite('FlutterLearn')
    delaySeconds.twoSecs()


def twoSecondDelay(termTwo):
    winPressFun.winButtonPress()
    pyautogui.typewrite(termTwo)
    delaySeconds.twoSecs()

def threeSecondDelay(threeSeconds):
    winPressFun.winButtonPress()
    pyautogui.typewrite(threeSeconds)
    delaySeconds.threeSecs()

def sixSecondDelay(appSix):
    winPressFun.winButtonPress()
    pyautogui.typewrite(appSix)
    delaySeconds.sixSecs()

def forEmulator(commandString):

    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl', 'alt', 't')
    pyautogui.sleep(2)
    pyautogui.typewrite(commandString)
    delaySeconds.twelveSecs()


def forGpuStatistics(commandString):

    pyautogui.sleep(2)
    pyautogui.hotkey('ctrl', 'alt', 't')
    pyautogui.sleep(2)
    pyautogui.typewrite(commandString)
    delaySeconds.twoSecs()

def forSystemMonitor():
    winPressFun.winButtonPress()
    pyautogui.typewrite('System Monitor')
    delaySeconds.twoSecs()