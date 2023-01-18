import sys, os
from colorama import Fore
from art import *


Art=text2art("SolarKit")
print(Fore.GREEN + Art)
print("Version 1.0.0 made by solar#0156")


print(Fore.GREEN+"""
1: Passgen               | 2: Dos tool
3: Mail spammer          | 4: Discord raid tool
5: Tg Spammer
""")

command = input('>>> ')


if command == '1':
  os.system('cmd /k "python __passgen__.py -h"')


elif command == '2':
  os.system('cmd /k "Dos.py"')
    

elif command == '3':
  os.system('cmd /k "python __mail__.py.py"')

elif command == '4':
  os.system('cmd /k "python __raid__.py"')

elif command == '5':
  os.system('cmd /k "python __tg__.py"')