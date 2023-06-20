from re import T
import pyautogui as pag
import msdata as ms
from setappsize import SetAppSize
from time import sleep
import os.path
import time
import img2str as i2s


def multicommand():
    while True : 
        ms.PrintUB_Bold()
        print("※멀티 커맨드")
        ms.PrintUB()      
        print("[1]Item ID 입력 : +0 ~ +13강 장비 생성\n[2]TXT 파일 실행 : Item ID\n[3]TXT 파일 실행 : 명령어\n[4]Item ID 입력 : 직접 입력")
        ms.PrintUB()      
        print("[0]메인메뉴")
        ms.PrintUB()      
        num2 = int(ms.InputNum(5))
        ms.clear()
        if num2==0:
            break
        elif num2 ==1:
            Command_Additem()
        elif num2 ==2:
            Command_Additems_Text()
        elif num2 ==3:
            Command_Text()
        elif num2 ==4:
            Command_Additems()
    #elif num2 ==5:
    #    Command_Direct2()
    
    #multicommand()


def Command_Additem():
    while True:
        ms.PrintUB_Bold()     
        print("※Item ID 입력 : +0 ~ +13강 장비 생성")
        ms.PrintUB()      
        print("+0강 Item ID를 입력하세요.")
        ms.PrintUB()      
        print("[0]뒤로가기")
        ms.PrintUB()    

        itemNum = (ms.InputNum(99999999))
        if itemNum=="0":
            ms.clear()
            return
        ms.ResetFirst()
        ms.CommandOpen()
        pag.typewrite("additems")
        for j in range(0,14):
            pag.press('space')
            temp = int(itemNum)+j
            pag.typewrite(str(temp))
        ms.CommandClose()


def autoAddItem(id, count):
    if count == "":
        count = 1

    ms.Command(f'additem {id} {count}')

def autoAddItemAll(id):

    #ms.ResetFirst()
    ms.CommandOpen()
    pag.typewrite("additems ")
    for j in range(0,14):
        temp = int(id)+j
        pag.typewrite(str(temp)+" ")
    ms.CommandClose()


def Command_Additems_Text():
    while True :
        ms.PrintUB_Bold()      
        print("※TXT 파일 실행 : Item ID")
        ms.PrintUB()      
        print("불러올 txt 파일명 입력하세요.\n([Enter]입력 시 additems.txt를 불러옵니다.)")
        ms.PrintUB()      
        print("[0]뒤로가기")
        ms.PrintUB() 

        while True  :           
            fileName = input(">")

            #종료 
            if fileName =="0":
                ms.clear()
                return
            #패스(기본 파일 있음)
            elif fileName =="":
                fileName = 'additems'
                break
            #패스(특정 파일 있음)
            elif os.path.isfile(fileName +".txt") :
                break
            else :
                print("파일이 없습니다.")

        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
        f.close()

        ms.ResetFirst()

        ms.CommandOpen()
        pag.typewrite("additems")
        
        for line in lines:
            pag.typewrite(" "+line)
        ms.CommandClose()

def autoAddItemText(filePath):
    with open(filePath) as f:
        lines = f.read().splitlines()
    f.close()
    #ms.ResetFirst()
    ms.CommandOpen()
    pag.typewrite("additems")
    for line in lines:
        pag.typewrite(" "+line)
    ms.CommandClose()

    # cmdStr= "additems"
    # for line in lines:
    #     cmdStr += " " + str(line)
    # ms.Command(cmdStr)
    sleep(2)


#R2M_Alpha_Command : makeitem X N > X in txtFile
def autoMakeItemText(filePath):
    with open(filePath) as f:
        lines = f.read().splitlines()
    f.close()
    ms.ResetFirst()
    #pag.typewrite("additems")
    for line in lines:
        if line.find(",") != -1 :
            itemID, itemAmount = line.split(',')
            ms.Command("makeitem "+itemID+" "+itemAmount)

        else :
            ms.Command("makeitem "+line+" 1")


