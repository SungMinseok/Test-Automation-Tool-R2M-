import pyautogui as pag
from time import sleep
import os
import msdata as ms
import time
import mergeImg
import shutil
import img2str

# path = "./screenshot/DropCheck"+ time.strftime("_%m%d")
# if not os.path.isdir(path):                                                           
#     os.mkdir(path)
# mergePath = path + "/Merge"
# if not os.path.isdir(mergePath):                                                           
#     os.mkdir(mergePath)      

line_UL = "┌"
line_UR = "┐"
line_DL = "└"
line_DR = "┘"
line_H = "│"
line_W = "─"
nameText = "드랍템 확인 TEST"
verText = "ver 1.0"
dateText = "210713"
makerText = "made by sms"
desText = "  " + "몬스터생성 > 킬 > 루팅 > n회 반복 > 아이템확인후스샷(이름/수량) > 텍스트 파일로 저장"
warnText= "  " + "테스트 전 장착한 장비를 모두 해제하고, 인벤토리 내부 슬롯을 최상단으로 맞추세요."


def DropCheck():
    global path, mergePath

    path = "./screenshot/DropCheck"+ time.strftime("_%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
    mergePath = path + "/Merge"
    if not os.path.isdir(mergePath):                                                           
        os.mkdir(mergePath)      

    ms.SetMainUI(nameText,verText,dateText,makerText,desText,warnText)
    # print("┌" + "┐".rjust(107,'─'))
    # print("│" + nameText.center(100) +"│")
    # print("│" + "│".rjust(107,'─'))
    # print("│" + (verText + " / " + dateText + " / " + makerText).rjust(106) +"│")
    # print("├" + "┤".rjust(107,'─'))

    print("┌" + "┐".rjust(107,'─'))
    print(" 드랍 테스트 방법을 선택해주세요.")
    print(" [1]직접입력    [2]텍스트파일(몬스터 ID 리스트)")#필요한거 : 몬스터id,한번에 죽일 량(300),대기 시간(30초),반복횟수(8),
    print(" [0]테스트메뉴")
    print("└" + "┘".rjust(107,'─'))
    #type = int(ms.InputNum(3))
    num2 = int(ms.InputNum(3))
    ms.clear()
    if num2==0:
        ms.TestMenu()
    elif num2==1:
        DropCheck1()
    elif num2==2:
        DropCheck2()
        
        
    DropCheck()
        
def DropCheck1():
    print("┌" + "┐".rjust(107,'─'))
    print(" 설정을 변경하시겠습니까?")
    print(" [1]기본 설정(500마리,10초,2회반복,1종류,최종대기10초)    [2]새로 설정")#필요한거 : 몬스터id,한번에 죽일 량(300),대기 시간(30초),반복횟수(8),
    print(" [0]테스트메뉴")
    print("└" + "┘".rjust(107,'─'))
    type1 = int(ms.InputNum(2))
    ms.clear()
    if type1==0:
        DropCheck()
    elif type1==1:
        monAmt = 500
        waitTime = 10
        loopAmt = 2
        dropCtg = 1
        lastWaitTime = 10
    
    elif type1==2:
        monAmt = int(input("몬스터 수를 입력해주세요.(250) : "))
        waitTime = int(input("대기 시간을 입력해주세요.(10) : "))
        loopAmt = int(input("반복 횟수를 입력해주세요.(1~) : "))
        dropCtg = int(input("드랍 아이템 종류 최대 갯수를 입력해주세요.(1~20) : "))
        lastWaitTime = int(input("최종 대기 시간을 입력해주세요.(30) : "))

    print("몬스터 ID를 입력해주세요. ([0]테스트메뉴) : ") 
    monId = int(ms.InputNum(9999999))
    ms.clear()
    if monId==0:
        DropCheck()
    else : 

    #while itemNum!="0":
        #print("실행 중... (예상 소요 시간 : "+str(loopAmt*waitTime+90)+")")
        print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+(loopAmt*(waitTime+3)+90)+lastWaitTime) +")")
#리셋
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.Move(ms.autoBtn)

        for i in range(0,int(loopAmt)):        
            print(str(i+1) + "/" + str(loopAmt), end='\r')
    #몬스터생성
            ms.Command("summon "+str(monId)+" "+str(monAmt))
    #살짝대기후 킬
            sleep(0.1)
            ms.Command("kill 0 15")
            ms.Move(ms.centerPos)
            sleep(0.1)
    #대기
            sleep(float(waitTime))
            ms.CMD_DoTeleport(i%4+3)
            sleep(3)

#n회 반복
#50초 대기(나머지 아이템 먹기)
        totalAmt = int(monAmt) * int(loopAmt)
        sleep(lastWaitTime)
        ms.Move(ms.autoBtn)

