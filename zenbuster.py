#!/usr/bin/env python3

##################################################
#                 ZenBuster.py                   #
#  Multi-Platform Multithreaded URL Enumeration  #
#       Author: Zach Griffin aka: 0xTas          #
#            Email: admin@0xTas.dev              #
#           https://github.com/0xTas             #
##################################################

__author__ = 0x546173
banner = """ 
      _-ooo-._     
    .OOOP   _ '.zg   _____          ____            _
   dOOOO   (_)  \   |__  /___ _ __ | __ ) _   _ ___| |_ ___ _ __
  OOOOOb         |    / // _ \ '_ \|  _ \| | | / __| __/ _ \ '__|
  OOOOOOOb       |   / /|  __/ | | | |_) | |_| \__ \ ||  __/ | 
  OOOOOOOOb      |  /____\___|_| |_|____/ \__,_|___/\__\___|_|v1.0
   OOO(_)OOb    /  
    YOOOOOY  _,'  
 jgs''-ooo-''      
 """
banner2 = """
   ____..--'    .-''-.  ,---.   .--.         _-ooo-,_          
  |        |  .'_ _   \ |    \  |  |       .OOOP _( )_`zg     
  |   .-'  ' / ( ` )   '|  ,  \ |  |      dOOOO (_ o _)\    
  |.-'.'   /. (_ o _)  ||  |\_ \|  |___, OOOOOb  (_,_)  |  
     /   _/ |  (_,_)___||  _( )_\  |___| OOOOOOOb       |  
   .'._( )_ '  \   .---.| (_ o _)  |     OOOO( )Ob      | 
 .'  (_'o._) \  `-'    /|  (_,_)\  |      O(_ o _)b    /  
 |    (_,_)|  \       / |  |    |  |       Y(_,_)Y  _,'    
 |_________|   `'-..-'  '--'    '--'     jgs''-ooo-''    
  _______     ___    _    .-'''-. ,---------.    .-''-.  .-------.            
 \  ____  \ .'   |  | |  / _     \\          \ .'_ _   \ |  _ _   \           
 | |    \ | |    :  | | (`' )/`--' `--.  ,---'/ ( ` )   '| ( ' )  |           
 | |____/ / :   '_  | |(_ o _).       |   \  . (_ o _)  ||(_ o _) /           
 |   _ _ '. '   ( \.-.| (_,_). '.     :_ _:  |  (_,_)___|| (_,_).' __v1.0         
 |  ( ' )  \\' (`. _` /|.---.  \  :    (_I_)  '  \   .---.|  |\ \  |  |        
 | (_{;}_) || (_ (_) _)\    `-'  |   (_(=)_)  \  `-'    /|  | \ `'   /        
 |  (_,_)  / \ /  . \ / \       /     (_I_)    \       / |  |  \    /         
 /_______.'   ``-'`-''   `-...-'      '---'     `'-..-'  ''-'   `'-'                                                                                                                        
"""
banner3 = """
          ,-,-.   ___       _                    
         / ( o \   _/ _ __ |_)    _ _|_ _  __     
         \ o ) /  /__(/_| ||_)|_|_>  |_(/_ |  v1.0  
       hjw`-'-'        
"""
spooktober_banner = """
 ('-. _ _-ooo-._         .-') _   ('-.       .-') _      
 ( OO).)OOOP  _ '.zg    (  OO) )_(  OO)     ( OO ) )     
  (_)dOOOO   (_)  \   ,(_)----.(,------.,--./ ,--,'      
    OOOOOb   .-')  |  |       | |  .---'|   \ |  |\      
    OOOOOOOb(OO )  |  '--.   /  |  |    |    \|  | )     
    OOOOOOOOb, '\  |  (_/   /  (|  '--. |  .     |/      
     OOO(_)OOb_)  /    /   /___ |  .--' |  |\    |       
      YOOOOOY  _,'    |        ||  `---.|  | \   |       
    jgs''-ooo-''      `--------'`------'`--'  `--'v1.0       
 .-. .-')                 .-')    .-') _     ('-.  _  .-')   
 \  ( OO )               ( OO ). (  OO) )  _(  OO)( \( -O )  
  ;-----.\  ,--. ,--.   (_)---\_)/     '._(,------.,------.  
  | .-.  |  |  | |  |   /    _ | |'--...__)|  .---'|   /`. ' 
  | '-' /_) |  | | .-') \  :` `. '--.  .--'|  |    |  /  | | 
  | .-. `.  |  |_|( OO ) '..`''.)   |  |  (|  '--. |  |_.' | 
  | |  \  | |  | | `-' /.-._)   \   |  |   |  .--' |  .  '.' 
  | '--'  /('  '-'(_.-' \       /   |  |   |  `---.|  |\  \  
  `------'   `-----'     `-----'    `--'   `------'`--' '--' 
"""
##########################
#     Logic Switches     #
##########################
state = {
'ssl': False,
'debug': False,
'quiet': False,
'lolcat': False,
'verbose': False,
'dry_run': False,
'no_color': False,
'host_bool': False,
'no_lolcat': False,
'assistance': False,
'log_results': False,
'wordlist_bool': False,
'extension_bool': False,
'directory_mode': False,
}

