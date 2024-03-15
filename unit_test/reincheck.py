import pyautogui as pag
from time import sleep
import os
import func.msdata as ms
import time


def ReinCheck():
    global path

    path = "./screenshot/강화 확인"+ time.strftime("_%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
        
    print("--------------------------------------------------------------")
    print("강화 확인 TEST")
    print("ver 1.0 / 210608 / made by sms")
    print("---------------------------------------------------------------")
    print("※테스트 전 인벤토리를 완전히 비워주세요.※")
    print("\n설명:모든 강화 수치에 대해 주문서 등록 가능 여부 스샷, +9강 다중강화 실행")
    print("\n생성할 장비 타입을 선택해주세요.")
    print("[1]무기(+13강)    [2]방어구(+13강)   [3]장신구(+9강)")
    print("[0]테스트메뉴")
    print("---------------------------------------------------------------")

    global equipType
    equipType = int(ms.InputNum(3))
    ms.clear()
    if equipType==0:
        ms.TestMenu()
    else: 
        print("---------------------------------------------------------------")
        print("[1]아이템id입력    [2]텍스트파일")
        print("[0]돌아가기")
        print("---------------------------------------------------------------")
        num2 = int(ms.InputNum(2))
        ms.clear()
        if num2==0:
            ReinCheck()
        elif num2 ==1:
            EquipCheck1()
        elif num2 ==2:
            EquipCheck2()
        
        ReinCheck()
        


def EquipCheck1():
   
    waitTime = 0.01
    waitTime2 = 0.2

    itemNum = input("+0강 아이템 id를 입력해주세요([0]테스트메뉴) : ")
    while itemNum!="0":

#아이템 별 폴더 추가 생성
        extraPath = path + "/"+ itemNum
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)        

#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.Command("additem 999 1000000")
        if equipType == 1 :
            ms.Command("additems 300 310 320 330 910140 910143")
        elif equipType == 2 :
            ms.Command("additems 301 311 321 331 910141 910144")
        elif equipType == 3 :
            ms.Command("additems 302 312 322 332 910142 910145")
        # ms.Command("additem 300 100")
        # ms.Command("additem 310 100")
        # ms.Command("additem 320 100")
        # ms.Command("additem 330 100")
        # ms.Command("additem 910140 100")
        # ms.Command("additem 910143 100")
        ms.CommandOpen()
        pag.typewrite("additems")
        for j in range(0,14):
            if equipType == 3 and j == 10:
                break
            pag.press('space')
            temp = int(itemNum)+j
            pag.typewrite(str(temp))


        ms.CommandClose()
        sleep(0.01)
        #인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        #강화UI 오픈
        ms.Move(ms.invenBtnRein)
        sleep(0.2)
        #주문서탭클릭>주문서0클릭>장비탭클릭>스샷
        for i in range(0,6):
            
            ms.Move(ms.invenReinBtnUp1)
            if i == 0 :
                ms.Move(ms.invenBtn0)
            elif i == 1 :
                ms.Move(ms.invenBtn1)
            elif i == 2 :
                ms.Move(ms.invenBtn2)
            elif i == 3 :
                ms.Move(ms.invenBtn3)
            elif i == 4 :
                ms.Move(ms.invenBtn4)
            elif i == 5 :
                ms.Move(ms.invenBtn5)

            ms.Move(ms.invenReinBtnUp0)
            sleep(0.05)

            if i == 0 :
                ms.Capture(extraPath+"/"+itemNum+"_일반")
            elif i == 1 :
                ms.Capture(extraPath+"/"+itemNum+"_축복")
            elif i == 2 :
                ms.Capture(extraPath+"/"+itemNum+"_저주")
            elif i == 3 :
                ms.Capture(extraPath+"/"+itemNum+"_고대")
            elif i == 4 :
                ms.Capture(extraPath+"/"+itemNum+"_일반[이벤트]")
            elif i == 5 :
                ms.Capture(extraPath+"/"+itemNum+"_축복[이벤트]")

        #다중강화 테스트
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.Command("additem 999 1000000")
        ms.Command("additem "+itemNum+" 16")        
        if equipType == 1 :
            ms.Command("additem 300 144")
        elif equipType == 2 :
            ms.Command("additem 301 144")
        elif equipType == 3 :
            ms.Command("additem 302 144")
        #인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        #강화UI 오픈
        ms.Move(ms.invenBtnRein)
        sleep(0.2)
        ms.Move(ms.invenReinBtnLeft1)
        ms.Move(ms.invenReinBtnUp1)
        ms.Move(ms.invenBtn0)
        ms.Move(ms.invenReinBtnUp0)
        ms.Move(ms.invenBtn0)
        ms.Move(ms.invenBtn1)
        ms.Move(ms.invenBtn2)
        ms.Move(ms.invenBtn3)
        ms.Move(ms.invenBtn4)
        ms.Move(ms.invenBtn5)
        ms.Move(ms.invenBtn6)
        ms.Move(ms.invenBtn7)
        ms.Move(ms.invenBtn8)
        ms.Move(ms.invenBtn9)
        ms.Move(ms.invenBtn10)
        ms.Move(ms.invenBtn11)
        ms.Move(ms.invenBtn12)
        ms.Move(ms.invenBtn13)
        ms.Move(ms.invenBtn14)
        ms.Move(ms.invenBtn15)
        ms.Move(ms.invenReinBtn9)
        ms.Move(ms.invenReinBtnDown2)
        itemNum = input("+0강 아이템 id를 입력해주세요([0]테스트메뉴) : ")

        

