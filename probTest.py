#from img2str import Img2Str

#from img2str import Indiv_Num_Return
import pytesseract
from time import sleep
import cv2
import time
import os
import msdata as ms
from datetime import datetime
import shutil
import img2str
import pyautogui as pag
import numpy as np
import pandas as pd
from openpyxl import load_workbook
#pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'
pag.FAILSAFE = False

# path = "./screenshot/Img2str"+ time.strftime("_%m%d")
# if not os.path.isdir(path):                                                           
#     os.mkdir(path)
    
#global path, mergePath

line_UL = "┌"
line_UR = "┐"
line_DL = "└"
line_DR = "┘"
line_H = "│"
line_W = "─"
nameText = "확률 테스트"
verText = "ver 1.0"
dateText = "220720"
makerText = "made by sms"
desText = "  " + "이미지 인식 후 텍스트 파일로 저장"
warnText= "  " + "테스트 전 장착한 장비를 모두 해제하고, 인벤토리 내부 슬롯을 최상단으로 맞추세요."


def ProbTest():
    global path, mergePath
    
    path = "./screenshot/ProbTest"+ time.strftime("_%Y%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
    

    ms.SetMainUI(nameText,verText,dateText,makerText,desText,warnText)
    #ms.PrintUB_Bold()
    print(
    "[1]스킬강화\
    \n[2]매터리얼합성\
    \n[3]장비강화\
    \n[4]영혼부여\
    \n[5]슬롯강화\
    \n[6]장비강화상세\
    \n[7]변신서번트휘장\
    "
    )
    ms.PrintUB()
    print("[0]뒤로")    
    ms.PrintUB_Bold()

    #type = int(ms.InputNum(3))
    selectedNum = int(ms.InputNum(10))
    ms.clear()
    if selectedNum==0:
        ms.MainMenu()
    elif selectedNum==1:
        EnchantSkill()
    elif selectedNum==2:
        CombineMaterial()
    elif selectedNum==3:
        ReinforceEquipment()
    elif selectedNum==4:
        EnchantSoul()
    elif selectedNum==5:
        slotEnchantProbTest()
    elif selectedNum==6:
        ReinforceEquipment_Detail()
    elif selectedNum==7:
        probTest_spotEnchant()
    #elif selectedNum==7:
    #    probTest_slotEnchant_equipment()
    ProbTest()
        
def EnchantSkill() :
    #ms.clear()
            

    skillID = input("확인할 스킬 ID 입력 :")
    skillLevel = input("확인할 스킬 레벨 입력 :")
    scrollID = input("스킬 등급 입력 [350]희귀 [351]영웅 [352]전설 : ")#350 351 352
    testCount = int(input("반복횟수 입력 :"))
    isFinalLevel = input("마지막 레벨이면 1 입력")
    
    
    curPath = path + "/" +time.strftime("_%H%M") + "_enchantSkill"
    if not os.path.isdir(curPath):                                                           
        os.mkdir(curPath)  
    
    print("실행 중...", end='\r')

    passCount = 0

    ms.Command("changeskillenchant "+skillID+" "+skillLevel)
    ms.Command("additem 999 1000000000")
    ms.Command("additem "+scrollID+" 100000")
    sleep(0.5)

    for i in range(0, testCount):
        if i%60 == 0 :
            ms.Command("additem 999 1000000000")


        ms.Move(ms.enchantSkillBtn)
        sleep(0.5)
        ms.Move(ms.centerPos)
        sleep(3)
        
        tempCaptureFileName = ms.captureSomeBox2("enchantSkillResultBox",curPath+"/"+str(i))
        resultText = img2str.getStringFromImg(tempCaptureFileName,'kor')
        #print(resultText)
        sleep(0.1)

        #ms.sleep(1.2)
        if "실패" not in resultText :  
            print("성공")
            passCount = passCount + 1
            ms.Command("changeskillenchant "+skillID+" "+skillLevel)
            ms.Move(ms.enchantSkillStartBtn)

            #failCount = failCount + 1
            #failCountArray[i] = failCountArray[i] + 1
            #totalCountArray[i] = passCountArray[i] + failCountArray[i]
        sleep(0.1)
        ms.Move(ms.centerPos)

        print(f'>{passCount}/{i+1}', end='\r')
        sleep(0.1)
                        
    print(f'최종결과(성공횟수/총횟수) : {passCount}/{i+1}')
    EnchantSkill()

def CombineMaterial() :
    
    ms.ResetFirst()
    sleep(0.1)

    materialID = input("확인할 매터리얼 ID 입력 :")
    testCount = int(input("반복횟수 입력(회당 30번) :"))


    curPath = path + "/" +time.strftime("_%H%M") + "_combineMaterial"
    if not os.path.isdir(curPath):                                                           
        os.mkdir(curPath)  
    

    ms.Command("additem 999 1000000000")

    for i in range(0, testCount):
        
        ms.Command("cleanupmaterial")
        ms.Command("addmaterial "+materialID+" 120")
        ms.Move(ms.menuPos4)
        sleep(0.05)
        ms.Move(ms.menuPos8)
        sleep(0.05)

        for j in range(0,3):

            ms.Move(ms.materialCombineTabBtn)
            ms.Move(ms.materialAutoInputBtn)
            ms.Move(ms.materialCombineBtn)
            sleep(0.1)
            ms.Move(ms.materialCombineOkBtn)
            sleep(0.5)
            ms.Escape()

            if j == 2 :
                ms.Capture(curPath+"/"+materialID+"_"+str(i))


    ProbTest()

    
def ReinforceEquipment():  
    print("--------------------------------------------------------------")
    print("※주의사항※")   
    print("실행 전 '장비강화.txt'에 아이템 아이디를 한 줄씩 입력해주세요.")   
    print("--------------------------------------------------------------")
    path_result = path + "/result"
    if not os.path.isdir(path_result):                                                           
        os.mkdir(path_result)

    #print("[1]일반강화 [2]다중강화 // [0]뒤로 : 3")
    type2Num = int(input("[1]일반강화 │ [0]뒤로 : "))
    #type2Num = int(ms.InputNum(2))
    if type2Num == 0 : 
        ProbTest()

    count = int(input("테스트 횟수(입력값당 20회) │ [0]뒤로 : "))
    if count == 0 : 
        ProbTest()
        

    print("[1]무기 [2]방어구 [3]장신구 [4]전리품 │ [0]뒤로 : ")
    type0Num = int(ms.InputNum(4))
    if type0Num == 0 : 
        ProbTest()

    if type0Num <=3 :
        print("[1]일반 [2]축복 [3]저주 [4]고대 // [0]뒤로 : ")
        type1Num = int(ms.InputNum(4))
        if type1Num == 0 : 
            ProbTest()
    
    print("확인 내용 : [1]강화 성공 [2]보존// [0]뒤로 : ")
    checkType0 = int(ms.InputNum(2))
    if checkType0 == 0 : 
        ProbTest()
    # else :
    #     print("수호팔찌340/파괴가면341/생명금관342")
    #     print("숙련나팔343/영혼부적344/극복성배345")
    #     print("전리품강화주문서 ID 입력 // [0]뒤로 : ")
    #     bookNum = int(ms.InputNum(999))
    #     if bookNum == 0 : 
    #         ProbTest()



    with open("장비강화.txt") as f:
        lines = f.read().splitlines()

    for itemNum in lines:
        print("총 예상 종료 시간 : "+ms.GetElapsedTime((10+ count * 17)*len(lines)) +")")

    #아이템 별 폴더 추가 생성
        #if folderCheck == 1:
        startTime = time.strftime("_%m%d%H%M")
        
        extraPath = path + "/"+ itemNum + "_"+ startTime
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
        else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
            shutil.rmtree(extraPath)                                                           
            os.mkdir(extraPath)  

        #성공횟수
        #count0 = count // 20
        passCount = 0

        #totalCount = len(lines)
        #count0, count1 = divmod(totalCount , 20)

        if count <= 0 :
                
            print("처음부터 다시 입력해주세요.")
            ReinforceEquipment()

        else :
            if type2Num == 1 :
                print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 17) +")")


                if type0Num <=3 :
                    bookNum = 300 + (type1Num-1)*10 + (type0Num-1)
                elif type0Num == 4:
                    if int(itemNum) <=430008 :
                        bookNum = 340
                    elif int(itemNum) <=431008:
                        bookNum = 341
                    elif int(itemNum) <=432008:
                        bookNum = 342
                    elif int(itemNum) <=433008:
                        bookNum = 343
                    elif int(itemNum) <=434008:
                        bookNum = 344
                    elif int(itemNum) <=435008:
                        bookNum = 345


                for i in range(0,count) :
                    
                    ms.ResetFirst()
                    ms.Command("cleanupinventory")
                    ms.Command("additem "+str(bookNum)+" 10000")
                    ms.Command("addenchantpoint 500000")
                    ms.Command("additem 999 1500000000")

                    ms.Command("additem "+itemNum+" 40")

                    sleep(0.01)
                    #인벤열기 >
                    ms.Move(ms.menuPos1)
                    sleep(1)
                    #강화UI 오픈
                    ms.Move(ms.invenBtnRein)
                    sleep(0.2)
                    
                    ms.Move(ms.invenReinBtnUp1)
                    ms.Move(ms.invenBtn0)
                    ms.Move(ms.invenReinBtnUp0)

                    txtName = path+"/"+str(itemNum)+"_"+str(bookNum)+"_"+str(count)+startTime+".txt"


                    for j in range(0,20) :
                        print(str(j+1) +"/20", end='\r')
                        ms.Move(getattr(ms, 'invenBtn{}'.format(j)))

                        #강화포인트 사용(최초 1회)
                        if j == 0 :
                            ms.Move(ms.reinActivateEnchantBtn0)
                            sleep(0.1)    
                            ms.Move(ms.reinActivateEnchantBtn1)

                        ms.Move(ms.invenReinBtnDown1)
                        sleep(1.5)    
                        ms.Move(ms.centerPos)         
                        sleep(1.5)       
                        ms.CaptureReinforceResult(extraPath+"/"+str(i*20+j))
                        resultText = img2str.getStringFromImg(extraPath+"/"+str(i*20+j)+".jpg",'chi_tra')
                        #img2str.Indiv_Item(txtName,extraPath+"/"+str(i)+".jpg")
                        
                        if resultText.find("成功") != -1 :
                            passCount = passCount + 1


                        sleep(0.3)       
                        ms.Move(ms.invenReinBtnDown1) 

                    ms.ResetFirst()
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
                    sleep(2)
                    ms.ResetFirst()

            # #다중강화
            # elif type2Num == 2 :
            #     print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 18) +")")

                
            #     for i in range(0,count) :
            #         print(str(i+1) +"/" + str(count), end='\r')
            #         ms.ResetFirst()

            #         ms.Command("cleanupinventory")

            #         if type0Num <=3 :
            #             bookNum = 300 + (type1Num-1)*10 + (type0Num-1)
            #         elif type0Num == 4:
            #             if int(itemNum) <=430008:
            #                 bookNum = 340
            #             elif int(itemNum) <=431008:
            #                 bookNum = 341
            #             elif int(itemNum) <=432008:
            #                 bookNum = 342
            #             elif int(itemNum) <=433008:
            #                 bookNum = 343
            #             elif int(itemNum) <=434008:
            #                 bookNum = 344
            #             elif int(itemNum) <=435008:
            #                 bookNum = 345
            #         ms.Command("additem "+str(bookNum)+" 100000")

            #         ms.Command("additem 999 1500000000")
            #         ms.Command("additem "+itemNum+" 16")

            #         sleep(0.01)
            #         #인벤열기 >
            #         ms.Move(ms.menuPos1)
            #         sleep(ms.waitTime)
            #         #강화UI 오픈
            #         ms.Move(ms.invenBtnRein)
            #         sleep(0.2)
            #         #다중강화 클릭
            #         ms.Move(ms.invenReinBtnLeft1)
            #         #주문서등록
            #         ms.Move(ms.invenReinBtnUp1)
            #         ms.Move(ms.invenBtn0)
            #         #장비등록준비
            #         ms.Move(ms.invenReinBtnUp0)
            #         #장비등록
            #         for k in range(0,16):
            #             ms.Move(getattr(ms, 'invenBtn{}'.format(k)))
                    
            #         txtName = path+"/"+str(itemNum)+"_"+str(bookNum)+"_"+str(count*16)+startTime+".txt"
            #         #강화도 클릭
            #         phaseNum = (int(itemNum) % 10) + 1
            #         ms.Move(getattr(ms, 'reinPhase{}'.format(phaseNum)))

            #         #강화시작 클릭
            #         ms.Move(ms.invenReinBtnDown2)

            #         #2초대기     
            #         sleep(3)       

            #         #스샷저장
            #         if phaseNum < 9 :
            #             ms.CaptureReinMultiResultBox(extraPath+"/"+str(i))
            #         else : 
            #             ms.Capture(extraPath+"/"+str(i))


            #         #반복종료 리턴(끝)
        totalCount = count * 20

        testResultText =\
            '\n'\
            +str(datetime.now())\
            +","+str(itemNum)\
            +","+str(bookNum)\
            +","+str(totalCount)\
            +","+str(passCount)\
            +","+str(round(passCount/totalCount*100,2))

        if not os.path.isfile(path_result+"./result.txt"):                                                           
            with open(path_result+"./result.txt",'a',encoding='utf-8') as tx:
                tx.write("날짜,itemID,bookNum,count,passCount,passProb")    

        with open(path_result+"./result.txt",'a',encoding='utf-8') as tx:
            tx.write(testResultText)

    ReinforceEquipment()