# Any funcs that modify this global state
# -are marked at the top of their scope with "global state".
# Furthermore, any funcs that include side-effects are marked
# -at the top of their scope with the 'global' declaration.


##########################
#        Imports         #
##########################
import os
import socket
import signal
import random
import platform
import threading
from time import sleep
from datetime import datetime
from urllib.parse import urlparse
from sys import argv as args, path
from concurrent.futures import ThreadPoolExecutor

# Non-Standard-Lib Import
try:
    import requests
except ImportError:
    try:
        os.system('cls') if platform.system() == 'Windows' else os.system('clear')
        cont = input('\n ZenBuster relies on the Python module "requests" to function. Would you like to install it now?  [Y/N]: ')

        if cont.lower() == 'y': 
            try:
                import subprocess
                subprocess.call(['python3','-m','pip','install','requests'])
                from site import getusersitepackages as user_site

                # Dynamically import packages that have been installed 
                # at runtime by appending them to our path
                if user_site not in path:
                    path.append(user_site)
                import requests
                sleep(2)
            except KeyboardInterrupt:
                raise SystemExit(0)
            except Exception as err:
                print(f'{err}\n\n Could not import critical module "requests"! script will now exit..')
                raise SystemExit(1)
        else:
            print(f' Could not import critical module "requests", script will now exit..')
            raise SystemExit(1)
        os.system('cls') if platform.system() == 'Windows' else os.system('clear')
    except Exception as err:
        print(f' {err}\n Could not import critical module "requests"! Script will now exit..')
        raise SystemExit(1)


##############################
#      Initialize Color      #
##############################
if '-nc' in args or '--no-color' in map(str.lower, args):
    state['no_color'] = True

os.system('cls') if platform.system() == 'Windows' else os.system('clear')
try:
    from termcolor import colored
except ImportError:
    cont = input('\n Termcolor module is not installed, would you like to install it now?  [Y/N]: ')

    if cont.lower() == 'y':
        try:
            import subprocess
            subprocess.call(['python3','-m','pip','install','termcolor'])

            # Solution from: https://stackoverflow.com/questions/56974185/import-runtime-installed-module-using-pip-in-python-3
            from site import getusersitepackages
            user_site = getusersitepackages()

            if user_site not in path:
                path.append(user_site)
            from termcolor import colored
            sleep(2)
        except Exception as err:
            print(f'{err}\n\n Could not import module Termcolor, script will not output color..')
            state['no_color'] = True
            sleep(4.20)
    else:
        print(f' Could not import module Termcolor, script will not output color..')
        state['no_color'] = True
        sleep(4.20)

# Windows terminal requires initialization via Colorama module to display color.
if platform.system() == 'Windows' and not state['no_color']:

    try:
        from colorama import init, deinit
    except ImportError:
        cont = input('\n Colorama module is not installed, would you like to install it now?  [Y/N]: ')

        if cont.lower() == 'y': 
            try:
                import subprocess
                subprocess.call(['python3','-m','pip','install','colorama'])
                from site import getusersitepackages

                user_site = getusersitepackages()
                # Dynamically import packages that have been installed 
                # by appending them to our path at runtime.
                if user_site not in path:  
                    path.append(user_site)
                from colorama import init, deinit
                sleep(2)
            except Exception as err:
                print(f'{err}\n\n Could not import module Colorama, script will not output color..')
                state['no_color'] = True
                sleep(4.20)
        else:
            print(f' Could not import module Colorama, script will not output color..')
            state['no_color'] = True
            sleep(4.20)
os.system('cls') if platform.system() == 'Windows' else os.system('clear')


##########################
#     Util Functions     #
##########################
def die(code: int) -> None:
    raise SystemExit(code)


def rngBanner() -> str:
    banners = [banner,banner2,banner3]
    return random.choice(banners)


def rngColor() -> str:
    colors = ['green','red','blue','cyan','yellow','magenta']
    return random.choice(colors)


def killColor() -> None:
    if platform.system() == 'Windows' and not state['no_color']: deinit()


def clearScreen() -> None:
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')


def zeroX(hexx: int) -> bool:
    try:
        hexxx = hex(hexx)[2:]
        hexxxx = hex(hexx)[:2].encode().hex()
        if (bytearray.fromhex(hexxxx).decode()+bytearray.fromhex(hexxx).decode()) == '0xTas': return True
        return False
    except:
        return False


def validateHost(hostname:str) -> bool:
    # Checks validity of given host, with support for both
    # ipv4 and ipv6 formatting, plus auto SSL detection.
    # Modifies "ssl" state flag, also "host", depending on given format.
    global state, host 
    print(' Validating Host...')
    try:
        if hostname.startswith('https'): state['ssl'] = True
        if hostname.startswith('http'):
            hostname = urlparse(hostname).netloc
            socket.gethostbyname(hostname)
            host = hostname
        elif hostname.replace('.','').isnumeric():
            host = socket.gethostbyaddr(host)[0]
        else:
            socket.gethostbyname(hostname)
        clearScreen()
        return True
    except:
        try:
            int(f'0x{hostname.replace(":","")}',16)
            host = socket.gethostbyaddr(host)[0]
            clearScreen()
            return True
        except Exception as err:
            print(f' Unable to parse hostname/URL: ({hostname}). Host may be unreachable, or perhaps a typo?.')
            return False


