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
time.sleep(2)

#Đi đến trang Telegram
pg.typewrite('https://web.telegram.org/a/')
time.sleep(1)
pg.press('enter')
time.sleep(2)

#Mở berasig (app Berasig được ghim lên đầu)
pg.leftClick(160,210)
time.sleep(2)
pg.leftClick(1070, 830)
time.sleep(4)
while True:
    #Auto click
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

    

