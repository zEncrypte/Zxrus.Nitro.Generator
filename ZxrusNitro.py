import os
import sys
import ctypes
import random, string
from time import sleep
from pystyle import Colors, Colorate
os.system("cls")

zxruss = "Zxrus Nitro Generator"
ctypes.windll.kernel32.SetConsoleTitleW(zxruss)
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

def sslooww(_str):
    for letter in _str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.03)

amount = int(input(f'\n{Colors.cyan} ¿Cuantos codigos de nitro deseas generar?: {Colors.white}'))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'{Colors.light_blue} [UNCHECKED] {Colors.light_gray}║ {Colors.white}{code}')
    value += 1

else:
    sslooww(f'\n {Colors.light_green} Los codigos entregados son {Colors.light_blue}UNCHECKED{Colors.light_green} por lo tanto no estan checkeados.\n')
    sleep(2)
    input(f'\n {Colors.white} [{Colors.yellow}!{Colors.white}]{Colors.white} Presiona 3 veces {Colors.red}Enter{Colors.white} para salir.{Colors.white}')
    input(f' {Colors.red} 1{Colors.white}')
    input(f' {Colors.red} 2{Colors.white}')
    os.system("cls")
    exit()
