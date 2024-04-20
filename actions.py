
from ast import main
import pyautogui as pgui

def checar_status(name, delay, x, y, rgb, button_name):
    print(f'checando{name}...')
    pgui.sleep(delay)
    if pgui.pixelMatchesColor(x, y, rgb):
        pgui.press(button_name)

def check_battle():
    return pgui.locateOnScreen('img/battle-list.png', region=main.REGIAO_BATTLE)