def EnchantSoul():
    print("--------------------------------------------------------------") 
    print("실행 전 영혼무기.txt에 아이템 ID, 영혼석.txt에 영혼석 ID를 한 줄씩 입력해주세요.")   
    print("--------------------------------------------------------------")

    nation_code = input("0:KR, 1:TW")

    lang_code = 'kor' if nation_code == "0" else 'chi_tra'
    find_str = '성공' if nation_code == "0" else '成功'


    contentPath = path + "/EnchantSoul"
    if not os.path.isdir(contentPath):                                                           
        os.mkdir(contentPath)      

    output_file_name = fr'{contentPath}/결과_{time.strftime("%y%m%d_%H%M%S")}.xlsx'

    count = int(input("영혼 부여 횟수를 입력해주세요(1~) : "))
    
    with open("영혼무기.txt") as f1:
        itemLines = f1.read().splitlines()
    with open("영혼석.txt") as f2:
        scrollLines = f2.read().splitlines()

    print("전체 실행횟수 : " + str(len(itemLines)))
    print("전체 예상 종료 시각 : " + str(ms.GetElapsedTime((10+count * 3.7 )* float(len(itemLines)))))


    for i in range(0,len(itemLines)):
        data = []
        print("3초 후 시작합니다..")
        sleep(3)
        print("실행 중... (예상 종료 시각 : "+ms.GetElapsedTime(10+count * 3.7) +")")
        #텍스트는 어차피 결과 쌓으면되니까 메인에 생성, 스크린샷은 아이템 폴더 내 내부로
        txtName = contentPath+"/"+str(itemLines[i])
        resultTxtFileName = contentPath+"/result.txt"

        #extraPath = extraPath + "/"+ itemLines[i] + time.strftime("_%H%M")
        extraPath = contentPath + "/"+ itemLines[i]
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
        else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
            shutil.rmtree(extraPath)                                                           
            os.mkdir(extraPath)  
            
        passCount = 0
        enchantPrice = ""

    #장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")

        ms.Command("additem "+ itemLines[i] +" 25")
        ms.Command("additem "+ scrollLines[i] +" "+str(count))

        ms.Command("additem 999 1500000000")
        ms.Move(ms.menuPos1)
        sleep(0.1)
        ms.Move(ms.invenBtnUp2)
        ms.Move(ms.invenBtn0)
    #영혼석 UI 오픈
        ms.Move(ms.invenBtn0)
        sleep(1)
        #대만
        #cardNameText = img2str.getStringFromImg(ms.captureSomeBox2("soulEnchantCardNameBox",extraPath+"/cardNameText"),'chi_tra')
        cardNameText = img2str.getStringFromImg(ms.captureSomeBox2("soulEnchantCardNameBox",extraPath+"/cardNameText"),lang_code)
        
        for j in range(0,count):
            print(str(j+1) +"/" + str(count), end='\r')
            ms.Move(ms.soulTargetBtn)
            if j == 0:
                ms.sleep(1)
                result_item_text = img2str.getStringFromImg(ms.captureSomeBox2("soulEnchantResultNameBox",extraPath+"/result_item_text"),lang_code)
                enchantPrice = img2str.getNumberFromImg(ms.captureSomeBox2("soulEnchantPriceBox",extraPath+"/priceText"))
                ms.sleep(1)
            ms.Move(ms.soulEnchantBtn)
            sleep(1.5)    
            ms.Move(ms.centerPos)         
            sleep(1.5)     
            
            ms.CaptureReinforceResult(extraPath+"/"+str(j))

            resultText = img2str.getStringFromImg(extraPath+"/"+str(j)+".jpg",lang_code)
            if resultText.find(find_str) != -1 :
                passCount = passCount + 1

            sleep(0.3)       
            ms.Move(ms.soulEnchantBtn)

        #data.append([itemLines[i],scrollLines[i],cardNameText,result_item_text,enchantPrice,passCount,count,f'{round(passCount/count*100,3)}%'])
        data = [[itemLines[i],scrollLines[i],cardNameText,result_item_text,enchantPrice,passCount,count,f'{round(passCount/count*100,3)}%']]
        columns=['재료장비ID', '영혼석ID', '변신명', '결과명','비용', '성공횟수','총횟수','성공률']
        result_df = pd.DataFrame(data, columns=columns)
        
        ms.save_df_to_excel(output_file_name,result_df)
        #result_df = pd.DataFrame(data, columns=['재료장비ID', '영혼석ID', '변신명', '결과명','비용', '성공횟수','총횟수','성공률'])

        #result_df.to_excel(output_file_name, index=False)

    os.startfile(os.path.abspath(output_file_name))
    #EnchantSoul()
    

    
