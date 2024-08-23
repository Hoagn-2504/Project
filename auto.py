import pyautogui as pg
import time 
time.sleep(2)
pg.doubleClick((41, 734))
time.sleep(1)
pg.typewrite('https://web.telegram.org/a/')
time.sleep(1)
pg.press('enter')
time.sleep(2)
pg.leftClick(250,270)
time.sleep(2)
pg.leftClick(1070, 840)
time.sleep(4)
while True:
    for _ in range(1000):
        pos = pg.position(950, 700)    
        pg.doubleClick(pos)
        cr = pg.position()
        if cr != pos:
            break
    time.sleep(5)
    pos = pg.position(950, 780)
    pg.leftClick(pos)

    

