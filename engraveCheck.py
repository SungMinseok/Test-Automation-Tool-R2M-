import pyautogui as pag
from time import sleep
import os
import shutil
import msdata as ms
import time
import img2str
import pandas as pd

langCode = ""


def EngraveCheck():
    global path
    path = "./screenshot/EngraveCheck"+ time.strftime("_%y%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)


    #print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    ms.PrintUB()
    print("각인 TEST")
    ms.PrintUB()
    #print("ver 1.0 / 210615")        
    print("[1]아이템id입력\n[2]텍스트파일\n[3]능력치찾기\n[4]능력치찾기(라이브)")
    print("[0]돌아가기")
    ms.PrintUB()
    num = int(ms.InputNum(4))
    ms.clear()
    if num==0:
        ms.TestMenu()
    elif num==1:
        Engraving1()
    elif num==2:
        Engraving2()
    elif num==3:
        Engraving3()
    elif num==4:
        Engraving4()
    
    EngraveCheck()

def Engraving1():

    itemNum = input("아이템 id를 입력해주세요([0]돌아가기) : ")
    if itemNum == "0" : 
        EngraveCheck()

    count = int(input("각인 테스트 횟수를 입력해주세요(1~) : "))
    print("[0]일반각인석 [1]축복각인석 : ")
    typeNum = int(ms.InputNum(1))

    extraPath = path + "/"+ itemNum + time.strftime("_%H%M")
    if not os.path.isdir(extraPath):                                                           
        os.mkdir(extraPath) 
    else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
        shutil.rmtree(extraPath)                                                           
        os.mkdir(extraPath)  
    #try : 
    if count <= 0 :
            
        print("다시 입력해주세요.")
        Engraving1()

    else :
        print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 3.2) +")")

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

            sleep(0.01)

    
        #print("다시 입력해주세요.")
    Engraving1()
        
def Engraving2():  
    
    targetTxtFileName = f'각인.txt'
    
    print(f'{targetTxtFileName=}')   
    count = int(input("각인 테스트 횟수를 입력해주세요(1~) : "))
    lang = int(input("[0]국내 [1]대만 : "))
    if lang == 0 :
        langCode = 'kor'
    else :
        langCode = 'chi_tra'
    # print("[0]한 화면 스크린샷 [1]전체 화면 스크린샷 : ")
    # captureTypeNum = int(ms.InputNum(1))

    with open(targetTxtFileName) as f:
        lines = f.read().splitlines()

    print("전체 실행횟수 : " + str(len(lines)))
    print("전체 예상 종료 시각 : " + str(ms.GetElapsedTime((10+count * 3.2 )* float(len(lines)))))

    for line in lines:
#아이템 별 폴더 추가 생성
        #if folderCheck == 1:
        itemID, scrollID = line.split(',')
        
        extraPath = path + "/"+ itemID + time.strftime("_%H%M")
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
            print("실행 중... (예상 종료 시각 : "+ms.GetElapsedTime(10+count * 3.2) +")")
            #print("실행 중 입니다...(예상 소요 시간 : " + str(count * 1.5) + " 초)")

            ms.ResetFirst()
            ms.Command("cleanupinventory")

            
            #if scrollID == 0 :
            ms.Command(f"additem 70{scrollID} 100000000")
            #elif scrollID ==1 :
                #ms.Command("additem 701 100000000")

            ms.Command("additem 999 2000000000")
            ms.Command("additem "+itemID+" 1")
            ms.Move(ms.menuPos1)
            ms.Move(ms.invenBtnUp2)
            ms.Move(ms.invenBtn0)
            pag.click()
            ms.Move(ms.invenBtn0)

            txtName = path+"/"+str(itemID)+"_"+str(count)+"EA"

            for i in range(0,count) :
                print(str(i+1) +"/" + str(count), end='\r')
                ms.Move(ms.engraveBtn)
                sleep(2)                
                #if captureTypeNum == 0 :
                ms.CaptureEngraveRes(extraPath+"/"+str(i))
                #if scrollID == 0 :
                    #img2str.Indiv_Engrave(txtName+"_0.txt",extraPath+"/"+str(i)+".jpg",langCode)
                #elif scrollID ==1 :
                img2str.Indiv_Engrave(f'{txtName}_{scrollID}.txt',extraPath+"/"+str(i)+".jpg",langCode)
                
                
                """5열분리"""

                
                
                
                # elif captureTypeNum ==1 : 
                #     ms.CaptureFull(extraPath+"/"+str(i))
                # sleep(0.01)
                #sleep(1)
        
        # except : 
        #     print("다시 입력해주세요.")
    Engraving2()



def Engraving3():
    """각인능력치찾기"""
    ms.PrintUB()
    print("각인 능력치 찾기 TEST")
    ms.PrintUB()

    itemNum = input("아이템 ID([0]돌아가기) : ")
    if itemNum == "0" : 
        EngraveCheck()

    targetStr = input("찾을 능력치 텍스트 : ")
    print("[0]일반각인석 [1]축복각인석 : ")
    typeNum = int(ms.InputNum(1))

    lang = int(input("[0]국내 [1]대만 : "))
    if lang == 0 :
        langCode = 'kor'
    else :
        langCode = 'chi_tra'

    extraPath = path + "/"+ itemNum + time.strftime("_%H%M")
    if not os.path.isdir(extraPath):                                                           
        os.mkdir(extraPath) 
    else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
        shutil.rmtree(extraPath)                                                           
        os.mkdir(extraPath)  
    #try : 
    #if count <= 0 :
            
    #    print("다시 입력해주세요.")
    #    Engraving3()

    #else :
    #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 3.2) +")")

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

    txtName = path+"/"+str(itemNum)

    i = 1
    resultText = ""
    
    while True :#targetStr == resultText :
        print(f'>{i}회 째 실시', end='\r')
        ms.Move(ms.engraveBtn)
        sleep(2)
        ms.CaptureEngraveRes(extraPath+"/"+str(i))
        resultText = img2str.Indiv_Engrave(txtName+"_"+str(typeNum)+".txt",extraPath+"/"+str(i)+".jpg",langCode)
        print(resultText)

        if targetStr in resultText :
            print(f'{i}번 만에 찾았다!')
            break

        #print("못찾았다")
        

        sleep(0.01)

        i=i+1

    
    Engraving3()

def Engraving4():

    targetStr = input("찾을 능력치 텍스트 : ")
    lang = int(input("[0]국내 [1]대만 : "))
    if lang == 0 :
        langCode = 'kor'
    else :
        langCode = 'chi_tra'
    
    extraPath = path + "/"+ time.strftime("_%H%M")
    if not os.path.isdir(extraPath):                                                           
        os.mkdir(extraPath) 
    else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
        shutil.rmtree(extraPath)                                                           
        os.mkdir(extraPath)  

    i = 1
    while True :#targetStr == resultText :
        print(f'>{i}회 째 실시', end='\r')
        ms.Move(ms.engraveBtn)
        sleep(2)
        ms.CaptureEngraveRes(extraPath+"/"+str(i))
        resultText = img2str.Indiv_Engrave(extraPath+"/"+str(i)+".txt",extraPath+"/"+str(i)+".jpg",langCode)
        print(resultText)

        if targetStr in resultText :
            print(f'{i}번 만에 찾았다!')
            break

        #print("못찾았다")
        

        sleep(0.01)

        i=i+1

    
    Engraving4()

if __name__ == "__main__" : 
    EngraveCheck()