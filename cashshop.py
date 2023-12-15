import msdata as ms
#import R2A
import time
def 직과금결제_미러로이드():
    #input("유료상점>재화>다이아4000 최우측 슬롯에 위치 후 아무 키나 누르세요.")

    ms.currentPlayer = ms.Player.Mirroid
    R2A.WindowClass.optimizeCurrentAppPos(R2A.WindowClass)
    ms.sleep(0.2)

    ms.Click(ms.cashshop_last_slot)
    ms.sleep(0.5)
    ms.Click(ms.cashshop_ok_btn)
    ms.sleep(2)
    
    ms.captureSomeBox3(0.4966,0.5495,0.3376,0.7444)
    #ms.captureSomeBox4("cashshop_module_box",
    #                   f'./screenshot/cashshoptest/module_{time.strftime("%y%m%d_%H%M%S")}')
    ms.sleep(0.2)
    #미러로이드 세로 화면 대응
    ms.currentPlayer = ms.Player.Mirroid
    R2A.WindowClass.optimizeCurrentAppPos(R2A.WindowClass)
    ms.sleep(0.2)

    ms.Click(ms.cashshop_module_ok_btn)
    #ms.Click(ms.lvBtn)
    ms.sleep(5)

    #미러로이드 세로 화면 대응
    ms.currentPlayer = ms.Player.Mirroid
    R2A.WindowClass.optimizeCurrentAppPos(R2A.WindowClass)
    ms.sleep(0.2)
    
    ms.captureSomeBox3(0,0,1,1)
    #ms.Capture(f'./screenshot/cashshoptest/result_{time.strftime("%y%m%d_%H%M%S")}')
    #ms.sleep(0.2)
    #ms.sleep(5)
    ms.Click(ms.cashshop_result_ok_btn)


if __name__ == "__main__" :

    ms.appX, ms.appY, ms.appW, ms.appH = 145,33,1194,677
    print(ms.appX)
    #R2A.currentAppName = "SM-N971N"

    for i in range(0,1):
        직과금결제_미러로이드()
