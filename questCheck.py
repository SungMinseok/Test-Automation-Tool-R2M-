import multicommand as mtc
from re import T
import pyautogui as pag
import msdata as ms
from setappsize import SetAppSize
from time import sleep
import os.path
import time
import img2str as i2s
from tqdm import tqdm

def questCheck():

#기본 세팅(폴더생성)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    path = "./screenshot/questCheck"+ time.strftime("_%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


    #screenWidth, screenHeight = pag.size()
    ms.PrintUB()
    print("questCheck")    
    print("questCheck.txt")    
    ms.PrintUB()

    with open("questCheck.txt") as f:
        lines = f.read().splitlines()

    lvNum = input("Press any key to start([0]테스트메뉴) : ")
    print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10 + 11*len(lines)) +")")


    ms.ResetFirst()
    ms.Command("flowcompleteequest 100490")
    ms.Command("flowremoveequest 100500")
    ms.Command("flowcompletequest "+lines[0])



    for i in range(0,len(lines)): #회당 11s


        print(str(i+1) +"/"+str(len(lines)) + " | questID : " + lines[i])

        ms.Command("cleanupinventory")

        ms.Move(ms.acceptQuestInNavigation)    
        sleep(0.2)
        pag.press('esc')

        sleep(0.5)
        
        ms.captureSomeBox2("questCheckBox",path+"/"+lines[i]+"_0") #퀘스트 사이드 팝업창
        sleep(0.2)
        ms.Move(ms.acceptQuestBtn)
        sleep(0.2)

        #몬스터 처치 카운팅 확인










        ms.captureSomeBox2("questCheckBox",path+"/"+lines[i]+"_1") #퀘스트 네비게이션
        ms.Command("completequest " + lines[i])
        sleep(1.1)
        ms.captureSomeBox2("characterAroundBox",path+"/"+lines[i]+"_2") #퀘스트 보상 경치/골드
        ms.Move(ms.menuPos1)
        sleep(0.5)
        ms.captureSomeBox2("inventoryBox",path+"/"+lines[i]+"_3") #퀘스트 보상 아이템
        ms.Move(ms.menuPos1)


def subQuestCheck():

#기본 세팅(폴더생성)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    path = "./screenshot/questCheck"+ time.strftime("_%m%d") + "/subQuest"
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


    #screenWidth, screenHeight = pag.size()
    ms.PrintUB()
    print("subQuestCheck")    
    print("subQuestCheck.txt")    
    ms.PrintUB()

    with open("subQuestCheck.txt") as f:
        lines = f.read().splitlines()

    lvNum = input("Press any key to start([0]테스트메뉴) : ")
    print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10 + 11*len(lines)) +")")


    ms.ResetFirst()
    ms.Command("flowcompleteequest 1120250")
    sleep(1)
    ms.Command("flowremoveequest 1120260")
    ms.Command("flowcompletequest "+lines[0])



    for i in range(0,len(lines)): #회당 11s


        print(str(i+1) +"/"+str(len(lines)) + " | questID : " + lines[i])

        ms.Command("cleanupinventory")

        ms.Move(ms.acceptQuestInNavigation2)    
        sleep(0.2)
        pag.press('esc')

        sleep(0.5)
        
        ms.captureSomeBox2("questCheckBox",path+"/"+lines[i]+"_0") #퀘스트 사이드 팝업창
        sleep(0.2)
        ms.Move(ms.acceptQuestBtn)
        sleep(0.2)
        ms.captureSomeBox2("questCheckBox",path+"/"+lines[i]+"_1") #퀘스트 네비게이션
        ms.Command("completequest " + lines[i])
        sleep(1.1)
        ms.captureSomeBox2("characterAroundBox",path+"/"+lines[i]+"_2") #퀘스트 보상 경치/골드
        ms.Move(ms.menuPos1)
        sleep(0.5)
        ms.captureSomeBox2("inventoryBox",path+"/"+lines[i]+"_3") #퀘스트 보상 아이템
        ms.Move(ms.menuPos1)


def questCheck_guild():

#기본 세팅(폴더생성)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    path = "./screenshot/questCheck"+ time.strftime("_%m%d") + "/guild"
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


    #screenWidth, screenHeight = pag.size()
    ms.PrintUB()
    print("questCheck_guild")    
    print("questCheck_guild.txt")    
    ms.PrintUB()

    with open("questCheck_guild.txt") as f:
        lines = f.read().splitlines()

    lvNum = input("Press any key to start([0]테스트메뉴) : ")
    print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10 + 11*len(lines)) +")")


    ms.ResetFirst()
    ms.Command("setguildlevel 10")
    ms.Command("setguildlevel 9")
    ms.Command("setguilddonate 100000 0")
    ms.Command("resetguild 0")
    ms.Command("cleanupinventory")
    sleep(5)

    ms.Move(ms.menuPos4)
    ms.Move(ms.menuPos5)
    sleep(0.2)
    ms.Move(ms.guildQuestTabBtn)

    for i in range(0,len(lines)): #회당 

        print(str(i+1) +"/"+str(len(lines)) + " | guildQuestID : " + lines[i])
        ms.Command("completequest " + lines[i])
        sleep(0.5)
        
        if i % 3 == 2:
            ms.captureSomeBox2("questListBox",path+"/"+lines[i-2]+"_"+lines[i]) #퀘스트 리스트

            ms.Command("resetguild 0")
            sleep(5)

            

