import json
from social_spam import Telegram
from argparse import *
from colorama import Fore, Back, Style

print(Fore.GREEN + """
  _______     _____                       
 |__   __|   / ____|                      
    | | __ _| (___  _ __   __ _ _ __ ___  
    | |/ _` |\___ \| '_ \ / _` | '_ ` _ \ 
    | | (_| |____) | |_) | (_| | | | | | |
    |_|\__, |_____/| .__/ \__,_|_| |_| |_|
        __/ |      | |                    
       |___/       |_|
                                        By solar#0156 
""")

#Json
config = open("tgconf.json", "r")
content = config.read()
settings = json.loads(content)

#Telegram
tg = Telegram()
tg.connect_user(api_id=settings["api_id"], api_hash=settings["api_hash"], phone_number=settings["phone_number"])

tg.get_chats()

# tg.send_message(user_id=settings["victim_id"], message=settings["message"], image=settings["__Image__"])

# tg.start_bombing(user_id=1370248012, amount=settings["amount"], message=settings["message"],  image=settings["__Image__"])

# tg.start_selective_spam(settings["api_id", "victim_id"], "HELLO FROM 97tEaM")