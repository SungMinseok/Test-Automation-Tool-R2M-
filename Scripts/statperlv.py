import img2str as i2s
import pyautogui as pag
from time import sleep
import os
import msdata as ms
import time
#import keyboard

def StatPerLv():

    #####기본 세팅(폴더생성)
    path = "./screenshot/레벨 별 스탯"+ time.strftime("_%m%d")
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
    ######################


    #screenWidth, screenHeight = pag.size()
    print("--------------------------------------------------------------")
    print("레벨별 스탯 TEST")    
    print("설명 : 레벨 별 스탯이 스크린샷으로 저장됩니다.")
    print("설명 : 레벨 별 경험치가 스크린샷으로 저장됩니다.")
    print("ver 1.1 / 210622 / made by sms")
    print("---------------------------------------------------------------")

    lvNum = input("최대 레벨을 설정해주세요.(1~199)([0]테스트메뉴) : ")
    print("실행중...")
    if lvNum!="0":
        
        try:
            for i in range(1,int(lvNum)+1):
                ms.ResetFirst()
                ms.Command("lv "+str(i))
                sleep(1)
                
                ms.Capture(path+"/레벨"+str(i)+"_0")

                ms.Move(ms.lvBtn)
                sleep(0.2)

                ms.Move(ms.statBtn)
                sleep(0.2)
                ms.Move(ms.statdetailBtn)
                sleep(0.2)
                ms.Capture(path+"/레벨"+str(i)+"_1")

                ms.Move(ms.statdetailPos)
                
                ms.DragUp(ms.statdetailPos)
                sleep(1.1)
                ms.Capture(path+"/레벨"+str(i)+"_2")

                # ms.Move(ms.statdetailPos)
                # ms.DragUp(ms.statdetailPos)
                # sleep(2)
                # ms.Capture(path+"/레벨"+str(i)+"_2")

                sleep(ms.waitTime)
        except KeyboardInterrupt:
        #except keyboard.is_preesed('f7'):
            print("종료")

"""
HUD 능력치창 캡처
"""
def captureCurrentStat():
    path = "./screenshot/captureCurrentStat"+ time.strftime("_%y%m%d")
    fileName= f'{path}/result.txt'
    if not os.path.isdir(path):                                                           
        os.mkdir(path)

    ms.ResetFirst()

    ms.Click(ms.lvBtn,1)
    ms.Click(ms.statBtn,0.2)
    ms.Click(ms.statdetailBtn,0.2)

    for i in range(0,4):
        if i != 0 :
            ms.Move(ms.statdetailPos)
            pag.dragRel(0, -500, 1, button='left')

            sleep(3)

        captureTargetName = ms.captureSomeBox("statDetailBox_statAmt")
        data = i2s.getNumbersInColumnFromImg_0(captureTargetName)
        print(data)


    with open(fileName,'a',encoding='utf-8') as f:
        #tx.write(tempCardNameArray[j] +"|" + tempCardAmountArray[j] + "\n")
        f.write(f'\n')



    # captureTargetName = ms.captureSomeBox("statDetailBox_statAmt")
    # data = i2s.getNumbersInColumnFromImg_0(captureTargetName)
    # print(data)

if __name__ == "__main__" : 
    #StatPerLv()
    captureCurrentStat()