def EquipCheck2():
    print("--------------------------------------------------------------")
    print("※주의사항※")   
    print("실행 전 강화.txt에 아이템 아이디를 한 줄씩 입력해주세요.")   
    print("--------------------------------------------------------------")

    with open("강화.txt") as f:
        lines = f.read().splitlines()

    for itemNum in lines:        
        extraPath = path + "/"+ itemNum
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.Command("additem 999 1000000")
        if equipType == 1 :
            ms.Command("additems 300 310 320 330 910140 910143")
        elif equipType == 2 :
            ms.Command("additems 301 311 321 331 910141 910144")
        elif equipType == 3 :
            ms.Command("additems 302 312 322 332 910142 910145")
        # ms.Command("additem 300 100")
        # ms.Command("additem 310 100")
        # ms.Command("additem 320 100")
        # ms.Command("additem 330 100")
        # ms.Command("additem 910140 100")
        # ms.Command("additem 910143 100")
        ms.CommandOpen()
        pag.typewrite("additems")
        for j in range(0,14):
            if equipType == 3 and j == 10:
                break
            pag.press('space')
            temp = int(itemNum)+j
            pag.typewrite(str(temp))


        ms.CommandClose()
        sleep(0.01)
        #인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        #강화UI 오픈
        ms.Move(ms.invenBtnRein)
        sleep(0.2)
        #주문서탭클릭>주문서0클릭>장비탭클릭>스샷
        for i in range(0,6):
            
            ms.Move(ms.invenReinBtnUp1)
            if i == 0 :
                ms.Move(ms.invenBtn0)
            elif i == 1 :
                ms.Move(ms.invenBtn1)
            elif i == 2 :
                ms.Move(ms.invenBtn2)
            elif i == 3 :
                ms.Move(ms.invenBtn3)
            elif i == 4 :
                ms.Move(ms.invenBtn4)
            elif i == 5 :
                ms.Move(ms.invenBtn5)

            ms.Move(ms.invenReinBtnUp0)
            sleep(0.05)

            if i == 0 :
                ms.Capture(extraPath+"/"+itemNum+"_일반")
            elif i == 1 :
                ms.Capture(extraPath+"/"+itemNum+"_축복")
            elif i == 2 :
                ms.Capture(extraPath+"/"+itemNum+"_저주")
            elif i == 3 :
                ms.Capture(extraPath+"/"+itemNum+"_고대")
            elif i == 4 :
                ms.Capture(extraPath+"/"+itemNum+"_일반[이벤트]")
            elif i == 5 :
                ms.Capture(extraPath+"/"+itemNum+"_축복[이벤트]")

        #다중강화 테스트
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.Command("additem 999 1000000")
        ms.Command("additem "+itemNum+" 16")        
        if equipType == 1 :
            ms.Command("additem 300 144")
        elif equipType == 2 :
            ms.Command("additem 301 144")
        elif equipType == 3 :
            ms.Command("additem 302 144")
        #인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        #강화UI 오픈
        ms.Move(ms.invenBtnRein)
        sleep(0.2)
        ms.Move(ms.invenReinBtnLeft1)
        ms.Move(ms.invenReinBtnUp1)
        ms.Move(ms.invenBtn0)
        ms.Move(ms.invenReinBtnUp0)
        ms.Move(ms.invenBtn0)
        ms.Move(ms.invenBtn1)
        ms.Move(ms.invenBtn2)
        ms.Move(ms.invenBtn3)
        ms.Move(ms.invenBtn4)
        ms.Move(ms.invenBtn5)
        ms.Move(ms.invenBtn6)
        ms.Move(ms.invenBtn7)
        ms.Move(ms.invenBtn8)
        ms.Move(ms.invenBtn9)
        ms.Move(ms.invenBtn10)
        ms.Move(ms.invenBtn11)
        ms.Move(ms.invenBtn12)
        ms.Move(ms.invenBtn13)
        ms.Move(ms.invenBtn14)
        ms.Move(ms.invenBtn15)
        ms.Move(ms.invenReinBtn9)
        ms.Move(ms.invenReinBtnDown2)
        sleep(11)
        ms.Capture(extraPath+"/"+itemNum+"_다중강화")
