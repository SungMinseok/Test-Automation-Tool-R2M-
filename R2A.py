ITEM_SLOT_COUNT = 21
CUSTOM_CMD_SLOT_COUNT = 27
ITEM_CHECK_BOX_COUNT = 26
DATA_SLOT_COUNT = 12 
app_type = 0
#currentAppName = ""

'''
기본 세팅(폴더생성)
'''
import os
path_resource = "./resource"
if not os.path.isdir(path_resource):                                                           
    os.mkdir(path_resource)
    
log_folder = "./log"
if not os.path.isdir(log_folder):                                                           
    os.mkdir(log_folder)


from enum import Enum
import random

class 직업(Enum):
    나이트 = 0
    아처 = 1
    위저드 = 2
    어쌔신 = 3
    버서커 = 4


import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QKeySequence,QPixmap, QColor
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout
from msdata import 플레이어변경, Player
#import asyncio
from PyQt5.QtCore import QTimer

# Connect the QAction button to the open_patch_notes function

class ImageTooltip(QWidget):
    def __init__(self, pixmap):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)
        self.setLayout(layout)

cache_path = f'./cache/cache.csv'
history_item_path = f'./data/etc/itemHistory.txt'
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(f'./etc/R2A_UI.ui')[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.set_button_styles(2)
        # QTimer를 사용하여 5분마다 export_cache 함수 실행
        self.auto_cache_save_timer = QTimer(self)#check_autoCacheSave
        self.auto_cache_save_timer.timeout.connect(self.export_cache)
        self.auto_cache_save_timer.start(300000)  # 300000 밀리초 = 5분
#region 복붙시작 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#region Main UI
        file_dict = ms.get_recent_file_list(os.getcwd())
        last_modified_date = list(file_dict.values())[0]

        self.setWindowTitle(f"R2A 5.0 | {last_modified_date}")
        self.statusLabel = QLabel(self.statusbar)

        self.setGeometry(1470,28,400,400)
        self.setFixedSize(450,1020)
        
        self.btn_teleport.clicked.connect(self.doTeleport)
        self.btn_customCmd_13.clicked.connect(multi.캐릭터재접속)
        self.btn_customCmd_14.clicked.connect(multi.캐릭터선택창)
        self.btn_customCmd_15.clicked.connect(multi.서버선택창)
        self.btn_customCmd_16.clicked.connect(multi.서드파티창)

        '''메뉴탭■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'''
        self.menu_patchnote.triggered.connect(lambda : self.파일열기("패치노트_R2A.txt"))

        # for i in range(0, 20):
        #     shortcut = QShortcut(Qt.Key_F1 + i, self)
        #     shortcut.activated.connect(getattr(self, f'btn_additem_execute_{i}').click)
        # for i in range(0, 12):
        #     shortcut = QShortcut(Qt.Key_F1 + i, self)
        #     shortcut.activated.connect(getattr(self, f'btn_custom_execute_{i}').click)
        '''단축키■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'''

        # for i in range(0, 12):
        #     button_name = f'btn_additem_execute_{i}'
        #     if hasattr(self, button_name):
        #         shortcut = QShortcut(QKeySequence(Qt.Key_F1 + i), self)
        #         button = getattr(self, button_name)
        #         shortcut.activated.connect(lambda : self.button.click)

        for i in range(0, ITEM_SLOT_COUNT):
            button_name = f'btn_additem_execute_{i}'
            if hasattr(self, button_name):
                #shortcut = QShortcut(QKeySequence(Qt.Key_F1 + i), self)
                button = getattr(self, button_name)
                if i <= 11 :
                    button.setText(f"생성 F{i+1}")
                else : 
                    button.setText(f"생성")

                #shortcut.activated.connect(button.click)

        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

#endregion

#region Set Values Default━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        curDirectory = os.getcwd()
        
        #self.input_itemListFile.setText("itemlist_220207.xlsx")
        #self.getXlData()
        #self.input_additemtext_name.setText("additems.txt")        
        #self.input_itemBookMark_name.setText(curDirectory + "/data/items/itemBookMarkList.txt")
        #self.applyItemBookMarkList()
        
        self.input_cmd_name.setText("multicommand.txt")

        self.input_teleportBookMark_name.setText(curDirectory + "/data/etc/teleportPos.txt")
        self.applyTeleportBookMarkList()

        #print(os.getcwd() + self.input_itemBookMark_name.text())
        self.applyTestCaseList()


        for i in range(0,CUSTOM_CMD_SLOT_COUNT) :
            getattr(self, f'label_custom_count_{i}').setText('0')

        #반응형 UI ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

        for i in range(0,ITEM_SLOT_COUNT) :
            getattr(self, f'input_additem_itemid_{i}').textChanged.connect(lambda _, x=i : self.getItemNameByInput(x))
            getattr(self, f'input_additem_itemid_{i}').textChanged.connect(lambda _, x=i : self.이미지로드(x))
            #getattr(self, f'item_img_{i}').mouseMoveEvent = self.onMouseMoveEvent(i)#(lambda _, x=i : self.onMouseMoveEvent(x))
           # getattr(self, f'item_img_{i}').mousePressEvent = self.onMouseMoveEvent(i)#(lambda _, x=i : self.onMouseMoveEvent(x))
            #getattr(self, f'item_img_{i}').mouseReleaseEvent = self.onMouseReleaseEvent(i)#(lambda _, x=i : self.onMouseReleaseEvent(x))


        # for i in range(0, 20):
        #     label = getattr(self, f'item_img_{i}')
        #     label.enterEvent = lambda event, slot=i: self.onMouseEnterEvent(slot)
        #     label.leaveEvent = lambda event, slot=i: self.onMouseLeaveEvent(slot)
        # # QVBoxLayout 레이아웃 생성 및 QLabel 추가
        # layout = QVBoxLayout()
        # for i in range(0,20) :
        #     layout.addWidget(getattr(self, f'item_img_{i}'))
        # self.setLayout(layout)


        self.input_itemName.textChanged.connect(self.getItemIdByInput)
        self.comboBox_itemType.currentTextChanged.connect(self.getItemIdByInput)
        
        #for i in range(0,12) :
        #    getattr(self, f'input_additem_itemName_{i}').textChanged.connect(lambda _, x=i : self.getItemIdByInput(x))
        #self.input_itemName.textChanged.connect(lambda : self.getItemNameByInput(x))
        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

        #XLSX파일 연동■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        #print('아이템 파일 로드 중')

        global df_item
        global df_tran
        global df_serv
        global df_resource_item
        df_tran = pd.read_excel("./data/변신 카드.xlsx",engine="openpyxl",usecols=[0,1,2,3])
        df_serv = pd.read_excel("./data/서번트 카드.xlsx",engine="openpyxl",usecols=[0,1,2,3])
        try:
            df_resource_item = pd.read_excel("./data/resource/아이템 리소스.xlsx",engine="openpyxl")
        except :
            pass
        #df_resource_item = df_resource_item.set_index("mID") 

        today = time.strftime('%y%m%d')
        itemFileName = f"./data/아이템_{today}.csv"

        try:
            df_item = pd.read_csv(itemFileName)
            print('아이템 파일 로드 성공...')
        except FileNotFoundError:
            print('아이템 파일 캐시 생성 중...')
            df_item = pd.read_excel("./data/아이템.xlsx", engine="openpyxl", usecols=[0, 1, 2, 3,23])
            df_item.to_csv(itemFileName, index=False)
        
            # 이전 날짜의 아이템 파일 삭제
            for file in os.listdir("./data"):
                if file.endswith(".csv"):
                    file_date = re.findall(r'\d{6}', file)[0]
                    if file_date < today:
                        os.remove(os.path.join("./data", file))




        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        
        # Cache파일 로드 (Load Cache)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        self.import_cache()
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
        self.comboBox_apptype.currentTextChanged.connect(lambda : 플레이어변경(self.comboBox_apptype.currentText()))
        #  Tab [Settings]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        self.btn_screenShot_setPos0.clicked.connect(lambda : self.getMousePos(2))
        self.btn_screenShot_setPos1.clicked.connect(lambda : self.getMousePos(3))
        self.btn_screenShot_openFile.clicked.connect(lambda : self.파일열기(self.input_screenShot_fileName.text()))
        self.btn_screenShot_capture.clicked.connect(self.takePicture)
        #self.btn_img2str_0.clicked.connect(lambda : self.getImg2Str(1))
        #self.btn_img2str_1.clicked.connect(lambda : self.getImg2Str(2))
        #self.comboBox_apptype.currentTextChanged.connect(self.set_apptype)
        
        
        
        #self.btn_setpos0.clicked.connect(lambda : self.getMousePos(0))
        #self.btn_setpos1.clicked.connect(lambda : self.getMousePos(1))
        #self.btn_setappsize.clicked.connect(self.setNewAppSize)
        #self.btn_setappsizewizard.clicked.connect(lambda : self.파일열기("setAppSizeIndex.py"))

    
    
        self.btn_temp_0.clicked.connect(lambda : self.set_button_styles(2))
        self.btn_temp_1.clicked.connect(lambda : self.set_button_styles(999))
        
        #221013
        self.btn_img2str_2.clicked.connect(lambda : self.translateImg(0))
    
        #self.btn_img2str_execute_1.clicked.connect(lambda : self.translateImg(0))

        self.btn_img2str_execute_4.clicked.connect(lambda : i2s.getStringFromImg2)

        for i in range(1,5) :
            #slotNum = i
            getattr(self, f'btn_img2str_execute_{i}').clicked.connect(lambda _, x=i : self.getImg2Str(x))

    #Tab [Hot]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self.comboBox_teleport.currentTextChanged.connect(self.changeTeleportBookMark)
        
        self.btn_teleportBookMark_openFile.clicked.connect(lambda : self.파일열기(self.input_teleportBookMark_name.text()))
        self.btn_teleportBookMark_setFile.clicked.connect(lambda : self.setFilePath(self.input_teleportBookMark_name))
        self.btn_teleportBookMark_apply.clicked.connect(self.applyTeleportBookMarkList)

        self.btn_subbtn_0.clicked.connect(lambda : self.executeCommand("cleanupinventory"))
        self.btn_subbtn_1.clicked.connect(lambda : self.executeCommand("additem 999 100000000"))
        self.btn_subbtn_2.clicked.connect(lambda : self.executeCommand("addcurrency 25 100000"))
        
        self.btn_subbtn_7.clicked.connect(multi.맨뒤캐릭터접속)#카드먹기_라이브
        self.btn_subbtn_8.clicked.connect(multi.카드먹기_라이브)#카드먹기_라이브
    
    #Tab [Item]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        #아이템 검색■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

        self.btn_searchItemName_all.clicked.connect(self.searchItemAll)
        self.btn_searchItemName.clicked.connect(lambda : self.copyText("item"))
        self.comboBox_itemhistory.currentTextChanged.connect(lambda : self.applyHistoryID("item"))

        #아이템/매터리얼 생성■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        for i in range(0,ITEM_SLOT_COUNT) :
            getattr(self, f'btn_additem_execute_{i}').clicked.connect(lambda _, x=i : self.아이템생성(x))
            if i != 0 :
                getattr(self, f'btn_additem_bookmark_{i}').clicked.connect(lambda _, x=i: self.아이템북마크추가(x))
        getattr(self, f'btn_additem_bookmark_0').clicked.connect(lambda _, x=i : self.아이템북마크제거(x))
        

        #0~13강 생성■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#

        self.btn_additemall.clicked.connect(self.additemAll)

        self.btn_item_txt_0.clicked.connect(lambda:self.setFilePath(self.input_item_txt_0))
        self.btn_item_txt_1.clicked.connect(lambda:self.파일열기(self.input_item_txt_0.text()))
        self.btn_item_txt_2.clicked.connect(lambda:self.additemText("additems"))
        self.btn_item_txt_3.clicked.connect(lambda:self.additemText("makeitem"))

    
    
    #Tab [Custom]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
        for i in range(0,CUSTOM_CMD_SLOT_COUNT) :
            getattr(self, f'btn_custom_execute_{i}').clicked.connect(lambda _, x=i : self.customCommand(x))

    
    
    
    #Tab [Command]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self.btn_cmd_openFile.clicked.connect(lambda : self.파일열기(self.input_cmd_name.text()))
        self.btn_cmd_setFile.clicked.connect(lambda : self.setFilePath(self.input_cmd_name))
        self.btn_cmd_apply.clicked.connect(self.applyCmdTextFile)
        self.btn_cmd_execute.clicked.connect(self.executeMultiCommand)
        for i in range(0,3) :
            getattr(self, f'btn_cmd_plus_{i}').clicked.connect(lambda _, x=i : self.control_multi_cmd(x))
        #self.btn_cmdBookMark_execute_0.clicked.connect(lambda : self.executeCommand(self.input_cmdBookMark_0.text()))
        #self.btn_cmdBookMark_execute_1.clicked.connect(lambda : self.executeCommand(self.input_cmdBookMark_1.text()))
        
        self.btn_testCase_openFile.clicked.connect(lambda : self.파일열기(".\data/etc/testCaseList.txt"))
        self.btn_testCase_apply.clicked.connect(self.applyTestCaseList)
        self.comboBox_testCase.currentTextChanged.connect(self.applyCurrentTestCase)
        self.btn_testCase_execute.clicked.connect(self.executeTestCase)
    #Tab [Character]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        #self.btn_setClass.clicked.connect(self.setClass)
        self.combo_setclass_3.currentTextChanged.connect(self.applySkillGroupList)
        self.comboBox_skillGroup.currentTextChanged.connect(self.changeSkillGroup)
        self.btn_skillmaster_opentxt.clicked.connect(self.open_skill_data)
        
        
        self.btn_skillGroup_execute.clicked.connect(lambda : self.executeCommand(\
            "changeskillenchant "+\
            self.input_skillGroup_id.text()+" "+\
            self.spinBox_skillGroup_level.text()+" "\
            ))
        self.btn_customCmd_0.clicked.connect(lambda : self.executeCommandByID(0))
        self.btn_customCmd_1.clicked.connect(lambda : self.executeCommandByID(1))
        self.btn_customCmd_2.clicked.connect(lambda : self.executeCommandByID(2))
        self.btn_customCmd_3.clicked.connect(lambda : self.executeCommandByID(3))
        self.btn_customCmd_4.clicked.connect(lambda : self.executeCommandByID(4))
        self.btn_lv.clicked.connect(lambda : self.executeCommandByID(5))
        self.btn_hp.clicked.connect(lambda : self.executeCommandByID(6))
        self.btn_mp.clicked.connect(lambda : self.executeCommandByID(7))
        
        self.btn_character_script_btn_0.clicked.connect(multi.캐릭터생성_알파)
        self.btn_character_script_btn_1.clicked.connect(multi.캐릭터생성_라이브)
        self.btn_character_script_btn_2.clicked.connect(multi.캐릭터탈퇴)

        #231013 리뉴얼
        self.btn_setClass_2.clicked.connect(self.get_skill_by_class)
        self.btn_classSkill_openDir.clicked.connect(lambda : self.파일열기("./data/character/skill/"))
        self.btn_setClass_check_0.clicked.connect(lambda : self.set_check_box_state("check_setskill_",3,2))
        self.btn_setClass_check_1.clicked.connect(lambda : self.set_check_box_state("check_setskill_",3,0))



        self.btn_setClass.clicked.connect(self.get_item_by_class)
        self.btn_classItem_openDir.clicked.connect(lambda : self.파일열기("./data/character/item/"))
        #self.btn_setskill_0.clicked.connect(lambda : self.파일열기(fr".\data\character\skill\testCaseList.txt"))
        self.btn_setClass_check_3.clicked.connect(lambda : self.set_check_box_state("check_setclass_",ITEM_CHECK_BOX_COUNT,2))
        self.btn_setClass_check_2.clicked.connect(lambda : self.set_check_box_state("check_setclass_",ITEM_CHECK_BOX_COUNT,0))

        for i in range(0,3) :
            getattr(self, f'btn_setskill_{i}').clicked.connect(lambda _, x=i : self.open_skill_file(x))
        for i in range(0,ITEM_CHECK_BOX_COUNT) :
            try:
                getattr(self, f'btn_setclass_{i}').clicked.connect(lambda _, x=i : self.open_item_file(x))
            except:
                continue

        for i in range(0,3) :
            getattr(self, f'btn_setskill_{i}').clicked.connect(lambda _, x=i : self.open_skill_file(x))
        for i in range(0,ITEM_CHECK_BOX_COUNT) :
            try:
                getattr(self, f'btn_setclass_{i}').clicked.connect(lambda _, x=i : self.open_item_file(x))
            except:
                continue

            #set_check_box_state

    #Tab [Character]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        '''
        TAB - DATA
        '''    
        for i in range(0,DATA_SLOT_COUNT) :
            getattr(self, f'btn_findData_openFile_{i}').clicked.connect(lambda _, x=i : self.데이터파일열기(x))
            getattr(self, f'btn_findData_openDir_{i}').clicked.connect(lambda _, x=i : self.데이터폴더열기(x))
            
#endregion

    #[App Window]▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    def getCurrentAppSize():
        print()

    def alignCurrentAppPos():
        print()

    def optimizeCurrentAppPos(self):
        print("optimizeCurrentAppPos")
        global currentAppName

        if currentAppName == "" :
            currentAppName = self.comboBox_appNameList.currentText()
        a = pag.getWindowsWithTitle(currentAppName)[0]
        a.moveTo(0,0)

        if ms.currentPlayer == ms.Player.LDPlayer :
            a.resizeTo(1469,838)
        elif ms.currentPlayer == ms.Player.Mirroid : #145,33,1196,678
            a.resizeTo(1469,710)
        
        try:
            self.setCurrentAppPos()
        except:
            pass

    def setCurrentAppPos(self):
        global currentAppName
        currentAppName = self.comboBox_appNameList.currentText()
        try :
            a = pag.getWindowsWithTitle(currentAppName)[0]
        except : 
            return
        
        x,y,w,h = sas.applyNewAppSize(a.left,a.top,a.right,a.bottom)
        self.label_appPos.setText("현재 앱 좌표(x,y,w,h) : {0}, {1}, {2}, {3}".format(x,y,w,h))

    def setCurrentAppTop(self):
        currentAppName = self.comboBox_appNameList.currentText()

        if currentAppName != "" :
        
            return
        
        a = pag.getWindowsWithTitle(currentAppName)[0]
        a.moveTo(a.left,a.top)

    def applyNewAppNameList(self):
        self.comboBox_appNameList.clear()
        a = self.input_appNameList_inclusiveStr.text()
        for i in pag.getAllTitles():
            if a not in i: 
                continue
            self.comboBox_appNameList.addItem(i)
    #▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨



    def executeCommand(self, cmd):
        self.setCurrentAppTop()
        ms.Command(cmd)
        self.activateWindow()

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

    # def executeCommand(self,cmd) :
    #     self.setCurrentAppTop()

    #     ms.Command(cmd)

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









#
    '''
    Functions - ITEM ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    '''

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

    def 아이템생성(self, slotNum) :
        
        cmdStr = self.comboBox_itemcmd.currentText()
        itemID = getattr(self, f'input_additem_itemid_{slotNum}').text()
        itemAmount = getattr(self, f'input_additem_amount_{slotNum}').text()
        
        if itemAmount == "" :
            itemAmount = 1
        #print(itemID, itemAmount)
        #multi.autoAddItem(itemID, itemAmount)

        self.executeCommand(f'{cmdStr} {itemID} {itemAmount}')

    def additem_bookmark(self) :
        
        itemID = self.input_additem_itemid_main.text()
        itemAmount = self.input_additem_amount_main.text()
        
        if itemAmount == "" :
            itemAmount = 1
        #print(itemID, itemAmount)
        #multi.autoAddItem(itemID, itemAmount)

        self.executeCommand(f'additem {itemID} {itemAmount}')
    def additemAll(self) :

        try:
            itemID = int(self.input_additemall_id.text())
        except :
            return

        temp_0 = "additems"
        temp_1 = ""
        for i in range(0,14):
            temp_1 += f' {str(itemID + i)}'

        cmd = f'{temp_0}{temp_1}'
        print(cmd)
        ms.Command(cmd,1)

    def additemText(self,type_str:str):

        try : 
            file_path = self.input_item_txt_0.text()
        except FileNotFoundError as errorMsg:
            self.popUp("에러",str(errorMsg))
            return

        with open(file_path) as f:
            content = f.read().strip()  # 파일 내용을 읽고 양쪽의 공백을 제거합니다
            bundle = ' '.join(content.split())  # 띄어쓰기로 구분하여 문자열로 저장
            print(len(bundle))


        cmd = f"additems {bundle}"
        delay = len(bundle) / 140
        
        ms.Command(cmd,delay)



    

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

    def 파일열기(self,filePath):
        # if filePath[0] != "/":
        #     filePath = "/"+ filePath
        # os.startfile(os.getcwd() + "/"+ filePath)
        print(os.getcwd())
        try:
            os.startfile(filePath)
        except : 
            try: 
                os.startfile(os.path.abspath(filePath))
            except:
                self.popUp(desText="파일 없음 : "+filePath)    
            
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
            try:
                getattr(self, f'input_additem_itemName_{slotNum}').setText("no name")
            except:
                pass

        if slotNum != 0 :
            line_edit = getattr(self, f'input_additem_itemName_{slotNum}')


        try:
            rarity = ms.DF값불러오기(df_item, "mID", itemID, "mRarity")
            if rarity == 0:
                line_edit.setStyleSheet("color: #b2b2b2;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 0
            elif rarity == 1:
                line_edit.setStyleSheet("color: #62c5b1;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 1
            elif rarity == 2:
                line_edit.setStyleSheet("color: #0e9bd9;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 2
            elif rarity == 3:
                line_edit.setStyleSheet("color: #b343d9;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 3
            elif rarity == 4:
                line_edit.setStyleSheet("color: #ff0000;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 4
            elif rarity == 5:
                line_edit.setStyleSheet("color: #fdb300;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 5
        except:
            if slotNum != 0 :

                line_edit.setStyleSheet("")  # Set font color for rarity level 0
            pass



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
                
                ms.텍스트파일_내용추가("item",itemName)
                self.applyHistory("item")
                pc.copy(self.input_itemid.text())

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
                self.input_additem_itemid_0.setText(str(itemID))
            except:
                print(f"no {target} name")

    #230712
    # def 리소스로드(self):

    #230712        
    def 이미지로드(self,slot_num):
        #image_path = './resource/Accessory_Cash_002.png'



        try:
            itemID = getattr(self, f'input_additem_itemid_{slot_num}').text()
            resource_id = df_item.loc[df_item["mID"] == int(itemID), "mResourceID"].values[0]
            res_name = df_resource_item.loc[df_resource_item["mID"] == int(resource_id), "mIconName"].values[0]

            #res_name = df_resource_item.loc[int(itemID),"mIconName"].values[0]
            image_path = f'./resource/{res_name}.png'
            # QPixmap 객체 생성
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                print('Error: QPixmap 객체 생성 실패')
                #sys.exit()

            # QLabel 위젯에 이미지 설정
            getattr(self, f'item_img_{slot_num}').setPixmap(pixmap)
        except Exception as e :
            print(e)
            empty_pixmap = QPixmap(1, 1)  # Create a QPixmap object with width and height of 1 pixel
            empty_pixmap.fill(QColor(0, 0, 0, 0))  # Fill the QPixmap with a transparent color
            getattr(self, f'item_img_{slot_num}').setPixmap(empty_pixmap)
            return
        
    #230717
    def 아이템북마크추가(self, slot_num):
        if slot_num == 0:
            return
        item_name = getattr(self, f'input_additem_itemName_{slot_num}').text()
        if item_name == "" :
            return
        
        ms.텍스트파일_내용추가(history_item_path,item_name)
        self.applyHistory("item")
    
    #230717
    def 아이템북마크제거(self, slot_num):
        #if slot_num != 0 :
        #    return
        print("45425")
        #item_name = getattr(self, f'input_additem_itemName_{slot_num}').text()
        item_name = self.comboBox_itemhistory.currentText()

        ms.텍스트파일_내용삭제(history_item_path,item_name)
        self.applyHistory("item")
#▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨



#▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨

    '''
    Functions - Custom
    '''
    def customCommand(self, slotNum) :
        cmd = getattr(self, f'input_custom_cmd_{slotNum}').text()
#        count = getattr(self, f'input_custom_count_{slotNum}').text()
        
        #print(itemID, itemAmount)
        #multi.Command_Text(itemID, itemAmount)
        #ms.Command(cmd)
        self.executeCommand(cmd)




#▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨

    '''
    Functions - Character ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    '''
    
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
        ,self.checkBox_setCharacter_10.isChecked()
        ,self.checkBox_setCharacter_11.isChecked()
        ,self.checkBox_setCharacter_12.isChecked()
        ]
        if self.comboBox_setClass.currentText() == "나이트":
            classNum = 0
        elif self.comboBox_setClass.currentText() == "아처":
            classNum = 1
        elif self.comboBox_setClass.currentText() == "위저드":
            classNum = 2
        elif self.comboBox_setClass.currentText() == "어쌔신":
            classNum = 3
        elif self.comboBox_setClass.currentText() == "버서커":
            classNum = 4
        sc.setClass_auto(classNum,checkBoxValues)

    def applySkillGroupList(self) :

        if self.combo_setclass_3.currentText() == "나이트":
            classNum = 0
        elif self.combo_setclass_3.currentText() == "아처":
            classNum = 1
        elif self.combo_setclass_3.currentText() == "위저드":
            classNum = 2
        elif self.combo_setclass_3.currentText() == "어쌔신":
            classNum = 3
        elif self.combo_setclass_3.currentText() == "버서커":
            classNum = 4

        fileName = f"./data/character/skill_master_{classNum}.txt"
     
        with open(fileName,encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()

        self.comboBox_skillGroup.clear()
        for i in range(0,len(lines)):
            line = lines[i].split(',')
            self.comboBox_skillGroup.addItem(line[2])

    def changeSkillGroup(self):
        
        if self.combo_setclass_3.currentText() == "나이트":
            classNum = 0
        elif self.combo_setclass_3.currentText() == "아처":
            classNum = 1
        elif self.combo_setclass_3.currentText() == "위저드":
            classNum = 2
        elif self.combo_setclass_3.currentText() == "어쌔신":
            classNum = 3
        elif self.combo_setclass_3.currentText() == "버서커":
            classNum = 4

        fileName = f"./data/character/skill_master_{classNum}.txt"

     
        with open(fileName,encoding='UTF-8') as f:
            lines = f.read().splitlines()
        f.close()
        
        for i in range(0,len(lines)):
            skillGroupID, maxEnchantValue, skillName = lines[i].split(',')
            #print(mapName)
            if self.comboBox_skillGroup.currentText() == skillName :
                self.input_skillGroup_id.setText(skillGroupID)
                #self.input_skillGroup_level.setText(maxEnchantValue)
                self.spinBox_skillGroup_level.setValue(int(maxEnchantValue))
                return


    def open_skill_data(self):
            
        selected_class = self.combo_setclass_3.currentText()
        classNum = 직업[selected_class].value if selected_class in 직업.__members__ else None
    
        fileName = f"data\character\skill_master_{classNum}.txt"

        self.파일열기(fileName)

    def get_skill_by_class(self):
        #class_id = 직업(self.combo_setclass_2.currentText()).value
        class_name = self.combo_setclass_2.currentText()
        check_box_list = [
            self.check_setskill_0.isChecked(),
            self.check_setskill_1.isChecked(),
            self.check_setskill_2.isChecked()
            ]
        sc.클래스별스킬습득(class_name,check_box_list)

    def get_item_by_class(self):
        #class_id = 직업(self.combo_setclass_2.currentText()).value
        class_name = self.combo_setclass.currentText()
        txt_list = []
        for i in range(ITEM_CHECK_BOX_COUNT):
            try:
                temp_val = getattr(self, f'check_setclass_{i}').isChecked()
                if temp_val :
                    temp_str = getattr(self, f'input_setclass_{i}').text()
                    txt_list.append(temp_str)
            except:
                continue
        sc.캐릭터아이템모음생성(class_name,txt_list)

    def open_skill_file(self, num):
        class_name = self.combo_setclass_2.currentText()
        if num == 0 :
            if class_name != "버서커":
                path = fr'.\data\character\skill\skill_공통.txt'
            else:
                path = fr'.\data\character\skill\skill_공통_버서커.txt'
                
        elif num == 1:
            path = fr'.\data\character\skill\skill_{class_name}.txt'
        elif num == 2:
            path = fr'.\data\character\skill\skill_master_{class_name}.txt'
        self.파일열기(path)

    def open_item_file(self, num):

        defaultDirectory = "./data/character/item/"
        txt_name = getattr(self, f'input_setclass_{num}').text()
        class_name = self.combo_setclass.currentText()

        file_name = ""
        temp_0 = os.path.join(defaultDirectory,f'{txt_name}.txt')
        temp_1 = os.path.join(defaultDirectory,f'{txt_name}_{class_name}.txt')
        #file_name_0 = os.path.join(defaultDirectory,f'{txt_name}.txt')
        if not os.path.isfile(temp_1) : 
            file_name = temp_0    
            if not os.path.isfile(temp_0) : 
                print(f'No File ... : {txt_name}')
                return
        else :
            file_name = temp_1   

        self.파일열기(file_name)

    # def get_item_by_class(self):
    #     class_name = self.combo_setclass_2.currentText()
    #     check_box_dict = {}
    #     for i in range(ITEM_CHECK_BOX_COUNT):
    #         temp_val = getattr(self, f'check_setclass_{i}').isChecked()
    #         check_box_dict[i] = temp_val

    #     txt_file_list = []
    def set_check_box_state(self,attr_str,count,state):
        for i in range(0,count):
            getattr(self, f'{attr_str}{i}').setCheckState(state)
    #Tab [Command]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    '''
    Functions - Character ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    '''
            
    def applyCmdTextFile(self) :
        try:
            with open(self.input_cmd_name.text(),encoding='UTF-8') as f:
                lines = f.read()#.splitlines()
            f.close()
        except :
            self.popUp("실패","경로 오류!\n")
        self.plainTextEdit_cmd.insertPlainText(lines)

    def executeMultiCommand(self) :
        headerText = self.combo_cmdHeader.currentText()
        footerText = self.combo_cmdHeader_2.currentText()
        commandText = self.plainTextEdit_cmd.toPlainText()
        if commandText == "" :
            return
        repeatCount = int(self.input_cmd_repeatCount.text()) if self.input_cmd_repeatCount.text() != "" else 1
        repeatDelay = int(self.input_cmd_repeatDelay.text()) if self.input_cmd_repeatDelay.text() != "" else 0
        repeatDelay2 = int(self.input_cmd_repeatDelay_2.text()) if self.input_cmd_repeatDelay_2.text() != "" else 0

    

        lines = commandText.splitlines()
        startTime = ms.GetElapsedTimeAuto(0)
        endTime = ms.GetElapsedTimeAuto((len(lines)*2+repeatDelay)*repeatCount)

        # self.label_cmd_startTime.setText("시작 시각 : {0}".format(startTime.strftime('%m-%d %H:%M:%S')))
        # self.label_cmd_endTime.setText("예상 종료 시각 : {0}".format(endTime.strftime('%m-%d %H:%M:%S')))


        for i in range(0,repeatCount) :
            # self.label_cmd_curRepeatCount.setText("총 {1}번 중 {0}번 째 실행 중...".format(str(i+1),str(repeatCount)))
            # self.progressBar_cmd.setValue(int(i/repeatCount*100))
            # QtWidgets.QApplication.processEvents()
            for line in lines:
                line = f'{headerText} {line} {footerText}'.strip()
                # if not headerText == "" :
                #     line = headerText + " " + line
                ms.Command(line,0.5)
                ms.sleep(repeatDelay2)
            if i < (repeatCount - 1) :
                ms.sleep(repeatDelay)

        consumedTime = ms.GetConsumedTime(startTime)
        #isTesting = 0

        # self.progressBar_cmd.setValue(100)
        # self.label_cmd_curRepeatCount.setText("-")
        # self.label_cmd_startTime.setText("시작 시각 : -")
        # self.label_cmd_endTime.setText("예상 종료 시각 : -")

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

    #231103
    def control_multi_cmd(self, num):
        total_text = self.plainTextEdit_cmd.toPlainText()
        if total_text == "" :
            return
        cur_text = total_text.splitlines()[len(total_text.splitlines())-1]

        if num == 0 :
            total_text += f'\n{int(cur_text)+1}'
        elif num == 1 :
            total_text += f'\n{int(cur_text)+10}'
        elif num == 2 :
            total_text += f'\n{int(cur_text)+100}'

        self.plainTextEdit_cmd.clear()
        self.plainTextEdit_cmd.insertPlainText(total_text)
    
    
    
    
    
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
    







    def 데이터파일열기(self, slotNum):
        source_folder = self.input_dataSourcePath.text()
        file_name = getattr(self, f'input_findData_{slotNum}').text()
        #source_path = os.path.join(source_folder,file_name)

        file_path = ms.get_latest_file_in_directory(source_folder,file_name)

        self.파일열기(f'{file_path}')
    
    def 데이터폴더열기(self, slotNum):
        source_folder = self.input_dataSourcePath.text()
        file_name = getattr(self, f'input_findData_{slotNum}').text()
        #source_path = os.path.join(source_folder,file_name)

        folder_path = ms.get_directory_of_latest_file(source_folder,file_name)

        self.파일열기(f'{folder_path}')





    #Functions━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    def setFilePath(self,target):
        path = QtWidgets.QFileDialog.getOpenFileName(self)
        if path != "" :
            target.setText(path[0])

    def setDirectoryPath(self, target):
        path = QtWidgets.QFileDialog.getExistingDirectory(self)
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

    def popUp(self,titleText="",desText ="",type = "about"):
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

    def set_button_styles(self, theme_option):
        color_bg = f'{random.randrange(0,256)},{random.randrange(0,256)},{random.randrange(0,256)}'
        
        
        '''
        1:기본
        2:랜덤
        3:고급
        '''
        style_options_others = {
            1: f"background-color: rgb(58, 117, 181);\ncolor: rgb(255, 255, 255);\nfont: bold",
            2: f"background-color: rgb({color_bg});\ncolor: rgb(255, 255, 255);\nfont: bold",
            999 : f"background-color: rgb({color_bg});\ncolor: rgb(255, 255, 255);\nfont: bold",
            # Add more themes as needed
        }
        style_options_main = {
            1: f"background-color: rgb(221, 235, 247);",
            2: f"background-color: rgb({color_bg});",#
            999 : f"background-color: rgb({color_bg});",#
            # Add more themes as needed
        }
        style_others = style_options_others.get(theme_option)
        style_main = style_options_main.get(theme_option)

        #if style:
        for widget in self.findChildren(QPushButton):
            if theme_option != 999 :
                widget.setStyleSheet(style_others)
            else:
                rand_color = f'{random.randrange(0,256)},{random.randrange(0,256)},{random.randrange(0,256)}'                
                widget.setStyleSheet(f"background-color: rgb({rand_color});\ncolor: rgb(255,255,255);\nfont: bold")

        for widget in self.findChildren(QLabel):
            if theme_option != 999 :
                widget.setStyleSheet(style_others)
            else:                
                widget.setStyleSheet(f"background-color: rgb({rand_color});\ncolor: rgb(255,255,255);\nfont: bold")

        #for widget in self.findChildren(QMainWindow):
        self.setStyleSheet(style_main)
        #else:
        #    print("Invalid theme option")
    
    def testTemp(self):
#아이템 이름 포함된 것 모두 찾기
        result = ms.findAllValInDataFrame(df_item,"mName","포션","mID")
        self.popUp("검색",str(result),"about")

    def import_cache(self) :
        global df_cache
        try :
            df_cache = pd.read_csv(f'{cache_path}',encoding='utf-8')
        except Exception as e: 
            
            if not os.path.isdir('./cache'):                                                           
                os.mkdir('./cache')
            print(e)
            return

        df_cache = df_cache.fillna(0)
        df_cache = df_cache.set_index('key').T.to_dict()

        try:
            x,y,w,h = str(df_cache['apppos_default']['value0']).split(',')
            sas.applyNewAppSize(x,y,w,h)
            self.label_appPos.setText("현재 앱 좌표(x,y,w,h) : {0}, {1}, {2}, {3}".format(ms.appX,ms.appY,ms.appW,ms.appH))

        except:
            pass


        for i in range(0,ITEM_SLOT_COUNT):
            try:

                val0 = df_cache[f'item_{i}']['value0']
                val1 = df_cache[f'item_{i}']['value1']
                if val0 != 0 :
                    getattr(self, f'input_additem_itemid_{i}').setText(str(int(val0)))
                if val1 != 0 :
                    getattr(self, f'input_additem_amount_{i}').setText(str(int(val1)))
            except:
                continue

        for i in range(0,CUSTOM_CMD_SLOT_COUNT):
            try:

                val0 = df_cache[f'cmd_{i}']['value0']
                val1 = df_cache[f'cmd_{i}']['value1']
                val2 = df_cache[f'cmd_{i}']['value2']
                if val0 != 0 :
                    getattr(self, f'input_custom_cmd_{i}').setText(str(val0))
                if val1 != 0 :
                    getattr(self, f'input_custom_comment_{i}').setText(str(val1))
                if val2 != 0 :
                    getattr(self, f'label_custom_count_{i}').setText(str(int(val2)))
            except:
                continue

        for i in range(0,ITEM_CHECK_BOX_COUNT):
            try:

                val0 = df_cache[f'setclass_cmd_{i}']['value0']
                val1 = df_cache[f'setclass_cmd_{i}']['value1']
                if val0 == "True":
                    getattr(self, f'check_setclass_{i}').setCheckState(2)
                if val1 != 0 :
                    getattr(self, f'input_setclass_{i}').setText(str(val1))
            except:
                continue

        for i in range(0,DATA_SLOT_COUNT):
            try:

                val0 = df_cache[f'findData_{i}']['value0']
                val1 = df_cache[f'findData_{i}']['value1']
                if val0 != 0:
                    getattr(self, f'input_findData_{i}').setText(str(val0))
                if val1 != 0 :
                    getattr(self, f'input_findData_comment_{i}').setText(str(val1))
            except:
                continue

    def export_cache(self, isForced = False):
        if not isForced : 
            if not self.check_autoCacheSave.isChecked() :
                return

        data = {}

        key = f'apppos_default'
        data[key] = {
            'value0': '0,0,1469,838',
        }

        
        for i in range(0,ITEM_SLOT_COUNT):
            tempVal0 = getattr(self, f'input_additem_itemid_{i}').text()
            tempVal1 = getattr(self, f'input_additem_amount_{i}').text()
            
            key = f'item_{i}'
            data[key] = {
                'value0': tempVal0,
                'value1': tempVal1
            }

        for i in range(0,CUSTOM_CMD_SLOT_COUNT):
            tempVal0 = getattr(self, f'input_custom_cmd_{i}').text()
            tempVal1 = getattr(self, f'input_custom_comment_{i}').text()
            tempVal2 = getattr(self, f'label_custom_count_{i}').text()
            
            key = f'cmd_{i}'
            data[key] = {
                'value0': tempVal0,
                'value1': tempVal1,
                'value2': tempVal2
            }

        for i in range(0,ITEM_CHECK_BOX_COUNT):
            tempVal0 = getattr(self, f'check_setclass_{i}').isChecked()
            tempVal1 = getattr(self, f'input_setclass_{i}').text()
            
            key = f'setclass_cmd_{i}'
            data[key] = {
                'value0': tempVal0,
                'value1': tempVal1,
            }

        for i in range(0,DATA_SLOT_COUNT):
            tempVal0 = getattr(self, f'input_findData_{i}').text()
            tempVal1 = getattr(self, f'input_findData_comment_{i}').text()
            
            key = f'findData_{i}'
            data[key] = {
                'value0': tempVal0,
                'value1': tempVal1,
            }

        # for i in range(0,3):
        #     tempVal0 = getattr(self, f'plainText_event_{i}').text()
            
        #     key = f'event_{i}'
        #     data[key] = {
        #         'value0': tempVal0
        #     }
        
        df = pd.DataFrame(data).T

  
        #df.to_csv(cache_path, index_label='Item')
        df.to_csv(cache_path, index_label='key',encoding='utf-8')

        print('export data successfully...')

    def closeEvent(self,event):
        print("end")

        self.export_cache(isForced= True)


    # async def schedules(self):
    #     await print("스케쥴")
    #     self.export_cache()
    # async def schedule_export_cache(self):
    #     await print('a')
    #     while True:
    #         await self.scedules()
    #         await asyncio.sleep(1)  # 5분(300초) 대기 후 다시 실행



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
import pyperclip as pc
import traceback

#endregion
# if __name__ == "__main__":
#     import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = MyWindow()#QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())
def make_log(msg, log_type : str = 'error', auto_open :bool = False):
    '''
    log_type : str = error / execute
    '''


    
    user_name = os.getlogin()
    log_file = fr".\log\log_{log_type}.txt"
    #error_message = traceback.format_exc()
    with open(log_file, "a") as file:
        file.write(f'\
date={time.strftime("%Y-%m-%d %H:%M:%S")}\n\
user={user_name}\n\
    {msg}\n\
────────────────────────────────────────\n')
    #print(f'생성실패 : {e}')
    if auto_open :
        os.startfile(log_file)

class ExceptionHandler:
    def __init__(self, original_hook):
        self.original_hook = original_hook

    def custom_hook(self, exc_type, exc_value, exc_traceback):
        # Handle the exception here
        print("An unhandled exception occurred:")
        msg = traceback.format_exception(exc_type, exc_value, exc_traceback)
        formatted_msg = ''.join(msg)
        make_log(formatted_msg,auto_open=True)

        # Optionally, save the traceback to a log file or perform other actions

        # Call the original exception hook
        if self.original_hook:
            self.original_hook(exc_type, exc_value, exc_traceback)

    def __call__(self, exc_type, exc_value, exc_traceback):
        self.custom_hook(exc_type, exc_value, exc_traceback)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    #try:
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    #app.exec_()
    sys.excepthook = ExceptionHandler(sys.excepthook)  # Override the exception hook
    sys.exit(app.exec_()) 
    # except Exception as e:
    #     msg = traceback.format_exc()
    #     make_log(msg,auto_open=True)