#from img2str import Img2Str
import enum
import pyautogui as pag
from time import sleep
import os
import msdata as ms
import time
import mergeImg
import pandas
import img2str as i2s
from datetime import datetime
import re
#import img2


line_UL = "┌"
line_UR = "┐"
line_DL = "└"
line_DR = "┘"
line_H = "│"
line_W = "─"
nameText = "장비 능력치 스크린샷 통합"
verText = "ver 1.2"
dateText = "210713"
makerText = "made by sms"
desText = "  " + "+0~+13강의 장비 아이템의 상세 내용 및 추가 정보를 스샷합니다.\n이미지 병합 기능 추가"
warnText= "  " + "테스트 전 장착한 장비를 모두 해제하고, 인벤토리 내부 슬롯을 최상단으로 맞추세요."

path = f'./screenshot/equipCheck{time.strftime("_%y%m%d")}'

if not os.path.isdir(path):                                                           
    os.mkdir(path)   

def SetMainUI(_nameText,_verText,_dateText,_makerText):
    
    ms.PrintUB()
    print(nameText)
    ms.PrintUB()

    # print("│" + _nameText.center(100) +"│")
    # print("│" + "│".rjust(107,'─'))
    # print("│" + (_verText + " / " + _dateText + " / " + _makerText).rjust(106) +"│")
    # print("├" + "┤".rjust(107,'─'))


def EquipCheck():

    global path, mergePath
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
    mergePath = path + "/Merge"
    if not os.path.isdir(mergePath):                                                           
        os.mkdir(mergePath)      

    SetMainUI(nameText,verText,dateText,makerText)
    # print("┌" + "┐".rjust(107,'─'))
    # print("│" + nameText.center(100) +"│")
    # print("│" + "│".rjust(107,'─'))
    # print("│" + (verText + " / " + dateText + " / " + makerText).rjust(106) +"│")
    # print("├" + "┤".rjust(107,'─'))
    #print(line_H + "※ 설명 ※".center(102) +"│")
    
    #ms.PrintUB()
    #print("├" + "┤".rjust(107,'─'))
    #print(desText)
    #print("├" + "┤".rjust(107,'─'))
    #print(line_H + "※ 사전세팅 ※".center(100) +"│")
    #print("├" + "┤".rjust(107,'─'))
    #print(warnText)
    #print("└" + "┘".rjust(107,'─'))
    #print("┌" + "┐".rjust(107,'─'))
    print("장비 타입")
    print("[1]무기/방어구(최대+13강)\n[2]장신구(최대+9강)\n[3]영혼무기(최대+13강)")
    
    ms.PrintUB()
    print("[0]테스트메뉴")
    ms.PrintUB()
    #print("└" + "┘".rjust(107,'─'))
    global equipType
    equipType = int(ms.InputNum(3))
    ms.clear()
    if equipType==0:
        ms.TestMenu()
    else: 
        
        
        ms.PrintUB()
        print("[1]아이템 ID\n[2]텍스트 파일")
        ms.PrintUB()
        print("[0]뒤로")
        ms.PrintUB()
        #print("---------------------------------------------------------------")
        num2 = int(ms.InputNum(3))
        ms.clear()
        if num2==0:
            EquipCheck()
        elif num2 ==1:
            EquipCheck1()
        elif num2 ==2:
            EquipCheck2()
        # elif num2 ==2:
        #     EquipCheck2()

        
        EquipCheck()
        


def EquipCheck1():
   
    waitTime = 0.01
    waitTime2 = 0.2

    itemNum = input("+0강 아이템 id를 입력해주세요([0]테스트메뉴) : ")
    while itemNum!="0":
        print("실행 중... (예상 소요 시간 : 알 수 없음)")
#아이템 별 폴더 추가 생성 하지말자
        #extraPath = path + "/"+ itemNum
        extraPath = path
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)        

#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")

        cmdStr= "additems"
        for j in range(0,14):
            cmdStr += " " + str(int(itemNum)+j)
        ms.Command(cmdStr,1)
        sleep(0.01)
