import os
import subprocess
import sys
import time
import random
import math
from settings import dict_settings

def helpText():
    print("""
This program was made by Anarb and it generates Bitcoin by searching multiple possible
wallet combinations until it's finds one with over 0 BTC and saves it into
a file called "wet.txt" in the results folder.
It's recommended to leave this running for a long time to get the best resaults, It's doesn't use up
that much resources so you can leave it in the background in the chance of you hitting a jackpot.
It's like mining but with less resources

Modyfied by: 
@anonymousl33t TikTok
@anonymousl337 Telegram
        """)

helpText()

print("threads: " + str(dict_settings["threads"] ))
print("save dry wallets: " + str(dict_settings["save_empty"] ))

while True:
    process1 = subprocess.Popen([sys.executable, "main.py"])
    process1.wait()