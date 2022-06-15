import os
import sys
import ctypes
import random, string
from time import sleep
from pystyle import Colors, Colorate
os.system("cls")

zxruss = "Zxrus Nitro Generator"
ctypes.windll.kernel32.SetConsoleTitleW(zxruss) #cmd tittle - titulo de la cmd
class ZxrusGen():

    print(Colorate.Vertical(Colors.blue_to_purple, """


▒███████▒▒██   ██▒ ██▀███   █    ██   ██████ 
▒ ▒ ▒ ▄▀░▒▒ █ █ ▒░▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ 
░ ▒ ▄▀▒░ ░░  █   ░▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   
  ▄▀▒   ░ ░ █ █ ▒ ▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒
▒███████▒▒██▒ ▒██▒░██▓ ▒██▒▒▒█████▓ ▒██████▒▒
░▒▒ ▓░▒░▒▒▒ ░ ░▓ ░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
░░▒ ▒ ░ ▒░░   ░▒ ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░
░ ░ ░ ░ ░ ░    ░    ░░   ░  ░░░ ░ ░ ░  ░  ░  
  ░ ░     ░    ░     ░        ░           ░  
░                                            

"""))
welcum = " ╔═════════════════════════════════════════╗\n ║  Welcome to Zxrus Nitro Generator       ║\n ║  Made by: https://github.com/zEncrypte  ║\n ╚═════════════════════════════════════════╝"
print(welcum)

def tortuga(_str):
    for letra in _str:
        sys.stdout.write(letra);sys.stdout.flush();sleep(0.03)

amount = int(input(f'\n{Colors.cyan} ¿How many nitro codes do you want to generate?: {Colors.white}'))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16)) #random strings - letras random
    f = open('codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'{Colors.light_blue} [UNCHECKED] {Colors.light_gray}║ {Colors.white}{code}')
    value += 1

else:
    tortuga(f'\n {Colors.light_green} The codes provided are {Colors.light_blue}UNCHECKED{Colors.light_green} therefore you should check them\n')
    sleep(2)
    input(f'\n {Colors.white} [{Colors.yellow}!{Colors.white}]{Colors.white} Press 3 times {Colors.red}Enter{Colors.white} to exit.{Colors.white}')
    input(f' {Colors.red} 1{Colors.white}')
    input(f' {Colors.red} 2{Colors.white}')
    os.system("cls") 
    exit() #salir - exit