#인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        
        for i in range(0,14):
            if equipType == 2 and i == 10:
                break
    #첫번째 클릭 > 상세 클릭> 대기후스샷0> 
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            ms.Move(ms.invenBtnDown2)
            sleep(1.5)
            ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_0")
    #설명창 위로밀기 > 대기 후 스샷1 > 
            ms.Move(ms.invenDesPos)
            ms.DragUp(ms.invenDesPos)
            ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_1")
    #추가정보클릭 > 대기후스샷2 > x버튼
            ms.Move(ms.invenAddDesPos)
            ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_2")

            if equipType == 3 :
                ms.Move(ms.invenSoulBtn)
                ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_3")
                ms.Move(ms.invenExitBtn)
            else :
                
                ms.Move(ms.invenExitBtn)

        mergeImg.MergeImg_Equip(itemNum, equipType,extraPath)

        print("스샷 경로 : "+extraPath)
        itemNum = input("+0강 아이템 id를 입력해주세요([0]테스트메뉴) : ")

        

def EquipCheck2():
   
    waitTime = 0.01
    waitTime2 = 0.2
    ms.PrintUB()
    fileName = input("2txt 파일명 입력(기본 : 장비수치)([0]돌아가기) : ")
    if fileName =="0":
        EquipCheck()
    elif fileName =="":
        fileName = "장비수치"

    try :
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
    except : 
        EquipCheck2()

    ms.clear()
    
    loopCount = 1
    for itemNum in lines:
        print("실행 중... (예상 소요 시간 : 알 수 없음)")
        print(str(loopCount) + "/" + str(len(lines)))

        extraPath = path

#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")

        cmdStr= "additems"
        for j in range(0,14):
            cmdStr += " " + str(int(itemNum)+j)
        ms.Command(cmdStr,1)
        sleep(0.01)
#인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        
        for i in range(0,14):
            if equipType == 2 and i == 10:
                break
            
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            ms.Move(ms.invenBtnDown2)
            sleep(1.3)
            #equipStatNameList = img2str.getKorTextFromImg(ms.captureSomeBox(ms.equipStatNameBox))
            #equipStatAmountList = img2str.getNumberFromImg(ms.captureSomeBox(ms.equipStatAmountBox))
            ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_0")
    #설명창 위로밀기 > 대기 후 스샷1 > 
            ms.Move(ms.invenDesPos)
            ms.DragUp(ms.invenDesPos)
            ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_1")
    #추가정보클릭 > 대기후스샷2 > x버튼
            ms.Move(ms.invenAddDesPos)
            sleep(0.1)
            ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_2")
            if equipType == 3 :
                ms.Move(ms.invenSoulBtn)
                ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_3")
                ms.Move(ms.invenExitBtn)
            else :
                
                ms.Move(ms.invenExitBtn)
        mergeImg.MergeImg_Equip(itemNum,equipType,extraPath)

            
        #print("스샷 경로 : "+extraPath)
        loopCount = loopCount +1

def EquipCheck3():
    """한장만 찍기"""
   
    waitTime = 0.01
    waitTime2 = 0.2
    ms.PrintUB()
    fileName = input("txt 파일명 입력(기본 : 장비수치)([0]돌아가기) : ")

    if fileName =="0":
        EquipCheck()
    elif fileName =="":
        fileName = "장비수치"
    try :
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
    except : 
        EquipCheck3()

    ms.clear()
    
    loopCount = 1

    
    for itemNum in lines:
        print("실행 중... (예상 소요 시간 : 알 수 없음)")
        print(str(loopCount) + "/" + str(len(lines)))

        extraPath = path
        totalList = [str]
        totalList.clear()
#장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")

        cmdStr= "additems"
        for j in range(0,14):
            cmdStr += " " + str(int(itemNum)+j)
        ms.Command(cmdStr,1)
        sleep(0.01)
