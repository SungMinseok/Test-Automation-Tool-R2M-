
import os

#####기본 세팅(폴더생성)
path_screenshot = "./screenshot"
if not os.path.isdir(path_screenshot):                                                           
    os.mkdir(path_screenshot)
######################

#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'd:\Tesseract-OCR\tesseract.exe'



from ctypes import resize
from pandas.core.frame import DataFrame
from pandas.io import excel
#from img2str import Img2Str
#import img2Str

import img2str
import pyautogui as pag
from time import sleep
import multicommand as multi
from setappsize import SetAppSize
from resolution import Resolution
from statperlv import StatPerLv
from setclass import SetClass
from equipcheck import EquipCheck
from reincheck import ReinCheck
from engraveCheck import EngraveCheck
from dropCheck import DropCheck
from itemInfoCheck import ItemInfoCheck
from probTest import ProbTest
from cmdBundle import GoCharacterSelectPage, initCmdBundle
import time
import datetime
import pandas as pd

import pyperclip as pc

import gc
from tqdm import tqdm

#import xlwings as xw


# with open("info.txt") as infoFile:
#     infoTxt = infoFile.read().splitlines()

# #infoTxt[0] : 개발모드/알파모드 확인
# #infoTxt[0] : 알파모드 앱사이즈 세팅 확인
# if infoTxt[0]== "0" :
#     devMode = 0

#     with open("info_appsize.txt") as infoAppsizeFile:
#         infoAppsizeTxt = infoAppsizeFile.read() 
#     infoAppsizeFile.close()

#     if infoAppsizeTxt== "0" :
#         with open("appsize.txt") as f:
#             appPos = f.read().splitlines()
#         #print("A")
#     else :
#         with open("appsize_"+infoAppsizeTxt+".txt") as f:
#             appPos = f.read().splitlines()

#         #print("B")

# elif infoTxt[0]== "1" : 
#     devMode =1
    
#     with open("appsize_dev.txt") as f:
#         appPos = f.read().splitlines()

def getBoxPos(x,y,w,h):
    return [x*appW+appX,y*appH+appY,w*appW,h*appH]

# #infoFile.close()

# # with open("appsize.txt") as f:
# #     appPos = f.read().splitlines()

# appX = int(appPos[0])
# appY = int(appPos[1])
# appW = int(appPos[2])
# appH = int(appPos[3])

# f.close()

appX, appY, appW, appH = 0,33,1428,805

#region mouse position
joyPos=[0.1092,0.805]
joy_cmd_pos = [0.1092,0.7429]

menuPos0=[0.773,0.043]
menuPos1=[0.82,0.043]
menuPos2=[0.865,0.043]
menuPos3=[0.914,0.043]
menuPos4=[0.961,0.043]
menuPos5=[0.773,0.157]
menuPos6=[0.82,0.157]
menuPos7=[0.865,0.157]
menuPos8=[0.914,0.157]
menuPos9=[0.961,0.157]
menuPos10=[0.773,0.271]
menuPos11=[0.82,0.271]
menuPos12=[0.865,0.271]
menuPos13=[0.914,0.271]
menuPos14=[0.961,0.271]
menuPos15=[0.773,0.385]
menuPos16=[0.82,0.385]
menuPos17=[0.865,0.385]
menuPos18=[0.914,0.385]
menuPos19=[0.961,0.385]
menuPos20=[0.773,0.499]
menuPos21=[0.82,0.499]

invenBtnUp0=[0.7486,0.157]
invenBtnUp1=[0.8515,0.157]
invenBtnUp2=[0.947,0.157]

autoImgBox=[0.7718*appW+appX,0.8917*appH+appY,0.0372*appW,0.0323*appH]#왼쪽위X,왼쪽위Y,가로,세로]

invenBtn0=[0.73,0.247]
invenBtn1=[0.788,0.247]
invenBtn2=[0.846,0.247]
invenBtn3=[0.906,0.247]
invenBtn4=[0.968,0.247]
invenBtn5=[0.73,0.353]
invenBtn6=[0.788,0.353]
invenBtn7=[0.846,0.353]
invenBtn8=[0.906,0.353]
invenBtn9=[0.968,0.353]
invenBtn10=[0.73,0.456]
invenBtn11=[0.788,0.456]
invenBtn12=[0.846,0.456]
invenBtn13=[0.906,0.456]
invenBtn14=[0.968,0.456]
invenBtn15=[0.73,0.559]
invenBtn16=[0.788,0.559]
invenBtn17=[0.846,0.559]
invenBtn18=[0.906,0.559]
invenBtn19=[0.968,0.559]
invenBtn20=[0.73,0.6384]
invenBtn21=[0.788,0.6384]
invenBtn22=[0.846,0.6384]
invenBtn23=[0.906,0.6384]
invenBtn24=[0.968,0.6384]

invenBtnRein=[0.813,0.756]#강화
invenBtnDown1=[0.858,0.756]#분해,분해내 일괄선택
invenBtnDown2=[0.945,0.754]#상세,분해 내 분해

invenDesPos=[0.812,0.821]#인벤중간(드래그용)
invenAddDesPos=[0.961,0.697]#추가정보

invenExitBtn=[0.977,0.153]#우상단X버튼
invenMainExitBtn=[0.984,0.112]
#invenSoulBtn=[0.961,0.4458]#영혼석 버튼(대만)
invenSoulBtn=[0.961,0.581]#영혼석 버튼(한국)

#UI내 탭 버튼
#7분할
uiTabBtn0_7 = [0.0871,0.1197]
uiTabBtn1_7 = [0.2164,0.1197]
uiTabBtn2_7 = [0.3521,0.1197]
uiTabBtn3_7 = [0.4926,0.1197]
uiTabBtn4_7 = [0.6332,0.1197]
uiTabBtn5_7 = [0.7807,0.1197]
uiTabBtn6_7 = [0.9115,0.1197]

