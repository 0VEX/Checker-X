# CheckerX
# --------------------------------------------------------------------------------

#libraries
from re import I
import time
from xml.dom.minidom import ElementInfo
from colorama import Fore , init
import os
import random
import threading
import requests
import sys

# Colors
init(autoreset=True)
m = Fore.MAGENTA
b = Fore.BLUE 
r = Fore.RED
y = Fore.YELLOW
c = Fore.CYAN
g = Fore.GREEN
w = Fore.WHITE
bl = Fore.BLACK
re = Fore.RESET
#---------------------------
lm = Fore.LIGHTMAGENTA_EX
lb = Fore.LIGHTBLUE_EX
lr = Fore.LIGHTRED_EX
ly = Fore.LIGHTYELLOW_EX
lc = Fore.LIGHTCYAN_EX
lg = Fore.LIGHTGREEN_EX
lw = Fore.LIGHTWHITE_EX
lbl = Fore.LIGHTBLACK_EX

# More
red = "\033[1;31;40m";yel = '\033[1;33;40m'
bloFT = "\033[1;36;40m"
grn = '\033[1;32;40m';wit = "\033[1;37;40m"
check_list = [
        ['https://instagram.com/','instagram',False],
        ['https://twitter.com/','twitter',False],
        ['https://facebook.com/','facebook',True],
        ['https://github.com/','github',True],
        ['https://usr.gg/','usr.gg',True],
        ['https://pinterest.com/','pinterest',True],
        ['https://t.me/','telegram',True],
        ['https://tellonym.me/','tellonym',True],
        ['https://tiktok.com/@','tiktok',True]]

# ---------------------------------------------------------------------------------------------------------

def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join(('' * int(space)) + var for var in var.splitlines())


def cls():
    if sys.platform == 'linux':os.system('clear')
    else:os.system('cls')

def logo():
  
  print(center(f"""\n\n
       ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗      ██╗  ██╗
      ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗     ╚██╗██╔╝            ~ {lr}Checker{lr} - {lr}X ~
      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝█████╗╚███╔╝ 
      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════╝██╔██╗      github.com/{lr}0VEX ~ IG : {lr}TheGreatVex 
      ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║     ██╔╝ ██╗
       ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝
                                                      {lr} Version 1.0 {re}
        """).replace('█', lr+"█"+lc).replace('~', lc+"~"+lc).replace('-', lr+"-"+lc))

#funct
def about():
    cls()
    print(center(f"""
       ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗      ██╗  ██╗
      ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗     ╚██╗██╔╝    
      ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝█████╗╚███╔╝ 
      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════╝██╔██╗      
      ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║     ██╔╝ ██╗
       ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝

 [+] Tool Created by V E X (Hussain)                                                         
                                                                                                    
 {lr}Author      :  {lc}Hussain [V E X]
 {lr}Github      :  {lc}https://github.com/0VEX
 {lr}instagram   :  {lc}https://instagram.com/thegreatvex
 {lr}Version     :  {lc}1.0
     
 {lr}[{w}0{lr}]{lc} Main Menu    {lr}[{w}99{lr}]{lc} Exit
        
        """).replace('█', lr+"█"+lc).replace('~', lc+"~"+lc).replace('-', lr+"-"+lc))
    
    info = input(f"{lr}[{w}?{lr}]{lc} Enter choice : ")
    if info == '0':
        cls()
        home()

    if info == '99':
        cls()
        sys.exit()
    
    else :print(f'\n{lr}[{w}!{lr}]{lc}wrong choice try agian');time.sleep(1);about()


def check(li:list):
    if li[-1]:
        cls()
        logo()
        print(f'{lr}[{w}+{lr}]{lc} Welcome to {li[1]} Checker {re}\n\n')
        leg = int(input(f'{lr}[{w}+{lr}]{lc} Length : '))
        lit = 'qwertyuiopasdfghjklzxcvbnm1234576890'
        print()
        while True:
            user = ("".join(random.choice(lit) for i in range(leg)))
            req = requests.get(f"{li[0]}{user}").status_code
            if req == 200:
                print(f"{lr}Unavailable >>{re} {user}")
            if req == 404:
               print(f"{g}Available >> {re} {user} {re}")


    else:
        cls()
        logo()
        print(f'''
        {lr}[{w}0{lr}]{lc} MainMenu             {lr}[{w}X{lr}]{lc} Exit

        ''')
        print(f'{lr}[{w}!{lr}]{lr} Sorry {li[1]} checker is not available yet ... \n')
        choice = input(f"{lr}[{w}?{lr}]{lc} Enter choice : ")
        if choice == '0':home()
        elif choice == 'x' or choice == 'X':sys.exit(0)
        else :print(f'\n{lr}[{w}!{lr}]{lc}wrong choice try agian');time.sleep(1);home()


def custom():
  cls()
  logo()
  print(f"          {lr}[{w}!{lr}]{lr} Before you start please know this is a {lc}beta{lr} version of custom site\n")
  print(f"     {lr}[{w}?{lr}]{lc} Examble --> {lr}(google.com){lc} it must be with the domain ,, {lr}only https sites works{re}\n\n")
  custom = input(f'{lr}[{w}?{lr}]{lc} Enter a site : ')
  cls()
  logo()
  print(f'{lr}[{w}+{lr}]{lc} Done creating {custom} Checker {re}\n\n')
  leg = int(input(f'{lr}[{w}+{lr}]{lc} Length : '))
  lit = 'qwertyuiopasdfghjklzxcvbnm1234576890'
  print()
  while True:
      user = ("".join(random.choice(lit) for i in range(leg)))
      req = requests.get(f"https://{custom}/{user}").status_code
      if req == 200:
          print(f"{lr}Unavailable >>{re} {user}")
      if req == 404:
          print(f"{g}Available >> {re} {user} {re}")


def home():
    cls()
    logo()
    print(f"""
               {lr}[{w}1{lr}]{lc} Checkers list        {lr}[{w}2{lr}]{lc} Custom checker   

                      {lr}[{w}99{lr}]{lc} About     {lr}[{w}0{lr}]{lc} Exit   
    """)
    choice = input(f"{lr}[{w}?{lr}]{lc} Enter choice : ")

    if choice == '1':
        cls()
        logo()
        print(f'''
           {lr}[{w}1{lr}]{lc} Instagram Checker  {lr}[{w}4{lr}]{lc} Github Checker     {lr}[{w}7{lr}]{lc} Telegram checker
           {lr}[{w}2{lr}]{lc} Twitter Checker    {lr}[{w}5{lr}]{lc} Usr.gg Checker     {lr}[{w}8{lr}]{lc} Tellonym checker
           {lr}[{w}3{lr}]{lc} Facebook Checker   {lr}[{w}6{lr}]{lc} Pinterset Checker  {lr}[{w}9{lr}]{lc} TikTok checker

           {lr}[{w}0{lr}]{lc} MainMenu           {lr}[{w}99{lr}]{lc} About             {lr}[{w}X{lr}]{lc} Exit
        ''')
        choice = input(f"{lr}[{w}?{lr}]{lc} Enter choice : ")
        if choice == '0':home()
        elif choice == '99':about()
        elif choice == 'x' or choice == 'X':sys.exit(0)
        elif int(choice) in range(1,10):check(check_list[int(choice)-1])
        else :print(f'\n{lr}[{w}!{lr}]{lc} Wrong choice try agian');time.sleep(3);home()
    elif choice == '2':custom()
    elif choice == '99':about()
    elif choice == '0':sys.exit(0)
    else :print(f'{lr}[{w}!{lr}]{lc} Wrong choice try agian');home()



if __name__ == '__main__':
    home()
