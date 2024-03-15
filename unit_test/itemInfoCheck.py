import pyautogui as pag
from time import sleep
import os
import func.msdata as ms
import time
import func.mergeImg

#global path
line_UL = "┌"
line_UR = "┐"
line_DL = "└"
line_DR = "┘"
line_H = "│"
line_W = "─"
nameText = "아이템 정보 확인(스크린샷)"
verText = "ver 1.0"
dateText = "210823"
makerText = "made by sms"
desText = "  " + "인벤토리 내 아이템의 상세 내용 및 추가 정보를 스샷합니다.(이미지 병합 기능)"
warnText= "  " + "테스트 전 장착한 장비를 모두 해제하고, 인벤토리 내부 슬롯을 최상단으로 맞추세요."

def SetMainUI(_nameText,_verText,_dateText,_makerText):
    
    print("┌" + "┐".rjust(107,'─'))
    print("│" + _nameText.center(100) +"│")
    print("│" + "│".rjust(107,'─'))
    print("│" + (_verText + " / " + _dateText + " / " + _makerText).rjust(106) +"│")
    print("├" + "┤".rjust(107,'─'))


def ItemInfoCheck():

    SetMainUI(nameText,verText,dateText,makerText)
    # print("┌" + "┐".rjust(107,'─'))
    # print("│" + nameText.center(100) +"│")
    # print("│" + "│".rjust(107,'─'))
    # print("│" + (verText + " / " + dateText + " / " + makerText).rjust(106) +"│")
    # print("├" + "┤".rjust(107,'─'))
    print(line_H + "※ 설명 ※".center(102) +"│")
    print("├" + "┤".rjust(107,'─'))
    print(desText)
    print("├" + "┤".rjust(107,'─'))
    print(line_H + "※ 사전세팅 ※".center(100) +"│")
    print("├" + "┤".rjust(107,'─'))
    print(warnText)
    print("└" + "┘".rjust(107,'─'))
    print("┌" + "┐".rjust(107,'─'))
    fileName = input("아이템 ID가 입력된 텍스트 파일명을 입력해주세요.([0]테스트 메뉴) : ")
    if fileName =="0":
        ms.TestMenu()

    try :
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
    except : 
        ItemInfoCheck()

    modeNum = input("[1]1장(기본) [2]2장(+아이템 설명) [3]3장(+추가정보) : ")
    ms.clear()




    #global path, mergePath
    path = fr'./screenshot/item_info_check_{time.strftime("_%y%m%d")}'
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
    mergePath = os.path.join(path , "Merge")
    if not os.path.isdir(mergePath):                                                           
        os.mkdir(mergePath)      









    screenshotCount = int(len(lines) / 15) + 1
    curCount = 0
        
    loopCount = 1
    for i in range(0,screenshotCount):
        #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+(loopAmt*(waitTime+3)+90)+lastWaitTime) +")")
        print(str(loopCount) + "/" + str(screenshotCount))
        print(modeNum + "장씩 스크린샷 저장됩니다.")

#아이템 별 폴더 추가 생성

        extraPath = path
            

#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        #ms.CommandOpen()
        #pag.typewrite("additems ")
        
        for j in range(0,15):
            try :
                temp = lines[i*15+j]
            except : 
                temp = ""
            pag.typewrite(str(temp)+" ")
        
        temp_0 = "additems"
        temp_1 = ""
        for j in range(0,15):
            temp_1 += f' {lines[i*15+j]}'

        cmd = f'{temp_0}{temp_1}'
        
        ms.Command(cmd,1)
        #ms.CommandClose()
        sleep(0.01)
#인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        
        for j in range(0,15):

            ms.Move(getattr(ms, 'invenBtn{}'.format(j)))
            ms.Move(ms.invenBtnDown2)
            sleep(1.3)
            ms.CaptureInvenDes(extraPath+"/"+str(i*15+j)+"_0")

            if modeNum == "2" or modeNum == "3" :
    #설명창 위로밀기 > 대기 후 스샷1 > 
                ms.Move(ms.invenDesPos)
                ms.DragUp(ms.invenDesPos)
                ms.CaptureInvenDes(extraPath+"/"+str(i*15+j)+"_1")
            
                if modeNum == "3" :
            #추가정보클릭 > 대기후스샷2 > x버튼
                    ms.Move(ms.invenAddDesPos)
                    sleep(0.1)
                    ms.CaptureInvenDes(extraPath+"/"+str(i*15+j)+"_2")
            # if equipType == 3 :
            #     ms.Move(ms.invenSoulBtn)
            #     ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_3")
            #     ms.Move(ms.invenExitBtn)
            # else :
                
            ms.Move(ms.invenExitBtn)

        mergeImg.MergeImg_Item(i*15,extraPath,modeNum)

            
        print("스샷 경로 : "+extraPath)
        loopCount = loopCount +1


