import os
import xlrd

import pandas as pd
real_default_path = './data'
if not os.path.isdir(real_default_path):                                                           
    os.mkdir(real_default_path)
default_path = "./data/preset"
if not os.path.isdir(default_path):                                                           
    os.mkdir(default_path)
    

# class PresetManager:
#     def __init__(self, default_path):
#         self.default_path = default_path

def save_preset(name, dataframe):
    file_path = os.path.join(default_path, f"preset_{name}.csv")
    # dataframe.to_excel(file_path, index=False)
    # dataframe.to_csv(file_path, index_label='key',encoding='utf-8')
    dataframe.to_csv(file_path, sep='\t', encoding='utf-16')
    print(f'save preset done... : {file_path}')

def load_preset(name):
    file_path = os.path.join(default_path, f"preset_{name}.csv")
    if os.path.exists(file_path):
        try:
            return pd.read_csv(file_path, sep='\t', encoding='utf-16')

        except xlrd.biffh.XLRDError as e:
            return -1
    else:
        print(f"Error: Preset '{name}' not found.")
        return None