def zenHelp() -> None:
    if state['no_color']:
        print('\n ZenBuster Command Usage: "./zenbuster.py [options]"')
        print('\n -h,             --help: Displays this help screen.')
        print('\n -d,             --dirs: Directory Enumeration Mode.')
        print('\n -s,             --ssl:  Forces Usage of HTTPS.')
        print('\n -u <URL/IP>,    --host: Host to Target for Scan.')
        print('\n -w <filepath>,  --wordlist: Path to Dictionary File.')
        print('\n -p <port>,      --port: Custom Port Option for Nonstandard Webservers.')
        print('\n -x <extensions>, --ext: Comma-Separated File Extensions (Dir mode only).')
        print('\n -O [filename],  --out-file: Log Results to a File (Accepts Custom Name/Path).')
        print('\n -v,             --verbose: Verbose Terminal Output.')
        print('\n -Q,             --quiet: Minimal Terminal Output.')
        print('\n -nr,            --no-lolcat: Disables Lolcat Output (Linux only).')
        print('\n -nc,            --no-color: Disables Colored Output.')
        print('\n -D,             --debug: Raises any Exceptions with Detailed Tracebacks.')
    else:
        print(colored('\n Zen',rngColor(),attrs=['bold'])
            +colored('Buster',rngColor(),attrs=['bold'])
            +' Command Usage: "'
            +colored('./ZenBuster.py ',rngColor())
            +colored('[options]',rngColor())+'"')
        print(colored('\n -h',rngColor())+',             '
            +colored('--help',rngColor())
            +': Displays this Help Screen and Exits.')
        print(colored('\n -d',rngColor())+',             '
            +colored('--dirs',rngColor())
            +': Directory Enumeration Mode.')
        print(colored('\n -s',rngColor())+',             '
            +colored('--ssl',rngColor())
            +': Forces Usage of HTTPS.')
        print(colored('\n -u ',rngColor())
            +colored('<URL/IP>',rngColor())
            +',    '+colored('--host',rngColor())
            +': Host to Target for Scan.')
        print(colored('\n -w ',rngColor())
            +colored('<filepath>',rngColor())
            +','+colored('  --wordlist',rngColor())
            +': Path to Dictionary File.')
        print(colored('\n -p',rngColor())
            +colored(' <port>',rngColor())
            +',      '+colored('--port',rngColor())
            +': Custom Port Option for Nonstandard Webservers.')
        print(colored('\n -x ',rngColor())
            +colored('<extensions>',rngColor())
            +', '+colored('--ext',rngColor())
            +': Comma-Separated File Extensions (Dir mode only).')
        print(colored('\n -O',rngColor())
            +colored(' [filename]',rngColor())
            +','+colored('  --out-file',rngColor())
            +': Log Results to a File (Accepts Custom Name/Path).')
        print(colored('\n -v',rngColor())
            +',             '
            +colored('--verbose',rngColor())
            +': Verbose Terminal Output.')
        print(colored('\n -Q',rngColor())
            +',             '
            +colored('--quiet',rngColor())
            +': Minimal Terminal Output')
        print(colored('\n -nr',rngColor())
            +',            '
            +colored('--no-rainbow',rngColor())
            +': Disables Rainbow Output (Linux only).')
        print(colored('\n -nc',rngColor())
            +',            '
            +colored('--no-color',rngColor())
            +': Disables Colored Output.')
        print(colored('\n -D',rngColor())
            +',             '
            +colored('--debug',rngColor())
            +': Raises any Exceptions with Detailed Tracebacks.')
    die(0)


def logResults(results: list, mode: str, host: str, filename: str) -> bool:
    # Logs contents of the enumerated results list to a file,
    # returns True if successful and False if exception occurs.
    log_time = datetime.now()
    try:
        with open(f'{filename}','a') as log_file:
            if mode == 'Dirs':
                log_file.write(f'Enumerated Directories for {host} at {log_time.date()} {str(log_time.hour).zfill(2)}:{str(log_time.minute).zfill(2)}:{str(log_time.second).zfill(2)}:\n\n')
                for result in results:
                    log_file.write(f'{result}\n')
                log_file.write('\n')
            else:
                log_file.write(f'Enumerated Subdomains for {host} at {log_time.date()} {str(log_time.hour).zfill(2)}:{str(log_time.minute).zfill(2)}:{str(log_time.second).zfill(2)}:\n\n')
                for result in results:
                    log_file.write(f'{result}\n')
                log_file.write('\n')
        return True
    except Exception as err:
        if state['debug']:
            raise err
        else:
            print(err)
        return False


# Handler for KeyboardInterrupting queued tasks.
exiting = threading.Event()
def signalHandler(signum,frame):
    exiting.set()
signal.signal(signal.SIGTERM, signalHandler)


