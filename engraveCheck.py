import pyautogui as pag
from time import sleep
import os
import shutil
import msdata as ms
import time
import img2str
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import re
# Create a Tkinter root window (you can hide it if you don't want to display it)
root = tk.Tk()
root.withdraw()

langCode = ""
signature_data_file = fr'./data/etc/각인보정.xlsx'
#global path
path = "./screenshot/EngraveCheck"+ time.strftime("_%y%m%d")
if not os.path.isdir(path):                                                           
    os.mkdir(path)
# def EngraveCheck():
#     global path
#     path = "./screenshot/EngraveCheck"+ time.strftime("_%y%m%d")
#     if not os.path.isdir(path):                                                           
#         os.mkdir(path)


#     #print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#     ms.PrintUB()
#     print(f"각인 TEST || {ms.get_last_modified_date(os.path.realpath(__file__))}")
#     ms.PrintUB()
#     #print("ver 1.0 / 210615")        
#     print("[1]아이템id입력\n[2]텍스트파일\n[3]능력치찾기\n[4]능력치찾기(라이브)\n[5]텍스트파일(231106)\n[6]각인보정")
#     print("[0]돌아가기")
#     ms.PrintUB()
#     num = int(ms.InputNum(45))
#     ms.clear()
#     if num==0:
#         ms.TestMenu()
#     elif num==1:
#         Engraving1()
#     elif num==2:
#         Engraving2()
#     elif num==3:
#         Engraving3()
#     elif num==4:
#         Engraving4()
#     elif num==5:
#         Engraving5()
#     elif num==6:
#         target_file_path = filedialog.askopenfilename(filetypes=[(("XLSX Files", "*.xlsx"))])
#         output_file_path = os.path.join(path, f'{os.path.basename(target_file_path).split(".")[0]}_보정.xlsx')
#         correct_signature_data(target_file_path,output_file_path)
    
#     EngraveCheck()

# def Engraving1():

#     itemNum = input("아이템 id를 입력해주세요([0]돌아가기) : ")
#     if itemNum == "0" : 
#         EngraveCheck()

#     count = int(input("각인 테스트 횟수를 입력해주세요(1~) : "))
#     print("[0]일반각인석 [1]축복각인석 : ")
#     typeNum = int(ms.InputNum(1))

#     lang = int(input("[0]국내 [1]대만 : "))
#     if lang == 0 :
#         langCode = 'kor'
#     else :
#         langCode = 'chi_tra'
#     extraPath = path + "/"+ itemNum + time.strftime("_%H%M")
#     if not os.path.isdir(extraPath):                                                           
#         os.mkdir(extraPath) 
#     else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
#         shutil.rmtree(extraPath)                                                           
#         os.mkdir(extraPath)  
#     #try : 
#     if count <= 0 :
            
#         print("다시 입력해주세요.")
#         Engraving1()

#     else :
#         print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 3.2) +")")

#         ms.ResetFirst()
#         ms.Command("cleanupinventory")

        
#         if typeNum == 0 :
#             ms.Command("additem 700 100000000")
#         elif typeNum ==1 :
#             ms.Command("additem 701 100000000")

#         ms.Command("additem 999 2000000000")
#         ms.Command("additem "+itemNum+" 1")
#         ms.Move(ms.menuPos1)
#         ms.Move(ms.invenBtnUp2)
#         ms.Move(ms.invenBtn0)
#         pag.click()
#         ms.Move(ms.invenBtn0)

#         txtName = path+"/"+str(itemNum)+"_"+str(count)+"EA"

#         for i in range(0,count) :
#             print(str(i+1) +"/" + str(count), end='\r')
#             ms.Move(ms.engraveBtn)
#             sleep(2)
#             #if captureTypeNum == 0 :
#             ms.CaptureEngraveRes(extraPath+"/"+str(i))
#             if typeNum == 0 :
#                 img2str.Indiv_Engrave(txtName+"_0.txt",extraPath+"/"+str(i)+".jpg",langCode)
#             elif typeNum ==1 :
#                 img2str.Indiv_Engrave(txtName+"_1.txt",extraPath+"/"+str(i)+".jpg",langCode)

#             sleep(0.01)

    
#         #print("다시 입력해주세요.")
#     Engraving1()
        
