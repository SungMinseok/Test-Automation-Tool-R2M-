import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(f'./etc/R2A_UI.ui')[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


#region 복붙시작 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#region Main UI
        self.setWindowTitle("R2A 4.0")
        self.statusLabel = QLabel(self.statusbar)

        self.setGeometry(1470,28,400,400)
        self.setFixedSize(450,1020)
        
        self.btn_teleport.clicked.connect(self.doTeleport)
        self.btn_customCmd_13.clicked.connect(multi.restartgame)
        self.btn_customCmd_14.clicked.connect(multi.go_character_selection_window)
        self.btn_customCmd_15.clicked.connect(multi.go_server_selection_window)
        self.btn_customCmd_16.clicked.connect(multi.logout)
        #단축키설정■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

        for i in range(0, 12):
            shortcut = QShortcut(Qt.Key_F1 + i, self)
            shortcut.activated.connect(getattr(self, f'btn_additem_execute_{i}').click)
        for i in range(0, 12):
            shortcut = QShortcut(Qt.Key_F1 + i, self)
            shortcut.activated.connect(getattr(self, f'btn_custom_execute_{i}').click)


        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

#endregion

#region Set Values Default━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        curDirectory = os.getcwd()
        
        #self.input_itemListFile.setText("itemlist_220207.xlsx")
        #self.getXlData()
        self.input_additemtext_name.setText("additems.txt")        
        self.input_itemBookMark_name.setText(curDirectory + "/data/items/itemBookMarkList.txt")
        self.applyItemBookMarkList()
        
        self.input_cmd_name.setText("multicommand.txt")

        self.label_appPos.setText("현재 앱 좌표(x,y,w,h) : {0}, {1}, {2}, {3}".format(ms.appX,ms.appY,ms.appW,ms.appH))
        self.input_teleportBookMark_name.setText(curDirectory + "/data/etc/teleportPos.txt")
        self.applyTeleportBookMarkList()

        #print(os.getcwd() + self.input_itemBookMark_name.text())
        self.applyTestCaseList()

        #반응형 UI ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        
        for i in range(0,12) :
            getattr(self, f'input_additem_itemid_{i}').textChanged.connect(lambda _, x=i : self.getItemNameByInput(x))
        
        self.input_itemName.textChanged.connect(self.getItemIdByInput)
        self.comboBox_itemType.currentTextChanged.connect(self.getItemIdByInput)
        
        #for i in range(0,12) :
        #    getattr(self, f'input_additem_itemName_{i}').textChanged.connect(lambda _, x=i : self.getItemIdByInput(x))
        #self.input_itemName.textChanged.connect(lambda : self.getItemNameByInput(x))
        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

        #XLSX파일 연동■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        # csvDf = pd.read_csv("./data/csv/csvList.csv",encoding='CP949')

        # itemDataFileName = ms.DF값불러오기(csvDf,"mData","item","fileName")
        # tranDataFileName = ms.DF값불러오기(csvDf,"mData","transform","fileName")
        # servDataFileName = ms.DF값불러오기(csvDf,"mData","servant","fileName")
        
        # ms.getXlFile(f"./data/아이템.xlsx")
        # ms.getCsvFile(f"./data/csv/{tranDataFileName}.csv")
        # ms.getCsvFile(f"./data/csv/{servDataFileName}.csv")
        global df_item
        global df_tran
        global df_serv
        #global df_cache
        #df_item = pd.read_excel("./data/아이템.xlsx",engine="openpyxl",usecols=[0,1,2,3])
        df_tran = pd.read_excel("./data/변신 카드.xlsx",engine="openpyxl",usecols=[0,1,2,3])
        df_serv = pd.read_excel("./data/서번트 카드.xlsx",engine="openpyxl",usecols=[0,1,2,3])
        #df_serv = pd.read_excel("./data/서번트 카드.xlsx",engine="openpyxl",usecols=[0,1,2,3])
                        

        today = time.strftime('%y%m%d')
        itemFileName = f"./data/아이템_{today}.csv"

        try:
            df_item = pd.read_csv(itemFileName)
        except FileNotFoundError:
            df_item = pd.read_excel("./data/아이템.xlsx", engine="openpyxl", usecols=[0, 1, 2, 3])
            df_item.to_csv(itemFileName, index=False)
        
            # 이전 날짜의 아이템 파일 삭제
            for file in os.listdir("./data"):
                if file.endswith(".csv"):
                    file_date = re.findall(r'\d{6}', file)[0]
                    if file_date < today:
                        os.remove(os.path.join("./data", file))




        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        
        # Cache파일 로드 (Load Cache)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        ms.getCsvFile(f"./data/csv/cache.csv")
        #ms.df_cache =ms.df_cache.fillna(0)
        
        for i in range(0,12) :
            try :
                itemID = int(ms.DF값불러오기(ms.df_cache,"key",f'itemCache{i}',"value0"))
                itemAmount = int(ms.DF값불러오기(ms.df_cache,"key",f'itemCache{i}',"value1"))
                getattr(self, f'input_additem_itemid_{i}').setText(str(itemID))
                getattr(self, f'input_additem_amount_{i}').setText(str(itemAmount))
            except :
                print("noVal in item Cache")
                pass
            try :
                getattr(self, f'input_custom_cmd_{i}').setText(str(ms.DF값불러오기(ms.df_cache,"key",f'cmdCache{i}',"value0")))
            except :
                print("noVal in cmd Cache")
                pass

        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
  
       
        #창 불러오기■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        
        self.comboBox_appNameList.clear()
        for i in pag.getAllTitles():
            if i == "": #or self.input_appNameList_inclusiveStr.text() in i:
                continue
            #mapName = lines[i].split(',')
            self.comboBox_appNameList.addItem(i)



        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#




        self.applyHistory("item")






#endregion
    
#region Tabs Interactive UI
        self.comboBox_appNameList.currentTextChanged.connect(self.setCurrentAppPos)
        self.btn_appNameList_optimize.clicked.connect(self.optimizeCurrentAppPos)
        self.btn_appNameList_apply.clicked.connect(self.applyNewAppNameList)
        #  Tab [Settings]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        self.btn_screenShot_setPos0.clicked.connect(lambda : self.getMousePos(2))
        self.btn_screenShot_setPos1.clicked.connect(lambda : self.getMousePos(3))
        self.btn_screenShot_openFile.clicked.connect(lambda : self.openFile(self.input_screenShot_fileName.text()))
        self.btn_screenShot_capture.clicked.connect(self.takePicture)
        #self.btn_img2str_0.clicked.connect(lambda : self.getImg2Str(1))
        #self.btn_img2str_1.clicked.connect(lambda : self.getImg2Str(2))
        
        
        
        
        #self.btn_setpos0.clicked.connect(lambda : self.getMousePos(0))
        #self.btn_setpos1.clicked.connect(lambda : self.getMousePos(1))
        #self.btn_setappsize.clicked.connect(self.setNewAppSize)
        #self.btn_setappsizewizard.clicked.connect(lambda : self.openFile("setAppSizeIndex.py"))

    
    
        self.btn_temp_0.clicked.connect(self.testTemp)
        
        #221013
        self.btn_img2str_2.clicked.connect(lambda : self.translateImg(0))
    
        #self.btn_img2str_execute_1.clicked.connect(lambda : self.translateImg(0))

        self.btn_img2str_execute_4.clicked.connect(lambda : i2s.getStringFromImg2)

        for i in range(1,5) :
            #slotNum = i
            getattr(self, f'btn_img2str_execute_{i}').clicked.connect(lambda _, x=i : self.getImg2Str(x))

    #Tab [Hot]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self.comboBox_teleport.currentTextChanged.connect(self.changeTeleportBookMark)
        
        self.btn_teleportBookMark_openFile.clicked.connect(lambda : self.openFile(self.input_teleportBookMark_name.text()))
        self.btn_teleportBookMark_setFile.clicked.connect(lambda : self.setFilePath(self.input_teleportBookMark_name))
        self.btn_teleportBookMark_apply.clicked.connect(self.applyTeleportBookMarkList)
    
        #self.btn_screenshot_setdir.clicked.connect(self.setFilePath)
        #self.btn_record_setdir.clicked.connect(self.setFilePath)

        self.btn_subbtn_0.clicked.connect(lambda : self.executeCommand("cleanupinventory"))
    
    #Tab [Item]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        #self.btn_cleanupmaterial.clicked.connect(lambda : self.executeCommand("cleanupmaterial"))

        for i in range(0,12) :
            getattr(self, f'btn_additem_execute_{i}').clicked.connect(lambda _, x=i : self.additem(x))
            #getattr(self, f'input_additem_itemid_{i}').textChanged.connect(lambda _, x=i : self.getItemNameByInput(x))
        
        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

        #self.btn_itemlist_openFile.clicked.connect(lambda : self.openFile(self.input_itemListFile.text()))
        #self.btn_itemlist_setFname.clicked.connect(lambda : self.setFilePath(self.input_itemListFile))
        #self.btn_itemlist_set.clicked.connect(self.getXlData)

        self.btn_searchItemName_all.clicked.connect(self.searchItemAll)
        self.btn_searchItemName.clicked.connect(lambda : self.copyText("item"))
        self.comboBox_itemhistory.currentTextChanged.connect(lambda : self.applyHistoryID("item"))
        #self.btn_itemlist_set.clicked.connect(lambda : self.popUp("성공","아이템 리스트 연동 성공!"))

        self.btn_goods.clicked.connect(self.additemGoods)
        #self.btn_additem.clicked.connect(self.additem)
        self.btn_additemall.clicked.connect(self.additemAll)
        self.btn_additemtext_setDir.clicked.connect(lambda : self.setFilePath(self.input_additemtext_name))
        self.btn_additemtext.clicked.connect(self.additemText)
        self.btn_additemtext_openFile.clicked.connect(lambda : self.openFile(self.input_additemtext_name.text()))
        
        
        
        self.btn_itemBookMark_openFile.clicked.connect(lambda : self.openFile(self.input_itemBookMark_name.text()))
        self.btn_itemBookMark_setFile.clicked.connect(lambda : self.setFilePath(self.input_itemBookMark_name))
        self.btn_itemBookMark_apply.clicked.connect(self.applyItemBookMarkList)
    
    
    
    
    #Tab [Custom]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
        for i in range(0,12) :
            getattr(self, f'btn_custom_execute_{i}').clicked.connect(lambda _, x=i : self.customCommand(x))

    
    
    
    #Tab [Command]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self.btn_cmd_openFile.clicked.connect(lambda : self.openFile(self.input_cmd_name.text()))
        self.btn_cmd_setFile.clicked.connect(lambda : self.setFilePath(self.input_cmd_name))
        self.btn_cmd_apply.clicked.connect(self.applyCmdTextFile)
        self.btn_cmd_execute.clicked.connect(self.executeMultiCommand)
        #self.btn_cmdBookMark_execute_0.clicked.connect(lambda : self.executeCommand(self.input_cmdBookMark_0.text()))
        #self.btn_cmdBookMark_execute_1.clicked.connect(lambda : self.executeCommand(self.input_cmdBookMark_1.text()))
        
        self.btn_testCase_openFile.clicked.connect(lambda : self.openFile(".\data/etc/testCaseList.txt"))
        self.btn_testCase_apply.clicked.connect(self.applyTestCaseList)
        self.comboBox_testCase.currentTextChanged.connect(self.applyCurrentTestCase)
        self.btn_testCase_execute.clicked.connect(self.executeTestCase)
    #Tab [Character]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self.btn_setClass.clicked.connect(self.setClass)
        self.comboBox_setClass.currentTextChanged.connect(self.applySkillGroupList)
        self.comboBox_skillGroup.currentTextChanged.connect(self.changeSkillGroup)
        self.btn_skillGroup_execute.clicked.connect(lambda : self.executeCommand(\
            "changeskillenchant "+\
            self.input_skillGroup_id.text()+" "+\
            self.input_skillGroup_level.text()+" "\
            ))
        self.btn_customCmd_0.clicked.connect(lambda : self.executeCommandByID(0))
        self.btn_customCmd_1.clicked.connect(lambda : self.executeCommandByID(1))
        self.btn_customCmd_2.clicked.connect(lambda : self.executeCommandByID(2))
        self.btn_customCmd_3.clicked.connect(lambda : self.executeCommandByID(3))
        self.btn_customCmd_4.clicked.connect(lambda : self.executeCommandByID(4))
        self.btn_lv.clicked.connect(lambda : self.executeCommandByID(5))
        self.btn_hp.clicked.connect(lambda : self.executeCommandByID(6))
        self.btn_mp.clicked.connect(lambda : self.executeCommandByID(7))
        
#endregion

    #[App Window]▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    def getCurrentAppSize():
        print()

    def alignCurrentAppPos():
        print()

    def optimizeCurrentAppPos(self):
        print("optimizeCurrentAppPos")
        currentAppName = self.comboBox_appNameList.currentText()
        a = pag.getWindowsWithTitle(currentAppName)[0]
        a.moveTo(0,0)
        a.resizeTo(1469,838)
        self.setCurrentAppPos()

    def setCurrentAppPos(self):
        currentAppName = self.comboBox_appNameList.currentText()
        a = pag.getWindowsWithTitle(currentAppName)[0]
        
        x,y,w,h = sas.applyNewAppSize(a.left,a.top,a.right,a.bottom)
        self.label_appPos.setText("현재 앱 좌표(x,y,w,h) : {0}, {1}, {2}, {3}".format(x,y,w,h))

    def applyNewAppNameList(self):
        self.comboBox_appNameList.clear()
        a = self.input_appNameList_inclusiveStr.text()
        for i in pag.getAllTitles():
            if a not in i: 
                continue
            self.comboBox_appNameList.addItem(i)
    #▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨



    def executeCommand(self, cmd):
        ms.Command(cmd)

    def doTeleport(self):
        arguments = [self.input_teleport_mapNum.text(),
        self.input_teleport_xPos.text(),
        self.input_teleport_yPos.text()]
        ms.executeCommand("doteleport",arguments)
        
        #ms.CMD_DoTeleport(self.comboBox_teleport.currentText())

    # def setTeleportPoint(self,item):
    #     if item == "바이런성" :
    #         ms.setTeleportNum = 3
    #     elif item == "푸리에성" :
    #         ms.setTeleportNum = 4   
    #     elif item == "로덴성" :
    #         ms.setTeleportNum = 5   
    #     elif item == "블랙랜드성" :
    #         ms.setTeleportNum = 6   
    #     elif item == "그렘린숲" :
    #         ms.setTeleportNum = 7   

    def executeCommand(self,cmd) :
        ms.Command(cmd)

    def executeCommandByID(self,cmdID) :
        cmd = ""
        if cmdID == 0 :
            cmd = "invincible on"
        elif cmdID == 1 :
            cmd = "invincible off"
        elif cmdID == 2 :
            cmd = "autocompletetransformcardcollection"
        elif cmdID == 3 :
            cmd = "autocompleteitemcollection"
        elif cmdID == 4 :
            cmd = "autocompleteservantcardcollection"
        elif cmdID == 5 :
            cmd = "lv " + self.input_lv.text()
        elif cmdID == 6 :
            cmd = "hp " + self.input_hp.text()
        elif cmdID == 7 :
            cmd = "mp " + self.input_mp.text()

        ms.Command(cmd)









#[Functions : ITEM]▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨

    def searchItem(self):
        itemType = self.comboBox_itemType.currentText()  
        if self.comboBox_itemType.currentText() == "일반" :
            itemType = ""

        result = ms.searchItemByName(itemType , self.input_itemName.text())
        #self.popUp("결과","ItemID : " + str(result) + "\n('OK'를 눌러 바로 생성)","searchItem")
        self.popUp("결과",str(result),"searchItem")

    def searchItemAll(self):
        targetName = self.input_itemName_all.text()  

        result = ms.findAllValInDataFrame(df_item,"mName",targetName,"mID")
        self.popUp("결과",str(result))

    def additemGoods(self) :
        multi.autoAddItem(ms.searchItemByName("", self.comboBox_goods.currentText()),self.input_goods_count.text())

    #def additem(self) :
    #    multi.autoAddItem(self.input_additem_id.text(),self.input_additem_count.text())

    def additem(self, slotNum) :
        
        itemID = getattr(self, f'input_additem_itemid_{slotNum}').text()
        itemAmount = getattr(self, f'input_additem_amount_{slotNum}').text()
        
        print(itemID, itemAmount)
        multi.autoAddItem(itemID, itemAmount)

    def additemAll(self) :
        multi.autoAddItemAll(self.input_additemall_id.text())

    def additemText(self):
        try : 
            multi.autoAddItemText(self.input_additemtext_name.text())
        except FileNotFoundError as errorMsg:
            self.popUp("에러",str(errorMsg))

    

    def applyItemBookMarkList(self) :
     
        with open("./data/items/itemBookMarkList.txt",encoding='UTF-8') as f:
            #lines = f.readlines()
            lines = f.read().splitlines()
        f.close()
        self.comboBox_goods.clear()
        for line in lines:
            self.comboBox_goods.addItem(line)

            
    def applyTeleportBookMarkList(self) :
     
        with open("./data/etc/teleportPos.txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        self.comboBox_teleport.clear()
        for i in range(0,len(lines)):
            mapName = lines[i].split(',')
            self.comboBox_teleport.addItem(mapName[0])
        
    def changeTeleportBookMark(self):
        
        with open("./data/etc/teleportPos.txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()
        
        for i in range(0,len(lines)):
            mapName, mapNum, xPos, yPos= lines[i].split(',')
            #print(mapName)
            if self.comboBox_teleport.currentText() == mapName :
                self.input_teleport_mapNum.setText(mapNum)
                self.input_teleport_xPos.setText(xPos)
                self.input_teleport_yPos.setText(yPos)
                return
            

        #     #ms.Command("d "+groupID +" "+maxEnchantLevel)
        # for line in lines:
        #     self.comboBox_goods.addItem(line)

    def openFile(self,filePath):
        # if filePath[0] != "/":
        #     filePath = "/"+ filePath
        # os.startfile(os.getcwd() + "/"+ filePath)
        try:
            os.startfile(filePath)
        except : 
            print("파일 없음 : "+filePath)    
            
    def openFileWithNoException(self,filePath):
        os.startfile(filePath)

    def getItemNameByInput(self,slotNum):
        itemID = getattr(self, f'input_additem_itemid_{slotNum}').text()
        #print(itemID)
        try :
            itemName = ms.DF값불러오기(df_item,"mID",itemID,"mName")
        #print(itemName)
            getattr(self, f'input_additem_itemName_{slotNum}').setText(itemName)
        except :
            print(f"no item ID : {itemID}")
            getattr(self, f'input_additem_itemName_{slotNum}').setText("no name")

    def getItemIdByInput(self):
        subString = self.comboBox_itemType.currentText()
        if subString != "일반" :
            itemName = f'{subString} {self.input_itemName.text()}'
        else :
            itemName = f'{self.input_itemName.text()}'

        try :
            itemID = ms.DF값불러오기(df_item,"mName",itemName,"mID")
            self.input_itemid.setText(str(itemID))
        except :
            self.input_itemid.setText("no id")

        # itemName = getattr(self, f'input_additem_itemName_{slotNum}').text()
        # try :
        #     itemID = ms.DF값불러오기(df_item,"mName",itemName,"mID")
        #     getattr(self, f'input_additem_itemid_{slotNum}').setText(itemName)
        # except :
        #     getattr(self, f'input_additem_itemid_{slotNum}').setText("Item ID")

    #230118
    def copyText(self, target:str):

        if target == "item":
            if self.input_itemName.text() != "" :
                itemName = ""
                subString = self.comboBox_itemType.currentText()
                if subString != "일반" :
                    itemName = f'{subString} {self.input_itemName.text()}'
                else :
                    itemName = f'{self.input_itemName.text()}'
                
                ms.createHistoryCache("item",itemName)
                self.applyHistory("item")
                cb.copy(self.input_itemid.text())

    #230118
    def applyHistory(self, target:str) :
        fileName = ""
        #try:
        if target == "item":
            fileName="./data/etc/itemHistory.txt"
            if os.path.exists(fileName) :
                with open(fileName,'r',encoding='UTF-8') as f:
                    lines = f.read().splitlines()
                f.close()

                self.comboBox_itemhistory.clear()

                for line in reversed(lines):
                    #x = lines[i].split(',')
                    #self.comboBox_itemhistory.addItem(x[0])
                    self.comboBox_itemhistory.addItem(line)

    #230119
    def applyHistoryID(self,target:str):#target = item/tran/serv
        if target == "item":
            try: 
                itemName = self.comboBox_itemhistory.currentText()
                itemID = ms.DF값불러오기(df_item,"mName",itemName,"mID")
                self.input_itemName_2.setText(str(itemID))
            except:
                print(f"no {target} name")
#▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨


#Tab [Custom]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    def customCommand(self, slotNum) :
        cmd = getattr(self, f'input_custom_cmd_{slotNum}').text()
        count = getattr(self, f'input_custom_count_{slotNum}').text()
        
        #print(itemID, itemAmount)
        #multi.Command_Text(itemID, itemAmount)
        ms.Command(cmd)




    #Tab [Character]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    
    def setClass(self) :
        classNum = 0
        checkBoxValues = [self.checkBox_setCharacter_1.isChecked()
        ,self.checkBox_setCharacter_2.isChecked()
        ,self.checkBox_setCharacter_3.isChecked()
        ,self.checkBox_setCharacter_4.isChecked()
        ,self.checkBox_setCharacter_5.isChecked()
        ,self.checkBox_setCharacter_6.isChecked()
        ,self.checkBox_setCharacter_7.isChecked()
        ,self.checkBox_setCharacter_8.isChecked()
        ,self.checkBox_setCharacter_9.isChecked()
        ]
        if self.comboBox_setClass.currentText() == "나이트":
            classNum = 1
        elif self.comboBox_setClass.currentText() == "아처":
            classNum = 2
        elif self.comboBox_setClass.currentText() == "위저드":
            classNum = 3
        elif self.comboBox_setClass.currentText() == "어쌔신":
            classNum = 4
        sc.setClass_auto(classNum,checkBoxValues)

    def applySkillGroupList(self) :
        if self.comboBox_setClass.currentText() == "나이트":
            className = "Knight"
        elif self.comboBox_setClass.currentText() == "아처":
            className = "Archer"
        elif self.comboBox_setClass.currentText() == "위저드":
            className = "Wizard"
        elif self.comboBox_setClass.currentText() == "어쌔신":
            className = "Assassin"

        fileName = "./data/character/setMaster"+className+".txt"
     
        with open(fileName,encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        self.comboBox_skillGroup.clear()
        for i in range(0,len(lines)):
            line = lines[i].split(',')
            self.comboBox_skillGroup.addItem(line[2])

    def changeSkillGroup(self):
        
        if self.comboBox_setClass.currentText() == "나이트":
            className = "Knight"
        elif self.comboBox_setClass.currentText() == "아처":
            className = "Archer"
        elif self.comboBox_setClass.currentText() == "위저드":
            className = "Wizard"
        elif self.comboBox_setClass.currentText() == "어쌔신":
            className = "Assassin"

        fileName = "./data/character/setMaster"+className+".txt"
     
        with open(fileName,encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()
        
        for i in range(0,len(lines)):
            skillGroupID, maxEnchantValue, skillName = lines[i].split(',')
            #print(mapName)
            if self.comboBox_skillGroup.currentText() == skillName :
                self.input_skillGroup_id.setText(skillGroupID)
                self.input_skillGroup_level.setText(maxEnchantValue)
                return




    #Tab [Command]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

            
    def applyCmdTextFile(self) :
        try:
            with open(self.input_cmd_name.text(),encoding='UTF-8') as f:
                lines = f.read()#.splitlines()
            f.close()
        except :
            self.popUp("실패","경로 오류!\n")
        self.plainTextEdit_cmd.insertPlainText(lines)

    def executeMultiCommand(self) :
        headerText = self.input_cmd_header.text()
        commandText = self.plainTextEdit_cmd.toPlainText()
        if commandText == "" :
            return
        repeatCount = self.input_cmd_repeatCount.text()
        repeatDelay = self.input_cmd_repeatDelay.text()

        if repeatCount == "":
            repeatCount = 1
        else :
            repeatCount = int(repeatCount)
        if repeatDelay == "":
            repeatDelay = 0
        else :
            repeatDelay = int(repeatDelay)

        lines = commandText.splitlines()
        startTime = ms.GetElapsedTimeAuto(0)
        endTime = ms.GetElapsedTimeAuto((len(lines)*2+repeatDelay)*repeatCount)

        self.label_cmd_startTime.setText("시작 시각 : {0}".format(startTime.strftime('%m-%d %H:%M:%S')))
        self.label_cmd_endTime.setText("예상 종료 시각 : {0}".format(endTime.strftime('%m-%d %H:%M:%S')))

        # self.timer = QtCore.QTimer(MainWindow)
        # self.timer.start(1000)
        # self.timer.timeout.connect(self.showTimer)
        # global isTesting
        # isTesting = 1

        for i in range(0,repeatCount) :
            #print(i)
            #self.label_cmd_curRepeatCount.setText("실행횟수 : {0}/{1}".format(str(i+1),str(repeatCount)))
            self.label_cmd_curRepeatCount.setText("총 {1}번 중 {0}번 째 실행 중...".format(str(i+1),str(repeatCount)))
            self.progressBar_cmd.setValue(int(i/repeatCount*100))
            QtWidgets.QApplication.processEvents()
            #self.label_cmd_curRepeatCount.repaint()
        #print(i+1 ,"번 째 실행", end='\r')
            for line in lines:
                if not headerText == "" :
                    line = headerText + " " + line
                ms.Command(line)
            
            if i < (repeatCount - 1) :
                ms.sleep(repeatDelay)

        consumedTime = ms.GetConsumedTime(startTime)
        #isTesting = 0

        self.progressBar_cmd.setValue(100)
        self.label_cmd_curRepeatCount.setText("-")
        self.label_cmd_startTime.setText("시작 시각 : -")
        self.label_cmd_endTime.setText("예상 종료 시각 : -")

        #self.timer.stop()
        if self.checkBox_setApp_0.isChecked() :
            self.showTestReport(
            "multiCmd"
            ,commandText
            ,repeatCount
            ,startTime.strftime('%m-%d %H:%M:%S')
            ,ms.GetCurrentTime().strftime('%m-%d %H:%M:%S')
            ,consumedTime#.strftime('%H:%M:%S')
            )

    def applyTestCaseList(self) :
     
        with open("./data/etc/testCaseList.txt",encoding='UTF-8') as f:
            #lines = f.readlines()
            lines = f.read().splitlines()
        f.close()
        self.comboBox_testCase.clear()
        # for line in lines:
        #     self.comboBox_testCase.addItem(line)
        for i in range(0,len(lines)):
            line = lines[i].split(',')
            self.comboBox_testCase.addItem(line[0])
            #self.input_testCase_moduleName.setText(line[1])
            #self.input_testCase_funcName.setText(line[2])
    def applyCurrentTestCase(self):
        with open("./data/etc/testCaseList.txt",encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()
        for i in range(0,len(lines)):
            line = lines[i].split(',')
            if line[0] == self.comboBox_testCase.currentText() :
            #self.comboBox_testCase.addItem(line[0])
                self.input_testCase_moduleName.setText(line[1])
                #self.input_testCase_funcName.setText(line[2])
                break

    def executeTestCase(self):
        try :
            self.openFileWithNoException(self.input_testCase_moduleName.text()+".exe")
            #tempFunc = getattr(importlib.import_module(self.input_testCase_moduleName.text()), self.input_testCase_funcName.text())
            #tempFunc()
            #getattr(self.input_testCase_moduleName.text(),self.input_testCase_funcName.text())
        except FileNotFoundError :
            self.openFileWithNoException(self.input_testCase_moduleName.text()+".py")

        except :
            self.popUp("오류","테스트 케이스 실행 불가")
#region Tab [Settings]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    def getMousePos(self,item):
        x,y = ms.GetMousePos()
        print(x,y)
        if item == 0:
            self.text_x0.setText(str(x))
            self.text_y0.setText(str(y))
        elif item == 1:
            self.text_x1.setText(str(x))
            self.text_y1.setText(str(y))
        elif item == 2:#스크린샷 좌측상단
            self.input_screenShot_x0.setText(str(x))
            self.input_screenShot_y0.setText(str(y))
            ratioX, ratioY = sas.getRatio(x, y)
            self.input_screenShot_x0_ratio.setText(str(ratioX))
            self.input_screenShot_y0_ratio.setText(str(ratioY))
            self.input_screenShot_x.setText(str(ratioX))
            self.input_screenShot_y.setText(str(ratioY))
           # print(float(self.input_screenShot_x1.text)-int(self.input_screenShot_x0.text))
            self.input_screenShot_w.setText(str(round(float(self.input_screenShot_x1_ratio.text())-float(self.input_screenShot_x0_ratio.text()),4)))
            self.input_screenShot_h.setText(str(round(float(self.input_screenShot_y1_ratio.text())-float(self.input_screenShot_y0_ratio.text()),4)))
            #self.input_screenShot_h.setText(str(y))
        elif item == 3:#스크린샷 우측하단
            self.input_screenShot_x1.setText(str(x))
            self.input_screenShot_y1.setText(str(y))
            ratioX, ratioY = sas.getRatio(x, y)
            self.input_screenShot_x1_ratio.setText(str(ratioX))
            self.input_screenShot_y1_ratio.setText(str(ratioY))
            self.input_screenShot_w.setText(str(round(float(self.input_screenShot_x1_ratio.text())-float(self.input_screenShot_x0_ratio.text()),4)))
            self.input_screenShot_h.setText(str(round(float(self.input_screenShot_y1_ratio.text())-float(self.input_screenShot_y0_ratio.text()),4)))

    def takePicture(self):
        if self.input_screenShot_x.text() != "0" :


            self.input_screenShot_fileName.setText(ms.captureSomeBox3(
            float(self.input_screenShot_x.text()),
            float(self.input_screenShot_y.text()),
            float(self.input_screenShot_w.text()),
            float(self.input_screenShot_h.text())
            ))
        #self.btn_setappsizewizard.clicked.connect(self.fileOpen)
    
    def getImg2Str(self,btnNum):
        fileName = self.input_screenShot_fileName.text()
        funcName = getattr(self, f'input_img2str_funcName_{btnNum}').text()
        langCode = getattr(self, f'input_img2str_langCode_{btnNum}').text()
        print(f'getImg2Str : {funcName}|{langCode}')
        try : 
            if langCode == "" :
                self.popUp("텍스트인식",getattr(i2s,funcName)(fileName))
            else :
                self.popUp("텍스트인식",getattr(i2s,funcName)(fileName,langCode))      

        except : 
            print("something wrong")

    def translateImg(self,btnNum):
        if self.input_screenShot_fileName.text() != "0" :
            if btnNum == 0 : #대만>한국
                targetStr = i2s.getStringFromImg(self.input_screenShot_fileName.text(),'chi_tra')
                #self.popUp("번역",targetStr)
                
                self.popUp("번역",tl.translateTW2KR(targetStr))
            #elif btnNum == 1 :
            #    self.popUp("텍스트인식",i2s.getStringFromImg(self.input_screenShot_fileName.text()))
            
    # def img2str(self,btnNum):
    #     if btnNum == 0 :
    #         targetStr = 


        
#endregion
    
    #Functions━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    def setFilePath(self,target):
        path = QtWidgets.QFileDialog.getOpenFileName(MainWindow)
        if path != "" :
            target.setText(path[0])

    def setDirectoryPath(self, target):
        path = QtWidgets.QFileDialog.getExistingDirectory(MainWindow)
        if path != "" :
            target.setText(path[0])

    # def getXlData(self):
    #     path = self.input_itemListFile.text()
    #     #if path != "" :
    #     try :
    #         ms.getXlFile(path)
    #         self.popUp("성공","아이템 리스트 연동 성공!\n")
    #     except :
    #         self.popUp("실패","경로 오류!\n")

    def popUp(self,titleText,desText,type = "about"):
        #if type == "about" :
        msg = QtWidgets.QMessageBox()  
        msg.setGeometry(1520,28,400,2000)

        #msg.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        msg.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        if type == "report" :
            msg.setFixedSize(500,500)

            
        if type == "searchItem" :
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            #msg.buttonClicked.connect(self.messageBoxButton,desText)
        #msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle(titleText)

        if type == "searchItem" :
            msg.setText("ItemID : " + str(desText) + "\n('OK'를 눌러 바로 생성)")      
        else:
            msg.setText(desText)

        x = msg.exec_()
        
        if type == "searchItem" :
            if x == QtWidgets.QMessageBox.Ok and desText.isnumeric():
                multi.autoAddItem(desText,"1")
      
        #elif type == "question" :
    # def messageBoxButton(self, i, desText):
    #     if i.text() == 'OK' :
    #         multi.autoAddItem(desText,"1")

    def showTestReport(self, testName, testDes, testCount, startTime, endTime, consumedTime):
        result = "테스트 유형 : {0}\
        \n테스트 횟수 : {2}회\
        \n시작 시각 : {3}\
        \n종료 시각 : {4}\
        \n총 소요 시간 : {5}\
        \n\n테스트 내용 :\n{1}\
        ".format(testName,testDes,testCount,startTime,endTime,consumedTime)
        
        self.popUp("테스트 결과",result,"report")

    def testTemp(self):
#아이템 이름 포함된 것 모두 찾기
        result = ms.findAllValInDataFrame(df_item,"mName","포션","mID")
        self.popUp("검색",str(result),"about")





    # def showTimer(self):
        
    #     #print("222")
    #     #curtime = 1
    #     #print(self.label_cmdTimer.text()[0])
    #     if isTesting == 1:
    #         curTime = int(self.label_cmdTimer.text()[0])
    #         curTime = curTime + 1
    #         self.label_cmdTimer.setText("{0}초".format(curTime))
    def closeEvent(self):
        print("end")

        # Cache파일 저장(Save Cache)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        #ms.getCsvFile(f"./data/csv/cacheList.csv")
        
        for i in range(0,12) :
            tempVal = getattr(self, f'input_additem_itemid_{i}').text()
            ms.saveCacheData(tempVal,'key',f'itemCache{i}',"value0")
        #for i in range(0,12) :
            tempVal = getattr(self, f'input_additem_amount_{i}').text()
            ms.saveCacheData(tempVal,'key',f'itemCache{i}',"value1")

        for i in range(0,12) :
            tempVal = getattr(self, f'input_custom_cmd_{i}').text()
            ms.saveCacheData(tempVal,'key',f'cmdCache{i}',"value0")

        ms.df_cache.to_csv(f"./data/csv/cache.csv",sep=',',na_rep='NaN',index=False)
        print(ms.df_cache)

        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#



        # quit_msg = "?"
        # reply = QtWidgets.QMessageBox.question(self,'Message',quit_msg, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        # if reply == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

    def closeEvent(self,event):
        super().closeEvent(event)
import msdata as ms
import multicommand as multi
import setclass as sc
import setappsize as sas
import img2str as i2s
import os
import translate as tl
#import engraveCheck
import importlib
import pandas as pd
import pyautogui as pag
#import clipboard as cb
import time
import re


#endregion
# if __name__ == "__main__":
#     import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = MyWindow()#QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()