def hardcoreQuestCheck():

#기본 세팅(폴더생성)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    path = "./screenshot/questCheck"+ time.strftime("_%m%d") + "/hardcore"
    if not os.path.isdir(path):                                                           
        os.makedirs(path)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


    #screenWidth, screenHeight = pag.size()
    ms.PrintUB()
    print("questCheck_hardcore")    
    print("questCheck_hardcore.txt")    
    ms.PrintUB()

    with open("questCheck_hardcore.txt") as f:
        lines = f.read().splitlines()

    lvNum = input("Press any key to start([0]테스트메뉴) : ")
    print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10 + 11*len(lines)) +")")


    ms.ResetFirst()
    #ms.Command("flowcompleteequest 1120250")
    #sleep(1)
    ms.Move(ms.acceptQuestInNavigation1)    
    sleep(0.2)
    ms.Move(ms.acceptQuestBtn)
    ms.Command("flowremovequest "+lines[len(lines)-1])
    sleep(1)
    ms.Command("acceptquest "+lines[0])



    for i in range(0,len(lines)): #회당 11s


        print(str(i+1) +"/"+str(len(lines)) + " | questID : " + lines[i])

        ms.Command("cleanupinventory")

        ms.captureSomeBox2("questCheckBox",path+"/"+lines[i]+"_0") #퀘스트 사이드 팝업창
        ms.Move(ms.acceptQuestInNavigation1)    
        sleep(1)
        ms.captureSomeBox2("questCheckBox",path+"/"+lines[i]+"_1") #퀘스트 네비게이션
        sleep(0.2)
        ms.Move(ms.acceptQuestBtn)
        #pag.press('esc')

        #sleep(0.5)
        
        sleep(0.2)
        ms.Command("completequest " + lines[i])
        sleep(1.1)
        ms.captureSomeBox2("characterAroundBox",path+"/"+lines[i]+"_2") #퀘스트 보상 경치/골드
        ms.Move(ms.menuPos1)
        sleep(0.5)
        ms.captureSomeBox2("inventoryBox",path+"/"+lines[i]+"_3") #퀘스트 보상 아이템
        ms.Move(ms.menuPos1)

        mtc.채팅및스샷저장(lines[i],path+"/"+lines[i]+"_4")



def quest_reward_check():

#기본 세팅(폴더생성)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    path = "./screenshot/questCheck"+ time.strftime("_%y%m%d") + "/quest_reward"
    if not os.path.isdir(path):                                                           
        os.makedirs(path)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


    #screenWidth, screenHeight = pag.size()
    ms.PrintUB()
    print("quest_reward_check.txt")    
    ms.PrintUB()

    with open("quest_reward_check.txt") as f:
        lines = f.read().splitlines()

    input("Press any key to start([0]테스트메뉴) : ")
    print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10 + 11*len(lines)) +")")


    ms.ResetFirst()

    for i in tqdm(range(0,len(lines))): #회당 

        ms.Command("cleanupinventory")
        ms.Command("completequest " + lines[i])
        mtc.채팅및스샷저장(lines[i],path+"/"+lines[i])



def quest_string_check():

#기본 세팅(폴더생성)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    path = "./screenshot/questCheck"+ time.strftime("_%y%m%d") + "/quest_string"
    if not os.path.isdir(path):                                                           
        os.makedirs(path)
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    target_txt = f"quest_string.txt"
    #screenWidth, screenHeight = pag.size()
    ms.PrintUB()
    print(target_txt)    
    ms.PrintUB()

    with open(target_txt) as f:
        lines = f.read().splitlines()

    input("Press any key to start([0]테스트메뉴) : ")
    print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10 + 11*len(lines)) +")")


    #ms.ResetFirst()

    ms.Command("flowremovequest "+lines[len(lines)-1])

    for i in tqdm(range(0,len(lines))): #회당 

        ms.Command("acceptquest " + lines[i])
        ms.Capture(path+"/"+lines[i],False)
        ms.Command("completequest " + lines[i])



if __name__ == "__main__" : 
    #questCheck()
    hardcoreQuestCheck()
    #quest_reward_check()