#인벤열기 >
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime)
        
        for i in range(0,14):
            #if equipType == 2 and i == 10:
            #    break
            
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            ms.Move(ms.invenBtnDown2)
            sleep(1.3)
            ms.CaptureInvenDes(extraPath+"/"+str(int(itemNum)+i)+"_0")

            equipStatNameList = i2s.getKorTextFromImg(ms.captureSomeBox("equipStatNameBox")).splitlines()
            equipStatAmountList = i2s.getNumberTextFromImg(ms.captureSomeBox("equipStatAmountBox")).splitlines()
            
            ms.Move(ms.invenExitBtn)
            print(f'{equipStatNameList=}')
            print(f'{equipStatAmountList=}')
            tempStr = ""
            for i in range(0,len(equipStatAmountList)) :
                tempStr += (f'{equipStatNameList[i]}{equipStatAmountList[i]}/')
            
            tempStr = tempStr.replace('력','')
            tempStr = tempStr.replace(' ','')
            totalList.append(tempStr)
            #totalList.append("\n")
        #mergeImg.MergeImg_Equip(itemNum,equipType,extraPath)


        print(totalList)        
        resultTxtFileName = f'equipCheckResult_{time.strftime("_%y%m%d_%H%M%S")}.txt'
        #if not os.path.isfile(resultTxtFileName):                                                           
        #    with open(resultTxtFileName,'a',encoding='utf-8') as tx:
        #        tx.write("날짜|영혼부여대상장비ID|영혼석ID|전용변신이름|영혼부여비용|성공횟수|총횟수|성공률")    

        with open(resultTxtFileName,'a',encoding='utf-8') as tx:
            tx.write('\n'.join(totalList))    
        #print("스샷 경로 : "+extraPath)
        loopCount = loopCount +1

#장신구 : 50초, 무기  : 64초


def EquipCheck4():
    """
    인벤토리 내 장비 수치 스크린샷+숫자인식 > 텍스트 파일생성
    """
    ms.PrintUB()
    fileName = input("txt 파일명 입력(기본 : 장비수치)([0]돌아가기) : ")

    if fileName =="0":
        EquipCheck()
    elif fileName =="":
        fileName = "장비수치"
    try :
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
    except : 
        EquipCheck4()

    ms.clear()
    
    loopCount = 1
    resultTxtFileName = f'{path}/equipCheckResult_{time.strftime("_%y%m%d_%H%M%S")}.txt'
    output_file_name = f'{path}/EquipCheck_Result{time.strftime("_%y%m%d_%H%M%S")}.xlsx'
    merge_path = fr'{path}\merge_{time.strftime("%y%m%d_%H%M%S")}'
        
    if not os.path.isdir(merge_path):                                                           
        os.mkdir(merge_path)   

    #print(f"3초 후 시작합니다...")
    #ms.sleep(3)
    how_time = 44 * len(lines)
    start_time = datetime.now()
    print(f"총 예상 소요 시간 : {ms.GetElapsedTime(how_time)}\n총 예상 종료 시각 : {ms.GetElapsedTime(how_time)}")
    for itemNum in lines:
        print(str(loopCount) + "/" + str(len(lines)))

        totalList = [str]
        totalList.clear()
        #장비생성
        ms.ResetFirst()
        ms.Command("cleanupinventory")

        cmdStr= "additems"
        for j in range(0,14):
            cmdStr += " " + str(int(itemNum)+j)
        ms.Command(cmdStr,1)
        sleep(0.01)


        #인벤열기 
        ms.Click(ms.menuPos1,0.3)
        

        curItemID = 0

        for i in range(0,14):
            data = []
            curItemID = int(itemNum) + i
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            ms.Move(ms.invenBtnDown2)
            sleep(1.3)
            targetStr = i2s.getNumbersInColumnFromImg_0(ms.captureSomeBox("equipStatAmountBox")).strip()
            stat_amount_str = f"{format_stats_ingame(targetStr,curItemID)}"
            stat_amount_list = stat_amount_str.strip().split('/')
            stat_count = len(stat_amount_list)#스탯개수

            allStatNameStr = i2s.getStringFromImg2(ms.captureSomeBox("equipStatNameBox"), 'kor+eng').strip()
            #allStatNameStr = allStatNameStr.replace('\n','/')
            tempList = allStatNameStr.split('\n')
            normal_stat_name_list = []
            special_stat_type_list = [] #슬레인/프로텍트 타입명
            special_stat_name_list = [] #슬레인/프로텍트 타입명
            special_stat_check = 0 #1로 바꾸면 그때부터 슬레인/프로텍트 능력치
            for statName in tempList :

                tempName = re.sub(r'[\d@]', ' ', statName).strip()

                tempName = change_stat_name(tempName)
                if tempName.endswith('인') or tempName.endswith('트'):
                    special_stat_type_list.append(tempName)
                    special_stat_check = 1
                elif special_stat_check == 0 :
                    if '최소' in tempName :
                        continue
                    else:
                        normal_stat_name_list.append(tempName)
                elif special_stat_check == 1 :
                    special_stat_name_list.append(tempName)

            normal_stat_count = len(normal_stat_name_list)
            normal_stat_list = []
            special_stat_list = []

            for j in range(0,stat_count):
                if j < normal_stat_count :
                    normal_stat_list.append(f'{normal_stat_name_list[j]}{stat_amount_list[j]}')
                else:
                    special_stat_list.append(f'{special_stat_name_list[j-normal_stat_count]}{stat_amount_list[j]}')


            
            ms.CaptureInvenDes(merge_path+"/"+str(int(itemNum)+i)+"_0")
            ms.Move(ms.invenExitBtn)


            data = [[str(curItemID),'/'.join(normal_stat_list),'/'.join(special_stat_list),'/'.join(special_stat_type_list),stat_amount_str]]
            columns=['ID','normal_stat','special_stat','special_type','only_amount']
            result_df = pandas.DataFrame(data,columns=columns)
            ms.save_df_to_excel(output_file_name,result_df,autoOpen=False)

            # with open(resultTxtFileName,'a',encoding='utf-8') as f:
            #     #f.write('\n'.join(finalStr))    
            #     f.write(finalStr)   
            # 
        equipType = 1 if curItemID < 400000 else 2 
        mergeImg.MergeImg_Equip(itemNum,equipType,merge_path,isSolo=True)
            
        #mergeImg.MergeImg_Equip(itemNum,equipType,extraPath)

        #print(totalList)        
        #if not os.path.isfile(resultTxtFileName):                                                           
        #    with open(resultTxtFileName,'a',encoding='utf-8') as tx:
        #        tx.write("날짜|영혼부여대상장비ID|영혼석ID|전용변신이름|영혼부여비용|성공횟수|총횟수|성공률")    

        #print("스샷 경로 : "+extraPath)
        loopCount = loopCount +1
    print(f"총 실제 소요 시간 : {ms.GetConsumedTime(start_time)}")

