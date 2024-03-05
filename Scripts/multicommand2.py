import pyautogui as pag
import msdata as ms
from time import sleep
import os.path
import time
import img2str as i2s
import random
import string
import inspect
#import R2A
app_pos = [0,33,1428,805]





def display_menu():
    functions = [func for func in globals() if callable(globals()[func]) and inspect.isfunction(globals()[func])]

    print("Menu:")
    for i, func_name in enumerate(functions, start=1):
        print(f"[{i}] {func_name}")

def execute_function_by_index(index):
    functions = [func for func in globals() if callable(globals()[func]) and inspect.isfunction(globals()[func])]

    if 1 <= index <= len(functions):
        selected_func_name = functions[index - 1]
        selected_func = globals()[selected_func_name]
        selected_func()
    else:
        print("Invalid index. Please select a valid option.")
        
if __name__ == "__main__":
    options = input('[0]LD [1]MIR\n>: ')

    # app_pos, app_type = ms.get_target_app_pos()
    # print(app_pos, app_type)
    # ms.appX, ms.appY, ms.appW, ms.appH = app_pos[0],app_pos[1],app_pos[2],app_pos[3]
    # ms.플레이어변경(app_type)
    if options == '0':
        ms.appX, ms.appY, ms.appW, ms.appH = 0,33,1428,805
        ms.플레이어변경('LDPlayer')
    elif options == '1':
        ms.appX, ms.appY, ms.appW, ms.appH = 145,33,1194,677
        ms.플레이어변경('Mirroid')
    while True:
        display_menu()
        user_input = input("Enter the index of the function to execute (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        try:
            index = int(user_input)
            execute_function_by_index(index)
        except ValueError:
            print("Invalid input. Please enter a number.")
