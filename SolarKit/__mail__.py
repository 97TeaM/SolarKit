import json
from social_spam import *
from colorama import *
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
class __spam__:
    mail = Mail()
    mail = connect.Mail(settings["mail", "token"])
    mail.set_message(settings["message", "message2"])
    mail.send_message(settings["victim_mail"]) # settings["__Image__"])

    def repeat(__spam__):
        return repeat(__spam__(settings["amount"]))