def Command_Text():
    while True :
#세팅값 불러오기&저장
        with open("info_mcmd.txt") as setFile:
            setValue = setFile.read().splitlines()
        setFile.close()

        term = int(setValue[0])
        count = int(setValue[1])

#UI 실행부
        ms.PrintUB_Bold()      
        print("※TXT 파일 실행 : 명령어")
        ms.PrintUB() 
        print("＊명령어 실행 간격 : ", setValue[0], "초")
        print("＊실행횟수 : ", setValue[1], "회")
        ms.PrintUB()  
        print("[9]설정변경")
        print("[0]뒤로가기")
        ms.PrintUB()          
        print("불러올 txt 파일명 입력해주세요\n([Enter]입력 시 multicommand.txt를 불러옵니다.)")
        ms.PrintUB()  

#Input 입력부
        while True  :           
            fileName = input(">")
            #종료 
            if fileName =="0":
                ms.clear()
                return
            #설정변경
            elif fileName == "9":
                setMsg = ["명령어 실행 대기 간격(초)을 입력해 주세요(0~)","실행 횟수를 입력해주세요(1~)"]
                ms.ChangeSetValue("info_mcmd",setMsg)
                print("설정변경 완료!")
                sleep(1)
                ms.clear()
                break
            #패스(기본 파일 있음)
            elif fileName =="":
                fileName = "multicommand"
                break
            #패스(특정 파일 있음)
            elif os.path.isfile(fileName +".txt") :
                break

            else :
                print("파일이 없습니다.")
        
        #설정 변경 시 처음부터 시작
        if fileName == "9":
            continue

#기능 실행부
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
        f.close()

        startTime = ms.GetCurrentTime()
        indivRunTime = len(lines) * 2.5 + term

        ms.clear()
        ms.PrintUB_Bold()      
        print("※TXT 파일 실행 : 명령어")
        ms.PrintUB() 
        print("＊명령어 실행 간격 : ", setValue[0], "초")
        print("＊실행횟수 : ", setValue[1], "회")
        ms.PrintUB()  
        print("총 예상 소요 시간 : ", count * indivRunTime , "초")
        print("총 예상 종료 시각 : ", ms.GetElapsedTime(count * indivRunTime))
        ms.PrintUB()  


        ms.ResetFirst()

        for i in range(0,count) :

            #ms.PrintUB()  
            print(i+1 ,"번 째 실행", end='\r')
            for line in lines:
                ms.Command(line)
                sleep(1)
            
            if i < (count - 1) :
                ms.sleep(term)

#기능 종료부

        endTime = ms.GetCurrentTime()
        totalRuntime = endTime -startTime

        ms.PrintUB() 
        print("실행 완료.") 
        ms.PrintUB()  
        print("총 소요 시간 : ", totalRuntime , "초")
        print("종료 시각 : ", ms.GetCurrentTime())
        ms.PrintUB()  


def Command_Additems():
    while True :
    #UI 실행부
        ms.PrintUB_Bold()      
        print("※Item ID 입력 : 직접 입력")
        ms.PrintUB() 
        print("[0]뒤로가기")
        ms.PrintUB()          
        print("Item ID를 스페이스로 구분하여 입력해주세요.")
        ms.PrintUB() 
        
        itemNums = input(">")
        if itemNums =="0":
            ms.clear()
            return
        ms.ResetFirst()

        ms.CommandOpen()
        pag.typewrite("additems " + str(itemNums))
        ms.CommandClose()



def Command_Direct1():
    
    commandText = input("명령어 입력 : ")
    count = int(input("실행 횟수를 입력해주세요(1~) : "))

    try : 
        if count <= 0 :
                
            print("다시 입력해주세요.")
            Command_Direct1()

        else :
            print("실행 중 입니다...(예상 소요 시간 : " + str(count * 1.5) + " 초)")

            ms.ResetFirst()

            for i in range(0,count) :
                ms.Command(commandText)
    
    except : 
        print("다시 입력해주세요.")
        Command_Direct1()

