import msdata as ms
import img2str as i2s
from time import sleep
import os

def 대기(초:float):
    sleep(초)

def 출력(str):
    print(str)

def 화면리셋() :
    ms.ResetFirst()
    return

def 명령어입력(커맨드:str) :
    ms.Command(커맨드)
    return

def 화면클릭(x,y) :
    return

def 화면클릭(버튼명:str) :
    btn_name = getattr(ms,버튼명)
    ms.Click(btn_name)
    return

def 스크린샷(박스명:str, 저장경로:str) :
    #box_name = getattr(ms,박스명)
    ms.captureSomeBox2(박스명, 저장경로)
    return

def 텍스트변환(이미지경로:str, 저장경로:str):
    data = i2s.getStringFromImg(이미지경로)
    
    with open(저장경로,'a',encoding='utf-8') as tx:
        tx.write(저장경로)
    return

def 현재디렉토리반환():
    current_script_path = os.path.abspath(__file__)
    return os.path.dirname(current_script_path)
    

def 결과저장디렉토리생성(경로:str):

    current_script_path = os.path.abspath(__file__)
    current_script_directory = os.path.dirname(current_script_path)

    result_directory = current_script_directory + f"/{경로}"
    if not os.path.isdir(result_directory):                                                           
        os.mkdir(result_directory)      
    return result_directory

def 대상파일읽기및리스트반환(텍스트파일명:str):
    
    with open(텍스트파일명) as f:
        lines = f.read().splitlines()

    return lines
