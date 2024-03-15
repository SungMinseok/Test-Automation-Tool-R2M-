import 트리거 as trig

current_directory = trig.현재디렉토리반환()
result_directory = trig.결과저장디렉토리생성("quick_slot_ban")
lines = trig.대상파일읽기및리스트반환(f'{current_directory}/퀵슬롯제한대상.txt')

결과물명 = f'{result_directory}/result.txt'


for line in lines :

    이미지명 = f'{result_directory}/{line}.jpg'

    trig.화면리셋()
    
    trig.명령어입력("cleanupinventory")

    trig.명령어입력(f'additem {line} 1')

    trig.화면클릭('menuPos1')

    trig.대기(1)

    trig.화면클릭('invenBtn0')

    trig.화면클릭('quickBtn0')

    trig.스크린샷('center_system_msg_box',이미지명)

    trig.텍스트변환(이미지명, 결과물명)