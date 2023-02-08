import sys
import time
from art import *
from colorama import Fore

class Raid:

    def text():
        Art=text2art("SolarRaid")
        print(Fore.GREEN + Art)


        def type(text):
            words = text
            for char in words:
                time.sleep(0.025)
                sys.stdout.write(char)
                sys.stdout.flush()

        type(Fore.GREEN + "Made by solar#0156\n")

        type(Fore.GREEN + "\nUsage: python __raid__.py")
    
    text()