# def Engraving2():  
    
#     targetTxtFileName = f'각인.txt'
    
#     print(f'{targetTxtFileName=}')   
#     count = int(input("각인 테스트 횟수를 입력해주세요(1~) : "))
#     #lang = int(input("[0]국내 [1]대만 : "))
#     lang_code = 'kor' if int(input("[0]국내 [1]대만 : ")) == 0 else 'chi_tra'
#     # if lang == 0 :
#     #     langCode = 'kor'
#     # else :
#     #     langCode = 'chi_tra'
#     # print("[0]한 화면 스크린샷 [1]전체 화면 스크린샷 : ")
#     # captureTypeNum = int(ms.InputNum(1))

#     with open(targetTxtFileName) as f:
#         lines = f.read().splitlines()

#     print("전체 실행횟수 : " + str(len(lines)))
#     print("전체 예상 종료 시각 : " + str(ms.GetElapsedTime((10+count * 3.2 )* float(len(lines)))))

#     for line in lines:
# #아이템 별 폴더 추가 생성
#         #if folderCheck == 1:
#         itemID, scrollID = line.split(',')
        
#         extraPath = path + "/"+ itemID + time.strftime("_%H%M")
#         if not os.path.isdir(extraPath):                                                           
#             os.mkdir(extraPath)  
#         else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
#             shutil.rmtree(extraPath)                                                           
#             os.mkdir(extraPath)  


#         #try : 
#         if count <= 0 :
                
#             print("다시 입력해주세요.")
#             Engraving2()

#         else :
#             print("실행 중... (예상 종료 시각 : "+ms.GetElapsedTime(10+count * 3.2) +")")
#             #print("실행 중 입니다...(예상 소요 시간 : " + str(count * 1.5) + " 초)")

#             ms.ResetFirst()
#             ms.Command("cleanupinventory")

            
#             #if scrollID == 0 :
#             ms.Command(f"additem {scrollID} 100000000")
#             #elif scrollID ==1 :
#                 #ms.Command("additem 701 100000000")

#             ms.Command("additem 999 2000000000")
#             ms.Command("additem "+itemID+" 1")
#             ms.Move(ms.menuPos1)
#             ms.Move(ms.invenBtnUp2)
#             ms.Move(ms.invenBtn0)
#             pag.click()
#             ms.Move(ms.invenBtn0)

#             txtName = path+"/"+str(itemID)+"_"+str(count)+"EA"

#             for i in range(0,count) :
#                 print(str(i+1) +"/" + str(count), end='\r')
#                 ms.Move(ms.engraveBtn)
#                 sleep(2)                
#                 #if captureTypeNum == 0 :
#                 ms.CaptureEngraveRes(extraPath+"/"+str(i))
#                 #if scrollID == 0 :
#                     #img2str.Indiv_Engrave(txtName+"_0.txt",extraPath+"/"+str(i)+".jpg",langCode)
#                 #elif scrollID ==1 :
#                 img2str.Indiv_Engrave(f'{txtName}_{scrollID}.txt',extraPath+"/"+str(i)+".jpg",lang_code)
                
                
                
#                 # elif captureTypeNum ==1 : 
#                 #     ms.CaptureFull(extraPath+"/"+str(i))
#                 # sleep(0.01)
#                 #sleep(1)
        
#         # except : 
#         #     print("다시 입력해주세요.")
#     Engraving2()



