# This was written for educational purpose only. Use it at your own risk.
# Author will be not responsible for any damage!
# This program created by ./Vlasta_Exefuxion. All Rights Reserved. © 2020
import os
import requests
from tqdm import tqdm
from time import sleep
banner = """

            \033[0;31m【V】【l】【a】【s】【t】【a】
    \033[0;31m【E】【x】【e】【f】【u】【x】【i】【o】【n】

          \033[34m ++++++++++++++++++++++++++++++++
           +  \033[33m【A】【d】【m】【i】【n】\033[34m   +
           +\033[33m【F】【i】【n】【d】【e】【r】\033[34m+
           +\033[33m【S】【c】【r】【i】【p】【t】\033[34m+
           \033[34m++++++++++++++++++++++++++++++++

                    \033[2;32mInformation :
           AFS Coded By ./Vlasta_Exefuxion
             \033[2;37mAll Rights Reserved. © 2020
"""
os.system("clear")
print (banner)
target = input("\n\033[0;31mroot@target \033[1;37m:\033[0;34m~\033[0;31m#\033[1;37m ")
f = open('hack_list.txt','r')
exefuxion = f.read()
scriper = exefuxion.split('\n')
for i in tqdm(range(100), mininterval = 3,
         desc ="\033[1;32mstarting"):
    	 sleep(.1)
for i in scriper:
	url = target+'/'+i
	code = requests.get(str(url)).status_code
	if code == 200:
		print ("\033[1;33m[\033[1;34m+\033[1;33m] FOUND \033[1;34m" + url )
	else:
		print ( "\033[0;31mNOT FOUND \033[0;37m" + url )