#인벤오픈
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        img2str.ResetTxtFile(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_names.txt","name")
        img2str.ResetTxtFile(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_amts.txt","amt")

        for j in range(0,dropCtg):
    #0번슬롯터치>상세터치>마우스 화면중간터치>스샷(이름,수량)
            ms.Move(getattr(ms, 'invenBtn{}'.format(j)))
            ms.Move(ms.invenBtnDown2)
            ms.Move(ms.centerPos)
            sleep(1.5)#터치한아이템 이름 사라지는 시간
            ms.CaptureInvenDes(path+"/"+str(monId)+"_"+str(totalAmt)+"EA_"+str(j)+"_name",1)
            img2str.Indiv_Item(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_names.txt",
            path+"/"+str(monId)+"_"+str(totalAmt)+"EA_"+str(j)+"_name.jpg")

            ms.CaptureInvenDes(path+"/"+str(monId)+"_"+str(totalAmt)+"EA_"+str(j)+"_amt",2)
            img2str.Indiv_Num(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_amts.txt",
            path+"/"+str(monId)+"_"+str(totalAmt)+"EA_"+str(j)+"_amt.jpg")
            
            ms.Move(ms.invenExitBtn)
            sleep(0.01)
    #0~20번슬롯 >반복

        #mergeImg.MergeImg_Drop(monId,monAmt*loopAmt,dropCtg,path)
#모든 스샷 병합

#끝


# #아이템 별 폴더 추가 생성 하지말자
#         #extraPath = path + "/"+ itemNum
#         extraPath = path
#         if not os.path.isdir(extraPath):                                                           
#             os.mkdir(extraPath)        
        print("스샷 경로 : "+path)
        DropCheck1()
    #DropCheck()

        

def DropCheck2():
    fileName = input("불러올 txt 파일명 입력해주세요([Enter]드랍.txt, [0]돌아가기) : ")
    if fileName =="0":
        DropCheck()
    elif fileName =="":
        fileName = '드랍'
    
    with open(fileName +".txt") as f:
        lines = f.read().splitlines()

    print("┌" + "┐".rjust(107,'─'))
    print(" 설정을 변경하시겠습니까?")
    print(" [1]기본 설정(50마리,25초,2회반복,15종류,최종대기20초)    [2]새로 설정")#필요한거 : 몬스터id,한번에 죽일 량(300),대기 시간(30초),반복횟수(8),
    print(" [0]테스트메뉴")
    print("└" + "┘".rjust(107,'─'))
    type1 = int(ms.InputNum(2))
    ms.clear()
    if type1==0:
        DropCheck()
    elif type1==1:
        monAmt = 50
        waitTime = 60
        loopAmt = 2
        dropCtg = 15
        lastWaitTime = 10
    
    elif type1==2:
        monAmt = int(input("몬스터 수를 입력해주세요.(250) : "))
        waitTime = int(input("대기 시간을 입력해주세요.(10) : "))
        loopAmt = int(input("반복 횟수를 입력해주세요.(1~) : "))
        dropCtg = int(input("드랍 아이템 종류 최대 갯수를 입력해주세요.(1~20) : "))
        lastWaitTime = int(input("최종 대기 시간을 입력해주세요.(30) : "))
            
    loopCount = 1
    print("3초 후 시작합니다...")
    sleep(3)
    print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+(loopAmt*(3)+90)*len(lines)+lastWaitTime) +")")
    #print("예상 종료 시간 : ")
    for monId in lines:
#아이템 별 폴더 추가 생성
        #if folderCheck == 1:
        extraPath = path + "/"+ monId
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
        else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
            shutil.rmtree(extraPath)                                                           
            os.mkdir(extraPath)  

        print("전체 : " +str(loopCount) + "/" + str(len(lines)))

#리셋
        ms.ResetFirst()
        ms.Command("cleanupinventory")
        ms.Move(ms.autoBtn)

        for i in range(0,int(loopAmt)):
            print(str(i+1) + "/" + str(loopAmt), end='\r')
    #몬스터생성
            ms.Command("summon "+str(monId)+" "+str(monAmt))
    #살짝대기후 킬
            sleep(0.1)
            ms.Command("kill 0 15")
            ms.Move(ms.centerPos)
            sleep(0.1)
    #대기
            #sleep(float(waitTime))
            sleep(float(waitTime))
            ms.CMD_DoTeleport(i%4+3)
            sleep(3)

#n회 반복
#50초 대기(나머지 아이템 먹기)
        totalAmt = int(monAmt) * int(loopAmt)
        sleep(lastWaitTime)
        ms.Move(ms.autoBtn)

#인벤오픈
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        #img2str.ResetTxtFile(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_names.txt","name")
        #img2str.ResetTxtFile(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_amts.txt","amt")

        for j in range(0,dropCtg):
    #0번슬롯터치>상세터치>마우스 화면중간터치>스샷(이름,수량)
            ms.Move(getattr(ms, 'invenBtn{}'.format(j)))
            ms.Move(ms.invenBtnDown2)
            ms.Move(ms.centerPos)
            sleep(1.5)#터치한아이템 이름 사라지는 시간
            ms.CaptureInvenDes(extraPath+"/"+str(monId)+"_"+str(totalAmt)+"EA_"+str(j)+"_name",1)
            img2str.Indiv_Item(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_names.txt",
            extraPath+"/"+str(monId)+"_"+str(totalAmt)+"EA_"+str(j)+"_name.jpg")

            ms.CaptureInvenDes(extraPath+"/"+str(monId)+"_"+str(totalAmt)+"EA_"+str(j)+"_amt",2)
            img2str.Indiv_Num(path+"/Merge/"+str(monId)+"_"+str(totalAmt)+"EA_amts.txt",
            extraPath+"/"+str(monId)+"_"+str(totalAmt)+"EA_"+str(j)+"_amt.jpg")
            
            ms.Move(ms.invenExitBtn)
            sleep(0.01)
    #0~20번슬롯 >반복
#모든 스샷 병합

#끝 
        print("스샷 경로 : "+path)
        loopCount += 1
    DropCheck2()








#     try :
#         with open(fileName +".txt") as f:
#             lines = f.read().splitlines()
#     except : 
#         EquipCheck2()

#     # print("---------------------------------------------------------------")
#     # print("아이템 별 폴더를 생성하시겠습니까?")
#     # print("[1]생성    [2]생성 안함")
#     # print("[0]돌아가기")
#     # print("---------------------------------------------------------------")
#     #folderCheck = int(ms.InputNum(2))
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

# #장신구 : 50초, 무기  : 64초, 영혼무기 :75초
#DropCheck()



if __name__ == "__main__" : 
    DropCheck()