########################################
#    Parse args for runtime options    #
########################################
log_filename = None
for i in range(1,len(args)):

    if args[i] == '-x' or args[i].lower() == '--ext':
        state['extension_bool'] = True
        if i == (len(args)-1) or args[i+1].startswith('-'):
            extensions = []
        else:
            extensions = args[i+1].split(',')
    elif args[i] == '-s' or args[i].lower() == '--ssl':
        state['ssl'] = True
    elif args[i] == '-d' or args[i].lower() == '--dirs':
        state['directory_mode'] = True
    elif args[i] == '-h' or args[i].lower() == '--help':
        state['assistance'] = True
    elif args[i] == '-u' or args[i].lower() == '--host':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            state['host_bool'] = False
        else:
            host = args[i+1]
            state['host_bool'] = validateHost(host)
    elif args[i] == '-p' or args[i].lower() == '--port':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            port = None
        else:
            try:
                port = args[i+1]
                if int(port) not in range(1,65536):
                    print(f' Invalid Port Number: {port}! \nFalling back to defaults..')
                    port = None
                    sleep(2)
                    clearScreen()
            except ValueError:
                print(f' Provided port: {port} is not a valid integer!\n Falling back to defaults..')
                port = None
                sleep(2)
                clearScreen()
    elif args[i] == '-v' or args[i].lower() == '--verbose':
        state['verbose'] = True
    elif args[i] == '-dr' or args[i].lower() == '--dry-run':
        state['dry_run'] = True
    elif args[i] == '-w' or args[i].lower() == '--wordlist':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            state['wordlist_bool'] = False
        else:
            wordlist = open(f'{args[i+1]}',encoding='latin-1').read()
            state['wordlist_bool'] = True
    elif args[i] == '-nr' or args[i].lower() == '--no-rainbow':
        state['no_lolcat'] = True
    elif args[i] == '-O' or args[i].lower() == '--out-file':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            pass
        else:
            log_filename = args[i+1]
        state['log_results'] = True
    elif args[i] == '-Q' or args[i].lower() == '--quiet':
        state['quiet'] = True
    elif args[i] == '-D' or args[i].lower() == '--debug':
        state['debug'] = True


################################
#    Defining Critical Data    #
################################
port = None
enumerated = []
tasks_complete = 0
lock = threading.Lock()
if log_filename == None: log_filename = 'zenResults.log'
ignored_codes = [c for c in range(500,600)]; ignored_codes.append(404)
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

# Defaults to interactive mode to populate host/wordlist if not correctly supplied up-front.
# Skips this process altogether if dry_run or help-mode are called.
if not state['dry_run'] and not state['assistance']:

    if not state['wordlist_bool'] and not state['host_bool'] and not state['directory_mode']:
        try:
            if state['no_color']:
                print(' Default Mode for ZenBuster is Subdomain Enumeration.')
                answer = input('\n Would you like to switch this behavior to Directory Enumeration now?  [Y/N]: ')
            else:
                print(' Default Mode for '
                    +colored('Zen',rngColor(),attrs=['bold'])
                    +colored('Buster',rngColor(),attrs=['bold'])+' is '
                    +colored('Subdomain',rngColor())+' Enumeration.')

                answer = input(' Would you like to switch this behavior to '
                    +colored('Directory',rngColor())+' Enumeration now?  ['
                    +colored('Y','green')+'/'
                    +colored('N','red')+']: ')
        except KeyboardInterrupt:
            if state['no_color']:
                print('\n [!] Caught KeyboardInterrupt.\n Exiting..')
            else:
                print(colored('\n [','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold'])+' Caught '
                    +colored('KeyboardInterrupt','yellow',attrs=['bold'])+'. ')
                print(colored(' Exiting..','red'))
            killColor()
            die(0)
        if answer.lower() == 'y': state['directory_mode'] = True
        clearScreen()


    if state['wordlist_bool']:
        try:
            enumerator_list = wordlist.splitlines()
            list_length = len(enumerator_list)
            if state['directory_mode'] and state['extension_bool']:
                if len(extensions) == 1:
                    list_length *= 2
                elif len(extensions) > 1:
                    list_length *= len(extensions)
        except:
            if state['no_color']:
                print(' [!] Please provide a valid wordlist file.\n Example: "./subdomains.py -w /usr/share/wordlists/subdomains.txt".')
            else:
                print(colored(' [','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold'])
                    +colored(' Please provide a valid wordlist file. ','red')
                    +colored('[','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold']))
                print(' Example: "./subdomains.py -w /usr/share/wordlists/subdomains.txt".')
            killColor()
            die(1)
    else:
        try:
            if state['no_color']:
                wordlist = open(input('\n Input Dictionary File: ')).read()
            else:
                wordlist = open(input(colored('\n Input Dictionary File: ',
                        'blue',attrs=['bold'])),encoding='latin-1').read()

            enumerator_list = wordlist.splitlines()
            list_length = len(enumerator_list)
            if state['directory_mode'] and state['extension_bool']:
                if len(extensions) == 1:
                    list_length *= 2
                elif len(extensions) > 1:
                    list_length *= len(extensions)
            clearScreen()
        except KeyboardInterrupt:
            if state['no_color']:
                print('\n [!] Caught KeyboardInterrupt.\n Exiting..')
            else:
                print(colored('\n [','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold'])
                    +' Caught '
                    +colored('KeyboardInterrupt','yellow',attrs=['bold'])+'. ')
                print(colored(' Exiting..','red'))
            killColor()
            die(0)
        except:
            if state['no_color']:
                print(' [!] Please provide a valid wordlist file. [!]')
                print(' Example: "./subdomains.py -w /usr/share/wordlists/subdomains.txt"')
            else:
                print(colored(' [','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold'])
                    +colored(' Please provide a valid wordlist file. ','red')
                    +colored('[','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold']))
                print(colored(' Example: ','green')
                    +'"./subdomains.py -w /usr/share/wordlists/subdomains.txt".')
            killColor()
            die(1)


    if not state['host_bool']:

        if state['no_color']:
            try:
                host = input(' [?] Input Target Host: ')  

                if validateHost(host):
                    clearScreen()
                else:
                    print(f' Unable to parse hostname/URL: ({host}). Host may be unreachable, or perhaps contains a typo?.')
                    killColor()
                    die(1)
            except KeyboardInterrupt:
                print('\n [!] Caught KeyboardInterrupt. [!]\n Exiting..')
                killColor()
                die(0)
        else:
            try:
                host = input(colored('\n [','blue',attrs=['bold'])
                    +colored('?','green',attrs=['bold'])
                    +colored(']','blue',attrs=['bold'])+' '
                    +colored('Input ','green',attrs=['bold'])
                    +colored('Target','red',attrs=['underline'])
                    +colored(' Host: ','magenta',attrs=['bold']))

                if validateHost(host):
                    clearScreen()
                else:
                    print(f' Unable to parse hostname/URL: ({host}). Host may be unreachable, or perhaps a typo?.')
                    killColor()
                    die(1)
            except KeyboardInterrupt:
                print(colored('\n [','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold'])
                    +' Caught '
                    +colored('KeyboardInterrupt','yellow',attrs=['bold'])
                    +'. ')
                print(colored(' Exiting..','red'))
                killColor()
                die(0)