# def EquipCheck1():
   
#     waitTime = 0.01
#     waitTime2 = 0.2

#     itemNum = input("+0강 아이템 id를 입력해주세요([0]테스트메뉴) : ")
#     while itemNum!="0":
#         print("실행 중... (예상 소요 시간 : 알 수 없음)")
# #아이템 별 폴더 추가 생성 하지말자
#         #extraPath = path + "/"+ itemNum
#         extraPath = path
#         if not os.path.isdir(extraPath):                                                           
#             os.mkdir(extraPath)        

# #장비생성
#         ms.ResetFirst()
#         ms.Command("cleanupinventory")
#         ms.CommandOpen()
#         pag.typewrite("additems")
#         for j in range(0,14):
#             if equipType == 2 and j == 10:
#                 break
#             pag.press('space')
#             temp = int(itemNum)+j
#             pag.typewrite(str(temp))


#         ms.CommandClose()
#         sleep(0.01)
# #인벤열기 >
#         ms.Move(ms.menuPos1)
#         sleep(ms.waitTime)
        
#         for i in range(0,14):
#             if equipType == 2 and i == 10:
#                 break
#     #첫번째 클릭 > 상세 클릭> 대기후스샷0> 
#             ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
#             ms.Move(ms.invenBtnDown2)
#             sleep(1.5)
#             ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_0")
#     #설명창 위로밀기 > 대기 후 스샷1 > 
#             ms.Move(ms.invenDesPos)
#             ms.DragUp(ms.invenDesPos)
#             ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_1")
#     #추가정보클릭 > 대기후스샷2 > x버튼
#             ms.Move(ms.invenAddDesPos)
#             ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_2")

#             if equipType == 3 :
#                 ms.Move(ms.invenSoulBtn)
#                 ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_3")
#                 ms.Move(ms.invenExitBtn)
#             else :
                
#                 ms.Move(ms.invenExitBtn)

#         mergeImg.MergeImg_Equip(itemNum, equipType,extraPath)

#         print("스샷 경로 : "+extraPath)
#         itemNum = input("+0강 아이템 id를 입력해주세요([0]테스트메뉴) : ")

        

# def EquipCheck2():
   
#     waitTime = 0.01
#     waitTime2 = 0.2
#     fileName = input("불러올 txt 파일명 입력해주세요(기본 : 장비수치)([0]돌아가기) : ")
#     if fileName =="0":
#         EquipCheck()

#     try :
#         with open(fileName +".txt") as f:
#             lines = f.read().splitlines()
#     except : 
#         EquipCheck2()

#     ms.clear()
#     #if folderCheck==0:
#     #    EquipCheck2()
#     # with open(fileName +".txt") as f:
#     #     lines = f.read().splitlines()
    
#     loopCount = 1
#     for itemNum in lines:
#         print("실행 중... (예상 소요 시간 : 알 수 없음)")
#         print(str(loopCount) + "/" + str(len(lines)))

# #아이템 별 폴더 추가 생성
#         # if folderCheck == 1 : 
#         #     extraPath = path + "/"+ itemNum
#         #     if not os.path.isdir(extraPath):                                                           
#         #         os.mkdir(extraPath)       
#         # elif folderCheck == 2 :
#         #     extraPath = path 
#         extraPath = path
            

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
#             if equipType == 2 and i == 10:
#                 break
            
#             ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
#             ms.Move(ms.invenBtnDown2)
#             sleep(1.3)
#             ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_0")
#     #설명창 위로밀기 > 대기 후 스샷1 > 
#             ms.Move(ms.invenDesPos)
#             ms.DragUp(ms.invenDesPos)
#             ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_1")
#     #추가정보클릭 > 대기후스샷2 > x버튼
#             ms.Move(ms.invenAddDesPos)
#             sleep(0.1)
#             ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_2")
#             if equipType == 3 :
#                 ms.Move(ms.invenSoulBtn)
#                 ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_3")
#                 ms.Move(ms.invenExitBtn)
#             else :
                
#                 ms.Move(ms.invenExitBtn)

#         mergeImg.MergeImg_Equip(itemNum,equipType,extraPath)

            
#         print("스샷 경로 : "+extraPath)
#         loopCount = loopCount +1

# #장신구 : 50초, 무기  : 64초

# #ItemInfoCheck()
        
if __name__ == "__main__" : 
    ItemInfoCheck()
    #EquipCheck3()
    #EquipCheck()