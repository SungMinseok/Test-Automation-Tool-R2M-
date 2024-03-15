import func.msdata as ms
import func.R2A as R2A
import time
#import unit_test.

import os
main_dir = "./screenshot/cashshop_payment"
if not os.path.isdir(main_dir):                                                           
    os.mkdir(main_dir)
def 직과금결제_미러로이드():
    #input("유료상점>재화>다이아4000 최우측 슬롯에 위치 후 아무 키나 누르세요.")

    ms.currentPlayer = ms.Player.Mirroid
    ms.appX, ms.appY, ms.appW, ms.appH = 145,33,1194,677
    #R2A.WindowClass.optimizeCurrentAppPos(R2A.WindowClass)
    ms.sleep(0.2)

    ms.Click([0.9489,0.808])#ms.cashshop_last_slot)
    ms.sleep(0.5)
    ms.Click([0.732,1.0059])#ms.cashshop_ok_btn)
    ms.sleep(2)
    
    ms.captureSomeBox3(0.4958,0.6381,0.3392,0.7386,dir=main_dir)#0.4966,0.5495,0.3376,0.7444)
    #ms.captureSomeBox4("cashshop_module_box",
    #                   f'./screenshot/cashshoptest/module_{time.strftime("%y%m%d_%H%M%S")}')
    ms.sleep(0.2)
    #미러로이드 세로 화면 대응
    ms.currentPlayer = ms.Player.Mirroid
    #R2A.WindowClass.optimizeCurrentAppPos(R2A.WindowClass)
    ms.sleep(0.2)

    ms.Click([0.6667,1.2452])#ms.cashshop_module_ok_btn)
    #ms.Click(ms.lvBtn)
    ms.sleep(5)

    #미러로이드 세로 화면 대응
    #ms.currentPlayer = ms.Player.Mirroid
    #R2A.WindowClass.optimizeCurrentAppPos(R2A.WindowClass)
    ms.sleep(0.2)
    
    ms.captureSomeBox3(0.5536,0.6248,0.2538,0.2423,dir=main_dir)
    #ms.Capture(f'./screenshot/cashshoptest/result_{time.strftime("%y%m%d_%H%M%S")}')
    #ms.sleep(0.2)
    #ms.sleep(5)
    ms.Click([0.6809,0.836])#ms.cashshop_result_ok_btn)


if __name__ == "__main__" :
    #R2A.starter()

    print('유료상점UI 최우측 상품 구매')
    count = input('반복 횟수 >: ')
    #R2A.currentAppName = "SM-N971N"
    

    for i in range(0,int(count)):
        직과금결제_미러로이드()
