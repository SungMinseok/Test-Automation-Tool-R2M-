# #from img2str import Img2Str_CardAmountBox
# import img2str
# import pyautogui as pag
# import msdata as ms
# from setappsize import SetAppSize
# from time import sleep
# import os.path
# import random
# import string

# #dadadawawawa
# def initCmdBundle():
#     while True : 
#         ms.PrintUB_Bold()
#         print("※멀티 커맨드")
#         ms.PrintUB()      
#         print("[1]회원 탈퇴\n[2]캐릭터 생성 및 기네아 진입(명령어X)\n[3]캐릭터 생성 및 이동튜토리얼(명령어X)\n[4]캐릭터 풀세팅")
#         ms.PrintUB()      
#         print("[0]메인메뉴")
#         ms.PrintUB()      
#         num2 = int(ms.InputNum(5))
#         ms.clear()
#         if num2==0:
#             break
#         elif num2 ==1:
#             deleteAccount()
#         elif num2 ==2:
#             createAccount()
#         elif num2 ==3:
#             Command_Text()
#         elif num2 ==4:
#             Command_Additems()
#     #elif num2 ==5:
#     #    Command_Direct2()
    
#     #multicommand()


# def 캐릭터탈퇴():
#     while True:
#         ms.PrintUB_Bold()     
#         print("※회원탈퇴")
#         ms.PrintUB()      
#         print("탈퇴 코드까지 자동 입력하여 회원 탈퇴")
#         print("사전세팅 : 마을/비전투 상태")
#         ms.PrintUB()      
#         print("[1]회원탈퇴 시작")
#         print("[0]뒤로가기")
#         ms.PrintUB()    

#         inputNum = (ms.InputNum(1))
#         if inputNum=="0":
#             ms.clear()
#             return
#         ms.ResetFirst()

#         ms.Move(ms.menuPos4)
#         ms.Move(ms.menuPos20)
#         ms.Move(ms.menuMiddleUpperTab5)
#         ms.Move(ms.deleteAccountBtn)
#         ms.Move(ms.okPos)
#         ms.sleep(1)
#         codeResultFileName = ms.captureSomeBox("deleteAccountCodeBox")
#         ms.sleep(0.5)
#         codeID = img2str.Indiv_Eng_Return(codeResultFileName)
#         print(codeID[0:4])
#         ms.sleep(0.5)
#         ms.Move(ms.deleteAccountCodeInput)

#         ms.inputCommand(codeID[0:4])
#         ms.sleep(0.1)
#         ms.Move(ms.okPos)


# def createAccount():
#     while True:
#         ms.PrintUB_Bold()     
#         print("※캐릭터 생성 및 기네아 진입(명령어X)")
#         ms.PrintUB()      
#         print("최초 튜토리얼 진행 및 기네아 섬까지 이동")
#         print("사전세팅 : 캐릭터 직업 선택창에서 대기(나이트)")
#         ms.PrintUB()      
#         print("[1]캐릭터 생성 시작")
#         print("[0]뒤로가기")
#         ms.PrintUB()    

#         inputNum = (ms.InputNum(1))
#         if inputNum=="0":
#             ms.clear()
#             return
#         #ms.ResetFirst()

#         ms.Move(ms.appUpPos)
#         sleep(0.01)
#         ms.Move(ms.characterNameBtn)
#         ms.sleep(0.5)
#         ms.Move(ms.characterNameInput)

#         randomName = ""
#         for i in range(8):
#             randomName += random.choice(string.ascii_letters)
#         ms.sleep(1)

#         ms.inputCommand(randomName)
#         ms.Move(ms.okPos)
#         ms.sleep(1)
        
#         ms.Move(ms.characterCreateBtn)
#         ms.sleep(0.5)

#         ms.Move(ms.characterCreateBtn)



#         ms.sleep(5)

        
#         tempText = ""

#         while tempText != "벨리타" :
#             print("텍스트 대기 중:", tempText)
#             belitaBoxName = ms.captureSomeBox("belitaBox")
#             tempText = img2str.Indiv_Kor_Return(belitaBoxName)
#             sleep(1)

#         ms.Move(ms.centerPos)
#         ms.sleep(0.5)
#         ms.Move(ms.getFirstQuestBtn)
#         ms.sleep(0.5)
#         ms.Move(ms.acceptQuestBtn)
#         ms.sleep(1)


#         pag.press('esc')
#         ms.sleep(0.5)
#         pag.press('esc')
#         ms.sleep(0.5)
#         pag.press('esc')
#         ms.sleep(0.5)
#         pag.press('esc')
#         ms.sleep(1)
#         ms.Move(ms.acceptQuestBtn)
#         ms.sleep(1)

#         pag.press('d')
#         ms.sleep(0.5)

#         pag.keyDown('w')
#         pag.keyDown('a')

