# import pyautogui as pag
import msdata as ms
import time
from time import sleep
# from equipcheck import EquipCheck
# from reincheck import ReinCheck
# from engraveCheck import EngraveCheck
# from soulCheck import SoulCheck
# from dropCheck import DropCheck
# from itemInfoCheck import ItemInfoCheck
# import img2str
# from probTest import ProbTest
import pandas as pd
# import openpyxl
# import numpy as np
# import matplotlib.pyplot as plt
# import cmdBundle
# import multicommand as mc
# import importlib
# import googletrans
# import clipboard as cb
# import pyperclip as pc

startTime = time.time()

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
csvDf = pd.read_csv("./data/csv/csvList.csv",encoding='CP949')
itemDataFileName = ms.findValInDataFrame(csvDf,"mData","item","fileName")
tranDataFileName = ms.findValInDataFrame(csvDf,"mData","transform","fileName")
servDataFileName = ms.findValInDataFrame(csvDf,"mData","servant","fileName")
ms.getCsvFile(f"./data/csv/{itemDataFileName}.csv")
ms.getCsvFile(f"./data/csv/{tranDataFileName}.csv")
ms.getCsvFile(f"./data/csv/{servDataFileName}.csv")

#print(ms.findValInDataFrame(ms.df_item,"mID",1,"mName"))
print(ms.findValInDataFrame(ms.df_item,"mName","마을 귀환 주문서","mID"))


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# a = pag.getWindowsWithTitle("alpha_1st")[0]
# print(a.size)
# print(a.left, a.top,a.right,a.bottom)


#pc.copy("ㄴㄹㅇㄴㄹ")
# print(cb.paste())
#ms.Command("11111")
#ms.Command("aaaaa")

# translator = googletrans.Translator()
# targetStr = str(input(">:"))
# result = translator.translate(targetStr,src = 'zh-tw', dest='ko')
# print(result.text)


# csv파일 읽기 221215
#ms.getCsvFile("itemList_221215.csv")
#df.set_index('mID', inplace = True)
#print(df.loc[72000,'mName'])
#df.set_index('mName', inplace = True)
#print(df.loc["+0 아이언 폴액스",'mID'])

#ms.findValInDataFrame(ms.df_item,"mName","+0 아이언 폴액스","mID")

#ms.getXlFile("itemList_220207.xlsx")
#print("완료")












#import sys, numpy
# #暗黑弓箭手

# for _ in range(3):
#     startPos = [0.8497,0.6102]
#     endPos = [0.8497,0.3602]
#     ms.DragToByPos(startPos, endPos, 0.63)
#     ms.sleep(2)
#temp = "EngraveCheck"

#obj = __import__(EngraveCheck.__module__)

#test = getattr(importlib.import_module("engraveCheck"), 'EngraveCheck')

#test()


# ms.CommandOpen()

# #pag.typewrite("additems ")
# pag.hotkey('hanguel')
# pag.typewrite("additems ")
# ms.CommandClose()

#ms.Command("additem")
# # # # # # imgName = input("put : ")
# # # # # # img2str.getNumberFromImg()

# a = np.array([3,4,5])
# # temp = [12]*3
# # b = [0]*3
# b = a/12
# b = np.round(a/12,2)
# #print(' / '.join(str(a)))
# print(' / '.join(map(str,a)))
# print(' / '.join(map(str,b)))




#pag.moveTo(10,10)
#pag.screenshot('my_region.png', region=(0, 0, 300, 300))
#im1 = pag.screenshot('pyautogui.png')

# ms.Move(ms.statdetailPos)
# ms.DragUp(ms.statdetailPos)
# sleep(2)2
# ms.Move(ms.statdetailPos)
# ms.DragUp(ms.statdetailPos)

#ms.Move(ms.menuPos1)
#EquipCheck()
#ReinCheck()
#ms.Resolution()
#EngraveCheck()
#ms.DragDown(ms.invenBtn2)
#SoulCheck()
#DropCheck()
#ItemInfoCheck()
# for idx in range(5) : 
#     ms.Move(getattr(ms, 'invenBtn{}'.format(idx)))


# ms.CaptureInvenDes("test",2)
# img2str.Indiv_Item('result.txt','test.jpg')

#global var

# def Test() :
#     global var
#     var = 3

# def Print() :
#     print(var)

# Test()
# Print()
# for i in range(0,10) :
#     print(0.094*float(i))


#ms.CaptureCenterChatBox("test")

#img2str.Indiv_Item("result_210907.txt","test_20210907_125445.jpg")

#img2str.Img2Str_CardAmountBox()

#ProbTest()
#EngraveCheck()



#region 엑셀 연동


# #getFile = pd.read_excel("aitem.xlsx",sheet_name='DT_Item',usecols="A,B")
# getFile = pd.read_excel("aitem.xlsx",usecols="A,B")
# df = pd.DataFrame(getFile)
# getFile.set_index('mID', inplace = True)


# while True:
#     itemName = input(">")
#     try:
#         print(int(getFile.index[getFile['mName']=='+0 '+itemName][0]))
#     except :
#         print("아이템 없음")
# #쭉출력
#     for i in range(100):
#         print(int(getFile.index[getFile['mName'].str.contains(itemName)][i]))
        
        
        
#         print(getFile[getFile['mName'].str.contains(itemName)][i])
#     print(int(df.index[df['mName'].str.contains(itemName)][0]))
#print(df.index[df['mName'].str.contains('포션')][2])
#print(len(df.index[df['mName'].str.contains('포션')]))


#endregion


#cmdBundle.initCmdBundle()

#mc.autoTest_regist2market("world","test0302")


# testCaseName = [autoTest_regist2market]
# mc.testCaseName("world","test0302")






# 캐릭터 재접속 

# ms.ResetFirst()
# ms.Move(ms.menuPos4)
# ms.Move(ms.menuPos20)
# sleep(0.5)
# ms.Move(ms.uiTabBtn5_7)
# ms.Move(ms.goCharacterSelectPageBtn)
# ms.Move(ms.okPos)






print(f'함수 수행 소요 시간 : {time.time()-startTime:.4f} sec')
sleep(2)