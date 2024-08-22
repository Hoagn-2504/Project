import pyautogui as pg
import time 
time.sleep(2)
pg.doubleClick((41, 734))
time.sleep(1)
pg.typewrite('https://web.telegram.org/a/')
time.sleep(2)
pg.press('enter')
time.sleep(2)
pg.leftClick(170,225)
time.sleep(2)
pg.leftClick(560, 860)
time.sleep(2)
while True:
    target_position = pg.position(500, 725)    
    pg.doubleClick(target_position)
    cr = pg.position()
    if cr != target_position :
        break