#         while tempText != "벨켄" :
#             print("텍스트 대기 중:", tempText)
#             belitaBoxName = ms.captureSomeBox("belitaBox")
#             tempText = img2str.Indiv_Kor_Return(belitaBoxName)
#             sleep(1)

#         pag.keyUp('w')
#         pag.keyUp('a')

        
#         for i in range(3):
#             pag.press('esc')
#             ms.sleep(0.5)

#         #ms.Command("cleanupinventory")
#         #ms.ResetFirst()
#         ms.Move(ms.acceptQuestBtn)
#         ms.sleep(0.5)

#         ms.Move(ms.menuPos1)
#         ms.sleep(0.5)
#         ms.Move(ms.invenBtn3)
#         ms.sleep(0.5)
#         ms.Move(ms.invenBtn3)
#         ms.sleep(0.5)
#         ms.Move(ms.invenMainExitBtn)
#         ms.sleep(0.5)
#         for i in range(3):
#             pag.press('esc')
#             ms.sleep(0.5)
#         ms.Move(ms.acceptQuestBtn)
#         ms.sleep(0.5)
#         ms.Move(ms.getFirstQuestBtn)
#         ms.sleep(0.5)
#         ms.Move(ms.okTeleportBtn)
#         ms.sleep(0.5)
#         ms.Move(ms.tutoMonPos)
#         ms.sleep(0.5)
#         ms.Move(ms.attackBtn)
#         ms.sleep(0.5)

#         while tempText != "호텐 플로츠" :
#             print("텍스트 대기 중:", tempText)
#             belitaBoxName = ms.captureSomeBox("belitaBox")
#             tempText = img2str.Indiv_Kor_Return(belitaBoxName)
#             sleep(1)

#         for i in range(3):
#             pag.press('esc')
#             ms.sleep(0.5)

#         ms.Move(ms.acceptQuestBtn)
#         ms.sleep(0.5)
#         ms.Move(ms.getFirstQuestBtn)
#         ms.sleep(0.5)
#         ms.Move(ms.okTeleportBtn)
#         ms.sleep(0.5)

#         ms.sleep(5)

#         for i in range(4):
#             pag.press('esc')
#             ms.sleep(0.5)

#         ms.Move(ms.acceptQuestBtn)

# def 캐릭터생성_알파():#명령어사용

#     ms.Move(ms.appUpPos)
#     sleep(0.01)
#     ms.Move(ms.characterNameBtn)
#     ms.sleep(0.5)
#     ms.Move(ms.characterNameInput)

#     randomName = ""
#     for i in range(8):
#         randomName += random.choice(string.ascii_letters)
#     ms.sleep(1)

#     ms.inputCommand(randomName)
#     ms.Move(ms.okPos)
#     ms.sleep(1)
    
#     ms.Move(ms.characterCreateBtn)
#     ms.sleep(0.5)

#     ms.Move(ms.characterCreateBtn)



#     ms.sleep(5)

    
#     tempText = ""

#     while tempText != "벨리타" :
#         print("텍스트 대기 중:", tempText)
#         belitaBoxName = ms.captureSomeBox("belitaBox")
#         tempText = img2str.Indiv_Kor_Return(belitaBoxName)
#         sleep(1)

#     ms.Move(ms.centerPos)
#     ms.sleep(0.5)
#     ms.Move(ms.getFirstQuestBtn)
#     ms.sleep(0.5)
#     ms.Move(ms.acceptQuestBtn)
#     ms.sleep(1)


#     pag.press('esc')
#     ms.sleep(0.5)
#     pag.press('esc')
#     ms.sleep(0.5)
#     pag.press('esc')
#     ms.sleep(0.5)
#     pag.press('esc')
#     ms.sleep(1)
#     ms.Move(ms.acceptQuestBtn)
#     ms.sleep(1)

#     pag.press('d')
#     ms.sleep(0.5)

#     pag.press('w')
#     pag.press('a')

#     ms.Command("flowcompletequest 100500")

#     ms.Move(ms.acceptQuestBtn)
#     ms.sleep(0.5)
#     ms.Move(ms.getFirstQuestBtn)
#     ms.sleep(0.5)
#     ms.Move(ms.okTeleportBtn)
#     ms.sleep(0.5)
#     ms.Move(ms.tutoMonPos)
#     ms.sleep(0.5)
#     ms.Move(ms.attackBtn)
#     ms.sleep(0.5)


# def GoCharacterSelectPage():
#     ms.ResetFirst()
#     ms.Move(ms.menuPos4)
#     ms.sleep(0.5)
#     ms.Move(ms.menuPos20)
#     ms.Move(ms.menuMiddleUpperTab5)
#     ms.Move(ms.goCharacterSelectPageBtn)
#     ms.Move(ms.okPos)

# if __name__ == "__main__" : 
#     #GoCharacterSelectPage()
#     #initCmdBundle()
#     캐릭터생성_알파()