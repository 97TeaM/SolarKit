from itertools import repeat
import json
from social_spam import Mail
from colorama import Fore, Back, Style
from __mail__ import *

print(Fore.GREEN + """
  __  __       _ _  _____                       
 |  \/  |     (_) |/ ____|                      
 | \  / | __ _ _| | (___  _ __   __ _ _ __ ___  
 | |\/| |/ _` | | |\___ \| '_ \ / _` | '_ ` _ \ 
 | |  | | (_| | | |____) | |_) | (_| | | | | | |
 |_|  |_|\__,_|_|_|_____/| .__/ \__,_|_| |_| |_|
                         | |                    
                         |_|                    
                                        By solar#0156
""")

#Json
config = open("config.json", "r")
content = config.read()
settings = json.loads(content)

#Spam
mail = Mail()
mail.connect_mail(settings["mail", "token"])

def spam():
  mail.set_message(settings["header", "message"])
  mail.send_message(settings["victim_mail"]) # settings["__Image__"])


for x in range(settings["amount"]):
  spam()