#아이템 상세 전체
invenDesPos0=[0.698,0.133]
invenDesPos1=[0.996,0.133]
invenDesPos2=[0.698,0.861]
#아이템 이름만
# invenNamePos0=[0.711,0.139]#왼쪽위
# invenNamePos1=[0.960,0.139]#오른쪽위
# invenNamePos2=[0,0.181]#왼쪽아래
#print("CCC")
invenNameBox=[0.721*appW + appX,0.132*appH + appY, appW*0.243, appH*0.046]
#아이템 수량만
# invenAmountPos0=[0.836,0.311]#왼쪽위
# invenAmountPos1=[0.915,0.311]#오른쪽위
# invenAmountPos2=[0.836,0.358]#왼쪽아래
invenAmountBox=[0.859*appW + appX,0.319*appH + appY, appW*0.067, appH*0.04]

#중앙 채팅창
centerChatBox = [0.355 *appW + appX, 0.758*appH + appY , appW*0.336, appH*0.031]


#능력치만
invenOnlyDesPos0=[0.698,0.314]
invenOnlyDesPos1=[0.925,0.314]
invenOnlyDesPos2=[0.698,0.861]
#강화UI
invenReinBtnUp0=[0.77,0.175]
invenReinBtnUp1=[0.92,0.175]
invenReinBtnLeft0=[0.07,0.144]
invenReinBtnLeft1=[0.07,0.221]
invenReinBtnDown0=[0.404,0.91]#단일강화>자동강화
invenReinBtnDown1=[0.558,0.91]#단일강화>강화
invenReinBtnDown2=[0.361,0.952]#다중강화>강화시작
invenReinBtn9=[0.587,0.589]
reinResultTextBox=[0.376*appW+appX,0.14*appH+appY,0.248*appW,0.047*appH]#왼쪽위X,왼쪽위Y,가로,세로]
reinPhase1=[0.176,0.765]
reinPhase2=[0.135,0.591]
reinPhase3=[0.144,0.392]
reinPhase4=[0.206,0.228]
reinPhase5=[0.305,0.139]
reinPhase6=[0.418,0.141]
reinPhase7=[0.514,0.226]
reinPhase8=[0.579,0.393]
reinPhase9=[0.589,0.587]
reinMultiResultBox=[0.245*appW+appX,0.366*appH+appY,0.236*appW,0.418*appH]#왼쪽위X,왼쪽위Y,가로,세로]

reinActivateEnchantBtn0=[0.579,0.675]
reinActivateEnchantBtn1=[0.582,0.626]

reinResultNameTextBox=[0.3528*appW+appX,0.2456*appH+appY,0.1343*appW,0.0449*appH]#왼쪽위X,왼쪽위Y,가로,세로]

#각인UI
engraveBtn=[0.496,0.896]
#engraveResultBox=[0.384*appW+appX,0.55*appH+appY,0.248*appW,0.172*appH]#왼쪽위X,왼쪽위Y,가로,세로
engraveResultBox=[0.389*appW+appX,0.547*appH+appY,0.252*appW,0.224*appH]#왼쪽위X,왼쪽위Y,가로,세로

#영혼석UI
soulTargetBtn=[0.861,0.26]
soulEnchantBtn=[0.489,0.849]
soulEnchantPriceBox=[0.4371*appW+appX,0.7654*appH+appY,0.1819*appW,0.0454*appH]#왼쪽위X,왼쪽위Y,가로,세로
soulEnchantCardNameBox=[0.1002*appW+appX,0.6835*appH+appY,0.1578*appW,0.0353*appH]#왼쪽위X,왼쪽위Y,가로,세로

#자동사냥
autoBtn=[0.784,0.906]
#퀵슬롯
quickBtn0=[0.273,0.859]
quickBtn1=[0.336,0.859]
quickBtn2=[0.398,0.859]
quickBtn3=[0.46,0.859]
quickBtn4=[0.539,0.859]
quickBtn5=[0.602,0.859]
quickBtn6=[0.663,0.859]
quickBtn7=[0.723,0.859]

centerPos=[0.5,0.5]
centerUpPos=[0.5,0.4]
#commandPos=[0.5,0.734]
commandPos=[0.8803,0.7329]#230714
executePos=[0.99,0.734]
okPos=[0.583,0.63]
cancelPos=[0.423,0.63]
appUpPos=[0.019,-0.026]

lvBtn=[0.023,0.048]#캐릭터장비창
statBtn=[0.264,0.156]
statdetailBtn=[0.231,0.794]
statdetailPos=[0.435,0.798]

statDetailBox_statAmt =[0.4867*appW+appX,0.1429*appH+appY,0.0644*appW,0.6683*appH]
statDetailBox_statName =[0.3137*appW+appX,0.1429*appH+appY,0.1751*appW,0.6708*appH]

