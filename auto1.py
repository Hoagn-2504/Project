import pyautogui as pg
import time 

while True:
    # pos = pg.position(1715, 750)    #dejen dogs
    pos = pg.position(1600, 580)    #ton
    pg.doubleClick(pos)
    cr = pg.position()
    if cr != pos:
        break