ITEM_SLOT_COUNT = 15
CUSTOM_CMD_SLOT_COUNT = 20
ITEM_CHECK_BOX_COUNT = 26
#DATA_SLOT_COUNT = 12 
app_type = 0
target_app_pos_txt_file = f'target_app_pos.txt'
import os
user_name = os.getlogin()

#app_pos_by_r2a = []

import subprocess
#import engraveCheck
import importlib
import pandas as pd
import pyautogui as pag
#import clipboard as cb
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
cache_folder = "./cache"
if not os.path.isdir(cache_folder):                                                           
    os.mkdir(cache_folder)


cache_path = f'./cache/cache_v5.csv'
try:
    df_cache = pd.read_csv(cache_path, sep='\t', encoding='utf-16', index_col='key')
except FileNotFoundError as e:
    print(f'{e} : 캐시 파일 없음')
currentAppName = ""


import PresetManager as pm
import xlrd
import msdata as ms
import multicommand as multi
import setclass as sc
import setappsize as sas
import img2str as i2s
import os
import translate as tl
import time
import re
import pyperclip as pc
import traceback
from enum import Enum
import random
import datetime

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
#from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout
from msdata import 플레이어변경, Player
#import asyncio
from PyQt5.QtCore import QTimer, QDateTime

# Connect the QAction button to the open_patch_notes function

class ImageTooltip(QWidget):
    def __init__(self, pixmap):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)
        self.setLayout(layout)

history_item_path = f'./data/etc/itemHistory.txt'
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(f'./etc/R2A_UI.ui')[0]
app_starttime = QDateTime.currentDateTime()#datetime.datetime.today()#.strftime("%Y-%m-%d %H:%M:%S")
print(f'{app_starttime=}')

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        print(999)
        #self.set_button_styles(2)
        # QTimer를 사용하여 5분마다 export_cache 함수 실행
        self.auto_cache_save_timer = QTimer(self)#check_autoCacheSave
        self.auto_cache_save_timer.timeout.connect(self.export_cache_all)
        self.auto_cache_save_timer.start(300000)  # 300000 밀리초 = 5분

        self.dateTimeEdit_app_starttime.setDateTime(app_starttime)
        self.unlock_screen_timer = QTimer(self)#check_autoCacheSave
        self.unlock_screen_timer.timeout.connect(self.stop_lock_screen)
        self.unlock_screen_timer.start(300000)  # 300000 밀리초 = 5분

