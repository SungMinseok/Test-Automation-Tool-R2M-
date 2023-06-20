import pyautogui as pag
import pyperclip

command = "additems"

# Copy the command to the clipboard
pyperclip.copy(command)

# Use hotkey to paste the command
pag.hotkey("ctrl", "v")