#아이템 별 폴더 추가 생성
        #if folderCheck == 1:
        # extraPath = path + "/"+ itemNum
        # if not os.path.isdir(extraPath):                                                           
        #     os.mkdir(extraPath)  
#     fileName = input("불러올 txt 파일명 입력해주세요([0]테스트메뉴) : ")

#     waitTime = 0.01
#     waitTime2 = 0.2
    
#     with open(fileName +".txt") as f:
#         lines = f.read().splitlines()


#     #while itemNum!="0":
    
#     for itemNum in lines:
#         #ms.Command(line)

# #아이템 별 폴더 추가 생성
#         extraPath = path + "/"+ itemNum
#         if not os.path.isdir(extraPath):                                                           
#             os.mkdir(extraPath)        

# #장비생성
#         ms.ResetFirst()
#         ms.Command("cleanupinventory")
#         ms.CommandOpen()
#         pag.typewrite("additems")
#         for j in range(0,14):
#             pag.press('space')
#             temp = int(itemNum)+j
#             pag.typewrite(str(temp))
#         ms.CommandClose()
#         sleep(0.01)
# #인벤열기 >
#         ms.Move(ms.menuPos1)
#         sleep(ms.waitTime)
        
#         for i in range(0,14):
#     #첫번째 클릭 > 상세 클릭> 대기후스샷0> 
#             if i == 0 :
#                 ms.Move(ms.invenBtn0)
#             elif i == 1 :
#                 ms.Move(ms.invenBtn1)
#             elif i == 2 :
#                 ms.Move(ms.invenBtn2)
#             elif i == 3 :
#                 ms.Move(ms.invenBtn3)
#             elif i == 4 :
#                 ms.Move(ms.invenBtn4)
#             elif i == 5 :
#                 ms.Move(ms.invenBtn5)
#             elif i == 6 :
#                 ms.Move(ms.invenBtn6)
#             elif i == 7 :
#                 ms.Move(ms.invenBtn7)
#             elif i == 8 :
#                 ms.Move(ms.invenBtn8)
#             elif i == 9 :
#                 ms.Move(ms.invenBtn9)
#             elif i == 10 :
#                 ms.Move(ms.invenBtn10)
#             elif i == 11 :
#                 ms.Move(ms.invenBtn11)
#             elif i == 12 :
#                 ms.Move(ms.invenBtn12)
#             elif i == 13 :
#                 ms.Move(ms.invenBtn13)
#             ms.Move(ms.invenBtnDown2)
#             sleep(0.2)
#             ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_0")
#     #설명창 위로밀기 > 대기 후 스샷1 > 
#             ms.Move(ms.invenDesPos)
#             ms.DragUp(ms.invenDesPos)
#             ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_1")
#     #추가정보클릭 > 대기후스샷2 > x버튼
#             ms.Move(ms.invenAddDesPos)
#             ms.Capture(extraPath+"/"+str(int(itemNum)+i)+"_2")
#             ms.Move(ms.invenExitBtn)

#     #ㅇ