def Command_Direct2():
    print("미완성")
    # commandCountText = "0"
    # commandText = "default"

    # while commandText != "0"
    #     commandCountText = str(int(commandCountText) + 1)
    #     commandText[int(commandCountText)-1] = input(commandCountText + "번째 명령어 입력(종료시 : 0) : ")
        
    # term = int(input("명령어 실행 대기 간격(초)을 입력해 주세요(0~) : "))

    # count = int(input("실행 횟수를 입력해주세요(1~) : "))

    # try : 
    #     if count <= 0 :
                
    #         print("다시 입력해주세요.")
    #         Command_Direct()

    #     else :
    #         print("실행 중 입니다...(예상 소요 시간 : " + str(count * 1.5) + " 초)")

    #         ms.ResetFirst()

    #         for i in range(0,count) :
    #             ms.Command(commandText)

    
    # except : 
    #     print("다시 입력해주세요.")
    #     Command_Direct()

# def multiCommand_auto(commandText, repeatCount, repeatDelay):
#     lines = commandText.splitlines()

#     for i in range(0,repeatCount) :
  
#         print(i+1 ,"번 째 실행", end='\r')
#         for line in lines:
#             ms.Command(line)
#             sleep(1)
        
#         if i < (count - 1) :
#             ms.sleep(term)


