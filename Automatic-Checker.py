import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

os.system("cls")
with open('tokens.txt', 'r') as f: #Check tokens from tokens.txt 1 per line
	for line in f:
	        time.sleep(0)
	        token = line.rstrip("\n")
	        headers = {
	            'Authorization': f'{token}'  
	        }
	        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers) # Discord Login Api

	        try:
	            if src.status_code == 200:
	                print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"+"+Fore.WHITE+"] "+Fore.RESET + token) #Valid Token
	            else:
	                print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"-"+Fore.WHITE+"] "+Fore.RESET + token) #Invalid Token
	        except Exception:
	            print(f"{Fore.CYAN}Error, please contact with Matty#8952 {Fore.RESET}") #If there's an error.