###############################
#        Print Banner         #
###############################
def printBanner() -> None:
    # Prints a banner based on configured color options.
    # Modifies "lolcat" state flag.
    global state
    if platform.system() == 'Linux':
        import subprocess
        funny_gato = subprocess.call(['which','lolcat'],stdout=subprocess.DEVNULL)

        if funny_gato == 0 and not state['no_lolcat']:
            state['lolcat'] = True

    if datetime.now().month == 10:
        banner2 = spooktober_banner

    if state['no_color']:
        print(rngBanner())

        if state['assistance']:
            print(' Assistance Mode                      URL Enumerator By: 0xTas')
        elif state['directory_mode']:
            print(' Directory Mode                       URL Enumerator By: 0xTas')
        else:
            print(' Subdomain Mode                       URL Enumerator By: 0xTas')
        print('-----------------------------------------------------------------')
    elif state['lolcat']:
        with open('zenBanner.txt','w') as banner_file:
            banner_file.write(rngBanner())

        os.system('lolcat zenBanner.txt; rm zenBanner.txt')
        print('\n')
        if state['assistance']:
            os.system('echo " Assistance Mode                      URL Enumerator By: 0xTas" | lolcat')
        elif state['directory_mode']:
            os.system('echo " Directory Mode                       URL Enumerator By: 0xTas" | lolcat')
        else:
            os.system('echo " Subdomain Mode                       URL Enumerator By: 0xTas" | lolcat')
        os.system('echo "-----------------------------------------------------------------" | lolcat')
    else:
        # Initialize color output if on Windows
        if platform.system() == 'Windows' and not state['no_color']: init()
        print(colored(rngBanner(),rngColor()))

        if state['assistance']:
            print(colored(' Assistance Mode                        URL Enumerator By: ',rngColor())
                +colored('0','blue',attrs=['bold'])
                +colored('x','magenta',attrs=['bold'])
                +colored('T','green')
                +colored('a','cyan')
                +colored('s','red'))
        elif state['directory_mode']:
            print(colored(' Directory Mode                         URL Enumerator By: ',rngColor())
                +colored('0','blue',attrs=['bold'])
                +colored('x','magenta',attrs=['bold'])
                +colored('T','green')
                +colored('a','cyan')
                +colored('s','red'))
        else:
            print(colored(' Subdomain Mode                         URL Enumerator By: ',rngColor())
                +colored('0','blue',attrs=['bold'])
                +colored('x','magenta',attrs=['bold'])
                +colored('T','green')
                +colored('a','cyan')
                +colored('s','red'))
        print(colored('-----------------------------------------------------------------',rngColor()))


