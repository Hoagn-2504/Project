import pyautogui as pg
import time 
time.sleep(2)
pg.doubleClick((41, 734))
time.sleep(1)
pg.typewrite('https://web.telegram.org/a/')
time.sleep(1)
pg.press('enter')
time.sleep(2)
pg.leftClick(270,350)
time.sleep(2)
pg.leftClick(360, 795)
time.sleep(4)
while True:
    for _ in range(1000):
        pos = pg.position(470, 750)    
        pg.doubleClick(pos)
    time.sleep(5)
    pos = pg.position(470, 800)
    pg.leftClick(pos)
    

