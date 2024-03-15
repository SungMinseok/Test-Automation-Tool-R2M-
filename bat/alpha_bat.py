import func.msdata as ms
import time
from time import sleep
import os

def alpha_bat_execute():
    timestr = time.strftime("_%Y%m%d")#time.strftime("_%Y%m%d_%H%M%S")
    path = f"./screenshot/alpha_bat{timestr}/"
    if not os.path.isdir(path):                                                           
        os.mkdir(path)
    
    
    batTargetName = ""
    curPath = ""


    sleep(3)
    #앱실행
    #로그인
    #서버접속
    #인게임접속
    #인게임
    #메뉴시작━━━━━━━━━━━━━━━━
    #유료상점
    #인벤토리
    batTargetName = "inventory"
    curPath = f"{path}/{batTargetName}"
    if not os.path.isdir(curPath):                                                           
        os.mkdir(curPath)
    
    #인벤토리-장비장착/해제
    ms.Move(ms.menuPos1)
    sleep(0.5)
    ms.Move(ms.invenBtnUp1)
    ms.Move(ms.invenBtn0)
    ms.Move(ms.invenBtn0)
    ms.Move(ms.lvBtn)
    sleep(0.5)
    
    ms.Capture(f"{curPath}/0")

    ms.Move(ms.invenBtn0)
    ms.Move(ms.invenBtn0)
    sleep(0.5)

    ms.Capture(f"{curPath}/1")
    #던전
    #거래소
    #퀘스트
    #변신
    #서번트
    #매터리얼
    #제작
    #길드
    #슬롯 강화
    #월드맵
    #아이템 사전
    #랭킹
    #공성/스팟
    #스킬
    #카오스 던전
    #PVP
    #아이템 도감
    #옵션
    #우편함
    #커뮤니티
    #기억
    #출석체크
    #캐릭터
    #아이템
    #파티
    #NPC
    #채팅













if __name__ == "__main__" : 
    #GoCharacterSelectPage()
    alpha_bat_execute()