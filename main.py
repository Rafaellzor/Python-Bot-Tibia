from argparse import Action
from asyncio import constants
import actions
import pyautogui as pgui
import json
from pynput.keyboard import Listener
from pynput import keyboard
import threading

REGIAO_BATTLE = (1745, 457, 159, 44)

def matar_target():                 #selecionar o target
    while Action.check.battle() == None:
            print('matando')
            pgui.press('space')
            while pgui.locateOnScreen('img/alvo-selecionado.jpg', confidence=0.7)!= None: #target selecinado
                print('esperando matar')
            print('procurando target')

def pegar_loot():
    loot = pgui.locateAllOnScreen('img/regiao-loot.png', confidence=0.8, region=(767, 366, 211, 214))   #clicar loot
    for box in loot:
        x, y = pgui.center(box)
        pgui.moveTo(x , y)
        pgui.click(button="right")

def way_point(path, wait):
    bandeira = pgui.locateOnScreen(path, confidence=0.8, region= constants.REGION_MAP)
    if bandeira:
        x, y = pgui.center(bandeira)
        pgui.moveTo(x, y)
        pgui.click()
        pgui.sleep(wait)

pgui.displayMousePosition()                                         #checar mana/life
def checar_status(name, delay, x , y, rgb, nome_botao):
    print(f'checando{name}...')
    pgui.sleep(delay)
    if pgui.pixelMatchesColor(x, y , rgb):
        pgui.press(nome_botao)

def comer_food():                                                   #comer food
    pgui.press('TECLA')
    print('comando food')

checar_status('mana', 10, 878, 32, (0, 63, 140), 'F7')              #CASTAR MANA FULL
checar_status('vida', 1, 17, 35, (100, 145, 4), 'F2')               #castar cura

def rodar():
    event_th.is_set()
    with open(f'{constants.FOLDER_NAME}/infos.json', 'r') as file:
        data = json.loads(file.read())
        while not event_th.is_set():                                #enquanto n forpressionado
            for item in data:    
                matar_target(seconds: float) -> None
                pgui.sleep(1)
                pegar_loot()
                way_point()
            actions.comer_food()

        def key_code(key):
            print('key ->', key)
            if key == keyboard.Key.esc:
                return False
            if key == keyboard.key.delet:
                rodar()

global event_th                                                     #ser enchergada em todos os escopos
event_th = threading.Event()
th_run = threading.Thread(target=rodar)                             #rodar no segindo terminal

with Listener(on_press= key_code) as listener:
                listener.join()