def slotEnchantProbTest():
    
    ms.clear()


    testCount = int(input("최소 실행 횟수 :"))
    #maxCount = int(input("최소 실패 횟수 :"))#100
    materialSlotEnchantTotalLevel = int(input("최대 강화 레벨(장비18|매터리얼26) : "))#25
        
    with open("슬롯강화상세.txt") as f:
        lines = f.read().splitlines()

    #print("총 예상 종료 시간 : "+ms.GetElapsedTime((10+ count * 108)*len(lines)) )
    #print("itemID,scrollID,isEnchanted,isBlessed,isKept,isSafe")

    for k in range(0,len(lines)):
    #장비/매터리얼 , 일반/고대 , 슬롯번호
    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        slotEnchantType, scrollType, slotNum = lines[k].split(',')
    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        print(slotEnchantType, scrollType, slotNum )
        slotEnchantType = int(slotEnchantType)
        scrollType = int(scrollType)
        slotNum = int(slotNum)
        
        #slotEnchantType = int(input("[0]장비 [1]매터리얼"))
        #scrollType = int(input("[0]일반 [1]고대"))#304 344
        #slotNum = int(input("슬롯번호(0~7) : "))#304 344

        itemID = 0
        directoryName = "_slotEnchant_material"
        if slotEnchantType == 0:    
            directoryName = "_slotEnchant_equipment"

        if scrollType == 0 :
            if slotEnchantType == 1 :
                itemID = 304
            else :
                itemID = 303
        else :
            if slotEnchantType == 1 :
                itemID = 334
            else :
                itemID = 333

        curPath = path + "/" +time.strftime("_%H%M") + directoryName
        if not os.path.isdir(curPath):                                                           
            os.mkdir(curPath)  
        
        print("시작시각 : ",ms.GetCurrentTime())
        print("3초 후 시작합니다.")
        ms.sleep(3)
        print("실행 중...", end='\r')
        #ms.ResetFirst()

        maxCount = testCount
        #materialSlotEnchantTotalLevel = 25
        failCountArray = [0] * materialSlotEnchantTotalLevel
        passCountArray = [0] * materialSlotEnchantTotalLevel
        totalCountArray = [0] * materialSlotEnchantTotalLevel
        costArray = [""] * materialSlotEnchantTotalLevel
            
        # #ms.Command("chengeequipslotenchantadvantagepercent 0")
        # ms.Command("cleanupequipslotenchant")

        # ms.Move(ms.menuPos4)
        # ms.Move(ms.menuPos11)

        # if slotEnchantType == 0 :
        #     ms.Move(ms.slotEnchantTypeBtn_equipment)
        # else :
        #     ms.Move(ms.slotEnchantTypeBtn_material)
            
            
        # ms.Move(getattr(ms, 'slotEnchantSlot{}'.format(slotNum)))
        
        # ms.sleep(0.1)
            
        # if scrollType == 1 :
        #     ms.Move(ms.slotEnchantToggleScroll)
            
        # ms.sleep(0.1)

        ms.ResetFirst()
        #ms.Command("chengeequipslotenchantadvantagepercent 0")
        #ms.Command("cleanupequipslotenchant")
        ms.Command("cleanupinventory")
        ms.Command("additem 999 2000000000")
        ms.Command("additem "+str(itemID)+" 500000")

        ms.Move(ms.menuPos4)
        ms.Move(ms.menuPos11)

        
        if slotEnchantType == 0 :
            ms.Move(ms.slotEnchantTypeBtn_equipment)
        else :
            ms.Move(ms.slotEnchantTypeBtn_material)
            
        ms.Move(getattr(ms, 'slotEnchantSlot{}'.format(slotNum)))
        ms.sleep(0.1)


        if scrollType == 1 :
            ms.Move(ms.slotEnchantToggleScroll)
            
        ms.sleep(0.1)

        for x in range(testCount):

            tempArray = np.array(totalCountArray[0:len(totalCountArray)])
            if np.all(tempArray>=maxCount) :
                #tempArray = []
                #print(f'{i}단계 이후 단계 모두 테스트 횟수 달성하여 0단계로 복귀')

                break


            ms.Command("chengeequipslotenchantadvantagepercent 0")
            ms.Command("cleanupequipslotenchant")

            if slotEnchantType == 0 :
                ms.Move(ms.slotEnchantTypeBtn_equipment)
            else :
                ms.Move(ms.slotEnchantTypeBtn_material)
                
                    
            ms.Move(getattr(ms, 'slotEnchantSlot{}'.format(slotNum)))
            ms.sleep(0.1)
            ms.Move(getattr(ms, 'slotEnchantSlot{}'.format(slotNum)))
            ms.sleep(0.1)

            # i : 등급
            for i in range(materialSlotEnchantTotalLevel):#매터슬롯강화총단계
                #print(i, "단계 \r",i) 

                tempArray = np.array(totalCountArray[i:len(totalCountArray)])
                if np.all(tempArray>=maxCount) :
                    #tempArray = []
                    print(f'{i}단계 이후 단계 모두 테스트 횟수 달성하여 0단계로 복귀')

                    break

                #failCount = 0
                while True :
                    

                    if totalCountArray[i] >= maxCount :
                        #print("테스트 횟수 초과로 현재 단계 패스")
                        print(f'{i}단계 : {totalCountArray[i]}번 중 {passCountArray[i]}번 성공 (테스트 횟수 달성하여 종료)')

                        ms.Command("chengeequipslotenchantadvantagepercent 1000000")
                        ms.Move(ms.slotEnchantBtn)
                        ms.sleep(1)
                        ms.Command("chengeequipslotenchantadvantagepercent 0")
                        break

                    ms.Move(ms.slotEnchantBtn)
                    ms.sleep(0.3)
                    resultImg = ms.captureSomeBox("slotEnchantResultBox")
                    resultText = img2str.getKorTextFromImg(resultImg)
                    costImg = ms.captureSomeBox("slotEnchantCostBox")
                    costArray[i] = img2str.getKorTextFromImg(costImg)

                    ms.sleep(1)
                    if resultText.find("성공") == -1 : #실패 > 현재 단계 총 100번까지 반복 > 중간에 성공하면 브레이크 후 다음 단계.
                        #failCount = failCount + 1
                        failCountArray[i] = failCountArray[i] + 1
                        totalCountArray[i] = passCountArray[i] + failCountArray[i]
                        

                    else :
                        #failCountArray[i] = failCountArray[i] + failCount
                        passCountArray[i] = passCountArray[i] + 1
                        totalCountArray[i] = passCountArray[i] + failCountArray[i]
                        #print("성공 {0}번, 실패 {1}번",failCountArray[i],passCountArray[i])
                        #debug = f'{i}단계 : {passCountArray[i]}번 성공, {failCountArray[i]}번 실패'
                        print(f'{i}단계 : {totalCountArray[i]}번 중 {passCountArray[i]}번 성공')
                        break


        for j in range(materialSlotEnchantTotalLevel):
            #print("j : ",j)
            testResultText =\
            str(datetime.now())\
            +"|"+str(slotEnchantType)\
            +"|"+str(slotNum)\
            +"|"+str(j)\
            +"|"+str(scrollType)\
            +"|"+str(passCountArray[j])\
            +"|"+str(failCountArray[j] + passCountArray[j])\
            +"|"+str(round(passCountArray[j]/(failCountArray[j] + passCountArray[j])*100,2))+"%"\
            +"|"+str(costArray[j])#\
            #+'\n'

            if not os.path.isfile(curPath+"./result.txt"):                                                           
                with open(curPath+"./result.txt",'a',encoding='utf-8') as tx:
                    tx.write("날짜|타입(장비/매터리얼)|슬롯번호|강화단계|고대여부|성공횟수|총횟수|성공률|강화비용\n")    

            with open(curPath+"./result.txt",'a',encoding='utf-8') as tx:
                tx.write(testResultText)
    
    print("종료시각 : ",ms.GetCurrentTime())


