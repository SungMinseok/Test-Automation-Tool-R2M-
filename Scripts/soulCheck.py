import pyautogui as pag
from time import sleep
import os
import msdata as ms
import time
import random

path = "./screenshot/영혼부여 확률 확인"+ time.strftime("_%m%d")
if not os.path.isdir(path):                                                           
    os.mkdir(path)

nameText = "영혼부여 확률 확인 TEST"
verText = "ver 1.0"
dateText = "210705"
makerText = "made by sms"
desText = "  " + "+0~+13강 중 랜덤 수치의 장비를 10개 생성하여 100번 테스트 합니다."
warnText= "  " + "테스트 전 장착한 장비를 모두 해제하고, 인벤토리 내부 슬롯을 최상단으로 맞추세요."

def SetMainUI(_nameText,_verText,_dateText,_makerText):
    
    print("┌" + "┐".rjust(107,'─'))
    print("│" + _nameText.center(100) +"│")
    print("│" + "│".rjust(107,'─'))
    print("│" + (_verText + " / " + _dateText + " / " + _makerText).rjust(106) +"│")
    print("├" + "┤".rjust(107,'─'))

def SetSubUI(_desText,_warnText):
    
    print("│" + "※ 설명 ※".center(102) +"│")
    print("├" + "┤".rjust(107,'─'))
    print(_desText)
    print("├" + "┤".rjust(107,'─'))
    print("│" + "※ 사전세팅 ※".center(100) +"│")
    print("├" + "┤".rjust(107,'─'))
    print(_warnText)
    print("└" + "┘".rjust(107,'─'))

def SoulCheck():

    SetMainUI(nameText,verText,dateText,makerText)
    SetSubUI(desText,warnText)
    # print("┌" + "┐".rjust(107,'─'))
    # print("│" + nameText.center(100) +"│")
    # print("│" + "│".rjust(107,'─'))
    # print("│" + (verText + " / " + dateText + " / " + makerText).rjust(106) +"│")
    # print("├" + "┤".rjust(107,'─'))
    # print("│" + "※ 설명 ※".center(102) +"│")
    # print("├" + "┤".rjust(107,'─'))
    # print(desText)
    # print("├" + "┤".rjust(107,'─'))
    # print("│" + "※ 사전세팅 ※".center(100) +"│")
    # print("├" + "┤".rjust(107,'─'))
    # print(warnText)
    # print("└" + "┘".rjust(107,'─'))
    # print("┌" + "┐".rjust(107,'─'))
    # print(" 영혼석 ID를 입력해주세요.")
    # print(" [0]테스트메뉴")
    # print("└" + "┘".rjust(107,'─'))
    # #global equipType
    # #equipType = int(ms.InputNum(2))
    # ms.clear()
    # if equipType==0:
    #     ms.TestMenu()
    # else: 
    print("┌" + "┐".rjust(107,'─'))
    print("[1]아이템id입력    [2]텍스트파일")
    print("[0]돌아가기")
    print("└" + "┘".rjust(107,'─'))
    num2 = int(ms.InputNum(2))
    ms.clear()
    if num2==0:
        SoulCheck()
    elif num2 ==1:
        SoulCheck1()
    elif num2 ==2:
        SoulCheck2()
        # elif num2 ==2:
        #     EquipCheck2()

    SoulCheck()
        


def SoulCheck1():
   
    waitTime = 0.01
    waitTime2 = 0.2

    itemNum = input("영혼 부여 대상 아이템 ID(+0강)를 입력해주세요([0]테스트메뉴) : ")
    if num2==0:
        SoulCheck()
    while itemNum!="0":
        print("실행 중... (예상 소요 시간 : 알 수 없음)")
#아이템 별 폴더 추가 생성
        extraPath = path + "/"+ itemNum
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)        

#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.CommandOpen()
        pag.typewrite("additem ")
        #for j in range(0,14):
        #pag.press('space')
        j = random.randrange(0,14)
        temp = int(itemNum)+j
        pag.typewrite(str(temp))


        ms.CommandClose()
        sleep(0.01)