#변신/서번트 카드 수량
cardAmountBox=[0.03*appW+appX,0.82*appH+appY,0.039*appW,0.034*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardNextPageBtn=[0.582,0.898]
cardFirst=[0.073,0.758]
cardSecond=[0.167,0.758]
cardNameBox = [0.0204*appW+appX,0.2017*appH+appY,0.1495*appW,0.0461*appH]
cardSlot0 = [0.0681,0.7136]
cardSlot1 = [0.1615,0.7136]
cardSlot2 = [0.2549,0.7136]
cardSlot3 = [0.3483,0.7136]
cardSlot4 = [0.4417,0.7136]
cardSlot5 = [0.5351,0.7136]
cardSlot6 = [0.6285,0.7136]
cardSlot7 = [0.7219,0.7136]
cardSlot8 = [0.8153,0.7136]
cardSlot9 = [0.9087,0.7136]
cardAmountBox0 = [0.0316*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox1 = [0.1243*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox2 = [0.2184*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox3 = [0.3125*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox4 = [0.4066*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox5 = [0.5*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox6 = [0.5941*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox7 = [0.6889*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox8 = [0.783*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로
cardAmountBox9 = [0.8757*appW+appX,0.8082*appH+appY,0.04*appW,0.0411*appH]#왼쪽위X,왼쪽위Y,가로,세로


#변신 등급버튼
transformCardRarityBtn6=[0.906,0.2]
transformCardRarityBtn5=[0.906,0.27]
transformCardRarityBtn4=[0.906,0.34]
transformCardRarityBtn3=[0.906,0.41]
transformCardRarityBtn2=[0.906,0.48]
transformCardRarityBtn1=[0.906,0.55]
transformCardRarityBtn0=[0.906,0.62]

#변신 카드 일반~전체 페이지
transformCardPage0 = 2
transformCardPage1 = 3
transformCardPage2 = 6
transformCardPage3 = 6
transformCardPage4 = 2
transformCardPage5 = 1
transformCardPage6 = 21

servantCardPage0 = 1

#스킬강화 버튼
enchantSkillStartBtn=[0.57,0.757]
enchantSkillBtn=[0.505,0.895]
enchantSkillResultBox=[0.4431*appW+appX,0.0996*appH+appY,0.1222*appW,0.0511*appH]#왼쪽위X,왼쪽위Y,가로,세로

#매터리얼 UI 버튼
materialCombineTabBtn=[0.214,0.126]
materialAutoInputBtn=[0.182,0.621]
materialCombineBtn=[0.448,0.692]
materialCombineOkBtn=[0.566,0.631]

#자동사냥 AUTO 텍스트 위치 ( 메인화면 확인용 )
autoBtnBox=[0.768*appW+appX,0.887*appH+appY,0.039*appW,0.032*appH]#왼쪽위X,왼쪽위Y,가로,세로

#회원 탈퇴
menuMiddleUpperTab5 = [0.784,0.123]
deleteAccountBtn = [0.589,0.711]
deleteAccountCodeBox=[0.581*appW+appX,0.493*appH+appY,0.056*appW,0.054*appH]#왼쪽위X,왼쪽위Y,가로,세로
deleteAccountCodeInput=[0.454,0.517]

#계정생성
characterNameBtn =[0.808,0.758]
characterNameInput = [0.505,0.449]
characterCreateBtn=[0.808,0.857]
belitaBox=[0.399*appW+appX,0.642*appH+appY,0.147*appW,0.068*appH]#왼쪽위X,왼쪽위Y,가로,세로
getFirstQuestBtn=[0.138,0.302]
acceptQuestBtn=[0.224,0.761]
exitQuestDialogueBtn=[0.907,0.677]
okTeleportBtn = [0.585,0.78]
tutoMonPos =[0.418,0.288]
attackBtn = [0.903,0.765]

#거래소
market_enterServerType0=[0.057,0.166]
market_enterServerType1=[0.135,0.166]
market_searchTab=[0.274,0.123]
market_registTab=[0.411,0.123]
market_invenBtn0=[0.732,0.375]
market_sellBtn0=[0.859,0.942]
market_sellBtn1=[0.58,0.847]
market_sellBtn2=[0.576,0.871]
market_cancelRegist=[0.601,0.419]
market_totalSellPriceBox=[0.154*appW+appX,0.935*appH+appY,0.074*appW,0.049*appH]#왼쪽위X,왼쪽위Y,가로,세로

#슬롯강화
slotEnchantResultBox=[0.4048*appW+appX,0.1845*appH+appY,0.2677*appW,0.0537*appH]#왼쪽위X,왼쪽위Y,가로,세로
slotEnchantBtn=[0.6107,0.9027]
slotEnchantCostBox=[0.4765*appW+appX,0.8217*appH+appY,0.1433*appW,0.0374*appH]#왼쪽위X,왼쪽위Y,가로,세로
slotEnchantTypeBtn_equipment=[0.0968,0.1256]
slotEnchantTypeBtn_material=[0.2756,0.1256]

slotEnchantSlot0=[0.1017,0.2338]
slotEnchantSlot1=[0.2805,0.2338]
slotEnchantSlot2=[0.1017,0.3507]
slotEnchantSlot3=[0.2805,0.3507]
slotEnchantSlot4=[0.1017,0.4689]
slotEnchantSlot5=[0.2805,0.4689]
slotEnchantSlot6=[0.1017,0.597]
slotEnchantSlot7=[0.2805,0.597]

slotEnchantToggleScroll=[0.4355,0.7114]




#캐릭터/서버선택
goCharacterSelectPageBtn = [0.9072,0.6035]
goServerSelectionBtn = [0.7486,0.6035]
logoutBtn = [0.5868,0.6035]

#캐릭터 선택 창 내 캐릭터 선택
selectCharacterNameBox = [0.1082*appW+appX,0.0299*appH+appY,0.1223*appW,0.0599*appH]#왼쪽위X,왼쪽위Y,가로,세로

#네비게이션
acceptQuestInNavigation = [0.2593,0.3005]
acceptQuestInNavigation1 = [0.2593,0.4002]
acceptQuestInNavigation2 = [0.2593,0.505]

#questCheck
inventoryBox =[0.7006*appW+appX,0.0923*appH+appY,0.3*appW,0.6995*appH]#왼쪽위X,왼쪽위Y,가로,세로
questCheckBox = [0*appW+appX,0.1421*appH+appY,0.3408*appW,0.6760*appH]#왼쪽위X,왼쪽위Y,가로,세로
characterAroundBox = [0.3422*appW+appX,0.2693*appH+appY,0.3282*appW,0.3878*appH]#왼쪽위X,왼쪽위Y,가로,세로
guildQuestTabBtn = [0.6381,0.1172]
questListBox = [0*appW+appX,0.1384*appH+appY,0.9986*appW,0.7930*appH]


#변신/서번트 휘장
cardSpotTabBtn = [0.6339,0.1147]
cardSpotGroubTabBtn0 = [0.0963,0.3204]
cardSpotGroubTabBtn1 = [0.0963,0.4352]
cardSpotGroubTabBtn2 = [0.0963,0.5424]
cardSpotGroubTabBtn3 = [0.0963,0.6521]
cardSpotGroubTabBtn4 = [0.0963,0.7668]
cardSpotGroubTabBtn5 = [0.0963,0.8741]

cardSpotActivateBtn = [0.8686,0.5885]
cardSpotActivateOkBtn = [0.5833,0.6297]

cardSpotEnchantResultBox = [0.3591*appW+appX,0.2319*appH+appY,0.3022*appW,0.0798*appH]

#장비 능력치창
equipStatNameBox = getBoxPos(0.7003,0.3093,0.1386,0.5466)
equipStatAmountBox = getBoxPos(0.8438,0.3093,0.0855,0.5466)

#채팅관련
mainhud_chat_btn = [0.0252,0.677] #채팅버튼, 채팅인풋박스
send_chat_btn = [0.2675,0.6907]
chat_popup_box = [0*appW+appX,0.1876*appH+appY,0.3046*appW,0.4708*appH]

#시스템메시지관련
center_system_msg_box = [0.355*appW+appX,0.6373*appH+appY,0.29*appW,0.0484*appH]

#endregion

waitTime = 0.3
waitTime2 = 0.3

        
# def ApplyAppSize():
            
#     with open("appsize.txt") as f:
#         appPos = f.read().splitlines()

#     appX = int(appPos[0])
#     appY = int(appPos[1])
#     appW = int(appPos[2])
#     appH = int(appPos[3])

def MainMenu():

    while True :
        clear()
        PrintUB_Bold()
        PrintInfo()
        print("AppSize :", appX, appY, appW, appH)
        #print(appX, appY, appW, appH)
        #print(invenNameBox[0])
        global devMode
        if devMode == 0 :
            print("Type : Alpha")
        else:    
            print("Type : Dev")
        PrintUB()
        #print("※R2M 전용")
        #PrintUB()

        print("[1]캐릭터 텔레포트\n[2]앱 위치 및 크기 설정\n[3]멀티 커맨드\n[4]명령어 모음")
        print("[5]테스트\n[6]텍스트 인식")  
        PrintUB()

        print("[98]Toggle Dev/Alpha\n[0]종료")    
        PrintUB()

        

        num = int(InputNum(99))
        clear()
        if num==0:
            quit()
        elif num == 1:
            DoTeleport()
        elif num == 2:
            SetAppSize()
        elif num==3:
            multi.multicommand()
        elif num==4:
            CommandBundle()
        elif num==5:
            TestMenu()
        elif num==6:
            img2str.Img2Str()
        elif num==98:
            if devMode == 0 :
                devMode=1
            else:
                devMode=0
                
            with open("info.txt",'w',encoding='utf-8') as infoFile:
                infoFile.write(str(devMode))
                
            infoFile.close()
            ResetAppSize()


    #MainMenu()

def clear():
    os.system('cls')

def PrintUB():
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def PrintUB_Bold():
    
    print("〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓")

def Move(des):
    pag.moveTo(des[0]*appW + appX, des[1]*appH + appY)
    #sleep(0.1)
    pag.click()        
    sleep(0.01)

def Click(target,delay = 0.01):
    x = target[0]*appW + appX
    y = target[1]*appH + appY
    pag.click(x,y)
    sleep(delay)

def DragUp(des):
    #pag.dragRel(des[0]*appW + appX, des[1]*appH + appY,3,button='left')
    pag.dragRel(0, -280, 1, button='left')
def DragDown(des):
    #pag.dragRel(des[0]*appW + appX, des[1]*appH + appY,3,button='left')
    pag.dragRel(0, 10, 0.5, button='right')
def DragToByPos(startPos, endPos, _duration = 1):
    pag.moveTo(startPos[0]*appW + appX, startPos[1]*appH + appY)
    pag.dragTo(endPos[0]*appW + appX, endPos[1]*appH + appY,duration = _duration,button='left')
def Capture(fileName,showDate = True):
    sleep(0.1)
    if showDate :
        timestr = time.strftime("_%Y%m%d_%H%M%S")
    else : 
        timestr = ""
    pag.screenshot(fileName + timestr + ".jpg", region=(appX, appY, appW, appH))
    sleep(0.1)

def CaptureReinforceResult(fileName):
    sleep(0.1)
    pag.screenshot(fileName + ".jpg", region=(reinResultTextBox[0],reinResultTextBox[1],reinResultTextBox[2],reinResultTextBox[3]))
    sleep(0.1)
def CaptureInvenDes(fileName,pos = 0):
    sleep(0.1)
    #timestr = time.strftime("_%Y%m%d_%H%M%S")
    if pos == 0 :#상세전체
        pag.screenshot(fileName  + ".jpg", region=(invenDesPos0[0]*appW + appX,invenDesPos0[1]*appH + appY, appW*(invenDesPos1[0]-invenDesPos0[0]), appH*(invenDesPos2[1]-invenDesPos0[1])))
    elif pos == 1 :#이름
        pag.screenshot(fileName  + ".jpg", region=(invenNameBox[0],invenNameBox[1],invenNameBox[2],invenNameBox[3]))
    elif pos == 2 :#수량
        pag.screenshot(fileName  + ".jpg", region=(invenAmountBox[0],invenAmountBox[1],invenAmountBox[2],invenAmountBox[3]))
    sleep(0.1)
def CaptureEngraveRes(fileName):
    sleep(0.1)
    #timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName  + ".jpg", region=(engraveResultBox[0],engraveResultBox[1],engraveResultBox[2],engraveResultBox[3]))
    sleep(0.1)
def CaptureCenterChatBox(fileName):
    sleep(0.1)
    #timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName + ".jpg", region=(centerChatBox[0],centerChatBox[1],centerChatBox[2],centerChatBox[3]))
    sleep(0.1)
def CaptureCardAmount(fileName, order):
    sleep(0.1)
    if order == 0 :
        #print("A")
        pag.screenshot(fileName + ".jpg", region=(cardAmountBox[0]+(0.004*order*appW+appX),cardAmountBox[1],cardAmountBox[2],cardAmountBox[3]))
    else :
        #print("B")
        pag.screenshot(fileName + ".jpg", region=(cardAmountBox[0]+(0.094*order*appW+appX),cardAmountBox[1],cardAmountBox[2],cardAmountBox[3]))
        #print(cardAmountBox[0])
    #print(int(order))
    #print(cardAmountBox[0]+0.095*float(order))
    sleep(0.1)
def CaptureReinMultiResultBox(fileName):
    sleep(0.1)
    #timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName  + ".jpg", region=(reinMultiResultBox[0],reinMultiResultBox[1],reinMultiResultBox[2],reinMultiResultBox[3]))
    sleep(0.1)

def CaptureFull(fileName):
    timestr = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(fileName + timestr + ".jpg")
    sleep(0.1)

# 
def captureSomeBox(boxName : str):
    """
    boxName : ms의 박스 변수명
    Returns : boxName.jpg으로 스크린샷 저장
    """

    resultJPGFileName = boxName + ".jpg"
    #print(boxName)
    #pag.screenshot(resultJPGFileName, region=(getattr(self, boxName)[0],getattr(self,boxName)[1],getattr(self,boxName)[2],getattr(self,boxName)[3]))
    pag.screenshot(resultJPGFileName, region=(globals()[boxName][0],globals()[boxName][1],globals()[boxName][2],globals()[boxName][3]))
    return str(resultJPGFileName)


def captureSomeBox2(boxName,resultPath):
    """
    boxName : ms의 박스 변수명\n
    resultPath : 경로지정 (.jpg 제외하고 입력)\n
    Returns : resultPath로 스크린샷 저장
    """
    resultJPGFileName = resultPath + ".jpg"
    #print(boxName)import os

    if os.path.exists(resultJPGFileName):
        # 이미 파일이 존재하는 경우, 번호를 붙여가며 존재하지 않는 파일명 찾기
        i = 0
        while True:
            i += 1
            numbered_resultJPGFileName = f"{resultPath}_{i}.jpg"
            if not os.path.exists(numbered_resultJPGFileName):
                resultJPGFileName = numbered_resultJPGFileName
                break

    pag.screenshot(resultJPGFileName, region=(globals()[boxName][0], globals()[boxName][1], globals()[boxName][2], globals()[boxName][3]))
    return resultJPGFileName

    #pag.screenshot(resultJPGFileName, region=(getattr(self, boxName)[0],getattr(self,boxName)[1],getattr(self,boxName)[2],getattr(self,boxName)[3]))
    pag.screenshot(resultJPGFileName, region=(globals()[boxName][0],globals()[boxName][1],globals()[boxName][2],globals()[boxName][3]))
    return resultJPGFileName

def captureSomeBox3(xRatio,yRatio,wRatio,hRatio):
    timestr = time.strftime("_%Y%m%d_%H%M%S")
    resultJPGFileName = ".\screenshot/screenshot"+ timestr + ".jpg"
    #print(boxName)
    #pag.screenshot(resultJPGFileName, region=(getattr(self, boxName)[0],getattr(self,boxName)[1],getattr(self,boxName)[2],getattr(self,boxName)[3]))
    pag.screenshot(resultJPGFileName, region=(xRatio*appW+appX,yRatio*appH+appY,wRatio*appW,hRatio*appH))
    #[0.154*appW+appX,0.935*appH+appY,0.074*appW,0.049*appH]
    return resultJPGFileName


def Command(command):       
    # print(command) 
    # Move(centerPos)
    # if devMode == 0 :
    #     pag.hotkey('z','x','c','v')
    # else:
    #     DragDown(centerPos)
    # sleep(waitTime)       
    # Move(commandPos)
    # sleep(waitTime)
    # pag.typewrite(command)
    # Move(centerUpPos)
    # sleep(0.1)
    # Move(executePos)
    # Move(centerUpPos)

    #230621 update
    try :
        command =command.replace('\n','')
    except:
        pass
    #Click(joy_cmd_pos)
    #sleep(1) 
    #pc.copy(command)
    Click(appUpPos)
    #pag.press('hangul')
    #pc.copy('')
    #pc.copy(command)
    pag.hotkey('z','x','c','v')
    sleep(0.1)
    #sleep(waitTime) 
    Click(joy_cmd_pos)


    #pag.hotkey("ctrl", "v")
    pag.typewrite(command)
    sleep(0.05)
    #Click(joyPos)  
    pag.press('enter')  
    sleep(0.05)
    Click(executePos)

    #sleep(0.5)
    #pag.press('enter')
    #pag.press(pag.KEYBOARD_KEYS('enter'))
    #pag.typewrite('\n')

    #pag.keyDown('enter')  # 'enter' 키를 누른 상태로 유지합니다.
    #pag.keyUp('enter')    # 'enter' 키를 떼어냅니다.


# 'enter' 키에 해당하는 가상 키 코드는 'enter'입니다.


    #Click(executePos)
    #Click(executePos)


def inputCommand(command):
    sleep(waitTime)
    pag.typewrite(command)
    sleep(1)
    Move(centerUpPos)

# def CommandOpen():
#     Move(commandPos)
#     sleep(waitTime)

#     if devMode == 0 :
#         pag.hotkey('z','x','c','v')
#     else:
#         DragDown(centerPos)
#     sleep(waitTime)    
#     Move(commandPos)
#     sleep(waitTime)
    
# def CommandClose():
#     sleep(waitTime)
#     Move(executePos)
#     sleep(0.1)
#     pag.click()
#     sleep(waitTime)

def ResetFirst():
    
    Move(appUpPos)
    sleep(0.01)
    Move(centerPos)
    pag.press('esc')
    sleep(0.01)
    pag.press('esc')
    sleep(0.01)
    pag.press('esc')
    sleep(0.01)
    Move(cancelPos)
    sleep(waitTime)

def Escape():
    pag.press('esc')
    sleep(0.01)


def DoTeleport():
    PrintUB()
    print("※이동할 지역 번호를 입력해주세요.")
    PrintUB()
    print("[1]메테오스탑 입구\n[2]왕의무덤 입구\n[3]바이런성\n[4]푸리에성\n[5]로덴성\n[6]블랙랜드성")
    PrintUB()
    print("[0]메인메뉴")
    PrintUB()

    num = int(InputNum(6))
    if num==0:
        MainMenu()
    # print("입력성공")
    # sleep(2)
    ResetFirst()
    if num==1:
        Command("doteleport 0 1860 404")
    elif num==2:
        Command("doteleport 0 1380 165")
    elif num==3:
        Command("doteleport 0 350 1100")
    elif num==4:
        Command("doteleport 0 410 125")
    elif num==5:
        Command("doteleport 0 1740 1150")
    elif num==6:
        Command("doteleport 0 1500 360")

setTeleportNum = 0

def CMD_DoTeleport(num):
    # if num == 99 :
    #     num = setTeleportNum
    ResetFirst()
    if num==0:
        MainMenu()
    elif num==1:
        Command("doteleport 0 1860 404")
    elif num==2:
        Command("doteleport 0 1380 165")
    elif num==3 or num == "바이런성":
        Command("doteleport 0 350 1100")
    elif num==4 or num == "푸리에성":
        Command("doteleport 0 410 125")
    elif num==5 or num == "로덴성":
        Command("doteleport 0 1740 1150")
    elif num==6 or num == "블랙랜드성":
        Command("doteleport 0 1500 360")        
    elif num==7 or num == "그렘린숲":
        Command("doteleport 0 527 399")
    elif num == "마을":
        Command("doteleport 0 550 250")

        
def TestMenu():
    clear()
    print("---------------------------------------------------------------")
    print("실행할 테스트를 선택해주세요.")
    print("[1]분해\n[2]레벨별스탯\n[3]장비수치확인\n[4]장비강화확인\n")
    print("[5]각인확인\n[6]드랍템확인\n[7]아이템정보확인\n[8]확률")
    print("[0]메인메뉴")
    print("---------------------------------------------------------------")
    
    num = int(InputNum(8))
    clear()
    if num==0:
        MainMenu()
    elif num == 1:
        Resolution()
    elif num == 2:
        StatPerLv()
    elif num == 3:
        EquipCheck()
    elif num == 4:
        ReinCheck()
    elif num == 5:
        EngraveCheck()
    elif num == 6:
        DropCheck()
    elif num == 7:
        ItemInfoCheck()
    elif num == 8:
        ProbTest()
    
    TestMenu()

def CommandBundle():
    print("---------------------------------------------------------------")
    print("실행할 명령어모음 번호를 입력해주세요.")
    print("[1]나이트풀세팅  [2]아처풀세팅   [3]위저드풀세팅 [4]어쌔신풀세팅")
    print("[0]메인메뉴")
    print("---------------------------------------------------------------")
    num = int(InputNum(5))
    clear()
    if num==0:
        MainMenu()
    elif num >= 1 or num<=4:

        print("---------------------------------------------------------------")
        print("타입 선택")
        print("[1]기본세팅  [2]서버이전세팅")
        print("[0]메인메뉴")
        print("---------------------------------------------------------------")
        typeNum = int(InputNum(2))
        clear()
        if typeNum==0:
            CommandBundle()
        elif typeNum==1:
            SetClass(num, True)
        elif typeNum==2:
            SetClass(num, False)

        


def InputNum(a):#최대번호
    num = input(">")
    while num.isalpha() or int(num) > int(a) or int(num)<0:
        print("다시 입력해주세요.")
        num = input(">")
    return num

def PrintInfo():
    #print("---------------------------------------------------------------")
    print("v1.9 | 220103")
    #print("---------------------------------------------------------------")


def ResetAppSize():
    if devMode==0:
        
        with open("appsize.txt") as f:
            appPos = f.read().splitlines()

    else :
        
        with open("appsize_dev.txt") as f:
            appPos = f.read().splitlines()

    global appX,appY,appW,appH,invenNameBox,invenAmountBox,engraveResultBox
    appX = int(appPos[0])
    appY = int(appPos[1])
    appW = int(appPos[2])
    appH = int(appPos[3])
    
    #MainMenu()
    #invenNameBox=[0.721*appW + appX,0.132*appH + appY, appW*0.243, appH*0.046]
    #invenAmountBox=[0.859*appW + appX,0.319*appH + appY, appW*0.067, appH*0.04]
    print(appW)
    engraveResultBox=[0.384*appW+appX,0.55*appH+appY,0.248*appW,0.172*appH]

def ResetAppSize211214():
    global devMode,appX,appY,appW,appH,invenNameBox,invenAmountBox,engraveResultBox,centerChatBox,reinResultTextBox,reinMultiResultBox,cardAmountBox,autoBtnBox

    with open("info.txt") as infoFile:
        infoTxt = infoFile.read().splitlines()

    #infoTxt[0] : 개발모드/알파모드 확인
    #infoTxt[0] : 알파모드 앱사이즈 세팅 확인
    if infoTxt[0]== "0" :
        devMode = 0

        with open("info_appsize.txt") as infoAppsizeFile:
            infoAppsizeTxt = infoAppsizeFile.read()

        
        if infoAppsizeTxt== "0" :
            with open("appsize.txt") as f:
                appPos = f.read().splitlines()
            #print("A")
        else :
            with open("appsize_"+infoAppsizeTxt+".txt") as f:
                appPos = f.read().splitlines()

            #print("B")

    elif infoTxt[0]== "1" : 
        devMode =1
        
        with open("appsize_dev.txt") as f:
            appPos = f.read().splitlines()


    infoFile.close()

    # with open("appsize.txt") as f:
    #     appPos = f.read().splitlines()

    appX = int(appPos[0])
    appY = int(appPos[1])
    appW = int(appPos[2])
    appH = int(appPos[3])

    infoAppsizeFile.close()
    f.close()

    invenNameBox=[0.721*appW + appX,0.132*appH + appY, appW*0.243, appH*0.046]
    invenAmountBox=[0.859*appW + appX,0.319*appH + appY, appW*0.067, appH*0.04]
    centerChatBox = [0.355 *appW + appX, 0.758*appH + appY , appW*0.336, appH*0.031]
    reinResultTextBox=[0.376*appW+appX,0.14*appH+appY,0.248*appW,0.047*appH]#왼쪽위X,왼쪽위Y,가로,세로]
    reinMultiResultBox=[0.245*appW+appX,0.366*appH+appY,0.236*appW,0.418*appH]#왼쪽위X,왼쪽위Y,가로,세로]
    engraveResultBox=[0.389*appW+appX,0.547*appH+appY,0.252*appW,0.224*appH]#왼쪽위X,왼쪽위Y,가로,세로
    cardAmountBox=[0.03*appW+appX,0.82*appH+appY,0.039*appW,0.034*appH]#왼쪽위X,왼쪽위Y,가로,세로
    autoBtnBox=[0.768*appW+appX,0.887*appH+appY,0.039*appW,0.032*appH]#왼쪽위X,왼쪽위Y,가로,세로




def SetMainUI(_nameText,_verText,_dateText,_makerText,_desText,_warnText):
    
    #print("┌" + "┐".rjust(107,'─'))
    #print(_nameText.center(100))
    PrintUB_Bold()
    print(_nameText + " | " + _dateText)
    PrintUB_Bold()
    #print("│" + "│".rjust(107,'─'))
    #print(_dateText)
    #print("│" + (_verText + " / " + _dateText + " / " + _makerText).rjust(106) +"│")
    # print("├" + "┤".rjust(107,'─'))    
    # print("│" + "※ 설명 ※".center(102) +"│")
    # print("├" + "┤".rjust(107,'─'))
    # print(_desText)
    # print("├" + "┤".rjust(107,'─'))
    # print("│" +  "※ 사전세팅 ※".center(100) +"│")
    # print("├" + "┤".rjust(107,'─'))
    # print(_warnText)
    # print("└" + "┘".rjust(107,'─'))

def GetElapsedTime(_time):
        
    now = datetime.datetime.now()
    #print((now+datetime.timedelta(seconds=_time)).strftime('%m-%d %H:%M:%S'))
    
    #pyqt5버전
    #return (now+datetime.timedelta(seconds=_time))#.strftime('%m-%d %H:%M:%S')
    #cmd버전
    return (now+datetime.timedelta(seconds=_time)).strftime('%m-%d %H:%M:%S')

def GetElapsedTimeAuto(_time):
        
    now = datetime.datetime.now()
    #print((now+datetime.timedelta(seconds=_time)).strftime('%m-%d %H:%M:%S'))
    
    #pyqt5버전
    return (now+datetime.timedelta(seconds=_time))#.strftime('%m-%d %H:%M:%S')
    #cmd버전
    #return (now+datetime.timedelta(seconds=_time)).strftime('%m-%d %H:%M:%S')

def ChangeSetValue(txtFileName, setMsg):


    setVal = list(range(0,len(setMsg)))
    tempMsg = list(range(0,len(setMsg)))
    
    for i in range(len(setMsg)) :
        tempMsg[i] = setMsg[i]

    for i in range(len(setMsg)) :
        
        print(setMsg[i])
        setVal[i] = input(">")


    setFile = open(txtFileName+ ".txt", 'w')

    for j in range(len(setMsg)) :
        setFile.write(str(setVal[j]))
        setFile.write('\n')
    
    setFile.close()



    setVal.clear()

    return

def GetCurrentTime():
        
    return datetime.datetime.now()#.strftime('%m-%d %H:%M:%S')


def GetConsumedTime(_startTime):
        
    now = datetime.datetime.now()
    #return (now - datetime.timedelta(seconds=_startTime)).strftime('%m-%d %H:%M:%S')
    return (now -_startTime)#.timedelta(seconds)#.strftime('%S')

def GetMousePos():
    return pag.position()

def VlookupData(excelFileName):
    if excelFileName == "" :
        excelFileName = "itemList.xlsx"

    getFile = pd.read_excel(excelFileName)

# def getXlFile(xlFileName):
#     #getFile = pd.read_excel(xlFileName,sheet_name='DT_Item',usecols="A,B")
#     if "item" in xlFileName :
#         global itemListDataFrame
#         itemListDataFrame = pd.read_excel(xlFileName,usecols="A,B")
#         itemListDataFrame.set_index('mID', inplace = True)
#     elif "transform" in xlFileName :
#         global transformListDataFrame
#         transformListDataFrame = pd.read_excel(xlFileName,usecols="A,B")
#         transformListDataFrame.set_index('mID', inplace = True)
#     elif "servant" in xlFileName :
#         global servantListDataFrame
#         servantListDataFrame = pd.read_excel(xlFileName,usecols="A,B")
#         servantListDataFrame.set_index('mID', inplace = True)


# def searchItemByName(itemType, itemName):
#     try:
#         if itemType != "" :
#             itemType = itemType + " "
#         result = DF값불러오기(df_item,"mName",f"{itemType}{itemName}","mID")
#         #if itemType == "" :
#         return result#int(itemListDataFrame.index[itemListDataFrame['mName']==itemType + itemName][0])

#         #else :
#         #    return int(itemListDataFrame.index[itemListDataFrame['mName']==itemType + " " +itemName][0])
#     except :
#         return "아이템 없음"

def executeCommand(mainCmd, arguments):
    temp = ""
    for i in range(0,len(arguments)) :
        
        temp = temp + " " + arguments[i]    
    temp = mainCmd + temp
    Command(temp)

# def executeTestCase():
#     #testCaseName = "autoTest_regist2market"
#     mc.testCaseName(1,1)

#아이템 이름 포함된 것 모두 찾기
def findAllValInDataFrame(df :DataFrame, refCol : str, refVal : str, indexCol : str):
    
    try:
        #temp = itemListDataFrame[itemListDataFrame['mName'].str.contains(str)]
        
        #for i in range(0,len(temp)) :
        #    resultText 
        pd.set_option('max_rows',40)
        pd.set_option('min_rows',40)

        if indexCol != "" :
            tempDf = df.copy()
            tempDf.set_index(indexCol, inplace = True)
        resultText=tempDf[tempDf[refCol].str.contains(refVal)]
        #print(resultText[0])
        return resultText#"success"
    except :
        return "아이템 없음"



def getCsvFile(fileName):
    global df_item
    global df_tran
    global df_serv
    global df_cache
    #getFile = pd.read_excel(xlFileName,sheet_name='DT_Item',usecols="A,B")
    #try : 
    #df_temp = pd.read_csv(fileName,encoding='CP949')
    df_temp = pd.read_csv(fileName)
    df_temp = df_temp.reset_index(drop=True)

    if "item" in fileName :
        df_item = df_temp.copy()
    elif "transform" in fileName :
        df_tran = df_temp.copy()
    elif "servant" in fileName :
        df_serv = df_temp.copy()
    elif "cache" in fileName :
        df_cache = df_temp.copy()
        #df_cache.set_index("mData", inplace = True)

    print(f"success, get csv file : {fileName}")
    
    return df_temp
    
# def getXlFile(fileName):
#     global df_item
#     global df_tran
#     global df_serv
#     global df_cache
#     #df_temp = pd.read_excel(fileName,engine="openpyxl")
#     #df_temp = df_temp.reset_index(drop=True)

#     current_time = datetime.datetime.now()
#     current_time_with_ms = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
#     print(current_time_with_ms)

#     #df_item = pd.read_excel(fileName,engine="openpyxl",usecols=[0,1,2,3])
#     if "아이템" in fileName :
#         for i in tqdm(range(1)):
#             app = xw.App(visible=False)
            
#             temp_book = app.books.add()
#             temp_book = xw.Book(fileName)
#             sheet = temp_book.sheets[0]

#             #col ="A:B"
#             #df_item = sheet.used_range.options(pd.DataFrame,index=False,columns = col).value
#             df_item = sheet.used_range.options(pd.DataFrame,index=False).value
#             df_item["mID"] = df_item["mID"].astype(int)
#             #df_item = df_item.reset_index(drop=True)
#             app.quit()
#             print(df_item)
        
#         #for chunk in tqdm(pd.read_excel(fileName,chunksize = 1000)):
#         #    print("4")
#         #df_temp = df_temp.reset_index(drop=True)
#         #df_item = df_temp.copy()
#     # elif "transform" in fileName :
#     #     df_tran = df_temp.copy()
#     # elif "servant" in fileName :
#     #     df_serv = df_temp.copy()
#     # elif "cache" in fileName :
#     #     df_cache = df_temp.copy()
#         #df_cache.set_index("mData", inplace = True)

#     current_time = datetime.datetime.now()
#     current_time_with_ms = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
#     print(current_time_with_ms)
#     print(f"success, get xl file : {fileName}")
    
    #return df_temp
# def findValInDataFrame(df : DataFrame, refCol : str, refVal : str, targetCol : str): #데이터 프레임, 참조할 열, 참조할 값, 찾을 값이 있는 열
#     tempDf = df.copy()
#     tempDf = tempDf.reset_index(drop=True)
    
#     tempDf.set_index(refCol, inplace = True)
#     #try : 
#     targetVal = tempDf.loc[refVal,targetCol]
#     del tempDf
#     gc.collect()
#     #print(f'findValInDataFrame:{targetVal}')
    
#     return targetVal
#     # except : 
#     #     print(f"error in {df}/{refCol}/{refVal}/{targetCol}")
#     #     del tempDf
#     #     gc.collect()


# def findValInDataFrame2(df : DataFrame, refCol : str, refVal : str, targetCol : str): #데이터 프레임, 참조할 열, 참조할 값, 찾을 값이 있는 열
    
#     targetVal = df.loc[df[refCol]==refVal,targetCol]
    
#     print(targetVal[1])
#     return targetVal[1]


def DF값불러오기(df : DataFrame, key : str, refVal : str, targetCol : str):


    # DataFrame에서 key 값에 해당하는 value1 가져오기
    try:
        resultVal = df.loc[df[key] == refVal, targetCol].values[0]
    except:
        resultVal = df.loc[df[key] == int(refVal), targetCol].values[0]
    print(resultVal)
    return resultVal


def saveCacheData(value : str,refCol :str, key : str , targetCol : str):#참조 데이터(index), 수정할 열(col)
    #tempID = df_cache[df_cache['mData']==val].index[0]
    
    #try :
    #tempDf = df_cache.reset_index(drop=True)
    #tempDf.set_index(refCol, inplace = True)
    #df_cache[tempID][targetCol] = val
    #except KeyError:
    #    print("keyError")
    #tempID =df_cache.index[df_cache['mData']]
    #tempID = findValInDataFrame(df_cache,"mData",val,"mText")
    #df_cache.loc[tempID,[]]
    df_cache.loc[df_cache[refCol]==key,targetCol] = value
    
def 텍스트파일_내용추가(파일명 :str, targetStr :str): #target : item/tran/serv
    #fName = f'./data/etc/{targetFileName}History.txt'

    # if not os.path.isfile(fName):                                                           
    #     with open(fName,'a',encoding='utf-8') as tx:
    #         tx.write("날짜|itemID|scrollID|isEnchanted|isBlessed|isKept|isSafe|totalCount|passCount|passProb")    
    contents = ""

    if os.path.exists(파일명) :
        with open(파일명,'r',encoding='utf-8') as f:
            contents = f.read()
        f.close()

    with open(파일명,'a',encoding='utf-8') as f:
        if targetStr not in contents :
            f.write(targetStr + "\n")

    f.close()

def 텍스트파일_내용삭제(파일명 :str, 삭제스트링 :str):
    #file_path = f'./data/etc/{파일명}History.txt'
    # Read the contents of the file
    with open(파일명, 'r',encoding='utf-8') as file:
        lines = file.readlines()

    # Search for the target string and remove it from the contents
    modified_lines = [line for line in lines if 삭제스트링 not in line]

    # Write the modified contents back to the file
    with open(파일명, 'w',encoding='utf-8') as file:
        file.writelines(modified_lines)

def 최신파일찾고열기():

    folder_path = r'D:\R2A'
    target_file = '아이템_230620 - 복사본.csv'

    def find_latest_file(folder):
        latest_file = None
        latest_time = datetime.datetime.min

        for root, dirs, files in os.walk(folder):
            if target_file in files:
                file_path = os.path.join(root, target_file)
                modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if modified_time > latest_time:
                    latest_file = file_path
                    latest_time = modified_time

        return latest_file

    latest_file_path = find_latest_file(folder_path)
    if latest_file_path:
        # 파일 실행 코드 작성
        print(f"가장 최신의 파일 실행: {latest_file_path}")
        os.startfile(os.path.normpath(latest_file_path))

    else:
        print(f"'{target_file}' 파일을 찾을 수 없습니다.")

# if __name__ == "__main__" : 
#     최신파일찾고열기()