#region Main UI
        file_dict = ms.get_recent_file_list(os.getcwd())
        last_modified_date = list(file_dict.values())[0]

        self.setWindowTitle(f"R2A 5.0 | {last_modified_date}")
        #self.statusLabel = QLabel(self.statusbar)

        self.setGeometry(1470,28,400,400)
        self.setFixedSize(450,1020)
        
        self.btn_teleport.clicked.connect(self.doTeleport)
        self.btn_customCmd_13.clicked.connect(multi.캐릭터재접속)
        self.btn_customCmd_14.clicked.connect(multi.캐릭터선택창)
        self.btn_customCmd_15.clicked.connect(multi.서버선택창)
        self.btn_customCmd_16.clicked.connect(multi.서드파티창)

        '''메뉴탭■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'''
        self.menu_patchnote.triggered.connect(lambda : self.파일열기("release_note_R2A.xlsx"))
        self.actionLog.triggered.connect(lambda : self.파일열기(fr"log\log_error_{user_name}.txt"))

        '''단축키■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'''

        for i in range(1, ITEM_SLOT_COUNT):
            button_name = f'btn_additem_execute_{i}'
            if hasattr(self, button_name):
                #shortcut = QShortcut(QKeySequence(Qt.Key_F1 + i), self)
                button = getattr(self, button_name)
                if i <= 12 :
                    button.setText(f"생성 F{i}")
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
        self.applyPresetList()

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
            df_item = pd.read_csv(itemFileName, encoding= 'utf-16',sep='\t')
            print('아이템 파일 로드 성공...')
        except FileNotFoundError:
            print('아이템 파일 캐시 생성 중...(1분 미만 소요)')
            df_item = pd.read_excel("./data/아이템.xlsx", engine="openpyxl", usecols=[0, 1, 2, 3,8,23])
            df_item.to_csv(itemFileName, index=False, encoding= 'utf-16',sep='\t')
    
        # 이전 날짜의 아이템 파일 삭제
        for file in os.listdir("./data"):
            if file.endswith(".csv"):
                file_date = re.findall(r'\d{6}', file)[0]
                if file_date < today:
                    os.remove(os.path.join("./data", file))




        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        
  
       
        #창 불러오기■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        
        self.comboBox_appNameList.clear()
        for i in pag.getAllTitles():
            if i == "": #or self.input_appNameList_inclusiveStr.text() in i:
                continue
            #mapName = lines[i].split(',')
            self.comboBox_appNameList.addItem(i)



        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#


        # Cache파일 로드 (Load Cache)■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        #self.import_cache()
        self.import_cache_all()
        self.set_target_app_size()
        플레이어변경(self.comboBox_apptype.currentText())
        self.applyNewAppNameList()
        '''any_widget : [QLineEdit,'input_00']'''
        self.import_cache_all([QComboBox,'comboBox_appNameList'])
       # print(app_pos_by_r2a)
        #■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■#
        '''패치노트'''
        try: 
            patch_show_count = 5

            last_starttime_str = self.import_cache_all([QDateTimeEdit,'dateTimeEdit_app_starttime'])
            last_starttime = QDateTime.fromString(last_starttime_str, Qt.ISODate)
            patch_note_check = self.import_cache_all([QCheckBox,'check_option_1'])
            is_next_day = app_starttime.date() > last_starttime.date()
            print(f'{is_next_day=}')
            print(f'{last_starttime=}')
            print(f'{patch_note_check=}')

            if patch_note_check.lower() == 'true' or ( patch_note_check.lower() == 'false' and is_next_day): 
                x, patch_see_again = self.popup2(
                    window_name='패치노트',
                    des_text=f"업데이트 배포 일자 : {last_modified_date}\n\n최신 업데이트 항목 {patch_show_count}개\n\n{ms.read_patch_notes('release_note_R2A.xlsx',patch_show_count)}", popup_type='patchnote')
            
                self.check_option_1.setChecked(not patch_see_again)
        except:
            pass
        #print(patch_see_again)
        # if x == QtWidgets.QMessageBox.Open :
        #     self.파일열기('release_note_R2A.xlsx')

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
    
        '''
        [Tab] - ITEM ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
        '''
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

        self.btn_item_3.clicked.connect(self.reset_item_slot)
        self.btn_item_0.clicked.connect(lambda : self.set_check_box_state("check_item_",999,2,start_num=1))
        self.btn_item_1.clicked.connect(lambda : self.set_check_box_state("check_item_",999,0,start_num=1))
        
        self.btn_item_preset_save.clicked.connect(lambda : self.save_preset('item'))
        #self.comboBox_item_preset.activated.connect(lambda : self.save_preset('item'))
        self.comboBox_item_preset.currentTextChanged.connect(lambda : self.load_preset('item'))
    #btn_item_preset_3
        self.btn_item_preset_2.clicked.connect(lambda : self.add_preset_bookmark('item'))
        for i in range(0,5) :
            getattr(self, f'btn_item_preset_bookmark_{i}').clicked.connect(lambda _, x=i : self.load_preset_by_bookmark(x, 'item'))
        self.btn_item_preset_0.clicked.connect(lambda : self.파일열기(os.path.join(self.input_preset_path.text(),\
                                                                              f'preset_item_{self.comboBox_item_preset.currentText()}.csv')))
        self.btn_item_preset_1.clicked.connect(lambda : self.파일열기(self.input_preset_path.text()))
        
        '''
        [Tab] - Custom ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
        '''
            
        for i in range(0,CUSTOM_CMD_SLOT_COUNT) :
            getattr(self, f'btn_custom_execute_{i}').clicked.connect(lambda _, x=i : self.customCommand(x))
            if i<12 :
                getattr(self, f'btn_custom_execute_{i}').setText(f'실행 F{i+1}')
            else:
                getattr(self, f'btn_custom_execute_{i}').setText(f'실행')

        self.btn_cmd_preset_save.clicked.connect(lambda : self.save_preset('cmd'))
        self.comboBox_cmd_preset.currentTextChanged.connect(lambda : self.load_preset('cmd'))
    #btn_cmd_preset_3
        self.btn_cmd_preset_3.clicked.connect(lambda : self.add_preset_bookmark('cmd'))
        for i in range(0,5) :
            getattr(self, f'btn_cmd_preset_bookmark_{i}').clicked.connect(lambda _, x=i : self.load_preset_by_bookmark(x, 'cmd'))
        self.btn_cmd_preset_0.clicked.connect(lambda : self.파일열기(os.path.join(self.input_preset_path.text(),\
                                                                              f'preset_cmd_{self.comboBox_cmd_preset.currentText()}.csv')))
        self.btn_cmd_preset_1.clicked.connect(lambda : self.파일열기(self.input_preset_path.text()))
        
        self.btn_cmd_1.clicked.connect(lambda : self.set_check_box_state("check_cmd_",999,2))
        self.btn_cmd_2.clicked.connect(lambda : self.set_check_box_state("check_cmd_",999,0))
        
        self.btn_item_preset_3.clicked.connect(lambda : self.delete_preset("item"))
        
        '''
        [Tab] - Command ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
        '''
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
    
        self.btn_cmd_0.clicked.connect(self.reset_cmd_slot)
        self.btn_cmd_preset_4.clicked.connect(lambda : self.delete_preset("cmd"))
    
    
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

        # for i in range(0,3) :
        #     getattr(self, f'btn_setskill_{i}').clicked.connect(lambda _, x=i : self.open_skill_file(x))
        # for i in range(0,ITEM_CHECK_BOX_COUNT) :
        #     try:
        #         getattr(self, f'btn_setclass_{i}').clicked.connect(lambda _, x=i : self.open_item_file(x))
        #     except:
        #         continue

            #set_check_box_state

    #Tab [Character]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        '''
        TAB - DATA
        '''    
        for i in range(0,999) :
            try:
                getattr(self, f'btn_findData_openFile_{i}').clicked.connect(lambda _, x=i : self.데이터파일열기(x))
                getattr(self, f'btn_findData_openDir_{i}').clicked.connect(lambda _, x=i : self.데이터폴더열기(x))
            except:
                break
            
#endregion

    #[App Window]▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    def getCurrentAppSize(self):
        #print()
        #cur_pos = self.label_appPos.text().split(',')
        label_app_pos = [int(x) for x in self.label_appPos.text().split(',')]

        return label_app_pos
    def set_target_app_size(self):
        with open(target_app_pos_txt_file,'w',encoding='UTF-8') as f:
            f.write(self.label_appPos.text())
            f.write('\n')
            f.write(self.comboBox_apptype.currentText())

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
        #self.label_appPos.setText("현재 앱 좌표(x,y,w,h) : {0}, {1}, {2}, {3}".format(x,y,w,h))
        self.label_appPos.setText(f'{x},{y},{w},{h}')

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
        targetName = self.input_itemName_all.text().replace('+','')

        result = ms.findAllValInDataFrame(df_item,"mName",targetName,"mID")
        self.popUp("결과",str(result),type='searchItem')

    def additemGoods(self) :
        multi.autoAddItem(ms.searchItemByName("", self.comboBox_goods.currentText()),self.input_goods_count.text())

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
        origin_path = os.getcwd()
        try:
            os.startfile(filePath)
        except : 
            try: 
                os.startfile(os.path.abspath(filePath))
            except:
                try:
                
                    os.startfile(os.path.join(origin_path,filePath))
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
            #print(f"no item ID : {itemID}")
            try:
                getattr(self, f'input_additem_itemName_{slotNum}').setText("no name")
            except:
                pass

        if slotNum != 0 :
            line_edit = getattr(self, f'input_additem_itemName_{slotNum}')
            image_label = getattr(self, f'item_img_{slotNum}')

        try:
            rarity = ms.DF값불러오기(df_item, "mID", itemID, "mRarity")
            if rarity == 0:
                color_code = '#b2b2b2'
                #line_edit.setStyleSheet("color: #b2b2b2;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 0
            elif rarity == 1:
                color_code = '#62c5b1'
                #line_edit.setStyleSheet("color: #62c5b1;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 1
            elif rarity == 2:
                color_code = '#0e9bd9'
                #line_edit.setStyleSheet("color: #0e9bd9;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 2
            elif rarity == 3:
                color_code = '#b343d9'
                #line_edit.setStyleSheet("color: #b343d9;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 3
            elif rarity == 4:
                color_code = '#ff0000'
                #line_edit.setStyleSheet("color: #ff0000;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 4
            elif rarity == 5:
                color_code = '#fdb300'
                #line_edit.setStyleSheet("color: #fdb300;background-color: rgb(0, 0, 0);")  # Set font color for rarity level 5
            line_edit.setStyleSheet(f"color: {color_code};background-color: rgb(0, 0, 0);")  # Set font color for rarity level 5
            image_label.setStyleSheet(f"background-color: {color_code};")  # Set font color for rarity level 5
        
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

    def applyHistoryID(self,target:str):#target = item/tran/serv
        if target == "item":
            try: 
                itemName = self.comboBox_itemhistory.currentText()
                itemID = ms.DF값불러오기(df_item,"mName",itemName,"mID")
                self.input_additem_itemid_0.setText(str(itemID))
            except:
                print(f"no {target} name")
  
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
            #print(e)
            empty_pixmap = QPixmap(1, 1)  # Create a QPixmap object with width and height of 1 pixel
            empty_pixmap.fill(QColor(0, 0, 0, 0))  # Fill the QPixmap with a transparent color
            getattr(self, f'item_img_{slot_num}').setPixmap(empty_pixmap)
            return
        
    def 아이템북마크추가(self, slot_num):
        if slot_num == 0:
            return
        item_name = getattr(self, f'input_additem_itemName_{slot_num}').text()
        if item_name == "" :
            return
        
        ms.텍스트파일_내용추가(history_item_path,item_name)
        self.applyHistory("item")
    
    def 아이템북마크제거(self, slot_num):
        #if slot_num != 0 :
        #    return
        print("45425")
        #item_name = getattr(self, f'input_additem_itemName_{slot_num}').text()
        item_name = self.comboBox_itemhistory.currentText()

        ms.텍스트파일_내용삭제(history_item_path,item_name)
        self.applyHistory("item")

    def reset_item_slot(self):
        for i in range(0,ITEM_SLOT_COUNT):
            getattr(self, f'input_additem_itemid_{i}').setText('')
            getattr(self, f'input_additem_amount_{i}').setText('')
        

#▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
#PRESET

    def applyPresetList(self) :
        preset_item_list = []
        preset_cmd_list = []

        directory_path = os.path.join(os.getcwd(),self.input_preset_path.text())
        for filename in os.listdir(directory_path):
            if filename.startswith("preset_item_") and filename.endswith(".csv"):
                preset_name = filename.replace("preset_item_", "").replace(".csv", "")
                preset_item_list.append(preset_name)
            elif filename.startswith("preset_cmd_") and filename.endswith(".csv"):
                preset_name = filename.replace("preset_cmd_", "").replace(".csv", "")
                preset_cmd_list.append(preset_name)

        self.comboBox_item_preset.clear()
        for val in preset_item_list:
            self.comboBox_item_preset.addItem(val)
        self.comboBox_cmd_preset.clear()
        for val in preset_cmd_list:
            self.comboBox_cmd_preset.addItem(val)

    def add_preset_bookmark(self,preset_type:str):
        cur_preset_name = getattr(self, f'comboBox_{preset_type}_preset').currentText()
        if cur_preset_name == "":
            self.show_statusbar_msg('choose preset first')
            return
        target_preset_num = getattr(self, f'spinBox_{preset_type}_preset').value()
        getattr(self, f'btn_{preset_type}_preset_bookmark_{target_preset_num-1}').setText(cur_preset_name)

    def load_preset_by_bookmark(self,num:int,preset_type:str):
        preset_name = getattr(self, f'btn_{preset_type}_preset_bookmark_{num}').text()
        self.load_preset(preset_type,preset_name)

    def delete_preset(self,preset_type:str):
        preset_name = getattr(self, f'comboBox_{preset_type}_preset').currentText()
        if preset_name == "" :
            self.popUp(desText='프리셋명을 지정하세요.')
            return

        preset_name = getattr(self, f'comboBox_{preset_type}_preset').currentText()
        directory_path = os.path.join(os.getcwd(),self.input_preset_path.text(),
                                      f'preset_{preset_type}_{preset_name}.csv')
        
        if self.popup2(f'Do you really want to delete preset : {preset_name}?') == QtWidgets.QMessageBox.Ok :

        
            os.remove(directory_path)
            self.applyPresetList()
        
        # else :
        #     QStyleHintReturnVariant

        
    def save_preset(self, preset_type : str, preset_name = "", reload = True) :
        '''
        reload 트루이면 저장 후 콤보박스 갱신(수동 저장 시)
        '''
        print(f'save preset {preset_type=} {preset_name=}')
        data = {}
        if preset_name == "":
            preset_name = getattr(self, f'input_{preset_type}_preset').text()


        if preset_type == 'cmd' : 

            if preset_name == "":
                self.show_statusbar_msg('need to insert preset name')
                return

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
        elif preset_type == 'item' : 

            if preset_name == "":
                self.show_statusbar_msg('need to insert preset name')
                return

            for i in range(1,ITEM_SLOT_COUNT):
                tempVal0 = getattr(self, f'input_additem_itemid_{i}').text()
                tempVal1 = getattr(self, f'input_additem_amount_{i}').text()
                
                key = f'item_{i}'
                data[key] = {
                    'value0': tempVal0,
                    'value1': tempVal1,
                }

        df = pd.DataFrame(data).T
        pm.save_preset(f'{preset_type}_{preset_name}', df)
        if reload :
            self.applyPresetList()

    def load_preset(self, preset_type : str, preset_name = "") :
        
        previous_preset_name = getattr(self, f'input_{preset_type}_preset').text()
        if previous_preset_name != "":
            self.save_preset(preset_type,previous_preset_name,reload=False) 
        # dump_preset_name = getattr(self, f'input_{preset_type}_preset').text()
        # if dump_preset_name != "" :
        #     self.save_preset(preset_type, dump_preset_name)

        if preset_name == "":                
            #try:
            preset_name = getattr(self, f'comboBox_{preset_type}_preset').currentText()
            if preset_name == "":                
            #except:
                self.show_statusbar_msg('need to select preset name')
                return
        
        df = pm.load_preset(f'{preset_type}_{preset_name}')            
        df = df.fillna('')
        df = df.T.to_dict()
        if preset_type == "cmd" :
            # if preset_name == "":                
            #     #try:
            #     preset_name = getattr(self, f'comboBox_{preset_type}_preset').currentText()
            #     if preset_name == "":                
            #     #except:
            #         self.show_statusbar_msg('need to select preset name')
            #         return
            
            # df = pm.load_preset(f'{preset_type}_{preset_name}')            
            # # if pd.isna(df) : 

            # #     #self.show_statusbar_msg(f'No preset name : {preset_name}')
            # #     self.popUp(desText=f'No preset name : {preset_name}')
            # #     return
            # df = df.fillna('')
            # df = df.T.to_dict()
            for i in range(0,CUSTOM_CMD_SLOT_COUNT):
                try:
                    val0 = df[i]['value0']
                    val1 = df[i]['value1']
                    val2 = df[i]['value2']
                    getattr(self, f'input_custom_cmd_{i}').setText(str(val0))
                    getattr(self, f'input_custom_comment_{i}').setText(str(val1))
                    getattr(self, f'label_custom_count_{i}').setText(str(int(val2)))
                except:
                    continue
            self.input_cmd_preset.setText(preset_name)        
        elif preset_type == "item" :
            # if preset_name == "":                
            #     #try:
            #     preset_name = getattr(self, f'comboBox_{preset_type}_preset').currentText()
            #     if preset_name == "":                
            #     #except:
            #         self.show_statusbar_msg('need to select preset name')
            #         return
            # df = pm.load_preset(f'{preset_type}_{preset_name}')
            
            # # if pd.isna(df) : 
            # #     #self.show_statusbar_msg(f'No preset name : {preset_name}')
            # #     self.popUp(desText=f'No preset name : {preset_name}')
            # #     return
            # df = df.fillna('')
            # df = df.T.to_dict()
            for i in range(1,ITEM_SLOT_COUNT):
                #try:
                val0 = df[i-1]['value0']
                val1 = df[i-1]['value1']
                try:
                    getattr(self, f'input_additem_itemid_{i}').setText(str(int(val0)))
                except:
                    getattr(self, f'input_additem_itemid_{i}').setText(str(val0))

                try:
                    getattr(self, f'input_additem_amount_{i}').setText(str(int(val1)))
                except:
                    getattr(self, f'input_additem_amount_{i}').setText(str(val1))
                # except Exception as e:
                #     #print(e)
                #     pass
                    #getattr(self, f'input_additem_itemid_{i}').setText('')
                    #getattr(self, f'input_additem_amount_{i}').setText('')
                
                    #continue
            getattr(self, f'input_{preset_type}_preset').setText(preset_name)

#▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨

    '''
    Functions - Custom ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    '''
    def customCommand(self, slotNum) :
        cmd = getattr(self, f'input_custom_cmd_{slotNum}').text()
        count = getattr(self, f'label_custom_count_{slotNum}').text()
        getattr(self, f'label_custom_count_{slotNum}').setText(str(int(count)+1))
        
        #print(itemID, itemAmount)
        #multi.Command_Text(itemID, itemAmount)
        #ms.Command(cmd)
        self.executeCommand(cmd)

    def reset_cmd_slot(self):
        for i in range(0,CUSTOM_CMD_SLOT_COUNT):
            getattr(self, f'input_custom_cmd_{i}').setText('')
            getattr(self, f'input_custom_comment_{i}').setText('')
            getattr(self, f'label_custom_count_{i}').setText('0')
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
                with open(f"{temp_0}", "w") as file:
                    pass

                    #return
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
    def set_check_box_state(self,attr_str,count,state,start_num = 0):
        try:
            for i in range(start_num,count):
                getattr(self, f'{attr_str}{i}').setCheckState(state)
        except AttributeError as e:
            #print(e)
            return
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
        #startTime = ms.GetElapsedTimeAuto(0)
        #endTime = ms.GetElapsedTimeAuto((len(lines)*2+repeatDelay)*repeatCount)

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

        #consumedTime = ms.GetConsumedTime(startTime)
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
            # 커서를 맨 끝으로 이동
        cursor = self.plainTextEdit_cmd.textCursor()
        cursor.movePosition(cursor.End)
        self.plainTextEdit_cmd.setTextCursor(cursor)
    
    
    
    
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

    def setFilePath(self,target,filter = ""):
        path = QtWidgets.QFileDialog.getOpenFileName(self,filter=('*.txt'))
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

    def popUp(self,titleText="",desText ="",type = "about",btn=''):
        #if type == "about" :
        msg = QtWidgets.QMessageBox()  
        #msg.setGeometry(1520,28,400,2000)

        msg.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        if type == "report" :
            msg.setFixedSize(500,500)

            
        if type == "searchItem" :
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            #msg.buttonClicked.connect(self.messageBoxBut
        msg.setWindowTitle(titleText)

        if type == "searchItem" :
            msg.setText("ItemID : " + str(desText) + "\n('OK'를 눌러 바로 생성)")      
        else:
            msg.setText(desText)

        x = msg.exec_()
        
        if type == "searchItem" :
            if x == QtWidgets.QMessageBox.Ok and desText.isnumeric():
                multi.autoAddItem(desText,"1")


        return x
    
    def popup2(self, des_text = "", popup_type = '', window_name = ''):

        msg = QtWidgets.QMessageBox()  
        #msg.setGeometry(1470,58,300,2000)
        msg.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        msg.setWindowTitle(window_name)
        msg.setWindowFlags(msg.windowFlags() | Qt.WindowStaysOnTopHint)
        if popup_type == "":
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.setText(des_text)
            return msg.exec_()
        elif popup_type == 'patchnote' :
                        # Create a checkbox
            checkbox = QtWidgets.QCheckBox("오늘은 그만 보기", msg)
            #checkbox1 = QtWidgets.QCheckBox("영원히 그만 보기", msg)
            #msg.setStandardButtons(QtWidgets.QMessageBox.Open | QtWidgets.QMessageBox.Cancel)
            msg.setStandardButtons(QtWidgets.QMessageBox.Cancel)

            msg.setCheckBox(checkbox)
            #msg.setCheckBox(checkbox1)
            msg.setText(des_text)
            #print(checkbox.isChecked())
            return msg.exec_(), checkbox.isChecked()#,checkbox1.isChecked()

            #msg.setStandardButtons(QtWidgets.QMessageBox.checkBox | QtWidgets.QMessageBox.Cancel)

      
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
                if 'item_img' in widget.objectName() :
                    #print(widget.objectName)
                    continue
                widget.setStyleSheet(f"background-color: rgb({rand_color});\ncolor: rgb(255,255,255);\nfont: bold")

        #for widget in self.findChildren(QMainWindow):
        self.setStyleSheet(style_main)
        #else:
        #    print("Invalid theme option")
    
    def testTemp(self):
#아이템 이름 포함된 것 모두 찾기
        result = ms.findAllValInDataFrame(df_item,"mName","포션","mID")
        self.popUp("검색",str(result),"about")


    '''
    Functions - Cache 캐시 (import/export) ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    '''

    # def import_cache(self) :
    #     global df_cache
    #     try :
    #         df_cache = pd.read_csv(f'{cache_path}',encoding='utf-8')
    #     except Exception as e: 
            
    #         if not os.path.isdir('./cache'):                                                           
    #             os.mkdir('./cache')
    #         print(e)
    #         return

    #     df_cache = df_cache.fillna(0)
    #     df_cache = df_cache.set_index('key').T.to_dict()

    #     try:
    #         x,y,w,h = str(df_cache['apppos_default']['value0']).split(',')
    #         sas.applyNewAppSize(x,y,w,h)
    #         self.label_appPos.setText("현재 앱 좌표(x,y,w,h) : {0}, {1}, {2}, {3}".format(ms.appX,ms.appY,ms.appW,ms.appH))

    #     except:
    #         pass


    #     for i in range(0,ITEM_SLOT_COUNT):
    #         try:

    #             val0 = df_cache[f'item_{i}']['value0']
    #             val1 = df_cache[f'item_{i}']['value1']
    #             if val0 != 0 :
    #                 getattr(self, f'input_additem_itemid_{i}').setText(str(int(val0)))
    #             if val1 != 0 :
    #                 getattr(self, f'input_additem_amount_{i}').setText(str(int(val1)))
    #         except:
    #             continue

    #     for i in range(0,CUSTOM_CMD_SLOT_COUNT):
    #         try:

    #             val0 = df_cache[f'cmd_{i}']['value0']
    #             val1 = df_cache[f'cmd_{i}']['value1']
    #             val2 = df_cache[f'cmd_{i}']['value2']
    #             if val0 != 0 :
    #                 getattr(self, f'input_custom_cmd_{i}').setText(str(val0))
    #             if val1 != 0 :
    #                 getattr(self, f'input_custom_comment_{i}').setText(str(val1))
    #             if val2 != 0 :
    #                 getattr(self, f'label_custom_count_{i}').setText(str(int(val2)))
    #         except:
    #             continue


    #     for i in range(0,5):
    #         try:
    #             val0 = df_cache[f'cmd_preset_bookmark_{i}']['value0']
    #             if val0 != 0 :
    #                 getattr(self, f'btn_cmd_preset_bookmark_{i}').setText(str(val0))
    #         except:
    #             continue
    #     for i in range(0,ITEM_CHECK_BOX_COUNT):
    #         try:

    #             val0 = df_cache[f'setclass_cmd_{i}']['value0']
    #             val1 = df_cache[f'setclass_cmd_{i}']['value1']
    #             if val0 == "True":
    #                 getattr(self, f'check_setclass_{i}').setCheckState(2)
    #             if val1 != 0 :
    #                 getattr(self, f'input_setclass_{i}').setText(str(val1))
    #         except:
    #             continue

    #     for i in range(0,DATA_SLOT_COUNT):
    #         try:

    #             val0 = df_cache[f'findData_{i}']['value0']
    #             val1 = df_cache[f'findData_{i}']['value1']
    #             if val0 != 0:
    #                 getattr(self, f'input_findData_{i}').setText(str(val0))
    #             if val1 != 0 :
    #                 getattr(self, f'input_findData_comment_{i}').setText(str(val1))
    #         except:
    #             continue
    
    def import_cache_all(self,any_widget = None):
        '''any_widget : [QLineEdit,'input_00']'''

        try:
            if df_cache is None :
            # Load CSV file with tab delimiter and utf-16 encoding
                df = pd.read_csv(cache_path, sep='\t', encoding='utf-16', index_col='key')
            else :
                df = df_cache
            if any_widget == None :
                all_widgets = self.findChildren((QLineEdit, QLabel, QComboBox, QCheckBox, QPlainTextEdit,QPushButton))
            else:
                all_widgets = [self.findChild(any_widget[0] ,any_widget[1])]
                #return 
            #all_widgets = self.findChildren((QLineEdit, QLabel, QComboBox, QCheckBox, QPlainTextEdit,QPushButton))

            for widget in all_widgets:
                object_name = widget.objectName()
                if object_name in df.index:
                    value = str(df.loc[object_name, 'value'])
                    if isinstance(widget, (QLineEdit,QLabel,QPushButton)):
                        widget.setText(value)
                    elif isinstance(widget, QComboBox):
                        # Set selected index based on the value, adjust as needed
                        index = widget.findText(value)
                        if index != -1:
                            widget.setCurrentIndex(index)
                    elif isinstance(widget, QCheckBox):
                        widget.setChecked(value.lower() == 'true')
                    elif isinstance(widget, QPlainTextEdit):
                        widget.setPlainText(value)

            if any_widget != None :
                return value
        except Exception as e:
            print(f"Error importing cache: {e}")

    def export_cache_all(self):
        try:
            data = {'key': [], 'value': []}

            all_widgets = self.findChildren((QLineEdit, QLabel, QComboBox, QCheckBox, QPlainTextEdit,QPushButton, QDateTimeEdit))

            for widget in all_widgets:
                value = ""
                if isinstance(widget, (QLineEdit,QLabel)) :
                    value = widget.text()
                elif isinstance(widget, (QPushButton)) :
                    if 'preset_bookmark' in widget.objectName() : 
                        value = widget.text()
                    else : 
                        continue
                elif isinstance(widget, QComboBox):
                    value = widget.currentText()
                elif isinstance(widget, QCheckBox):
                    value = str(widget.isChecked())
                elif isinstance(widget, QPlainTextEdit):
                    value = widget.toPlainText()
                elif isinstance(widget, QDateTimeEdit):
                    value = widget.dateTime().toString(Qt.ISODate)

                if value != "":
                    key = widget.objectName()
                    data['key'].append(key)
                    data['value'].append(value)

            df = pd.DataFrame(data)
            df.set_index('key', inplace=True)
            df.to_csv(cache_path, sep='\t', encoding='utf-16')
            print(f"exporting cache successfully!")
        except Exception as e:
            print(f"Error exporting cache: {e}")
        # data = {}

        # for widget in self.findChildren(QLineEdit):
        #     value = widget.text()
        #     if value != "":
        #         key = widget.objectName()
        #         data[key] = widget.text()
        #         #print(widget.objectName(), widget.text())

        # df = pd.DataFrame.from_dict(data, orient='index', columns=['value'])
        # df.index.name = 'key'
        # df.to_csv(cache_path, sep='\t', encoding='utf-16')
        
    # def export_cache(self, isForced = False):
    #     if not isForced : 
    #         if not self.check_autoCacheSave.isChecked() :
    #             return

    #     data = {}

    #     key = f'apppos_default'
    #     data[key] = {
    #         'value0': '0,0,1469,838',
    #     }

        
    #     for i in range(0,ITEM_SLOT_COUNT):
    #         tempVal0 = getattr(self, f'input_additem_itemid_{i}').text()
    #         tempVal1 = getattr(self, f'input_additem_amount_{i}').text()
            
    #         key = f'item_{i}'
    #         data[key] = {
    #             'value0': tempVal0,
    #             'value1': tempVal1
    #         }

    #     for i in range(0,CUSTOM_CMD_SLOT_COUNT):
    #         tempVal0 = getattr(self, f'input_custom_cmd_{i}').text()
    #         tempVal1 = getattr(self, f'input_custom_comment_{i}').text()
    #         tempVal2 = getattr(self, f'label_custom_count_{i}').text()
            
    #         key = f'cmd_{i}'
    #         data[key] = {
    #             'value0': tempVal0,
    #             'value1': tempVal1,
    #             'value2': tempVal2
    #         }        
            
    #     for i in range(0,5):
    #         tempVal0 = getattr(self, f'btn_cmd_preset_bookmark_{i}').text()
            
    #         key = f'cmd_preset_bookmark_{i}'
    #         data[key] = {
    #             'value0': tempVal0,
    #         }

    #     for i in range(0,ITEM_CHECK_BOX_COUNT):
    #         tempVal0 = getattr(self, f'check_setclass_{i}').isChecked()
    #         tempVal1 = getattr(self, f'input_setclass_{i}').text()
            
    #         key = f'setclass_cmd_{i}'
    #         data[key] = {
    #             'value0': tempVal0,
    #             'value1': tempVal1,
    #         }

    #     for i in range(0,DATA_SLOT_COUNT):
    #         tempVal0 = getattr(self, f'input_findData_{i}').text()
    #         tempVal1 = getattr(self, f'input_findData_comment_{i}').text()
            
    #         key = f'findData_{i}'
    #         data[key] = {
    #             'value0': tempVal0,
    #             'value1': tempVal1,
    #         }

    #     # for i in range(0,3):
    #     #     tempVal0 = getattr(self, f'plainText_event_{i}').text()
            
    #     #     key = f'event_{i}'
    #     #     data[key] = {
    #     #         'value0': tempVal0
    #     #     }
        
    #     df = pd.DataFrame(data).T

  
    #     #df.to_csv(cache_path, index_label='Item')
    #     df.to_csv(cache_path, index_label='key',encoding='utf-8')

    #     print('export data successfully...')



    def closeEvent(self,event):
        print("end")

        #self.export_cache(isForced= True)
        self.export_cache_all()

    def show_statusbar_msg(self,msg):
        self.statusbar.showMessage(msg)
    # async def schedules(self):
    #     await print("스케쥴")
    #     self.export_cache()
    # async def schedule_export_cache(self):
    #     await print('a')
    #     while True:
    #         await self.scedules()
    #         await asyncio.sleep(1)  # 5분(300초) 대기 후 다시 실행

    def stop_lock_screen(self):
        if self.check_unlockscreen.isChecked():
            ms.Click(ms.r2a_app_pos)



def make_log(msg, log_type : str = 'error', auto_open :bool = False, auto_upload :bool = True):
    '''
    log_type : str = error / execute
    '''


    
    log_file = fr".\log\log_{log_type}_{user_name}.txt"
    
    # Check if the log file exists
    if not os.path.exists(log_file):
        with open(log_file, "w"):
            pass  # Create the file if it doesn't exist
    with open(log_file, "r") as file:        
        existing_logs = file.read()

    with open(log_file, "w") as file:
        file.write(f'\
date={time.strftime("%Y-%m-%d %H:%M:%S")}\n\
user={user_name}\n\n\
{msg}\n\n\
────────────────────────────────────────\n\
{existing_logs}\
')
    #print(f'생성실패 : {e}')
    if auto_open :
        os.startfile(log_file)
    if auto_upload :
        os.startfile(os.path.join(log_folder,'upload_log.bat'))

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

#if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
#try:
        
# app = QApplication(sys.argv) 
# myWindow = WindowClass() 
# myWindow.show()
# sys.excepthook = ExceptionHandler(sys.excepthook)  # Override the exception hook
# sys.exit(app.exec_()) 


def starter():
    
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    sys.excepthook = ExceptionHandler(sys.excepthook)  # Override the exception hook
    sys.exit(app.exec_()) 

if __name__ == "__main__" :
    starter()