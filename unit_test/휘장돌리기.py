import func.msdata as ms
import func.img2str as img2str
import os

while True:
    os.system("pause")

    resultText = ""
    ms.sleep(1)
    while resultText.find("成功") == -1 : #실패 > 현재 단계 총 100번까지 반복 > 중간에 성공하면 브레이크 후 다음 단계.

        ms.Move(ms.cardSpotActivateBtn)
        ms.sleep(0.5)
        ms.Move(ms.cardSpotActivateOkBtn)
        ms.sleep(1.5)

        tempCaptureFileName = ms.captureSomeBox("cardSpotEnchantResultBox")
        resultText = img2str.getStringFromImg(tempCaptureFileName,'chi_tra')
    #endregion