###################################
#         Enum Functions          #
###################################
def enumSubdomains(enumerator:str) -> None:
    # Enumerates subdomain for target with enumerator from wordlist.
    # Appends valid subdomains to enumerated list. 
    global enumerated
    if exiting.is_set(): return

    if state['ssl']:
        if port != None:
            enum_item = f'https://{enumerator}.{host}:{port}'
        else:
            enum_item = f'https://{enumerator}.{host}'
    else:
        if port != None:
            enum_item = f'http://{enumerator}.{host}:{port}'
        else:
            enum_item = f'http://{enumerator}.{host}'

    try:
        if state['verbose']:
            with lock:
                if state['no_color']:
                    print(f' [~] Trying: {enum_item}                         '
                        ,end='\r',flush=True)
                else:
                    print(colored(' [',rngColor(),attrs=['bold'])
                        +colored('~',rngColor(),attrs=['bold'])
                        +colored(']',rngColor(),attrs=['bold'])
                        +f' Trying: {enum_item}                  ',
                        end='\r',flush=True)

        r = requests.get(enum_item, headers=headers, stream=True, timeout=5, allow_redirects=True)
    except:
        return
    else:
        if r.status_code in ignored_codes:
            return
        else:
            with lock:
                if r.history:
                    r.status_code = r.history[0].status_code
                if not state['quiet']:

                    if state['no_color']:
                        print(f' [+] Subdomain Found: {enum_item.split("//")[1]} | Status: ({r.status_code})           ')
                    else:
                        print(colored(' [','blue',attrs=['bold'])
                            +colored('+','green',attrs=['bold'])
                            +colored(']','blue',attrs=['bold'])
                            +' Subdomain Found: '
                            +colored(f'{enum_item.split("//")[1]}','cyan',attrs=['bold','underline'])
                            +' | Status: ('
                            +colored(f'{r.status_code}','green',attrs=['bold'])
                            +')           ')
                enumerated.append(f'{enum_item} | Status: ({r.status_code})')


def enumDirectories(enumerator:str) -> None:
    # Enumerates directory/file/resource for target with enumerator from wordlist (+extensions).
    # Appends valid endpoints to enumerated list.
    global enumerated
    if exiting.is_set(): return

    if state['ssl'] and not '#' in enumerator:
        if port != None:
            enum_item = f'https://{host}:{port}/{enumerator}'
        else:
            enum_item = f'https://{host}/{enumerator}'
    elif not state['ssl'] and not '#' in enumerator:
        if port != None:
            enum_item = f'http://{host}:{port}/{enumerator}'
        else:
            enum_item = f'http://{host}/{enumerator}'
    else:
        return

    try:
        if state['verbose']:
            with lock:
                if state['no_color']:
                    print(f' [~] Trying: {enum_item}                      ',
                        end='\r',flush=True)
                else:
                    print(colored(' [',rngColor(),attrs=['bold'])
                        +colored('~',rngColor(),attrs=['bold'])
                        +colored(']',rngColor(),attrs=['bold'])
                        +f' Trying: {enum_item}                 ',
                        end='\r',flush=True)

        r = requests.get(enum_item, headers=headers, stream=True, timeout=5, allow_redirects=True)
    except:
        pass # Pass here instead of return so our extensions loop below still runs if applicable
    else:
        if r.status_code in ignored_codes:
            pass
        else:
            with lock:
                if not state['quiet']:
                    if state['no_color']:
                        if r.history:
                            print('[+] Endpoint Found: ',end='')
                            print(f'{enum_item} ({r.history[0].status_code}) -> {r.history[-1].url} | Status: ({r.status_code}) ')
                        else:
                            print(f' [+] Endpoint Found: {enum_item} | Status: ({r.status_code})    ')
                    else:
                        if r.history:
                            print(colored(' [','blue',attrs=['bold'])
                                +colored('+','green',attrs=['bold'])
                                +colored(']','blue',attrs=['bold'])
                                +' Endpoint Found: '
                                +colored(f'{enum_item}','cyan',attrs=['bold','underline'])+' ('
                                +colored(f'{r.history[0].status_code}',rngColor(),attrs=['bold'])+')'
                                +colored(' -> ',rngColor())
                                +colored(f'{r.history[-1].url}','cyan',attrs=['bold','underline'])
                                +' | Status: ('
                                +colored(f'{r.status_code}','green',attrs=['bold'])+') ')
                        else:
                            print(colored(' [','blue',attrs=['bold'])
                                +colored('+','green',attrs=['bold'])
                                +colored(']','blue',attrs=['bold'])
                                +' Endpoint Found: '
                                +colored(f'{enum_item}','cyan',attrs=['bold','underline'])
                                +' | Status: ('
                                +colored(f'{r.status_code}','green',attrs=['bold'])+')         ')   
     
                if r.history:
                    enumerated.append(f'{enum_item} ({r.history[0].status_code}) -> {r.history[-1].url} | Status: ({r.status_code})')
                else:
                    enumerated.append(f'{enum_item} | Status: ({r.status_code})')

    # Loops over enumerator with requested file extensions.
    if state['extension_bool']:
        for ext in extensions:
            try:
                if state['verbose']:
                    with lock:
                        if state['no_color']:
                            print(f' [~] Trying: {enum_item}.{ext}          ',
                                end='\r',flush=True)
                        else:
                            print(colored(' [',rngColor(),attrs=['bold'])
                                +colored('~',rngColor(),attrs=['bold'])
                                +colored(']',rngColor(),attrs=['bold'])
                                +f' Trying: {enum_item}.{ext}               ',
                                end='\r',flush=True)

                r = requests.get(f'{enum_item}.{ext}', headers=headers,
                                    stream=True, timeout=5, allow_redirects=True)
            except:
                return # Now we can return, there's nothing else to do.
            else:
                if r.status_code in ignored_codes:
                    return
                else:
                    with lock:
                        if not state['quiet']:
                            if state['no_color']:
                                if r.history:
                                    print('[+] Endpoint Found: ',end='')
                                    print(f'{enum_item}.{ext} | Status: ({r.history[0].status_code}) -> {r.history[-1].url} | Status: ({r.status_code}) ')
                                else:
                                    print(f' [+] Endpoint Found: {enum_item}.{ext} | Status: ({r.status_code})        ')
                            else:
                                if r.history:
                                    print(colored(' [','blue',attrs=['bold'])
                                        +colored('+','green',attrs=['bold'])
                                        +colored(']','blue',attrs=['bold'])
                                        +' Endpoint Found: '
                                        +colored(f'{enum_item}.{ext}','cyan',attrs=['bold','underline'])+' ('
                                        +colored(f'{r.history[0].status_code}',rngColor(),attrs=['bold'])+')'
                                        +colored(' -> ',rngColor())
                                        +colored(f'{r.history[-1].url}','cyan',attrs=['bold','underline'])
                                        +' | Status: ('
                                        +colored(f'{r.status_code}','green',attrs=['bold'])+') ')
                                else:
                                    print(colored(' [','blue',attrs=['bold'])
                                        +colored('+','green',attrs=['bold'])
                                        +colored(']','blue',attrs=['bold'])+
                                        ' Endpoint Found: '
                                        +colored(f'{enum_item}.{ext}','cyan',
                                        attrs=['bold','underline'])+' | Status: ('
                                        +colored(f'{r.status_code}','green',
                                        attrs=['bold'])+')   ')

                        if r.history:
                            enumerated.append(f'{enum_item}.{ext} ({r.history[0].status_code}) -> {r.history[-1].url} | Status: ({r.status_code})')
                        else:
                            enumerated.append(f'{enum_item}.{ext} | Status: ({r.status_code})')