def autoTest_regist2market(marketType = 0,fileName = ""):#일반/통합,id텍스트파일명

    
#UI 실행부
    ms.PrintUB_Bold()      
    print("※거래소 아이템 등록 확인 테스트")
    # ms.PrintUB() 
    # print("＊명령어 실행 간격 : ", setValue[0], "초")
    # print("＊실행횟수 : ", setValue[1], "회")
    # ms.PrintUB()  
    # print("[9]설정변경")
    # print("[0]뒤로가기")
    ms.PrintUB()          
    fileName = input("[0]일반거래소 [1]통합거래소 : ")
    fileName = input("불러올 txt 파일명 : ")
    
    path = "./screenshot/autoTest_regist2market"+ time.strftime("_%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
        
    path_result = path + "/result"
    if not os.path.isdir(path_result):                                                           
        os.mkdir(path_result)

    with open(fileName +".txt") as f:
        lines = f.read().splitlines()
    f.close()

    totalCount = len(lines)
    count0, count1 = divmod(totalCount , 25)
    #count0 = totalCount/25
    #count1 = totalCount%25


    ms.ResetFirst()


    ms.Move(ms.menuPos3)
    sleep(2)
    if marketType == "world":
        ms.Move(ms.market_enterServerType1)
    else:
        ms.Move(ms.market_enterServerType0)
    sleep(2)

    for i in range(0,count0):

        ms.Move(ms.market_searchTab)
        sleep(2)

        ms.Command("cleanupinventory")
        ms.CommandOpen()
        pag.typewrite("additems ")
        for j in range(0,25):
            curID = lines[25*i+j]
            # if curID[len(curID)-1] == "8":
            #     pag.typewrite(str(int(curID)-1) + " ")
            pag.typewrite(curID + " ")
        ms.CommandClose()
        ms.Command("additem 999 10000000")

        ms.Move(ms.market_registTab)
        sleep(3)

        ms.Capture(path+ "/"+lines[25*i]+"_"+lines[25*i+24]+"_start",False)

        for k in range(0,25):
            ms.Move(ms.market_invenBtn0)
            sleep(2)
            ms.Move(ms.market_sellBtn0)
            sleep(0.5)
            ms.Move(ms.market_sellBtn1)
            sleep(0.5)
            ms.Move(ms.market_sellBtn2)
            sleep(3)
            
        ms.Capture(path+ "/"+lines[25*i]+"_"+lines[25*i+24]+"_end",False)
        getData = i2s.getNumberFromImg(ms.captureSomeBox2("market_totalSellPriceBox",path_result + "/result_" +str(i)))
        if getData == "250":
            testResult = "pass"
        else :
            testResult = "fail"

        testResultText =\
            '\n'\
            +lines[25*i]\
            +","+lines[25*i+24]\
            +","+getData\
            +","+testResult

        with open(path_result+"./result.txt",'a',encoding='utf-8') as tx:
            tx.write(testResultText)

        for l in range(0,25):
            ms.Move(ms.market_cancelRegist)
            sleep(2.2)
    
    #for i in range(0,count1):
    if count1 >0 : 
        
        ms.Move(ms.market_searchTab)
        sleep(3)

        ms.Command("cleanupinventory")
        ms.CommandOpen()
        pag.typewrite("additems ")
        for j in range(0,count1):
            curID = lines[25*count0+j]
            # if curID[len(curID)-1] == "8":
            #     pag.typewrite(str(int(curID)-1) + " ")
            pag.typewrite(lines[25*count0+j] + " ")
        ms.CommandClose()
        ms.Command("additem 999 10000000")

        ms.Move(ms.market_registTab)
        sleep(3)

        ms.Capture(path+ "/"+lines[25*count0]+"_"+lines[25*count0+count1-1]+"_start",False)

        for k in range(0,count1):
            ms.Move(ms.market_invenBtn0)
            sleep(2)
            ms.Move(ms.market_sellBtn0)
            sleep(0.5)
            ms.Move(ms.market_sellBtn1)
            sleep(0.5)
            ms.Move(ms.market_sellBtn2)
            sleep(3)

        ms.Capture(path+ "/"+lines[25*count0]+"_"+lines[25*count0+count1-1]+"_end",False)
        #i2s.Indiv_Num(path_result+".txt",ms.captureSomeBox2("market_totalSellPriceBox",path_result + "/result_f" ))
        getData = i2s.getNumberFromImg(ms.captureSomeBox2("market_totalSellPriceBox",path_result + "/result_f"))
        if getData == "250":
            testResult = "pass"
        else :
            testResult = "fail"

        testResultText =\
            '\n'\
            +lines[25*count0]\
            +","+lines[25*count0+count1-1]\
            +","+getData\
            +","+testResult

        with open(path_result+"./result.txt",'a',encoding='utf-8') as tx:
            tx.write(testResultText)

        for l in range(0,count1):
            ms.Move(ms.market_cancelRegist)
            sleep(2.2)

def executeCmdPackage(cmd) :
    ms.ResetFirst()
    ms.Move(ms.menuPos4)
    ms.Move(ms.menuPos20)

def restartgame():
    """
    캐릭터 재접속
    """
    
    #ms.Command("doteleport 0 550 250")
    #ms.sleep(5)

    ms.Move(ms.menuPos4)
    ms.Move(ms.menuPos20)
    ms.sleep(0.1)
    ms.Move(ms.menuMiddleUpperTab5)
    ms.Move(ms.goCharacterSelectPageBtn)
    ms.sleep(0.01)
    ms.Move(ms.okPos)
    ms.sleep(0.2)

    ms.sleep(4)

    ms.Move(ms.characterCreateBtn)

def go_character_selection_window():
    """
    캐릭터 선택창
    """
    
    #ms.Command("doteleport 0 550 250")
    #ms.sleep(5)

    ms.Move(ms.menuPos4)
    ms.Move(ms.menuPos20)
    ms.sleep(0.1)
    ms.Move(ms.menuMiddleUpperTab5)
    ms.Move(ms.goCharacterSelectPageBtn)
    ms.sleep(0.01)
    ms.Move(ms.okPos)
    ms.sleep(0.2)

def go_server_selection_window():
    """
    서버 선택창
    """
    
    #ms.Command("doteleport 0 550 250")
    #ms.sleep(5)

    ms.Move(ms.menuPos4)
    ms.Move(ms.menuPos20)
    ms.sleep(0.1)
    ms.Move(ms.menuMiddleUpperTab5)
    ms.Move(ms.goServerSelectionBtn)
    ms.sleep(0.01)
    ms.Move(ms.okPos)
    ms.sleep(0.2)

def logout():
    """
    로그아웃&서드파티 선택창
    """
    
    #ms.Command("doteleport 0 550 250")
    #ms.sleep(5)

    ms.Move(ms.menuPos4)
    ms.Move(ms.menuPos20)
    ms.sleep(0.1)
    ms.Move(ms.menuMiddleUpperTab5)
    ms.Move(ms.logoutBtn)
    ms.sleep(0.01)
    ms.Move(ms.okPos)
    ms.sleep(0.2)


def chat_ingame(chat : str, screenshot_path = ""):
    """
    채팅팝업 내 채팅발생
    """
    ms.ResetFirst()
    ms.Click(ms.mainhud_chat_btn,0.2)
    ms.Click(ms.mainhud_chat_btn,0.1)

    pag.typewrite(chat)

    ms.Click(ms.send_chat_btn,0.1)
    ms.Click(ms.send_chat_btn,0.1)

    sleep(0.5)

    if screenshot_path == "" :
        ms.captureSomeBox("")
    else :
        ms.captureSomeBox2("chat_popup_box",screenshot_path)
    ms.ResetFirst()

# def autoTest_reinforceEquipment(reinType,count,equipType,scrollType,fileName):  #일반/다중강화, 테스트횟수, 장비타입(1무기/2방어구/3장신구/4전리품), 주문서타입(1일반/2축복/3저주/4고대)
    
#     path = "./screenshot/autoTest_reinforceEquipment"+ time.strftime("_%m%d")
#     if not os.path.isdir(path):                                                           
#         os.mkdir(path)
        
#     path_result = path + "/result"
#     if not os.path.isdir(path_result):                                                           
#         os.mkdir(path_result)



#     if equipType <=3 :
#         print("[1]일반 [2]축복 [3]저주 [4]고대 // [0]뒤로 : ")
#         scrollType = int(ms.InputNum(4))
#         if scrollType == 0 : 
#             ProbTest()
#     # else :
#     #     print("수호팔찌340/파괴가면341/생명금관342")
#     #     print("숙련나팔343/영혼부적344/극복성배345")
#     #     print("전리품강화주문서 ID 입력 // [0]뒤로 : ")
#     #     bookNum = int(ms.InputNum(999))
#     #     if bookNum == 0 : 
#     #         ProbTest()



#     with open("장비강화.txt") as f:
#         lines = f.read().splitlines()

#     for itemNum in lines:
#         print("총 예상 종료 시간 : "+ms.GetElapsedTime((10+ count * 17)*len(lines)) +")")

# #아이템 별 폴더 추가 생성
#         #if folderCheck == 1:
#         startTime = time.strftime("_%m%d%H%M")
        
#         extraPath = path + "/"+ itemNum + startTime
#         if not os.path.isdir(extraPath):                                                           
#             os.mkdir(extraPath)  
#         else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
#             shutil.rmtree(extraPath)                                                           
#             os.mkdir(extraPath)  

#         if count <= 0 :
                
#             print("처음부터 다시 입력해주세요.")
#             ReinforceEquipment()

#         else :
#             if reinType == "single" :
#                 print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 17) +")")

#                 #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 3.2) +")")

#                 ms.ResetFirst()
#                 ms.Command("cleanupinventory")


#                 if equipType <=3 :
#                     bookNum = 300 + (scrollType-1)*10 + (equipType-1)
#                 elif equipType == 4:
#                     if int(itemNum) <=430008 :
#                         bookNum = 340
#                     elif int(itemNum) <=431008:
#                         bookNum = 341
#                     elif int(itemNum) <=432008:
#                         bookNum = 342
#                     elif int(itemNum) <=433008:
#                         bookNum = 343
#                     elif int(itemNum) <=434008:
#                         bookNum = 344
#                     elif int(itemNum) <=435008:
#                         bookNum = 345
#                 ms.Command("additem "+str(bookNum)+" "+str(count))

#                 ms.Command("additem 999 1500000000")
#                 ms.Command("additem "+itemNum+" "+str(count*2))

#                 sleep(0.01)
#                 #인벤열기 >
#                 ms.Move(ms.menuPos1)
#                 sleep(ms.waitTime)
#                 #강화UI 오픈
#                 ms.Move(ms.invenBtnRein)
#                 sleep(0.2)
                
#                 ms.Move(ms.invenReinBtnUp1)
#                 ms.Move(ms.invenBtn0)
#                 ms.Move(ms.invenReinBtnUp0)

#                 txtName = path+"/"+str(itemNum)+"_"+str(bookNum)+"_"+str(count)+startTime+".txt"

#                 for i in range(0,count) :
#                     print(str(i+1) +"/" + str(count), end='\r')
#                     ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
#                     ms.Move(ms.invenReinBtnDown1)
#                     sleep(1.5)    
#                     ms.Move(ms.centerPos)         
#                     sleep(1.5)       
#                     ms.CaptureReinforceResult(extraPath+"/"+str(i))
#                     img2str.Indiv_Item(txtName,extraPath+"/"+str(i)+".jpg")
                        
#                     sleep(0.3)       
#                     ms.Move(ms.invenReinBtnDown1) 
#             #다중강화
#             elif reinType == "multi":
#                 print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 18) +")")

                
#                 for i in range(0,count) :
#                     print(str(i+1) +"/" + str(count), end='\r')
#                     ms.ResetFirst()

#                     ms.Command("cleanupinventory")

#                     if equipType <=3 :
#                         bookNum = 300 + (scrollType-1)*10 + (equipType-1)
#                     elif equipType == 4:
#                         if int(itemNum) <=430008:
#                             bookNum = 340
#                         elif int(itemNum) <=431008:
#                             bookNum = 341
#                         elif int(itemNum) <=432008:
#                             bookNum = 342
#                         elif int(itemNum) <=433008:
#                             bookNum = 343
#                         elif int(itemNum) <=434008:
#                             bookNum = 344
#                         elif int(itemNum) <=435008:
#                             bookNum = 345
#                     ms.Command("additem "+str(bookNum)+" 100000")

#                     ms.Command("additem 999 1500000000")
#                     ms.Command("additem "+itemNum+" 16")

#                     sleep(0.01)
#                     #인벤열기 >
#                     ms.Move(ms.menuPos1)
#                     sleep(ms.waitTime)
#                     #강화UI 오픈
#                     ms.Move(ms.invenBtnRein)
#                     sleep(0.2)
#                     #다중강화 클릭
#                     ms.Move(ms.invenReinBtnLeft1)
#                     #주문서등록
#                     ms.Move(ms.invenReinBtnUp1)
#                     ms.Move(ms.invenBtn0)
#                     #장비등록준비
#                     ms.Move(ms.invenReinBtnUp0)
#                     #장비등록
#                     for k in range(0,16):
#                         ms.Move(getattr(ms, 'invenBtn{}'.format(k)))
                    
#                     txtName = path+"/"+str(itemNum)+"_"+str(bookNum)+"_"+str(count*16)+startTime+".txt"
#                     #강화도 클릭
#                     phaseNum = (int(itemNum) % 10) + 1
#                     ms.Move(getattr(ms, 'reinPhase{}'.format(phaseNum)))

#                     #강화시작 클릭
#                     ms.Move(ms.invenReinBtnDown2)

#                     #2초대기     
#                     sleep(3)       

#                     #스샷저장
#                     if phaseNum < 9 :
#                         ms.CaptureReinMultiResultBox(extraPath+"/"+str(i))
#                     else : 
#                         ms.Capture(extraPath+"/"+str(i))


#                     #반복종료 리턴(끝)


if __name__ == "__main__" : 
    multicommand()