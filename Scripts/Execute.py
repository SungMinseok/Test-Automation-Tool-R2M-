import os
import pandas as pd
import subprocess

cache_folder = "./cache"
cache_path = f'./cache/cache_v5.csv'
downloader_name = 'R2A_Download.bat'
if not os.path.isdir(cache_folder):                                                           
    os.mkdir(cache_folder)

try:

    df_cache = pd.read_csv(cache_path, sep='\t', encoding='utf-16', index_col='key')


    '''자동업데이트'''
    print('자동 업데이트 여부 체크 중...')
    try:
        is_auto_update = df_cache.loc['check_option_0', 'value']
        #print(f'{is_auto_update=}')
        if is_auto_update == 'True':
            print('업데이트 자동 실행...')
            try:
                process = subprocess.Popen(downloader_name, shell=True)

                process.wait()
            except:
                print(f'다운로더 없음, 업데이트 실패 : {downloader_name} 경로 확인 필요')
        else:
            print('업데이트 자동 실행 하지 않음')
    except:
        print('업데이트 체크 캐시 없음 : 패스...')

except FileNotFoundError as e :
    print(e)
    pass

'''패치노트여부'''
import R2A
R2A.starter()