#####################################
#        Progress Functions         #
#####################################
def taskProgress(future) -> None:
    # Tracks and reports progress for each task in the thread pool.
    # Prints numerical progress if not verbose mode
    global tasks_complete
    if state['verbose'] or exiting.is_set():
        with lock:
            if state['directory_mode'] and state['extension_bool']:
                if len(extensions) == 1:
                    tasks_complete += 2
                else:
                    tasks_complete += len(extensions)
            else:
                tasks_complete += 1
        return

    elif not state['verbose']:
        with lock:
            if state['no_color']:
                if not state['directory_mode']:
                    print(f' [~] Enumerating Subdomain {tasks_complete+1}/{list_length}. Progress: ~{round((tasks_complete/list_length)*100,2)}% Done.     '
                            ,end='\r',flush=True)
                else:
                    print(f' [~] Enumerating Directory {tasks_complete+1}/{list_length}. Progress: ~{round((tasks_complete/list_length)*100,2)}% Done.     '
                            ,end='\r',flush=True)
            else:
                if not state['directory_mode']:
                    print(colored(' [',rngColor())+colored('~',rngColor())
                        +colored(']',rngColor())+' Enumerating Subdomain '
                        +colored(f'{tasks_complete}','red')+'/'
                        +colored(f'{list_length}','green')+'. Progress: '
                        +colored('~','cyan')
                        +f'{round((tasks_complete/list_length)*100,2)}'
                        +colored('%','magenta')+' Done.       ',
                        end='\r',flush=True) 
                else:
                    print(colored(' [',rngColor())+colored('~',rngColor())
                        +colored(']',rngColor())+' Enumerating Directory '
                        +colored(f'{tasks_complete}','red')+'/'
                        +colored(f'{list_length}','green')+'. Progress: '
                        +colored('~','cyan')
                        +f'{round((tasks_complete/list_length)*100,2)}'
                        +colored('%','magenta')+' Done.       ',
                        end='\r',flush=True)

            if state['directory_mode'] and state['extension_bool']:
                if len(extensions) == 1:
                    tasks_complete += 2
                else:
                    tasks_complete += (1*len(extensions))
            else:
                tasks_complete += 1


def reportResults(time_started: datetime) -> None:
    # Calculates the time the scan took to complete,
    # calls the logReults function if desired,
    # prints the final results to stdout and exits the program. 
    end_time = datetime.now()
    delta_time = end_time - time_started
    elapsed_time = round(delta_time.total_seconds())

    if state['log_results']:
        print('\n')
        if state['directory_mode']:
            if logResults(enumerated, 'Dirs',f'{host}', log_filename):
                print(f' Results successfully logged to "{log_filename}"')
            else:
                print(' [!] Could not log results to a file!')
        else:
            if logResults(enumerated, 'Subs',f'{host}', log_filename):
                print(f' Results successfully logged to "{log_filename}"')
            else:
                print(' [!] Could not log results to a file!')

    if state['no_color']:
        print('\n')
        print(f' Finished Enumerating At: {end_time.date()} ',end='')
        print(f'{str(end_time.hour).zfill(2)}:{str(end_time.minute).zfill(2)}:{str(end_time.second).zfill(2)}.')
        print(f' Found {len(enumerated)} Valid Endpoints in {round(elapsed_time/60,2)} Minutes:\n')
        if enumerated:
            for item in enumerated:
                print(' '+item)
        else:
            print(' Nobody here but us chickens :(')
        killColor()
        die(0)
    else: # Colored Output
        print('\n')
        print(f' Finished Enumerating At: {end_time.date()} ',end='')
        print(f'{str(end_time.hour).zfill(2)}:{str(end_time.minute).zfill(2)}:{str(end_time.second).zfill(2)}.')
        print(f' Found {len(enumerated)} Valid Endpoints in {round(elapsed_time/60,2)} Minutes:\n')
        if enumerated:
            for item in enumerated:
                if state['directory_mode'] and ' (30' in item:
                    print(' '+item[:item.index(' (30')+2]
                        +colored(item[item.index(' (30')+2:item.index(' (30')+5],rngColor())
                        +item[item.index(' (30')+5:len(item)-4]
                        +colored(item[len(item)-4:len(item)-1],rngColor())
                        +item[len(item)-1])
                else:
                    print(' '+item[:len(item)-4]
                        +colored(item[len(item)-4:len(item)-1],rngColor())
                        +item[len(item)-1])
        else:
            print(' Nobody here but us chickens :(')
        killColor()
        die(0)


