import pyautogui as pag
from time import sleep
import os
import func.msdata as ms
import time

def Resolution():
    global path

    path = "./screenshot/분해 결과"+ time.strftime("_%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)

    print("--------------------------------------------------------------")
    print("분해 TEST")
    print("ver 1.1 / 210608 / made by sms")        
    print("[1]아이템id입력    [2]텍스트파일")
    print("[0]돌아가기")
    print("---------------------------------------------------------------")
    num2 = int(ms.InputNum(2))
    ms.clear()
    if num2==0:
        ms.TestMenu()
    elif num2 ==1:
        Resolution1()
    elif num2 ==2:
        Resolution2()
    
    Resolution()

def Resolution1():

    waitTime = 0.2
    waitTime2 = 0.2
    itemNum = input("+0강 아이템 id를 입력해주세요([0]돌아가기) : ")
    while itemNum!="0":
        
        #아이템 별 폴더 추가 생성
        extraPath = path + "/"+ itemNum
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath) 
        
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        
        cmdStr= "additems"
        for j in range(0,14):
            cmdStr += " " + str(int(itemNum)+j)
        ms.Command(cmdStr,1)
        sleep(0.01)
        # ms.CommandOpen()
        # pag.typewrite("additems")
        # for j in range(0,14):
        #     pag.press('space')
        #     temp = int(itemNum)+j
        #     pag.typewrite(str(temp))
        # ms.CommandClose()

        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        ms.Move(ms.invenBtnDown1)
        sleep(ms.waitTime2)
        ms.Move(ms.invenBtnDown1)
        sleep(ms.waitTime2)
        ms.Move(ms.invenBtnDown2)
        sleep(ms.waitTime)
        ms.Move(ms.okPos)
        sleep(ms.waitTime)
        ms.Move(ms.okPos)

        sleep(1)
        ms.Capture(extraPath+"/분해결과_"+itemNum)

        itemNum = input("+0강 아이템 id를 입력해주세요([0]돌아가기) : ")
        
def Resolution2():    
    # print("--------------------------------------------------------------")
    # print("아이템 별 폴더를 생성하시겠습니까?")   
    # print("[0]생성 안함    [1]생성")
    # print("---------------------------------------------------------------")
    # folderCheck = int(ms.InputNum(1))
    # ms.clear()
    folderCheck = 0
    fileName = input("불러올 txt 파일명 입력해주세요([0]테스트메뉴) : ")
    if fileName == "" :
        fileName = "분해"

    waitTime = 0.01
    waitTime2 = 0.2
    
    with open(fileName +".txt") as f:
        lines = f.read().splitlines()

    for itemNum in lines:

#아이템 별 폴더 추가 생성
        if folderCheck == 1:
            extraPath = path + "/"+ itemNum
            if not os.path.isdir(extraPath):                                                           
                os.mkdir(extraPath)  
        
        ms.ResetFirst()
        ms.Command("cleanupinventory")

        
        cmdStr= "additems"
        for j in range(0,14):
            cmdStr += " " + str(int(itemNum)+j)
        ms.Command(cmdStr,1)
        sleep(0.01)
        # ms.CommandOpen()
        # pag.typewrite("additems")
        # for j in range(0,14):
        #     pag.press('space')
        #     temp = int(itemNum)+j
        #     pag.typewrite(str(temp))
        # ms.CommandClose()

        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        ms.Move(ms.invenBtnDown1)
        sleep(ms.waitTime2)
        ms.Move(ms.invenBtnDown1)
        sleep(ms.waitTime2)
        ms.Move(ms.invenBtnDown2)
        sleep(ms.waitTime)
        ms.Move(ms.okPos)
        sleep(ms.waitTime)
        ms.Move(ms.okPos)

        sleep(1)
        if folderCheck == 1:
            ms.Capture(extraPath+"/"+itemNum)
        else :
            ms.Capture(path+"/"+itemNum)

        #itemNum = input("+0강 아이템 id를 입력해주세요([0]돌아가기) : ")
        

if __name__ == "__main__" : 
    Resolution()