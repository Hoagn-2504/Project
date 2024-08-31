import pyautogui as pg
import time 

time.sleep(2)
pg.hotkey('win', 'r')
time.sleep(1)
pg.write('chrome')
time.sleep(1)
pg.press('enter')
time.sleep(1)
pg.hotkey('alt', 'space')
time.sleep(1)
pg.press('x')
time.sleep(2)
pg.write('https://web.telegram.org/a/')
pg.press('enter')
time.sleep(2)
pg.leftClick(160,210)
time.sleep(2)
pg.leftClick(1070, 840)
time.sleep(4)
while True:
    for _ in range(2000):
        pos = pg.position(700, 600)    
        pg.doubleClick(pos)
        cr = pg.position()
        if cr != pos:
            break
    time.sleep(5)
    pos = pg.position(950, 780)
    pg.leftClick(pos)

    

