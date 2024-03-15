import pyautogui as pag
import func.msdata as ms
from time import sleep


with open("appsize.txt") as f:
    appPos = f.read().splitlines()

appX = int(appPos[0])
appY = int(appPos[1])
appW = int(appPos[2])
appH = int(appPos[3])

try:
    while True:
        sleep(3)
        x,y = pag.position()
        print(round((x-appX)/appW,3), round((y-appY)/appH,3), x, y)


except KeyboardInterrupt:
    print("종료")