from time import sleep
import numpy as np
import cv2
import time
import os
def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8) :
    try : 
        n = np.fromfile(filename,dtype)
        img = cv2.imdecode(n,flags)
        return img
    except Exception as e:
        print(e)
        return None

def imwrite(filename, img, params =None) :
    try :
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext,img,params)
        if result :
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e :
        print(e)
        return False


def MergeImg_Equip(_itemNum,_equipType,_extraPath):
    
    for k in range(0,4):
        if k == 3 and _equipType != 3:
            break
        target = [0 for i in range(14)]

        for i in range(0,14):
            #print(i)
            if _equipType == 2 and i == 10:
                break
            target[i] = imread(_extraPath+"/"+str(int(_itemNum)+i)+"_"+str(k)+".jpg")

        temp = imread(_extraPath+"/"+str(int(_itemNum)+0)+"_"+str(k)+".jpg")
        targetNull = 255- temp

        mergeh0 = cv2.hconcat([target[0],target[1],target[2],target[3],target[4]])
        mergeh1 = cv2.hconcat([target[5],target[6],target[7],target[8],target[9]])
        if _equipType != 2 :
            mergeh2 = cv2.hconcat([target[10],target[11],target[12],target[13],targetNull])
            mergev = cv2.vconcat([mergeh0,mergeh1,mergeh2])
        else :
            mergev = cv2.vconcat([mergeh0,mergeh1])

        imwrite(_extraPath+"/Merge/"+str(_itemNum)+"_merge_"+str(k)+'.jpg', mergev)

        
def MergeImg_Item(_itemNum,_extraPath,_modeNum):
    
    for k in range(0,int(_modeNum)):
        
        target = [0 for i in range(15)]

        for i in range(0,15):
            #print(i)
            # if _equipType == 2 and i == 10:
            #     break
            try : 
                target[i] = imread(_extraPath+"/"+str(int(_itemNum)+i)+"_"+str(k)+".jpg")
            except :
                target[i] = imread(_extraPath+"/"+str(int(_itemNum))+"_"+str(k)+".jpg")

        temp = imread(_extraPath+"/"+str(int(_itemNum)+0)+"_"+str(k)+".jpg")
        targetNull = 255- temp

        mergeh0 = cv2.hconcat([target[0],target[1],target[2],target[3],target[4]])
        mergeh1 = cv2.hconcat([target[5],target[6],target[7],target[8],target[9]])
        
        mergeh2 = cv2.hconcat([target[10],target[11],target[12],target[13],target[14]])
        mergev = cv2.vconcat([mergeh0,mergeh1,mergeh2])

        imwrite(_extraPath+"/Merge/"+str(_itemNum)+"_merge_"+str(k)+'.jpg', mergev)

def MergeImg_Drop(_monId,_amt,_dropCtg,_extraPath):
    print("ee")
    imgMaxCount = 20
    #for k in range(0,2):
    target = [0 for i in range(imgMaxCount)]

    for i in range(0,_dropCtg):
        target[i] = imread(_extraPath+"/"+str(_monId)+"_"+str(_amt)+"EA_"+str(i)+"_name.jpg")
        
    for i in range(_dropCtg,imgMaxCount):
        target[i] = imread(_extraPath+"/"+str(_monId)+"_"+str(_amt)+"EA_0_name.jpg")

    # temp = imread(_extraPath+"/"+str(int(_itemNum)+0)+"_"+str(k)+".jpg")
    # targetNull = 255- temp

    # mergeh0 = cv2.hconcat([target])
    # mergeh1 = cv2.hconcat([target[5],target[6],target[7],target[8],target[9]])
    # if _equipType != 2 :
    #     mergeh2 = cv2.hconcat([target[10],target[11],target[12],target[13],targetNull])
    #     mergev = cv2.vconcat([mergeh0,mergeh1,mergeh2])
    # else :
    mergev0 = cv2.vconcat([target[0],target[1],target[2],target[3],target[4],target[5],target[6],target[7],target[8],target[9],target[10]
    ,target[11],target[12],target[13],target[14],target[15],target[16],target[17],target[18],target[19]])

    imwrite(_extraPath+"/Merge/"+str(_monId)+"_"+str(_amt)+"EA_"+str(i)+"_name.jpg", mergev0)


    target = [0 for i in range(20)]

    for i in range(0,_dropCtg):
        target[i] = imread(_extraPath+"/"+str(_monId)+"_"+str(_amt)+"EA_"+str(i)+"_amt.jpg")

    for i in range(_dropCtg,imgMaxCount):
        target[i] = imread(_extraPath+"/"+str(_monId)+"_"+str(_amt)+"EA_0_amt.jpg")

    mergev1 = cv2.vconcat([target[0],target[1],target[2],target[3],target[4],target[5],target[6],target[7],target[8],target[9],target[10]
    ,target[11],target[12],target[13],target[14],target[15],target[16],target[17],target[18],target[19]])

    imwrite(_extraPath+"/Merge/"+str(_monId)+"_"+str(_amt)+"EA_"+str(i)+"_amt.jpg", mergev1)


    mergeh = cv2.hconcat([mergev1,mergev0])

    imwrite(_extraPath+"/Merge/"+str(_monId)+"_"+str(_amt)+"EA_"+str(i)+".jpg", mergeh)

#MergeImg_Equip(33320, 2,"./screenshot/장비수치 확인"+ time.strftime("_%m%d"))
#MergeImg_Drop(19000,200,10,"./screenshot/드랍템 확인"+ time.strftime("_%m%d"))