###########################
#      Main Function      #
###########################
def zenBuster() -> None:
    # Populates the thread pool, and awaits completion of the tasks. 
    # Catches KeyboardInterrupt if desired, and calls func to display results.
    if not state['quiet']: printBanner()
    if state['assistance']: return zenHelp()
    if state['dry_run']: return die(0)

    try:
        start_time = datetime.now()
        if state['directory_mode']:

            if state['no_color']:
                print(f'\n Enumerating Directories for {host}\n')
            else:
                print(colored('\n Enumerating',rngColor())
                    +colored(' Directories','green')+' for: '
                    +colored(f'{host}',rngColor())+'\n')

            with ThreadPoolExecutor() as executor:
                try:
                    futures = [executor.submit(enumDirectories, enumerator) for enumerator in enumerator_list]
                    for future in futures:
                        future.add_done_callback(taskProgress)
                    while tasks_complete < list_length:
                        sleep(0.420)
                except KeyboardInterrupt:
                    exiting.set()
                    if state['no_color']:
                        print('\n [!] Caught KeyboardInterrupt. [!]          \n Preparing to Exit..                  ')
                    else:
                        print(colored('\n [','yellow',attrs=['bold'])
                            +colored('!','red',attrs=['bold'])
                            +colored(']','yellow',attrs=['bold'])+' Caught '
                            +colored('KeyboardInterrupt','yellow',attrs=['bold'])+'. '
                            +colored('[','yellow',attrs=['bold'])
                            +colored('!','red',attrs=['bold'])
                            +colored(']                      ','yellow',attrs=['bold']))
                        print(colored(' Preparing to Exit..                  ','red'))
                    executor.shutdown(wait=False,cancel_futures=True)
                    if state['no_color']:
                        print('\n [..] Cleaning up Running Threads and Preparing Gathered Results..                  \n')
                    else:
                        print(colored('\n [','red')+colored('.',rngColor())
                            +colored('.',rngColor())+colored(']','red')
                            +colored(' Cleaning up Running Threads and Preparing Gathered Results..             \n',rngColor()))  
        else:
            if state['no_color']:
                print(f'\n Enumerating Subdomains for {host}\n')
            else:
                print(colored('\n Enumerating',rngColor())
                    +colored(' Subdomains','green')+' for: '
                    +colored(f'{host}',rngColor())+'\n')
            with ThreadPoolExecutor() as executor:
                try:
                    futures = [executor.submit(enumSubdomains, enumerator) for enumerator in enumerator_list]
                    for future in futures:
                        future.add_done_callback(taskProgress)
                    while tasks_complete < list_length:
                        sleep(0.420)
                except KeyboardInterrupt:
                    exiting.set()
                    if state['no_color']:
                        print('\n [!] Caught KeyboardInterrupt. [!]          \n Preparing to Exit..                  ')
                    else:
                        print(colored('\n [','yellow',attrs=['bold'])
                            +colored('!','red',attrs=['bold'])
                            +colored(']','yellow',attrs=['bold'])+' Caught '
                            +colored('KeyboardInterrupt','yellow',attrs=['bold'])+'. '
                            +colored('[','yellow',attrs=['bold'])
                            +colored('!','red',attrs=['bold'])
                            +colored(']                      ','yellow',attrs=['bold']))
                        print(colored(' Preparing to Exit..                  ','red'))
                    executor.shutdown(wait=False,cancel_futures=True)
                    if state['no_color']:
                        print('\n [..] Cleaning up Running Threads and Preparing Gathered Results..                  \n')
                    else:
                        print(colored('\n [','red')+colored('.',rngColor())
                            +colored('.',rngColor())+colored(']','red')
                            +colored(' Cleaning up Running Threads and Preparing Gathered Results..             \n',rngColor()))

    # After our threads are finished:
        reportResults(start_time)

    except KeyboardInterrupt:
        killColor()
        die(0)
    except Exception as err:
        if state['no_color']:
            print(f'\n [!] Unrecoverable Error:\n {err}')
            if state['debug']: raise err
        else:
            print(colored(' [','red')+colored('!','yellow')+colored(']','red')
                +colored(' Unrecoverable Error:','yellow')
                +colored(f'\n {err}','red'))
            if state['debug']: raise err
        killColor()
        die(1)


if zeroX(__author__):
    zenBuster()