def ReinforceEquipment_Detail():  
    print(ms.PrintUB())
    print("장비강화상세.txt")   
    print("아이템ID,주문서ID,확률업(on:1/off:0)")       
    print(ms.PrintUB())

    path_result = path + "/result_reinforce_detail"
    path_resultTxtFile = path_result + "/result" + time.strftime("_%Y%m%d") + ".txt"

    if not os.path.isdir(path_result):                                                           
        os.mkdir(path_result)

    lang = int(input("언어 설정 | [0]한국[1]대만 : "))
    curLangCode = ""
    if lang == 0 :
        curLangCode = "kor"
    elif lang == 1:
        curLangCode = "chi_tra"

    count = int(input("테스트 횟수(입력값당 20회) │ [0]뒤로 : "))
    if count == 0 : 
        ProbTest()

    with open("장비강화상세.txt") as f:
        lines = f.read().splitlines()

    print("총 예상 종료 시간 : "+ms.GetElapsedTime((10+ count * 108)*len(lines)) )
    print("itemID,scrollID,isEnchanted,isBlessed,isKept,isSafe")

    for k in range(1,len(lines)):

    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        itemID, scrollID, isEnchanted, isBlessed, isKept, isSafe = lines[k].split(',')
    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    #아이템 별 폴더 추가 생성
        startTime = time.strftime("%H%M")
        
        extraPath = path + "/"+ itemID + "_"+ startTime
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
        else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
            shutil.rmtree(extraPath)                                                           
            os.mkdir(extraPath)  

        #성공횟수
        passCount = 0
        #축복 전용
        passCount1 = 0
        passCount2 = 0
        passCount3 = 0

        if count <= 0 :
                
            print("처음부터 다시 입력해주세요.")
            ReinforceEquipment()

        else :
            #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 108) +")")

            print(str(k) +"/"+str(len(lines)-1) + " | "+ lines[k])


            for i in range(0,count) :

                
                ms.ResetFirst()
                ms.Command("cleanupinventory")
                ms.Command("additem "+str(scrollID)+" 10000")
                ms.Command("addenchantpoint 500000")
                ms.Command("additem 999 1500000000")

                ms.Command("additem "+itemID+" 40")

                sleep(0.01)
                #인벤열기 >
                ms.Move(ms.menuPos1)
                sleep(1)
                #강화UI 오픈
                ms.Move(ms.invenBtnRein)
                sleep(0.2)
                
                ms.Move(ms.invenReinBtnUp1)
                ms.Move(ms.invenBtn0)
                ms.Move(ms.invenReinBtnUp0)

                #txtName = path+"/"+str(itemID)+"_"+str(scrollID)+"_"+str(count)+startTime+".txt"


                for j in range(0,20) :
                    print(str((j+1)*i) +"/"+ str(count*20), end='\r')
                    sleep(0.1)
                    ms.Move(getattr(ms, 'invenBtn{}'.format(j)))

                    #강화포인트 사용(최초 1회)
                    if isEnchanted == "1" and j == 0 :
                        ms.Move(ms.reinActivateEnchantBtn0)
                        sleep(0.1)    
                        ms.Move(ms.reinActivateEnchantBtn1)

                    ms.Move(ms.invenReinBtnDown1)
                    sleep(1.5)    

                    if isSafe == "0" :
                        ms.Move(ms.centerPos)         
                        sleep(1.5)       
                        ms.CaptureReinforceResult(extraPath+"/"+str(i*20+j))
                        resultText = img2str.getStringFromImg(extraPath+"/"+str(i*20+j)+".jpg",curLangCode)#대만 : 'chi_tra' 한국 : 'kor'
                        #img2str.Indiv_Item(txtName,extraPath+"/"+str(i)+".jpg")
                    
                        expectedText = ""

                        if isKept == "1" :
                            if lang == 0 :
                                expectedText = "보존"#대만 : 沒有 국내 : 보존
                            elif lang == 1 :
                                expectedText = "沒有"
                        else :
                            if lang == 0 :
                                expectedText = "성공"#대만 : 沒有 국내 : 보존
                            elif lang == 1 :
                                expectedText = "成功"
                            #expectedText ="성공"#대만 : 成功 국내 : 성공

                        
                        sleep(0.3)       
                        ms.Move(ms.invenReinBtnDown1) 
                        sleep(0.3)       
                        

                        if resultText.find(expectedText) != -1 :
                            passCount = passCount + 1
                            
                            if isBlessed == "1":
                                try : 
                                    resultNameText = img2str.getNumberFromImg( ms.captureSomeBox2("reinResultNameTextBox",extraPath+"/"+str(i*20+j)+"_blessed"))
                                    curValue = int(itemID) % 10
                                    plusValue = int(resultNameText[1])
                                    if plusValue - curValue == 1:
                                        passCount1 = passCount1 + 1
                                    elif plusValue - curValue == 2:
                                        passCount2 = passCount2 + 1
                                    elif plusValue - curValue == 3:
                                        passCount3 = passCount3 + 1
                                
                                except : 
                                    print("error 1")
                            
                    else : 
                        if isBlessed == "1":
                            
                            try : 
                                resultNameText = img2str.getNumberFromImg( ms.captureSomeBox2("reinResultNameTextBox",extraPath+"/"+str(i*20+j)+"_blessed"))
                                curValue = int(itemID) % 10
                                plusValue = int(resultNameText[1])
                                if plusValue - curValue == 1:
                                    passCount1 = passCount1 + 1
                                elif plusValue - curValue == 2:
                                    passCount2 = passCount2 + 1
                                elif plusValue - curValue == 3:
                                    passCount3 = passCount3 + 1
                            
                            except : 
                                print("error 1")

                ms.ResetFirst()
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
                sleep(2)
                ms.ResetFirst()

        totalCount = count * 20

        
        if isBlessed == "1":
            passCountArray = np.array([passCount1,passCount2,passCount3])
            passProbArray = np.round(passCountArray/totalCount*100,2)
            
            #passCount = str(str(passCount1)+" / "+str(passCount2)+" / "+str(passCount3)+" / ")
            #print(passCount)
        else :
            passCountArray = np.array([passCount])
            passProbArray = np.round(passCountArray/totalCount*100,2)



        testResultText =\
            '\n'\
            +str(datetime.now())\
            +"|"+str(itemID)\
            +"|"+str(scrollID)\
            +"|"+str(isEnchanted)\
            +"|"+str(isBlessed)\
            +"|"+str(isKept)\
            +"|"+str(isSafe)\
            +"|"+str(totalCount)\
            +"|"+str(' / '.join(map(str,passCountArray)))\
            +"|"+str(' / '.join(map(str,passProbArray)))

        if not os.path.isfile(path_resultTxtFile):                                                           
            with open(path_resultTxtFile,'a',encoding='utf-8') as tx:
                tx.write("날짜|itemID|scrollID|isEnchanted|isBlessed|isKept|isSafe|totalCount|passCount|passProb")    

        with open(path_resultTxtFile,'a',encoding='utf-8') as tx:
            tx.write(testResultText)
            

    