#인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        
        for i in range(0,14):
            if equipType == 2 and i == 10:
                break
    #첫번째 클릭 > 상세 클릭> 대기후스샷0> 
            # if i == 0 :
            #     ms.Move(ms.invenBtn0)
            # elif i == 1 :
            #     ms.Move(ms.invenBtn1)
            # elif i == 2 :
            #     ms.Move(ms.invenBtn2)
            # elif i == 3 :
            #     ms.Move(ms.invenBtn3)
            # elif i == 4 :
            #     ms.Move(ms.invenBtn4)
            # elif i == 5 :
            #     ms.Move(ms.invenBtn5)
            # elif i == 6 :
            #     ms.Move(ms.invenBtn6)
            # elif i == 7 :
            #     ms.Move(ms.invenBtn7)
            # elif i == 8 :
            #     ms.Move(ms.invenBtn8)
            # elif i == 9 :
            #     ms.Move(ms.invenBtn9)
            # elif i == 10 :
            #     ms.Move(ms.invenBtn10)
            # elif i == 11 :
            #     ms.Move(ms.invenBtn11)
            # elif i == 12 :
            #     ms.Move(ms.invenBtn12)
            # elif i == 13 :
            #     ms.Move(ms.invenBtn13)
                
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            ms.Move(ms.invenBtnDown2)
            sleep(0.2)
            ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_0")
    #설명창 위로밀기 > 대기 후 스샷1 > 
            ms.Move(ms.invenDesPos)
            ms.DragUp(ms.invenDesPos)
            ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_1")
    #추가정보클릭 > 대기후스샷2 > x버튼
            ms.Move(ms.invenAddDesPos)
            ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_2")
            ms.Move(ms.invenExitBtn)

            


        print("스샷 경로 : "+extraPath)
        itemNum = input("+0강 아이템 id를 입력해주세요([0]테스트메뉴) : ")

        

def SoulCheck2():
    print("--------------------------------------------------------------") 
    print("실행 전 영혼무기.txt에 아이템 ID, 영혼석.txt에 영혼석 ID를 한 줄씩 입력해주세요.")   
    print("--------------------------------------------------------------")

    count = int(input("영혼 부여 횟수를 입력해주세요(1~) : "))
    # fileName = input("불러올 txt 파일명 입력해주세요(기본 : 영혼무기)([0]돌아가기) : ")
    # if fileName =="0":
    #     SoulCheck()
    # try :
    #     with open(fileName +".txt") as f:
    #         lines = f.read().splitlines()
    #     f.close
    # except : 
    #     print("파일이 존재하지 않습니다.")
    #     SoulCheck2()


    # fileName_Soul = input("불러올 txt 파일명 입력해주세요(기본 : 영혼석)([0]돌아가기) : ")
    # if fileName_Soul =="0":
    #     SoulCheck()
    # try :
    #     with open(fileName_Soul +".txt") as f:
    #         lines_Soul = f.read().splitlines()
    #     f.close
    # except : 
    #     print("파일이 존재하지 않습니다.")
    #     SoulCheck2()
    

    with open("영혼무기.txt") as f1:
        itemLines = f1.read().splitlines()
    with open("영혼석.txt") as f2:
        scrollLines = f2.read().splitlines()


    for itemNum in itemLines:
        print("전체 실행횟수 : " + str(len(lines)))
        print("전체 예상 종료 시각 : " + str(ms.GetElapsedTime((10+count * 3.2 )* float(len(lines)))))



    loopCount = 1
    for itemNum in lines:
        print("실행 중... (예상 소요 시간 : 알 수 없음)")
        print(str(loopCount) + "/" + str(len(lines)))

#아이템 별 폴더 추가 생성
        #if folderCheck == 1 : 
        extraPath = path + "/"+ itemNum
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)       
        #elif folderCheck == 2 :
        #    extraPath = path 

            

#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.CommandOpen()
        pag.typewrite("additems")
        for j in range(0,14):
            pag.press('space')
            temp = int(itemNum)+j
            pag.typewrite(str(temp))
        ms.CommandClose()
        sleep(0.01)
#인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        
        for i in range(0,14):
            if equipType == 2 and i == 10:
                break
    #첫번째 클릭 > 상세 클릭> 대기후스샷0> 
            # if i == 0 :
            #     ms.Move(ms.invenBtn0)
            # elif i == 1 :
            #     ms.Move(ms.invenBtn1)
            # elif i == 2 :
            #     ms.Move(ms.invenBtn2)
            # elif i == 3 :
            #     ms.Move(ms.invenBtn3)
            # elif i == 4 :
            #     ms.Move(ms.invenBtn4)
            # elif i == 5 :
            #     ms.Move(ms.invenBtn5)
            # elif i == 6 :
            #     ms.Move(ms.invenBtn6)
            # elif i == 7 :
            #     ms.Move(ms.invenBtn7)
            # elif i == 8 :
            #     ms.Move(ms.invenBtn8)
            # elif i == 9 :
            #     ms.Move(ms.invenBtn9)
            # elif i == 10 :
            #     ms.Move(ms.invenBtn10)
            # elif i == 11 :
            #     ms.Move(ms.invenBtn11)
            # elif i == 12 :
            #     ms.Move(ms.invenBtn12)
            # elif i == 13 :
            #     ms.Move(ms.invenBtn13)
            
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            ms.Move(ms.invenBtnDown2)
            sleep(0.2)
            ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_0")
    #설명창 위로밀기 > 대기 후 스샷1 > 
            ms.Move(ms.invenDesPos)
            ms.DragUp(ms.invenDesPos)
            ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_1")
    #추가정보클릭 > 대기후스샷2 > x버튼
            ms.Move(ms.invenAddDesPos)
            ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_2")
            ms.Move(ms.invenExitBtn)

            
        print("스샷 경로 : "+extraPath)
        loopCount = loopCount +1