def 각인능력치찾기_알파():
    """각인능력치찾기"""
    ms.PrintUB()
    print("각인 능력치 찾기 TEST")
    ms.PrintUB()

    itemNum = input("아이템 ID([0]돌아가기) : ")
    if itemNum == "0" : 
        return

    targetStr = input("찾을 능력치 텍스트 : ")
    print("[0]일반각인석 [1]축복각인석 : ")
    typeNum = int(ms.InputNum(1))

    lang = int(input("[0]국내 [1]대만 : "))
    if lang == 0 :
        langCode = 'kor'
    else :
        langCode = 'chi_tra'

    extraPath = path + "/"+ itemNum + time.strftime("_%H%M")
    if not os.path.isdir(extraPath):                                                           
        os.mkdir(extraPath) 
    else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
        shutil.rmtree(extraPath)                                                           
        os.mkdir(extraPath)  
    #try : 
    #if count <= 0 :
            
    #    print("다시 입력해주세요.")
    #    Engraving3()

    #else :
    #print("실행 중... (예상 종료 시간 : "+ms.GetElapsedTime(10+count * 3.2) +")")

    ms.ResetFirst()
    ms.Command("cleanupinventory")

    
    if typeNum == 0 :
        ms.Command("additem 700 100000000")
    elif typeNum ==1 :
        ms.Command("additem 701 100000000")

    ms.Command("additem 999 2000000000")
    ms.Command("additem "+itemNum+" 1")
    ms.Move(ms.menuPos1)
    ms.Move(ms.invenBtnUp2)
    ms.Move(ms.invenBtn0)
    pag.click()
    ms.Move(ms.invenBtn0)

    txtName = path+"/"+str(itemNum)

    i = 1
    resultText = ""
    
    while True :#targetStr == resultText :
        print(f'>{i}회 째 실시', end='\r')
        ms.Move(ms.engraveBtn)
        sleep(2)
        ms.CaptureEngraveRes(extraPath+"/"+str(i))
        resultText = img2str.Indiv_Engrave(txtName+"_"+str(typeNum)+".txt",extraPath+"/"+str(i)+".jpg",langCode)
        print(resultText)

        if targetStr in resultText :
            print(f'{i}번 만에 찾았다!')
            break

        #print("못찾았다")
        

        sleep(0.01)

        i=i+1

    

def 각인능력치찾기_라이브():

    targetStr = input("찾을 능력치 텍스트 : ")
    lang = int(input("[0]국내 [1]대만 : "))
    if lang == 0 :
        langCode = 'kor'
    else :
        langCode = 'chi_tra'
    
    extraPath = path + "/"+ time.strftime("_%H%M")
    if not os.path.isdir(extraPath):                                                           
        os.mkdir(extraPath) 
    else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
        shutil.rmtree(extraPath)                                                           
        os.mkdir(extraPath)  

    i = 1
    while True :#targetStr == resultText :
        print(f'>{i}회 째 실시', end='\r')
        ms.Move(ms.engraveBtn)
        sleep(2)
        ms.CaptureEngraveRes(extraPath+"/"+str(i))
        resultText = img2str.Indiv_Engrave(extraPath+"/"+str(i)+".txt",extraPath+"/"+str(i)+".jpg",langCode)
        print(resultText)

        if targetStr in resultText :
            print(f'{i}번 만에 찾았다!')
            break

        #print("못찾았다")
        

        sleep(0.01)

        i=i+1

    
    #Engraving4()

def 각인확인(): 
    '''
    2023-11-06
    xlsx 저장
    '''
    
    
    targetTxtFileName = f'각인.txt'
    isFileOpen = input('1 입력 시 각인.txt 파일 오픈(각인석 id 미입력 시 자동 축각)')
    if isFileOpen == '1':
        os.startfile(targetTxtFileName)
    

    print(f'{targetTxtFileName=}')   
    count = int(input("각인 테스트 횟수를 입력해주세요(1~) : "))
    lang_code = 'kor' if int(input("[0]국내 [1]대만 : ")) == 0 else 'chi_tra'
    shot_wait_time = 2 if lang_code == 'kor' else 2.2

    with open(targetTxtFileName) as f:
        lines = f.read().splitlines()

    print("전체 실행횟수 : " + str(len(lines)))
    print("전체 예상 종료 시각 : " + str(ms.GetElapsedTime((10+count * 3 )* float(len(lines)))))

    for line in lines:
#아이템 별 폴더 추가 생성
        #if folderCheck == 1:
        try:
            itemID, scrollID = line.split(',')
        except:
            itemID = line
            scrollID = '701'
        result_file_name = os.path.join(path,f'{itemID}_{scrollID}.xlsx')
        
        extraPath = path + "/"+ itemID + time.strftime("_%H%M")
        if not os.path.isdir(extraPath):                                                           
            os.mkdir(extraPath)  
        else :#있을경우 삭제하고 다시생성(스샷 덮어쓰기가 안되서...0719)
            shutil.rmtree(extraPath)                                                           
            os.mkdir(extraPath)  

        #try : 
        if count <= 0 :
                
            print("다시 입력해주세요.")
            return

        else :
            print("실행 중... (예상 종료 시각 : "+ms.GetElapsedTime(10+count * 3.2) +")")
            #print("실행 중 입니다...(예상 소요 시간 : " + str(count * 1.5) + " 초)")

            ms.ResetFirst()
            ms.Command("cleanupinventory")

            
            #if scrollID == 0 :
            ms.Command(f"additem {scrollID} 100000000")
            #elif scrollID ==1 :
                #ms.Command("additem 701 100000000")

            ms.Command("additem 999 2000000000")
            ms.Command("additem "+itemID+" 1")
            ms.Move(ms.menuPos1)
            ms.Move(ms.invenBtnUp2)
            ms.Move(ms.invenBtn0)
            pag.click()
            ms.Move(ms.invenBtn0)

            #data = []
                
            for i in range(0,count) :
                print(str(i+1) +"/" + str(count), end='\r')
                ms.Move(ms.engraveBtn)
                sleep(shot_wait_time)                
                #if captureTypeNum == 0 :
                img_file_name = ms.CaptureEngraveRes(extraPath+"/"+str(i))
                
                result_text = img2str.extract_text_from_image(img_file_name,lang_code)
                lines = result_text.split('\n')

                temp_data = []
                row_data = [i]
                columns = ['index']
                
                for j, line in enumerate(lines, start=1):
                    row_data.append(line)
                    columns.append(str(j))

                #data.append(row_data)
                temp_data.append(row_data)
                df = pd.DataFrame(temp_data, columns=columns)
                
                ms.save_df_to_excel(result_file_name,df,autoOpen=False)

                
                
                
                # elif captureTypeNum ==1 : 
                #     ms.CaptureFull(extraPath+"/"+str(i))
                # sleep(0.01)
                #sleep(1)
        
        # except : 
        #     print("다시 입력해주세요.")


def 각인보정():
    
    target_file_path = filedialog.askopenfilename(filetypes=[(("XLSX Files", "*.xlsx"))])
    output_file_path = os.path.join(path, f'{os.path.basename(target_file_path).split(".")[0]}_보정.xlsx')
    #try:
    # 각인보정 파일 읽기
    correction_df = pd.read_excel(signature_data_file)
    correction_df = correction_df.applymap(str)
    data_df = pd.read_excel(target_file_path)
    correction_df['before'] = correction_df['before'].apply(lambda x: re.escape(x))
    correction_dict = correction_df.set_index('before')['after'].to_dict()
    
    data_df = data_df.replace(correction_dict, regex=True)
    # 수정된 내용을 새 파일로 저장
    data_df.to_excel(target_file_path, index=False)
    
    print("각인 데이터가 보정되었습니다.")
    # except Exception as e:
    #     print(f"보정 과정에서 오류 발생: {e}")

# 각인보정 함수 호출
#correct_signature_data('각인보정.xlsx', '각인데이터 문서.xlsx')



import inspect
def display_menu():
    functions = [func for func in globals() if callable(globals()[func]) and inspect.isfunction(globals()[func])]
    ms.PrintUB()
    print(f"각인 TEST || {ms.get_last_modified_date(os.path.realpath(__file__))}")
    ms.PrintUB()
    for i, func_name in enumerate(functions, start=1):
        print(f"[{i}] {func_name}")
    ms.PrintUB()

def execute_function_by_index(index):
    functions = [func for func in globals() if callable(globals()[func]) and inspect.isfunction(globals()[func])]

    if 1 <= index <= len(functions):
        selected_func_name = functions[index - 1]
        selected_func = globals()[selected_func_name]
        selected_func()
    else:
        print("Invalid index. Please select a valid option.")
        
if __name__ == "__main__":
    
    # app_pos, app_type = ms.get_target_app_pos()
    # print(app_pos, app_type)
    # ms.appX, ms.appY, ms.appW, ms.appH = app_pos[0],app_pos[1],app_pos[2],app_pos[3]
    # ms.플레이어변경(app_type)

    while True:
        display_menu()
        user_input = input("Enter the index of the function to execute (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        try:
            index = int(user_input)
            execute_function_by_index(index)
        except ValueError:
            print("Invalid input. Please enter a number.")
