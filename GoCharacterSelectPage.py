#from img2str import Img2Str_CardAmountBox
import img2str
import pyautogui as pag
import msdata as ms
from setappsize import SetAppSize
from time import sleep
import os.path
import random
import string

def GoCharacterSelectPage():
    ms.ResetFirst()
    ms.Move(ms.menuPos4)
    ms.sleep(0.5)
    ms.Move(ms.menuPos20)
    ms.Move(ms.menuMiddleUpperTab5)
    ms.Move(ms.goCharacterSelectPageBtn)
    ms.Move(ms.okPos)

if __name__ == "__main__" : 
    #GoCharacterSelectPage()
    GoCharacterSelectPage()