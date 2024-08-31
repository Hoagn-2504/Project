import pyautogui as pg
import time 

#Mở Chrome
time.sleep(2)
pg.hotkey('win', 'r')
time.sleep(1)
pg.write('chrome')
time.sleep(1)
pg.press('enter')
time.sleep(1)

#Chỉnh kích thước Chrome sang toàn màn hình nếu chưa full
pg.hotkey('alt', 'space')
time.sleep(1)
pg.press('x')
time.sleep(1)

#Đi đến trang Telegram
pg.typewrite('https://web.telegram.org/a/')
time.sleep(1)
pg.press('enter')
time.sleep(1)

#Mở berasig
pg.position(250,145)
time.sleep(1)
pg.doubleClick(250,145)
time.sleep(1)
pg.write('berasig bot')
time.sleep(1)
pg.press('enter')
time.sleep(1)
pg.leftClick(1070, 830)
time.sleep(5)

#Auto click
while True:
    for _ in range(2000):
        pos = pg.position(700, 600)    
        pg.doubleClick(pos)
        cr = pg.position()
        if cr != pos:
            break
    #Nhấn vào Done
    time.sleep(5)
    pos = pg.position(950, 780)
    pg.leftClick(pos)

    

