import time
import pyautogui

def screenshot():
    name=int(round(time.time()*1000))
    name='C:/Users/naiks/Desktop/python projects/screenshot data/{}.png'.format(name)
    time.sleep(5)
    img= pyautogui.screenshot(name)
    img.show()

screenshot()