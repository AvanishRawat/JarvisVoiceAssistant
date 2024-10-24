import os
import subprocess as sp
import pyttsx3
from decouple import config






paths = {
    "notepad" : "C:\\Windows\\notepad",
    "discord" : "C:\\Users\\Avanish\\AppData\\Local\\Discord\\app-1.0.9166\\Discord",
    "calculator":"C:\\Windows\\System32\\calc.exe"

}


def open_camera():
    sp.run('start microsoft.windows.camera',shell = True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

