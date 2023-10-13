from typing import Set
from numpy import select
import pyautogui as pag
from time import sleep
#from msdata import Player
import msdata as ms
import os


def SetAppSize():
    ms.PrintUB()
    print("※앱 크기&위치 설정")
    ms.PrintUB()
    print("[1]새로 설정하기\n[2]설정 불러오기\n[3]설정값 확인")
    ms.PrintUB()
    print("[0]메인메뉴")
    ms.PrintUB()
    selectedNum = int(ms.InputNum(2))
    ms.clear()
    if selectedNum==0:
        ms.MainMenu
    elif selectedNum==1:
        ResetAppSize()
    elif selectedNum==2:
        SetAppSize_Set()
    
    ms.ResetAppSize211214()

def ResetAppSize():
    ms.PrintUB()
    print("※마우스 포인터를 앱플레이어의 [좌측 상단 모서리]에 위치시켜주세요(5초)")
    sleep(5)
    
    appX1, temp = pag.position()
    appY1 = temp + 30

    print("※마우스 포인터를 앱플레이어의 [하단 끝]에 위치시켜주세요(5초)")
    sleep(5)
    appX2, appY2 = pag.position()

    appHeight = appY2 - appY1
    #appWidth = round(appHeight * 1.773)
    appWidth = round(appHeight * 1.773)
    #appWidth = round(appHeight * 1.754)

    print("앱 크기 설정 완료 : ", appWidth,", ",appHeight)
    with open("info_appsize.txt",'w',encoding='utf-8') as f:
        f.write("0")
    f.close()
    sleep(2)
    #print("설정 완료되었습니다. 종료하려면 엔터, 다시 설정하려면 1 입력해주세요...")

    f = open("appsize.txt", 'w')

    f.write(str(appX1))
    f.write('\n')
    f.write(str(appY1))
    f.write('\n')
    f.write(str(appWidth))
    f.write('\n')
    f.write(str(appHeight))

    f.close()

    ms.appX = int(appX1)
    ms.appY = int(appY1)
    ms.appW = int(appWidth)
    ms.appH = int(appHeight)

def applyNewAppSize(x0,y0,x1,y1):
    
    if ms.currentPlayer == ms.Player.Mirroid :
        x = int(x0) + 145
        y = int(y0) + 33
        h = int(y1) - y
        #w = round(h * 1.773)
        w = round(h * 1.763348)

        # f = open("info_appsize.txt", 'w')
        # f.write("0")
        # f.close()

        # f = open("appsize.txt", 'w')
        # f.write(str(x)+'\n'+str(y)+'\n'+str(w)+'\n'+str(h))
        # f.close()

        ms.appX = int(x)
        ms.appY = int(y)
        ms.appW = int(w)
        ms.appH = int(h)
    elif ms.currentPlayer == ms.Player.LDPlayer :
        
        x = int(x0)
        #y = int(y0) + 30
        y = int(y0) + 33
        h = int(y1) - y
        #w = round(h * 1.773)
        w = round(h * 1.77382)

        ms.appX = int(x)
        ms.appY = int(y)
        ms.appW = int(w)
        ms.appH = int(h)

    return x,y,w,h

def getCurAppSize():

    return ms.appX,ms.appY,ms.appW,ms.appH

def getRatio(x,y):
    return round((x-ms.appX)/ms.appW,4), round((y-ms.appY)/ms.appH,4)

def SetAppSize_Set():
    ms.clear()

    ms.PrintUB()
    print("※세팅 번호 N을 입력해주세요.")
    print("(폴더 내 appsize_N.txt)")
    ms.PrintUB()
    print("[0]메인메뉴")
    ms.PrintUB()
    
    setNum = int(ms.InputNum(999))
    tempFileName = "appsize_"+str(setNum)+".txt"
    
    if setNum == 0 :
        ms.MainMenu()

    while not os.path.isfile(tempFileName) :
        print("Error : 해당 번호의 세팅이 없습니다.")
        setNum = int(ms.InputNum(999))
        tempFileName = "appsize_"+str(setNum)+".txt"



    if setNum == 0 :
        ms.MainMenu()

    tempFileName = "appsize_"+str(setNum)+".txt"
    if os.path.isfile(tempFileName) :
        
        with open(tempFileName) as f:
            appPos = f.read().splitlines()

        ms.appX = int(appPos[0])
        ms.appY = int(appPos[1])
        ms.appW = int(appPos[2])
        ms.appH = int(appPos[3])
        
        print("※앱 크기 설정 완료 : ", appPos[0], appPos[1], appPos[2],appPos[3])
        
        with open("info_appsize.txt",'w',encoding='utf-8') as f:
            f.write(str(setNum))
        f.close()
        sleep(1)
        
        #ms.MainMenu()
    else :
        print("Error : 해당 번호의 세팅이 없습니다.")
        SetAppSize_Set()
