import pandas as pd
import os

def convert_excel_to_csv(excel_file, csv_file, encoding='utf-8'):
    # 엑셀 파일을 DataFrame으로 읽어옴
    translation_table = pd.read_excel(excel_file)
    
    # CSV 파일로 저장 (한글 인코딩 설정 포함)
    translation_table.to_csv(csv_file, index=False, encoding=encoding)

def find_translation(target, mTableName, mLanguageCode, mString, csv_file='번역 문자열.csv', encoding='utf-8'):
    if not os.path.exists(csv_file):
        # 최초 1회 실행 시 엑셀 파일을 CSV로 변환
        convert_excel_to_csv('번역 문자열.xlsx', csv_file, encoding)
    
    # CSV 파일을 DataFrame으로 읽어옴
    translation_table = pd.read_csv(csv_file, encoding=encoding)
    
    # 주어진 조건에 맞는 행을 필터링하여 결과를 얻음
    filtered_rows = translation_table[
        (translation_table['mTableName'] == mTableName) &
        (translation_table['mLanguageCode'] == mLanguageCode) &
        (translation_table['mString'] == mString)
    ]
    
    # 번역 내용을 출력
    if not filtered_rows.empty:
        translations = filtered_rows['mTranslateString'].tolist()
        for translation in translations:
            print(translation)
    else:
        print('해당 조건에 맞는 번역이 없습니다.')

# 예시 입력과 함께 함수 호출
while(True):
    target = input("찾을 번역 입력 > ")#'파이어 워크스'
    mTableName = 'DT_TransformCard'
    mLanguageCode = 1
    mString = target

    find_translation(target, mTableName, mLanguageCode, mString)
