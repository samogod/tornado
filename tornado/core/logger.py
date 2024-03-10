# logging outputs

from datetime import datetime
from importlib.metadata import version
from colorama import Fore as clr, Style

now = datetime.now()
time_now = now.strftime("%d-%m-%Y %H:%M:%S")

cyan = clr.CYAN
green = '\033[92m'
yellow = '\033[93m'
purple = '\033[35m'
red = clr.RED
bright = Style.BRIGHT
blue = clr.BLUE
reset = Style.RESET_ALL
Datetime = ("[" + cyan + time_now + reset + "]")

banner = f"""
______      U  ___ u    ____       _   _         _        ____       U  ___ u 
|_ " _|      \/"_ \/ U |  _"\ u   | \ |"|    U  /"\  u   |  _"\       \/"_ \/ 
  | |        | | | |  \| |_) |/  <|  \| |>    \/ _ \/   /| | | |      | | | | 
 /| |\   .-,_| |_| |   |  _ <    U| |\  |u    / ___ \   U| |_| |\ .-,_| |_| | 
u |_|U    \_)-\___/    |_| \_\    |_| \_|    /_/   \_\   |____/ u  \_)-\___/  
_// \\_        \\      //   \\_   ||   \\,-.  \\    >>    |||_          \\    
(__) (__)      (__)    (__)  (__)  (_")  (_/  (__)  (__)  (__)_)        (__)   v{version('tornado')}

{green}\x1B[3manonymously reverse shell over tor network using hidden services without portforwarding\x1B[0m{reset}           
                                {reset}\x1B[3msamet-g / samogod\x1B[0m{reset} 
"""

def good(msg):
    print("[" + green + bright + 'SUCCESS' + reset + '] ' + msg)

def goodt(msg):
    print(Datetime +" [" + green + bright +'SUCCESS' + reset + '] '+msg)

def error(msg):
    print("[" + red + bright + 'ERR' + reset + '] ', msg)

def errort(msg):
    print(Datetime +" [" + red + bright +'ERR' + reset + '] ',msg)

def info(msg):
    print("[" + blue + 'INF' + reset + "] " + msg)

def input(msg):
    print("[" + purple + 'INPUT' + reset + "] " + msg)

def infot(msg):
    print(Datetime +" [" + blue + 'INF' + reset + "] "+msg)

def warn(msg):
    print("[" + yellow + 'WRN' + reset + "] " + msg)

def warnt(msg):
    print(Datetime +" [" + yellow + 'WRN' + reset + "] "+msg)
