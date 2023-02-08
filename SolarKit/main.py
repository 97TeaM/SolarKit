import sys, os
from colorama import Fore
from art import *


Art=text2art("SolarKit")
print(Fore.GREEN + Art)
print("Version 1.0.2 made by solar#0156")


print(Fore.GREEN+"""
1: Passgen               | 2: Dos tool
3: Mail spammer          | 4: Discord raid tool
5: Tg Spammer            | 6: Discord nuke tool
""")

command = input('>>> ')


if command == '1':
  os.system('cmd /k "python passgen.py -h"')
# os.system('sh "python passgen.py -h"')

elif command == '2':
  os.system('cmd /k "node dos.js"')
# os.system('sh "node dos.js"')

elif command == '3':
  os.system('cmd /k "python mail.py.py"')
# os.system('sh "python mail.py"')

elif command == '4':
  os.system('cmd /k "python discord_raid.py"')
# os.system('sh "python raid.py"')

elif command == '5':
  os.system('cmd /k "python tg_spam.py"')
# os.system('sh "python tg_spam.py"')

################### NUKE ISN'T IMPLEMENTED, MY FULL NUKE TOOL ISNT OPEN-SOURCE FOR NOW. ###################

elif command == '5':
  os.system('cmd /k "python nuke.py"')
# os.system('sh "python nuke.py"')