def probTest_spotEnchant():#221020
    
    ms.clear()

    testCount = int(input("최소 실행 횟수 :"))
    maxLevel = int(input("최대 강화 레벨(15) : "))#25
        
    with open("스팟강화상세.txt",encoding="UTF-8") as f:
        lines = f.read().splitlines()

    for k in range(1,len(lines)):
    #변신/서번트, 유게/벨제/헤라/가이/유피
    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        cardType, groupNum = lines[k].split(',')
    #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
        print(cardType, groupNum )
        cardType = int(cardType)
        groupNum = int(groupNum)

        itemID = 0
        directoryName = "_spotEnchant"

        curPath = path + "/" +time.strftime("_%H%M") + directoryName
        if not os.path.isdir(curPath):                                                           
            os.mkdir(curPath)  
        
        print("시작시각 : ",ms.GetCurrentTime())
        print("3초 후 시작합니다.")
        ms.sleep(3)
        #print("실행 중...", end='\r')

        maxCount = testCount
        failCountArray = [0] * maxLevel
        passCountArray = [0] * maxLevel
        totalCountArray = [0] * maxLevel
        costArray = [""] * maxLevel

        ms.Command("pushlevelpoint "+str(cardType)+" 5000000")
        

    ####################

        for x in range(maxCount):

            tempArray = np.array(totalCountArray[0:len(totalCountArray)])
            if np.all(tempArray>=maxCount) :
                break
    #region 초기화 후 재접속

            ms.Command("initspotenchant "+str(cardType))


            ms.ResetFirst()

            ms.Move(ms.menuPos4)
            ms.Move(ms.menuPos20)
            ms.sleep(0.1)
            ms.Move(ms.menuMiddleUpperTab5)
            ms.Move(ms.goCharacterSelectPageBtn)
            ms.sleep(0.01)
            ms.Move(ms.okPos)
            ms.sleep(0.2)

            ms.sleep(2)

            tempText = ""

            while tempText.find("선택") == -1 :
                waitTextFileName = ms.captureSomeBox("selectCharacterNameBox")
                tempText = img2str.getStringFromImg(waitTextFileName,'kor')
                #print("텍스트 대기 중:", tempText)
                sleep(0.3)

            ms.Move(ms.characterCreateBtn)
            ms.sleep(15)

            while tempText.find("AUTO") == -1 :
                waitTextFileName = ms.captureSomeBox("autoBtnBox")
                tempText = img2str.getStringFromImg(waitTextFileName,'eng')
                #print("텍스트 대기 중:", tempText)
                sleep(0.3)


            ms.Move(ms.menuPos4)

            if cardType == 0 :
                ms.Move(ms.menuPos6)
            else :
                ms.Move(ms.menuPos7)
            ms.sleep(1)
                
            ms.Move(ms.uiTabBtn4_7)
            ms.sleep(0.1)
                
            ms.Move(getattr(ms, 'cardSpotGroubTabBtn{}'.format(groupNum)))
            ms.sleep(0.1)