#장신구 : 50초, 무기  : 64초
def format_stats_ingame(input_str : str,itemID : int):
    """
    인게임 능력치 스트링을 [개별]로 받아와서 수/수/수... 형태로 리턴\n
    능력치 스샷찍은 직후에 바로 사용
    """
    # split the input string by lines
    lines = input_str.strip().split('\n')
    
    # initialize an empty list to hold the final result
    result_list = []
    
    for i, line in enumerate(lines):
        total = 0
        if i == 0 and itemID < 300000:
            continue

        # if line.startswith('4') :
        #     line[0] = '+'
        line = line.replace(',', '.')
        if '(' in line :
            #line = line.replace('(', '').replace(')', '')
            #values = line.strip().split('+')
            line = line.replace('+', '')
            line = line.replace(')', '')
            values = line.strip().split('(')
            
            for i, value in enumerate(values):
                # print(i,value)
                # if i == 0 :
                #     continue

                try:
                    total += int(value.strip())
                except:
                    continue

        else :            
            #values = line.strip().split('+')
            value = line[1:]
            
            try :
                if not value[0].isdigit() and not '%' in line:
                    continue
                if '%' in value :
                    total = value.replace('.00%','')
                    total = total.replace('0%','')
                    total = total.replace('%','')
                else:
                    total = value
            except :
                total = 0

        if total != 0 :
            result_list.append(total)
    
    #return f'{itemID}/' + '/'.join(str(x) for x in result_list) + "\n"
    return '/'.join(str(x) for x in result_list) + "\n"

def change_stat_name(stat_name):
    substitutions = {
        ' ':'',
        '몰': '물',
        '물리공격력(최대)': '물리공격',
        '공격속도': '공속',
        '명중력': '명중',
        '공격력': '공격',
        '원거리':'원',
        '근접':'근',
        # Add more substitutions as needed
    }

    for original, replacement in substitutions.items():
        stat_name = stat_name.replace(original, replacement)
    return stat_name

if __name__ == "__main__" : 
    EquipCheck4()
    #EquipCheck3()
    #EquipCheck()