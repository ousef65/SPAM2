import os
from os import system
import time
import keyboard
import pyautogui
from termcolor import colored
from colorant import Colorant
import subprocess

subprocess.call(f'mode con: cols=100 lines=30', shell=True)

#Settings
TOGGLE_KEY = 'F1'  # Toggle on/off colorant key
XFOV = 50  # X-Axis FOV
YFOV = 45  # Y-Axis FOV
INGAME_SENSITIVITY = 0.977 # Replace this with the your in-game sensitivity value
FLICKSPEED = 1.07437623 * (INGAME_SENSITIVITY ** -0.9936827126)  # Calculate flick speed
MOVESPEED = 1.5 / (3 * INGAME_SENSITIVITY) # Calculate move speed

monitor = pyautogui.size()
CENTER_X, CENTER_Y = monitor.width // 2, monitor.height // 2

def main():
    os.system('title Colorant Modded')
    colorant = Colorant(CENTER_X - XFOV // 2, CENTER_Y - YFOV // 2, XFOV, YFOV, FLICKSPEED, MOVESPEED)
    print(colored('''
                  

             ▄████▄   ▒█████   ██▓     ▒█████   ██▀███   ▄▄▄       ███▄    █ ▄▄▄█████▓
            ▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▒██▒  ██▒▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
            ▒▓█    ▄ ▒██░  ██▒▒██░    ▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
            ▒▓▓▄ ▄██▒▒██   ██░▒██░    ▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
            ▒ ▓███▀ ░░ ████▓▒░░██████▒░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
            ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
              ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
            ░        ░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒    ░░   ░   ░   ▒      ░   ░ ░   ░      
            ░ ░          ░ ░      ░  ░    ░ ░     ░           ░  ░         ░          
            ░                      
                                            MODDED V.1                                                                     
''', 'magenta'))
    print()
    print(colored('[Info]', 'green'), colored('Set enemies to', 'white'), colored('Purple', 'magenta'))
    print(colored('[Info]', 'green'), colored(f'Press {colored(TOGGLE_KEY, "magenta")} to toggle ON/OFF Colorant', 'white'))
    print(colored('[Info]', 'green'), colored(f'Press', 'white'), colored('F2', 'magenta'), colored('to toggle ON/OFF Detection Window', 'white'))
    print(colored('[Info]', 'green'), colored('RightMouse', 'magenta'), colored('= Aimbot,', 'white'))
    print(colored('[Info]', 'green'), colored('LeftAlt', 'magenta'), colored('= Triggerbot', 'white'))
    print(colored('[Info]', 'green'), colored('V', 'magenta'), colored('= Silentaim', 'white'))
    status = 'Disabled'
    
    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                colorant.toggle()
                status = 'Enabled ' if colorant.toggled else 'Disabled'
            print(f'\r{colored("[Status]", "green")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'green'), colored('Exiting...', 'white') + '\n')
    finally:
        colorant.close()

if __name__ == '__main__':
    main()