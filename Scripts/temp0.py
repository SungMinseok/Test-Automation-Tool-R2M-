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
#pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

  
def temp0():  
    print(ms.PrintUB())
    #path = input("경로 입력 : ")
    #path = "./screenshot/ProbTest_0718/11089_07182155"
    #fileName = "D:\R2MAUTO_ONWORKING\r2mauto_220715\screenshot\ProbTest_0718\11089__07182155"
    #path = #"./screenshot/ProbTest_0718/11089__07182155/"
    defaultPath = "./screenshot/ProbTest_0718/"

    
    paths = os.listdir(defaultPath)
    # ["11089__07182155"
    # ,"11090__07182205"
    # ,"11091__07182215"
    # ,"11092__07182224"
    # ,"12229__07182234"
    # ,"12230__07182243"
    # ,"12231__07182253"
    # ,"12232__07182202"
    
    
    
    
    # ]
    
    
    
    checkString = "沒有"#input("포함 단어 입력 : ")    
    print(ms.PrintUB())
    passCount = 0

    for j in range(len(paths)):
        

        for i in range (0,99) : 

            #getText = img2str.getStringFromImg("./screenshot/ProbTest_0718/11089_07182155/0.jpg",'chi_tra')
            getText = img2str.getStringFromImg(defaultPath + paths[j] + "/"+str(i)+".jpg",'chi_tra')

            if getText.find(checkString) != -1 :
                passCount = passCount + 1

            # if not os.path.isfile("./temp0.txt"):                                                           
            #     with open("./result.txt",'a',encoding='utf-8') as tx:
            #         tx.write("날짜,itemID,scrollID,isKept,isBlessed,isEnchanted,count,passCount,passProb")    

        with open("./resultTTTTT.txt",'a',encoding='utf-8') as tx:
            tx.write("\n"+paths[j]+"," +str(passCount))
            

def temp1():
    pag.mouseDown()
    pag.click(200,200)
    pag.click(200,205)
    pag.click(200,210)
    pag.click(200,220)
    pag.mouseUp()
    # ms.Click(ms.invenBtn0,0)
    # ms.Click(ms.invenBtn1,0)
    # ms.Click(ms.invenBtn2,0)
    # ms.Click(ms.invenBtn3,0)
if __name__ == "__main__" : 
    #temp0()
    temp1()#gpg커맨드창오픈