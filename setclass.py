import pyautogui as pag
from time import sleep
import os
import msdata as ms
import time

def SetClass(classNum, isDefault):

    if isDefault :

        equipCheck = input("기본 장비를 생성하려면 1을 입력하세요(Skip : Enter) : ")
        tutoCheck = input("튜토리얼 스킵처리하려면 1을 입력하세요(Skip : Enter) : ")
        skillDefaultCheck = input("공용 스킬북을 사용하려면 1을 입력하세요(Skip : Enter) : ")
        skillCheck = input("클래스 스킬북을 사용하려면 1을 입력하세요(Skip : Enter) : ")
        skillUpCheck = input("스킬 최대 레벨로 설정하려면 1을 입력하세요(Skip : Enter) : ")
        matCheck = input("매터리얼 생성하려면 1을 입력하세요(Skip : Enter) : ")
        bootyCheck = input("전리품 생성하려면 1을 입력하세요(Skip : Enter) : ")
        stuffCheck = input("기타 아이템을 생성하려면 1을 입력하세요(Skip : Enter) : ")
#서버이전
    else :
        equipCheck = "1"
        tutoCheck = "1"
        skillDefaultCheck = "1"
        skillCheck = "1"
        skillUpCheck = "1"
        matCheck = "1"
        bootyCheck = "1"
        stuffCheck = "1"


    ms.ResetFirst()
    sleep(0.5)

    if tutoCheck == "1":
        ms.Command("flowcompletequest 100500")
        sleep(1)

    sleep(0.2)

    ms.Command("cleanupinventory")

    if skillDefaultCheck == "1":
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime2)
        ms.Move(ms.invenBtnUp2)
        pag.click()
        sleep(ms.waitTime2)

        ms.Command("additems 4900 4901 4902 4903 4904 4905")
        ms.Command("additems 4900 4901 4902 4903 4904 4905")

        for i in range(0,6):
            #ms.Move(ms.invenBtn+str(i))
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            pag.click()
            pag.click()
            sleep(1.1)

            
        ms.Command("cleanupinventory")

            
    ms.ResetFirst()




    if equipCheck == "1":
        
        if classNum == 1:
            fileName = "setknight"
        elif classNum ==2:
            fileName = "setarcher"
        elif classNum ==3:
            fileName = "setwizard"
        elif classNum ==4:
            fileName = "setassassin"
        
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()

        for line in lines:
            ms.Command(line)

    ms.Command("lv 99")
    # Command("additems 14053 304040 314080 324100 334040 344060 4000 4001 4002 4004 4005 4006 4007 4008 4009 4010")
    # Command("addtransformcard 152 1")

    if skillCheck == "1":
        ms.Move(ms.menuPos1)
        sleep(ms.waitTime2)
        ms.Move(ms.invenBtnUp2)
        pag.click()
        sleep(ms.waitTime2)

        if classNum == 1:
            skillCount = 10
        elif classNum ==2:
            skillCount = 10
        elif classNum ==3:
            skillCount = 20
        elif classNum ==4:
            skillCount = 10


        for i in range(0,skillCount):
            #ms.Move(ms.invenBtn+str(i))
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            pag.click()
            pag.click()
            sleep(1.1)



            
    if skillUpCheck == "1":    
        if classNum == 1:
            ms.Command("changeskillenchant 94004 5")
            ms.Command("changeskillenchant 94005 5")
            ms.Command("changeskillenchant 94008 5")
            ms.Command("changeskillenchant 94009 5")
            ms.Command("changeskillenchant 94006 3")
            ms.Command("changeskillenchant 94007 3")
            ms.Command("changeskillenchant 94010 3")
        elif classNum ==2:
            ms.Command("changeskillenchant 95002 5")
            ms.Command("changeskillenchant 95003 5")
            ms.Command("changeskillenchant 95004 5")
            ms.Command("changeskillenchant 95008 5")
            ms.Command("changeskillenchant 95005 3")
            ms.Command("changeskillenchant 95006 3")
            ms.Command("changeskillenchant 95009 3")
        elif classNum ==3:
            ms.Command("changeskillenchant 96003 5")
            ms.Command("changeskillenchant 96004 5")
            ms.Command("changeskillenchant 96005 5")
            ms.Command("changeskillenchant 96200 5")
            ms.Command("changeskillenchant 96201 5")
            ms.Command("changeskillenchant 96202 5")
            ms.Command("changeskillenchant 96203 5")
            ms.Command("changeskillenchant 96006 3")
            ms.Command("changeskillenchant 96007 3")
            ms.Command("changeskillenchant 96008 3")
            ms.Command("changeskillenchant 96100 3")
            ms.Command("changeskillenchant 96101 3")
            ms.Command("changeskillenchant 96102 3")
            ms.Command("changeskillenchant 96103 3")
            ms.Command("changeskillenchant 96104 3")
            ms.Command("changeskillenchant 96105 3")
            ms.Command("changeskillenchant 96204 3")
            ms.Command("changeskillenchant 96205 3")
        elif classNum ==4:
            ms.Command("changeskillenchant 97003 5")
            ms.Command("changeskillenchant 97004 5")
            ms.Command("changeskillenchant 97005 5")
            ms.Command("changeskillenchant 97006 5")
            ms.Command("changeskillenchant 97007 3")
            ms.Command("changeskillenchant 97008 3")
            ms.Command("changeskillenchant 97009 3")

    if matCheck == "1":
        with open("setmaterial.txt",encoding="UTF-8") as f:
            lines = f.read().splitlines()
        for line in lines:
            ms.Command(line)

    if bootyCheck == "1":
        ms.Command("additems 430009 431009 432009 433009 434009 435009")


    if stuffCheck == "1":
        with open("setclassbasic.txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        for line in lines:
            ms.Command(line)

        if classNum == 1:
            ms.Command("additem 105 200")
        elif classNum ==2:
            ms.Command("additem 199040 10000")
        elif classNum ==3:
            ms.Command("additem 411 10000")
        elif classNum ==4:
            ms.Command("additem 142 10000")

    if not isDefault:
        with open("setmigration.txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        for line in lines:
            ms.Command(line)

            
def setClass_auto(classNum, checkBoxValues):

    defaultDirectory = "./data/character/"
    
    className = ""
    if classNum == 1:
        className = "Knight"
    elif classNum ==2:
        className = "Archer"
    elif classNum ==3:
        className = "Wizard"
    elif classNum ==4:
        className = "Assassin"

    ms.ResetFirst()
    #sleep(0.5)
    #ms.Command("cleanupinventory")
#[장비]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if checkBoxValues[0]:
        fileName = defaultDirectory + "setEquips" + className
        
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
        f.close()

        for line in lines:
            ms.Command(line)
    # if tutoCheck == "1":
    #     ms.Command("flowcompletequest 100500")
    #     sleep(1)

    #sleep(0.2)

#[변신/서번트]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if checkBoxValues[1]:
        fileName = defaultDirectory + "setCard" + className
        
        with open(fileName +".txt") as f:
            lines = f.read().splitlines()
        f.close()

        for line in lines:
            ms.Command(line)

#[매터리얼]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if checkBoxValues[2]:
        fileName = defaultDirectory + "setMaterial"
        
        with open(fileName +".txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        for i in range(0,len(lines)):
            materialID, materialName = lines[i].split(',')
            ms.Command("addmaterial "+materialID +" 1")

#[전리품]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if checkBoxValues[3]:
        fileName = defaultDirectory + "setTrophy"
        
        with open(fileName +".txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        for line in lines:
            ms.Command(line)
            
#[스킬(공통)]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if checkBoxValues[4]:
        fileName = defaultDirectory + "setSkillsCommon"
        
        with open(fileName +".txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        for line in lines:
            ms.Command(line)
            ms.Command(line)

        ms.Move(ms.menuPos1)
        sleep(ms.waitTime2)
        ms.Move(ms.invenBtnUp2)
        pag.click()
        sleep(ms.waitTime2)
        
        ms.Command("lv 65")

        for i in range(0,6):
            #ms.Move(ms.invenBtn+str(i))
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            pag.click()
            pag.click()
            sleep(1.1)
            
        ms.ResetFirst()
        #ms.Command("cleanupinventory")
            
#[스킬(클래스)]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if checkBoxValues[5]:
        if checkBoxValues[4]:
            ms.Command("cleanupinventory")

        fileName = defaultDirectory + "setSkills" + className
        
        with open(fileName +".txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        ms.CommandOpen()
        pag.typewrite("additems")
        for line in lines:
            pag.typewrite(" "+line)
        ms.CommandClose()

        ms.CommandOpen()
        pag.typewrite("additems")
        for line in lines:
            pag.typewrite(" "+line)
        ms.CommandClose()

        ms.Move(ms.menuPos1)
        sleep(ms.waitTime2)
        ms.Move(ms.invenBtnUp2)
        pag.click()
        sleep(ms.waitTime2)

        ms.Command("lv 65")

        for i in range(0,len(lines)):
            #ms.Move(ms.invenBtn+str(i))
            ms.Move(getattr(ms, 'invenBtn{}'.format(i)))
            pag.click()
            pag.click()
            sleep(1.1)
            
        ms.ResetFirst()
        #ms.Command("cleanupinventory")
            

#[스킬 마스터]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    if checkBoxValues[6]:
        fileName = defaultDirectory + "setMaster" + className
        
        with open(fileName +".txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        for i in range(0,len(lines)):
            groupID, maxEnchantLevel, skillName= lines[i].split(',')
            ms.Command("changeskillenchant "+groupID +" "+maxEnchantLevel)
            
            
#[소모품]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    if checkBoxValues[7]:

        fileName = defaultDirectory+"setBasicItems" 

        with open(fileName +".txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        for line in lines:
            ms.Command(line)
            
        if classNum == 1:
            ms.Command("additem 105 200")
        elif classNum ==2:
            ms.Command("additem 199040 10000")
        elif classNum ==3:
            ms.Command("additem 411 10000")
        elif classNum ==4:
            ms.Command("additem 142 10000")

#[서버이전]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    if checkBoxValues[8]:

        fileName = "setMigration" 

        with open(fileName +".txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        for line in lines:
            ms.Command(line)
            


if __name__ == "__main__" : 
    SetClass()