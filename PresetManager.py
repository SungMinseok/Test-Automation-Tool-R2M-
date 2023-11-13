import os


import pandas as pd
default_path = "./data/preset"
if not os.path.isdir(default_path):                                                           
    os.mkdir(default_path)
    

# class PresetManager:
#     def __init__(self, default_path):
#         self.default_path = default_path

def save_preset(name, dataframe):
    file_path = os.path.join(default_path, f"preset_{name}.xlsx")
    dataframe.to_excel(file_path, index=False)
    print(f'save preset done... : {file_path}')

def load_preset(name):
    file_path = os.path.join(default_path, f"preset_{name}.xlsx")
    if os.path.exists(file_path):
        return pd.read_excel(file_path)
    else:
        print(f"Error: Preset '{name}' not found.")
        return None