#endregion



            # i : 등급
            for i in range(maxLevel):#매터슬롯강화총단계
                #print(i, "단계 \r",i) 

                tempArray = np.array(totalCountArray[i:len(totalCountArray)])
                if np.all(tempArray>=maxCount) :
                    #tempArray = []
                    print(f'{i}단계 이후 단계 모두 테스트 횟수 달성하여 0단계로 복귀')

                    break

                #failCount = 0
                while True :
                    

                    if totalCountArray[i] >= maxCount :
                        #print("테스트 횟수 초과로 현재 단계 패스")
                        print(f'{i}단계 : {totalCountArray[i]}번 중 {passCountArray[i]}번 성공 (테스트 횟수 달성하여 종료)')

    #region 횟수 초과로 다음단계 넘어가기 (마지막 단계 제외)
                        if i + 1 < maxLevel : 

                            tempText = ""
                            while tempText.find("성공") == -1 :
                                        
                                ms.Move(ms.cardSpotActivateBtn)
                                ms.sleep(0.5)
                                ms.Move(ms.cardSpotActivateOkBtn)
                                ms.sleep(1.5)

                                waitTextFileName = ms.captureSomeBox("cardSpotEnchantResultBox")
                                tempText = img2str.getStringFromImg(waitTextFileName,'kor')
    #endregion

                        break

                    #region 결과확인
                    print(f'{totalCountArray[i]}/{maxCount}', end='\r')
                    ms.Move(ms.cardSpotActivateBtn)
                    ms.sleep(0.5)
                    ms.Move(ms.cardSpotActivateOkBtn)
                    ms.sleep(1.5)

                    tempCaptureFileName = ms.captureSomeBox("cardSpotEnchantResultBox")
                    resultText = img2str.getStringFromImg(tempCaptureFileName,'kor')
                    #endregion

                    ms.sleep(1)
                    if resultText.find("성공") == -1 : #실패 > 현재 단계 총 100번까지 반복 > 중간에 성공하면 브레이크 후 다음 단계.
                        #failCount = failCount + 1
                        failCountArray[i] = failCountArray[i] + 1
                        totalCountArray[i] = passCountArray[i] + failCountArray[i]
                        

                    else :
                        #failCountArray[i] = failCountArray[i] + failCount
                        passCountArray[i] = passCountArray[i] + 1
                        totalCountArray[i] = passCountArray[i] + failCountArray[i]
                        #print("성공 {0}번, 실패 {1}번",failCountArray[i],passCountArray[i])
                        #debug = f'{i}단계 : {passCountArray[i]}번 성공, {failCountArray[i]}번 실패'
                        print(f'{i}단계 : {totalCountArray[i]}번 중 {passCountArray[i]}번 성공')
                        break


                    if i + 1 != maxLevel :
                        tempArray = np.array(totalCountArray[(i+1):len(totalCountArray)])
                        if np.all(tempArray>=maxCount) :
                            #tempArray = []
                            print(f'{i+1}단계 이후 단계 모두 테스트 횟수 달성하여 0단계로 복귀')

                            break


        resultTextFileName = curPath+"./result"+time.strftime("_%Y%m%d_%H%M")+".txt"

        for j in range(maxLevel):
            #print("j : ",j)
            testResultText =\
            str(datetime.now())\
            +"|"+str(cardType)\
            +"|"+str(groupNum)\
            +"|"+str(j)\
            +"|"+str(passCountArray[j])\
            +"|"+str(failCountArray[j] + passCountArray[j])\
            +"|"+str(round(passCountArray[j]/(failCountArray[j] + passCountArray[j])*100,2))+"%"\
            +'\n'

            if not os.path.isfile(resultTextFileName):                                                           
                with open(resultTextFileName,'a',encoding='utf-8') as tx:
                    tx.write("날짜|타입(변신/서번트)|슬롯번호|강화단계|성공횟수|총횟수|성공률\n")    

            with open(resultTextFileName,'a',encoding='utf-8') as tx:
                tx.write(testResultText)
        print("개별종료시각 : ",ms.GetCurrentTime())
    
    print("전체종료시각 : ",ms.GetCurrentTime())
###############

def save_df_to_excel(output_file_name, df):
    if os.path.exists(output_file_name):
        # 파일이 이미 존재하면 기존 내용을 불러옵니다
        existing_df = pd.read_excel(output_file_name)
        # 기존 DataFrame에 이어붙입니다 (column은 제외)
        combined_df = pd.concat([existing_df, df], axis=0, ignore_index=True)
    else:
        # 파일이 존재하지 않으면 새 파일로 저장
        combined_df = df

    combined_df.to_excel(output_file_name, index=False)
    print(f"Data saved to {output_file_name}")


if __name__ == "__main__" : 
    ProbTest()