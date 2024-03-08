import pyautogui as pag
from time import sleep
import os
import shutil
import msdata as ms
import time
import img2str

path = "./screenshot/ReinforceCheck"+ time.strftime("_%m%d")
if not os.path.isdir(path):                                                           
    os.mkdir(path)

def ReinforceCheck():
    print("--------------------------------------------------------------")
    print("강화 TEST")
    print("ver 211102")        
    print("[1]아이템id입력    [2]텍스트파일")
    print("[0]돌아가기")
    print("---------------------------------------------------------------")
    num = int(ms.InputNum(2))
    ms.clear()
    if num==0:
        ms.TestMenu()
    elif num==1:
        Reinforce1()
    elif num==2:
        Reinforce2()
    
    ReinforceCheck()

def Reinforce1():

    itemNum = input("강화할 장비 id를 입력해주세요(안전강화 이상) // [0]뒤로 : ")
    if itemNum == "0" : 
        ReinforceCheck()

    count = int(input("테스트 횟수를 입력해주세요(1~) // [0]뒤로: "))
    if count == 0 : 
        ReinforceCheck()

    print("[1]무기 [2]방어구 [3]장신구 // [0]뒤로 : ")
    type0Num = int(ms.InputNum(3))
    if type0Num == 0 : 
        ReinforceCheck()

    print("[1]일반 [2]축복 [3]저주 [4]고대 // [0]뒤로 : ")
    type1Num = int(ms.InputNum(4))
    if type1Num == 0 : 
        ReinforceCheck()

    extraPath = path + "/"+ itemNum + time.strftime("_%H%M")
    if not os.path.isdir(extraPath):                                                           
        os.mkdir(extraPath) 
    else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
        shutil.rmtree(extraPath)                                                           
        os.mkdir(extraPath)  
    #try : 
    if count <= 0 :
            
        print("다시 입력해주세요.")
        Reinforce1()

    else :
        #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 3.2) +")")

        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.Command("additem 999 2000000000")
        
        if typeNum == 0 :
            ms.Command("additem 700 100000000")
        elif typeNum ==1 :
            ms.Command("additem 701 100000000")

        ms.Command("additem 999 2000000000")
        ms.Command("additem "+itemNum+" 1")
        ms.Move(ms.menuPos1)
        ms.Move(ms.invenBtnUp2)
        ms.Move(ms.invenBtn0)
        pag.click()
        ms.Move(ms.invenBtn0)

        txtName = path+"/"+str(itemNum)+"_"+str(count)+"EA"

        for i in range(0,count) :
            print(str(i+1) +"/" + str(count), end='\r')
            ms.Move(ms.engraveBtn)
            sleep(2)
            #if captureTypeNum == 0 :
            ms.CaptureEngraveRes(extraPath+"/"+str(i))
            if typeNum == 0 :
                img2str.Indiv_Engrave(txtName+"_0.txt",extraPath+"/"+str(i)+".jpg")
            elif typeNum ==1 :
                img2str.Indiv_Engrave(txtName+"_1.txt",extraPath+"/"+str(i)+".jpg")

            sleep(0.01)

    
        #print("다시 입력해주세요.")
    Engraving1()
        
def Engraving2():  
    print("--------------------------------------------------------------")
    print("※주의사항※")   
    print("실행 전 각인.txt에 아이템 아이디를 한 줄씩 입력해주세요.")   
    print("--------------------------------------------------------------")

    count = int(input("각인 테스트 횟수를 입력해주세요(1~) : "))
    print("[0]일반각인석 [1]축복각인석 : ")
    typeNum = int(ms.InputNum(2))
    # print("[0]한 화면 스크린샷 [1]전체 화면 스크린샷 : ")
    # captureTypeNum = int(ms.InputNum(1))

    with open("각인.txt") as f:
        lines = f.read().splitlines()

    for itemNum in lines:

#아이템 별 폴더 추가 생성
        #if folderCheck == 1:
        
        extraPath = path + "/"+ itemNum + time.strftime("_%H%M")
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
        else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
            shutil.rmtree(extraPath)                                                           
            os.mkdir(extraPath)  

        #try : 
        if count <= 0 :
                
            print("다시 입력해주세요.")
            Engraving2()

        else :
            print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 3.2) +")")
            #print("실행 중 입니다...(예상 소요 시간 : " + str(count * 1.5) + " 초)")

            ms.ResetFirst()
            ms.Command("cleanupinventory")

            
            if typeNum == 0 :
                ms.Command("additem 700 100000000")
            elif typeNum ==1 :
                ms.Command("additem 701 100000000")

            ms.Command("additem 999 2000000000")
            ms.Command("additem "+itemNum+" 1")
            ms.Move(ms.menuPos1)
            ms.Move(ms.invenBtnUp2)
            ms.Move(ms.invenBtn0)
            pag.click()
            ms.Move(ms.invenBtn0)

            txtName = path+"/"+str(itemNum)+"_"+str(count)+"EA"

            for i in range(0,count) :
                print(str(i+1) +"/" + str(count), end='\r')
                ms.Move(ms.engraveBtn)
                sleep(2)                
                #if captureTypeNum == 0 :
                ms.CaptureEngraveRes(extraPath+"/"+str(i))
                if typeNum == 0 :
                    img2str.Indiv_Engrave(txtName+"_0.txt",extraPath+"/"+str(i)+".jpg")
                elif typeNum ==1 :
                    img2str.Indiv_Engrave(txtName+"_1.txt",extraPath+"/"+str(i)+".jpg")
                # elif captureTypeNum ==1 : 
                #     ms.CaptureFull(extraPath+"/"+str(i))
                # sleep(0.01)
        
        # except : 
        #     print("다시 입력해주세요.")
    Engraving2()
