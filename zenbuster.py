#!/usr/bin/env python3

             ##################################################
             #                 ☯ZenBuster.py                 #
             #  Multi-Platform Multithreaded URL Enumeration  #
             #       Author: Zach Griffin, aka: 0xTas         #
             #            Email: admin@0xTas.dev              #
             #       Github: https://github.com/0xTas         #
             #       Twitter: https://twitter.com/0xTas       #
             ##################################################

##############################################################################
#                      Copyright © 2022 Zach Griffin                         #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful, but     #
#    WITHOUT ANY WARRANTY; without even the implied warranty of              #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                    #
#    See the GNU General Public License for more details.                    #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program. If not, see <https://www.gnu.org/licenses/>    #
##############################################################################

__author__ = 0x546173
banner = """ 
      _-ooo-._     
    .OOOP   _ '.zg   _____          ____            _
   dOOOO   (_)  \   |__  /___ _ __ | __ ) _   _ ___| |_ ___ _ __
  OOOOOb         |    / // _ \ '_ \|  _ \| | | / __| __/ _ \ '__|
  OOOOOOOb       |   / /|  __/ | | | |_) | |_| \__ \ ||  __/ | 
  OOOOOOOOb      |  /____\___|_| |_|____/ \__,_|___/\__\___|_|v1.1
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
 |   _ _ '. '   ( \.-.| (_,_). '.     :_ _:  |  (_,_)___|| (_,_).' __v1.1         
 |  ( ' )  \\' (`. _` /|.---.  \  :    (_I_)  '  \   .---.|  |\ \  |  |        
 | (_{;}_) || (_ (_) _)\    `-'  |   (_(=)_)  \  `-'    /|  | \ `'   /        
 |  (_,_)  / \ /  . \ / \       /     (_I_)    \       / |  |  \    /         
 /_______.'   ``-'`-''   `-...-'      '---'     `'-..-'  ''-'   `'-'                                                                                                                        
"""
banner3 = """
          ,-,-.   ___       _                    
         / ( o \   _/ _ __ |_)    _ _|_ _  __     
         \ o ) /  /__(/_| ||_)|_|_>  |_(/_ |  v1.1  
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
    jgs''-ooo-''      `--------'`------'`--'  `--'v1.1       
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
'nested': False,
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

"""Any funcs that modify this global state object
are marked at the top of their scope with "global state".
Furthermore, any funcs that include side-effects are marked
at the top of their scope with the 'global' declaration."""


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
from sys import argv as args, path
from concurrent.futures import ThreadPoolExecutor

# Non-Standard-Lib Import
try:
    import requests
except ImportError:
    try:
        os.system('cls') if platform.system() == 'Windows' else os.system('clear')
        cont = input('\n ZenBuster relies on the Python module "requests" to function.'
            ' Would you like to install it now?  [Y/N]: ')

        if cont.lower() == 'y': 
            try:
                import subprocess
                subprocess.call(['python3','-m','pip','install','requests'])
                from site import getusersitepackages as user_site

                """Dynamically import packages that have been installed 
                at runtime by appending them to our path"""
                if user_site not in path:
                    path.append(user_site)
                import requests
                sleep(2)
            except KeyboardInterrupt:
                raise SystemExit(0)
            except Exception as err:
                print(f'{err}\n\n Could not import critical module "requests"!'
                    ' script will now exit..')
                raise SystemExit(1)
        else:
            print(f' Could not import critical module "requests",'
                ' script will now exit..')
            raise SystemExit(1)
        os.system('cls') if platform.system() == 'Windows' else os.system('clear')
    except Exception as err:
        print(f' {err}\n Could not import critical module "requests"!'
            ' Script will now exit..')
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
    cont = input('\n Termcolor module is not installed, '
        'would you like to install it now?  [Y/N]: ')

    if cont.lower() == 'y':
        try:
            import subprocess
            subprocess.call(['python3','-m','pip','install','termcolor'])

            # Solution from: 
            # https://stackoverflow.com/questions/56974185/import-runtime-installed-module-using-pip-in-python-3
            from site import getusersitepackages
            user_site = getusersitepackages()

            if user_site not in path:
                path.append(user_site)
            from termcolor import colored
            sleep(2)
        except Exception as err:
            print(f'{err}\n\n Could not import module Termcolor, '
                'script will not output color..')
            state['no_color'] = True
            sleep(4.20)
    else:
        print(f' Could not import module Termcolor, '
            'script will not output color..')
        state['no_color'] = True
        sleep(4.20)

# Windows terminal requires initialization via Colorama module to display color.
if platform.system() == 'Windows' and not state['no_color']:

    try:
        from colorama import init, deinit
    except ImportError:
        cont = input('\n Colorama module is not installed,'
            ' would you like to install it now?  [Y/N]: ')

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
                print(f'{err}\n\n Could not import module Colorama,'
                    ' script will not output color..')
                state['no_color'] = True
                sleep(4.20)
        else:
            print(f' Could not import module Colorama,'
                ' script will not output color..')
            state['no_color'] = True
            sleep(4.20)
os.system('cls') if platform.system() == 'Windows' else os.system('clear')


##########################
#     Util Functions     #
##########################
def die(code: int) -> None:
    if platform.system() == 'Windows' and not state['no_color']: deinit()
    raise SystemExit(code)


def width() -> int:
    return os.get_terminal_size()[0] - 15


def rngBanner() -> str:
    banners = [banner,banner2,banner3]
    return random.choice(banners)


def rngColor() -> str:
    colors = ['green','red','blue','cyan','yellow','magenta']
    return random.choice(colors)


def clearScreen() -> None:
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')


def zero_X(hexx: int) -> bool:
    try:
        hexxx = hex(hexx)[2:]
        hexxxx = hex(hexx)[:2].encode().hex()
        if (bytearray.fromhex(hexxxx).decode()
            +bytearray.fromhex(hexxx).decode()) == '0xTas': return True
        return False
    except:
        return False


def validateHost(hostname: str) -> bool:
    """Checks validity of given host, with support for both
    ipv4 and ipv6 formatting, plus auto SSL detection.
    Modifies "ssl" and "nested" state flags, 
    also "host", and "nested_dir" depending on given format."""
    global state, host, nested_dir
    print(' Validating Host...')
    try:
        parts = [e for e in hostname.split('/') if e != '']
        if hostname.startswith('https'): state['ssl'] = True
        if hostname.startswith('http'):
            hostname = parts[1]
            socket.gethostbyname(hostname)
            if len(parts) > 2 and state['directory_mode']:
                state['nested'] = True
                nested_dir = '/'+'/'.join(parts[2:])
                host = hostname
            else:
                host = hostname
        elif hostname.replace('.','').isnumeric():
            host = socket.gethostbyaddr(host)[0]
            if len(parts) > 1 and state['directory_mode']:
                state['nested'] = True
                nested_dir = '/'+'/'.join(parts[1:])
        else:
            hostname = parts[0]
            socket.gethostbyname(hostname)
            if len(parts) > 1 and state['directory_mode']:
                state['nested'] = True
                nested_dir = '/'+'/'.join(parts[1:])
                host = f'{hostname}'
            else:
                host = hostname
        clearScreen()
        return True
    except:
        try:
            if 'http' in parts[0]:
                hostname = parts[1]
            else:
                hostname = parts[0]
            int(f'0x{hostname.replace(":","")}',16)
            host = socket.gethostbyaddr(hostname)[0]
            if len(parts) >= 2 and state['directory_mode']:
                state['nested'] = True
                nested_dir = f'{"/"+"/".join(parts[2:]) if "http" in parts[0] else "/"+"/".join(parts[1:])}'
            clearScreen()
            return True
        except Exception as err:
            return False


def zenHelp() -> None:
    if state['no_color']:
        print('\n ZenBuster Command Usage: "./zenbuster.py [options]"')
        print('\n -h,             --help: Displays this help screen.')
        print('\n -d,             --dirs: Directory Enumeration Mode.')
        print('\n -s,             --ssl:  Forces Usage of HTTPS.')
        print('\n -u <URL/IP>,    --host: Host to Target for Scan.')
        print('\n -w <filepath>,  --wordlist: Path to Dictionary File.')
        print('\n -p <port>,      --port: '
            'Custom Port Option for Nonstandard Webservers.')
        print('\n -x <extensions>, --ext: '
            'Comma-Separated File Extensions (Dir mode only).')
        print('\n -o [filename],  --out-file: '
            'Log Results to File (Accepts Custom Name/Path).')
        print('\n -v,             --verbose: Verbose Terminal/Log Output.')
        print('\n -q,             --quiet: Minimal Terminal Output.')
        print('\n -nl,            --no-lolcat: '
            'Disables lolcat Output (Linux only).')
        print('\n -nc,            --no-color: Disables Colored Output.')
        print('\n -ic <codes>,    --ignore-codes: List of Status Codes to Exclude.')
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
        print(colored('\n -o',rngColor())
            +colored(' [filename]',rngColor())
            +','+colored('  --out-file',rngColor())
            +': Log Results to File (Accepts Custom Name/Path).')
        print(colored('\n -v',rngColor())
            +',             '
            +colored('--verbose',rngColor())
            +': Verbose Terminal/Log Output.')
        print(colored('\n -q',rngColor())
            +',             '
            +colored('--quiet',rngColor())
            +': Minimal Terminal Output')
        print(colored('\n -nl',rngColor())
            +',            '
            +colored('--no-lolcat',rngColor())
            +': Disables Rainbow Output (Linux only).')
        print(colored('\n -nc',rngColor())
            +',            '
            +colored('--no-color',rngColor())
            +': Disables Colored Output.')
        print(colored('\n -ic',rngColor())
            +colored(' <codes>',rngColor())
            +',    '+colored('--ignore-codes',rngColor())
            +': List of Status Codes to Exclude.')
    die(0)


def logResults(results: list, mode: str, host: str, filename: str) -> bool:
    # Logs contents of the enumerated results list to a file,
    # returns True if successful and False if exception occurs.
    log_time = datetime.now()
    try:
        with open(f'{filename}','a') as log_file:
            log_file.write(f'Enumerated '
                f'{"Directories" if mode == "Dirs" else "Subdomains"} for {host} '
                f'at {log_time.date()}'
                f' {str(log_time.hour).zfill(2)}:{str(log_time.minute).zfill(2)}:'
                f'{str(log_time.second).zfill(2)}:\n\n')
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


# Handler for KeyboardInterrupting threaded tasks.
exiting = threading.Event()
def signalHandler(signum,frame):
    exiting.set()
signal.signal(signal.SIGTERM, signalHandler)


########################################
#    Parse args for runtime options    #
########################################
port = None
extensions = []
nested_dir = None
log_filename = None
excluded_codes = []
for i in range(1,len(args)):

    if args[i].lower() == '-x' or args[i].lower() == '--ext':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            pass
        else:
            state['extension_bool'] = True
            extensions = args[i+1].split(',')
            try:
                for x in range(i+2,len(args)):
                    if args[x].startswith('-'):
                        break
                    elif not args[x].endswith(','):
                        extensions.append(args[x])
                        break
                    else:
                        extensions.append(args[x].replace(',',''))
            except:
                pass
            finally:
                extensions = [e for e in set(extensions) if e != '']
    elif args[i].lower() == '-s' or args[i].lower() == '--ssl':
        state['ssl'] = True
    elif args[i].lower() == '-d' or args[i].lower() == '--dirs':
        state['directory_mode'] = True
    elif args[i].lower() == '-h' or args[i].lower() == '--help':
        state['assistance'] = True
    elif args[i].lower() == '-u' or args[i].lower() == '--host':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            state['host_bool'] = False
        else:
            """Statement below fixes issue where specifying dir-mode flag *after* the host flag
            fails to trigger nested-dir logic because the global state hasn't been set
            properly before the call to validateHost()."""
            if '-d' in map(str.lower, args) or '--dirs' in map(str.lower, args):
                state['directory_mode'] = True
            host = args[i+1]
            state['host_bool'] = validateHost(host)
    elif args[i].lower() == '-p' or args[i].lower() == '--port':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            port = None
        else:
            try:
                port = args[i+1]
                if int(port) not in range(1,65536):
                    print(f' Invalid Port Number: {port}!')
                    print(' Falling back to defaults..')
                    port = None
                    sleep(2)
                    clearScreen()
            except ValueError:
                print(f' Provided port: {port} is not a valid integer!')
                print(' Falling back to defaults..')
                port = None
                sleep(2)
                clearScreen()
    elif args[i].lower() == '-v' or args[i].lower() == '--verbose':
        state['verbose'] = True
    elif args[i].lower() == '-dr' or args[i].lower() == '--dry-run':
        state['dry_run'] = True
    elif args[i].lower() == '-w' or args[i].lower() == '--wordlist':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            state['wordlist_bool'] = False
        else:
            wordlist = open(f'{args[i+1]}',encoding='latin-1').read()
            state['wordlist_bool'] = True
    elif args[i].lower() == '-nl' or args[i].lower() == '--no-lolcat':
        state['no_lolcat'] = True
    elif args[i].lower() == '-o' or args[i].lower() == '--out-file':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            pass
        else:
            log_filename = args[i+1]
        state['log_results'] = True
    elif args[i].lower() == '-q' or args[i].lower() == '--quiet':
        state['quiet'] = True
    elif args[i].lower() == '--debug':
        state['debug'] = True
    elif args[i].lower() == '-ic' or args[i].lower() == '--ignore-codes':
        if i == (len(args)-1) or args[i+1].startswith('-'):
            pass
        else:
            excluded_codes = args[i+1].split(',')
            try:
                for c in range(i+2,len(args)):
                    if args[c].startswith('-'):
                        break
                    elif not args[c].endswith(','):
                        excluded_codes.append(args[c])
                        break
                    else:
                        excluded_codes.append(args[c].replace(',',''))
            except:
                pass
            finally:
                # Remove NaN entries, duplicates, and empty strings.
                excluded_codes = [''.join(n for n in x if n.isdigit()) for x in excluded_codes]
                excluded_codes = [int(z) for z in set(excluded_codes) if z != '']


# Prevent misuse of extensions arg from breaking program logic further down..
if not state['directory_mode']:
    state['extension_bool'] == False
    extensions = []
if state['verbose']:
    state['log_results'] = True

################################
#    Defining Critical Data    #
################################
enumerated = []
tasks_complete = 0
lock = threading.Lock()
if log_filename == None: log_filename = 'zenResults.log'
ignored_codes = [c for c in range(500,600)]; ignored_codes.append(404)
if excluded_codes: ignored_codes.extend(excluded_codes)
ignored_codes = [c for c in set(ignored_codes) if c != '']
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

# Defaults to interactive mode to populate host/wordlist if not correctly supplied up-front.
# Skips this process altogether if dry_run or help-mode are called.
if not state['dry_run'] and not state['assistance']:

    if not state['wordlist_bool'] and not state['host_bool'] and not state['directory_mode']:
        try:
            if state['no_color']:
                print(' Default Mode for ZenBuster is Subdomain Enumeration.')
                answer = input('\n Would you like to switch this behavior to'
                    ' Directory Enumeration now?  [Y/N]: ')
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
            die(0)
        if answer.lower() == 'y': state['directory_mode'] = True
        clearScreen()


    if state['wordlist_bool']:
        try:
            enumerator_list = wordlist.splitlines()
            total_tasks = len(enumerator_list)
            if state['directory_mode'] and state['extension_bool']:
                if len(extensions) == 1:
                    total_tasks *= 2
                elif len(extensions) == 2:
                    total_tasks *= 3
                elif len(extensions) > 2:
                    total_tasks *= len(extensions)
        except:
            if state['no_color']:
                print(' [!] Please provide a valid wordlist file.')
                print(' Example: '
                    '"./subdomains.py -w /usr/share/wordlists/subdomains.txt".')
            else:
                print(colored(' [','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold'])
                    +colored(' Please provide a valid wordlist file. ','red')
                    +colored('[','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold']))
                print(' Example: '
                    '"./subdomains.py -w /usr/share/wordlists/subdomains.txt".')
            die(1)
    else:
        try:
            if state['no_color']:
                wordlist = open(input('\n Input Dictionary File: ')).read()
            else:
                wordlist = open(input(colored('\n Input Dictionary File: ',
                        'blue',attrs=['bold'])),encoding='latin-1').read()

            enumerator_list = wordlist.splitlines()
            total_tasks = len(enumerator_list)
            if state['directory_mode'] and state['extension_bool']:
                if len(extensions) == 1:
                    total_tasks *= 2
                elif len(extensions) == 2:
                    total_tasks *= 3
                elif len(extensions) > 2:
                    total_tasks *= len(extensions)
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
            die(0)
        except:
            if state['no_color']:
                print(' [!] Please provide a valid wordlist file. [!]')
                print(' Example: '
                    '"./subdomains.py -w /usr/share/wordlists/subdomains.txt"')
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
            die(1)


    if not state['host_bool']:

        if state['no_color']:
            try:
                host = input(' [?] Input Target Host: ')  

                if validateHost(host):
                    clearScreen()
                else:
                    print(f' Unable to parse hostname/URL: ({host}). '
                        'Host may be unreachable, or perhaps contains a typo?.')
                    die(1)
            except KeyboardInterrupt:
                print('\n [!] Caught KeyboardInterrupt. [!]\n Exiting..')
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
                    print(f' Unable to parse hostname/URL: ({host}). '
                        'Host may be unreachable, or perhaps a typo?.')
                    die(1)
            except KeyboardInterrupt:
                print(colored('\n [','yellow',attrs=['bold'])
                    +colored('!','red',attrs=['bold'])
                    +colored(']','yellow',attrs=['bold'])
                    +' Caught '
                    +colored('KeyboardInterrupt','yellow',attrs=['bold'])
                    +'. ')
                print(colored(' Exiting..','red'))
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
        funny_gato = subprocess.call(['which','lolcat'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

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
        print('-'*65)
    elif state['lolcat']:
        with open('zenBanner.txt','w') as banner_file:
            banner_file.write(rngBanner())

        os.system('lolcat zenBanner.txt; rm zenBanner.txt')
        print('\n')
        if state['assistance']:
            os.system('echo " Assistance Mode                      '
                'URL Enumerator By: 0xTas" | lolcat')
        elif state['directory_mode']:
            os.system('echo " Directory Mode                       '
                'URL Enumerator By: 0xTas" | lolcat')
        else:
            os.system('echo " Subdomain Mode                       '
                'URL Enumerator By: 0xTas" | lolcat')
        os.system('echo '
            '"-----------------------------------------------------------------"'
            ' | lolcat')
    else:
        # Initialize color output if on Windows
        if platform.system() == 'Windows' and not state['no_color']: init()
        print(colored(rngBanner(),rngColor()))

        if state['assistance']:
            print(colored(' Assistance Mode                        '
                'URL Enumerator By: ',rngColor())
                +colored('0','blue',attrs=['bold'])
                +colored('x','magenta',attrs=['bold'])
                +colored('T','green')
                +colored('a','cyan')
                +colored('s','red'))
        elif state['directory_mode']:
            print(colored(' Directory Mode                         '
                'URL Enumerator By: ',rngColor())
                +colored('0','blue',attrs=['bold'])
                +colored('x','magenta',attrs=['bold'])
                +colored('T','green')
                +colored('a','cyan')
                +colored('s','red'))
        else:
            print(colored(' Subdomain Mode                         '
                'URL Enumerator By: ',rngColor())
                +colored('0','blue',attrs=['bold'])
                +colored('x','magenta',attrs=['bold'])
                +colored('T','green')
                +colored('a','cyan')
                +colored('s','red'))
        print(colored('-'*65
            ,rngColor()))


###################################
#         Enum Functions          #
###################################
def enumSubdomains(enumerator:str) -> None:
    # Enumerates subdomain for target with enumerator from wordlist.
    # Appends valid subdomains to enumerated list. 
    global enumerated
    if exiting.is_set(): return
    verbose = state['verbose']

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
        r = requests.get(enum_item, headers=headers, stream=True, timeout=5)
    except:
        return
    else:
        if r.status_code in ignored_codes:
            return
        else:
            with lock:
                r_length = str(len(r.content))
                if r.history:
                    r.status_code = r.history[0].status_code
                if not state['quiet']:
                    endpoint = enum_item.split('//')[1]
                    if state['no_color']:
                        print(f' [+]Subdomain Found: {endpoint} '
                            f'{f"[{r_length}] " if verbose else ""}'
                            f'({r.status_code})'.ljust(width()))
                    else:
                        print(colored(' [','blue',attrs=['bold'])
                            +colored('+','green',attrs=['bold'])
                            +colored(']','blue',attrs=['bold'])
                            +'Subdomain Found: '
                            +colored(f'{endpoint}',
                                'cyan',attrs=['bold','underline'])
                            +f' {f"[{r_length}] " if verbose else ""}('
                            +colored(f'{r.status_code}','green',attrs=['bold'])
                            +')'.ljust(width()))
                enumerated.append(f'{enum_item} '
                    f'{f"[Len: {r_length}] " if verbose else ""}'
                    f'({r.status_code})')


def enumDirectories(enumerator:str) -> None:
    # Enumerates directory/file/resource for target with enumerator from wordlist (+extensions).
    # Appends valid endpoints to enumerated list.
    global enumerated
    if exiting.is_set(): return
    verbose = state['verbose']

    if state['ssl'] and not '#' in enumerator:
        if port != None:
            enum_item = f'https://{host}:{port}{nested_dir if state["nested"] else ""}/{enumerator}'
        else:
            enum_item = f'https://{host}{nested_dir if state["nested"] else ""}/{enumerator}'
    elif not state['ssl'] and not '#' in enumerator:
        if port != None:
            enum_item = f'http://{host}:{port}{nested_dir if state["nested"] else ""}/{enumerator}'
        else:
            enum_item = f'http://{host}{nested_dir if state["nested"] else ""}/{enumerator}'
    else:
        return

    try:
        r = requests.get(enum_item, headers=headers, stream=True, timeout=5)
    except:
        pass # Pass here instead of return so our extensions loop below still runs if applicable
    else:
        if r.status_code in ignored_codes:
            pass
        else:
            with lock:
                if not state['quiet']:
                    r_length = str(len(r.content))
                    enum_item_fmt =  enum_item.split("//")[1].replace(f"{host}","").replace(f":{port}","")
                    location_item = r.url.split("//")[1].replace(f"{host}","").replace(f":{port}","")
                    if state['no_color']:
                        if r.history:
                            print('[+]Endpoint Found: ',end='')
                            print(f'{enum_item_fmt} '
                                f'{f"[{r_length}] " if verbose else ""}'
                                f'({r.history[0].status_code}) ->',end='')
                            print(f' {location_item} '
                                f'{f"[{r_length}] " if verbose else ""}'
                                f'({r.status_code})'.ljust(width()))
                        else:
                            print(f' [+]Endpoint Found: {enum_item_fmt} '
                                f'{f"[{r_length}] " if verbose else ""}'
                                f'({r.status_code})'.ljust(width()))
                    else:
                        if r.history:
                            print(colored(' [','blue',attrs=['bold'])
                                +colored('+','green',attrs=['bold'])
                                +colored(']','blue',attrs=['bold'])
                                +'Endpoint Found: '
                                +colored(f'{enum_item_fmt}',
                                    'cyan',attrs=['bold','underline'])
                                +f' {f"[{r_length}] " if verbose else ""}('
                                +colored(f'{r.history[0].status_code}',
                                    rngColor(),attrs=['bold'])+')'
                                +colored(' -> ',rngColor())
                                +colored(f'{location_item}',
                                    'cyan',attrs=['bold','underline'])
                                +f' {f"[{r_length}] " if verbose else ""}('
                                +colored(f'{r.status_code}',
                                    'green',attrs=['bold'])+')'.ljust(width()))
                        else:
                            print(colored(' [','blue',attrs=['bold'])
                                +colored('+','green',attrs=['bold'])
                                +colored(']','blue',attrs=['bold'])
                                +'Endpoint Found: '
                                +colored(f'{enum_item_fmt}',
                                    'cyan',attrs=['bold','underline'])
                                +f' {f"[{r_length}] " if verbose else ""}('
                                +colored(f'{r.status_code}',
                                    'green',attrs=['bold'])+')'.ljust(width()))   
                if r.history:
                    enumerated.append(f'{enum_item} '
                        f'{f"[Len: {r_length}] " if verbose else ""}'
                        f'({r.history[0].status_code})'
                        f' -> {r.url} {f"[Len: {r_length}] " if verbose else ""}'
                        f'({r.status_code})')
                else:
                    enumerated.append(f'{enum_item} '
                        f'{f"[Len: {r_length}] " if verbose else ""}'
                        f'({r.status_code})')

    # Loops over enumerator with requested file extensions.
    if state['extension_bool']:
        for ext in extensions:
            if f'.{ext}' in enumerator: return # Avoid duplicate scans.
            try:
                r = requests.get(f'{enum_item}.{ext}', headers=headers,stream=True, timeout=5)
            except:
                return # Now we can return, there's nothing else to do.
            else:
                if r.status_code in ignored_codes:
                    return
                else:
                    with lock:
                        if not state['quiet']:
                            r_length = str(len(r.content))
                            enum_item_fmt =  enum_item.split("//")[1].replace(f"{host}","").replace(f":{port}","")
                            location_item = r.url.split("//")[1].replace(f"{host}","").replace(f":{port}","")
                            if state['no_color']:
                                if r.history:
                                    print('[+]Endpoint Found: ',end='')
                                    print(f'{enum_item_fmt}.{ext} '
                                        f'{f"[{r_length}] " if verbose else ""}'
                                        f'({r.history[0].status_code}) '
                                        f'-> {location_item} {f"[{r_length}] " if verbose else ""}'
                                        f'({r.status_code})'.ljust(width()))
                                else:
                                    print(f' [+]Endpoint Found: {enum_item_fmt}.{ext} '
                                        f'{f"[{r_length}] " if verbose else ""}'
                                        f'({r.status_code})'.ljust(width()))
                            else:
                                if r.history:
                                    print(colored(' [','blue',attrs=['bold'])
                                        +colored('+','green',attrs=['bold'])
                                        +colored(']','blue',attrs=['bold'])
                                        +'Endpoint Found: '
                                        +colored(f'{enum_item_fmt}.{ext}',
                                            'cyan',attrs=['bold','underline'])
                                        +f' {f"[{r_length}] " if verbose else ""}('
                                        +colored(f'{r.history[0].status_code}',
                                            rngColor(),attrs=['bold'])
                                        +')'+colored(' -> ',rngColor())
                                        +colored(f'{location_item}',
                                            'cyan',attrs=['bold','underline'])
                                        +f' {f"[{r_length}] " if verbose else ""}('
                                        +colored(f'{r.status_code}',
                                            'green',attrs=['bold'])
                                        +')'.ljust(width()))
                                else:
                                    print(colored(' [','blue',attrs=['bold'])
                                        +colored('+','green',attrs=['bold'])
                                        +colored(']','blue',attrs=['bold'])+
                                        'Endpoint Found: '
                                        +colored(f'{enum_item_fmt}.{ext}','cyan',
                                        attrs=['bold','underline'])
                                        +f' {f"[{r_length}] " if verbose else ""}('
                                        +colored(f'{r.status_code}','green',
                                        attrs=['bold'])+')'.ljust(width()))
                        if r.history:
                            enumerated.append(f'{enum_item}.{ext} '
                                f'{f"[Len: {r_length}] " if verbose else ""}'
                                f'({r.history[0].status_code}) '
                                f'-> {r.url} {f"[Len: {r_length}] " if verbose else ""}'
                                f'({r.status_code})')
                        else:
                            enumerated.append(f'{enum_item}.{ext} '
                                f'{f"[Len: {r_length}] " if verbose else ""}'
                                f'({r.status_code})')


#####################################
#        Progress Functions         #
#####################################
def taskProgress(future) -> None:
    # Tracks and reports progress for each task in the thread pool.
    # Prints numerical progress based on tasks_complete/total_tasks.
    # Modifies 'tasks_complete' for both local and global use.
    global tasks_complete
    if exiting.is_set():
        with lock:
            tasks_complete += (len(extensions)+1)
        return

    with lock:
        if state['no_color']:
            print(f' [~] Enumerating '
                f'{"Directory" if state["directory_mode"] else "Subdomain"} '
                f'{tasks_complete+1}/{total_tasks}.'
                f' Progress: ~{round((tasks_complete/total_tasks)*100,2)}% Done.',
                end='\r',flush=True)
        else:
            print(colored(' [',rngColor())+colored('~',rngColor())
                +colored(']',rngColor())
                +f' Enumerating {"Directory" if state["directory_mode"] else "Subdomain"} '
                +colored(f'{tasks_complete}','red')+'/'
                +colored(f'{total_tasks}','green')+'. Progress: '
                +colored('~','cyan')
                +f'{round((tasks_complete/total_tasks)*100,2)}'
                +colored('%','magenta')+' Done.',
                end='\r',flush=True) 
        tasks_complete += (len(extensions)+1)


def reportResults(time_started: datetime) -> None:
    # Calculates the time the scan took to complete,
    # calls the logReults function if desired,
    # prints the final results to stdout and exits the program.
    end_time = datetime.now()
    delta_time = end_time - time_started
    elapsed_time = round(delta_time.total_seconds())

    # Blacklist removes redundant/implied entries from results
    # Avoids creating log files with just the base URL that you already knew about.
    blacklist = [f'http://{host}', f'https://{host}', f'http://{host}/',
                f'https://{host}/', f'http://{host}:{port}',f'https://{host}:{port}',
                f'http://{host}:{port}/', f'https://{host}:{port}/', f'http://{host}{nested_dir}',
                f'https://{host}{nested_dir}', f'http://{host}{nested_dir}/', f'https://{host}{nested_dir}/',
                f'http://{host}:{port}{nested_dir}', f'https://{host}:{port}{nested_dir}',
                f'http://{host}:{port}{nested_dir}/', f'https://{host}:{port}{nested_dir}/']

    results = [] # Removing duplicates from enumerated list.
    [results.append(r) for r in enumerated if r not in results 
        and r.split()[0] not in blacklist]

    if state['log_results'] and results:
        print('\n')
        if logResults(results, f'{"Dirs" if state["directory_mode"] else "Subs"}',
            f'{host}', log_filename):
            print(f' {"(Verbose) " if state["verbose"] else ""}'
                f'Results successfully logged to "{log_filename}"')
        else:
            print(' [!] Could not log results to a file!')

    if state['no_color']:
        print(f' Finished Enumerating At: {end_time.date()} ',end='')
        print(f'{str(end_time.hour).zfill(2)}:{str(end_time.minute).zfill(2)}:'
            f'{str(end_time.second).zfill(2)}.')
        print(f' Found {len(results)} Valid Endpoints in '
            f'{round(elapsed_time/60,2)} Minutes:'.ljust(width()))
        print('\n')
        if results:
            for item in results:
                print(' '+item)
        else:
            print(' Nobody here but us chickens :(')
        die(0)
    else: # Colored Output
        print(f' Finished Enumerating At: {end_time.date()} ',end='')
        print(f'{str(end_time.hour).zfill(2)}:{str(end_time.minute).zfill(2)}:'
            f'{str(end_time.second).zfill(2)}.')
        print(f' Found {len(results)} Valid Endpoints in '
            f'{round(elapsed_time/60,2)} Minutes:'.ljust(width()))
        print()
        if results:
            for item in results:
                if state['directory_mode'] and ' (30' in item:
                    # Indexing-surgery to color just our response codes.
                    # There's probably a more readable way to write this ¯\_(ツ)_/¯
                    print(' '+item[ : item.index(' (30')+2]
                        +colored(item[item.index(' (30')+2 : item.index(' (30')+5],rngColor())
                        +item[item.index(' (30')+5 : len(item)-4]
                        +colored(item[len(item)-4 : len(item)-1],rngColor())
                        +item[len(item)-1])
                else:
                    print(' '+item[ : len(item)-4]
                        +colored(item[len(item)-4 : len(item)-1],rngColor())
                        +item[len(item)-1])
        else:
            print(' Nobody here but us chickens :(')
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
        enum_func = enumDirectories if state['directory_mode'] else enumSubdomains

        if state['no_color']:
            print('\n Enumerating '
                f'{"Directories" if state["directory_mode"] else "Subdomains"}'
                f' for {host+nested_dir if state["nested"] else host} '
                f'{" Port: "+port if port != None else ""}\n'
                f'{" Ignoring Status Codes: 5xx" if state["verbose"] else ""}'
                f'{","+ ",".join([c for c in map(str,ignored_codes) if not c.startswith("5")]) if state["verbose"] else ""}'
                '\n')
        else:
            print(colored('\n Enumerating',rngColor())
                +colored(f' {"Directories" if state["directory_mode"] else "Subdomains"}',
                    'green')
                +' for: '
                +colored(f'{host+nested_dir if state["nested"] else host}',
                rngColor())
                +colored(f'{" Port: "+port if port != None else ""}',rngColor())+'\n'
                +colored(f' {"Ignoring Status Codes: " if state["verbose"] else ""}', 'red')
                +f'{"5xx" if state["verbose"] else ""}'
                f'{","+ ",".join([c for c in map(str,ignored_codes) if not c.startswith("5")]) if state["verbose"] else ""}'
                '\n')

        with ThreadPoolExecutor() as executor:
            try:
                futures = [executor.submit(enum_func, enumerator) 
                    for enumerator in enumerator_list]

                for future in futures:
                    future.add_done_callback(taskProgress)
                while tasks_complete < total_tasks:
                    sleep(0.420)
            except KeyboardInterrupt:
                exiting.set()
                print('\n ')
                if state['no_color']:
                    print('\n [!] Caught KeyboardInterrupt. [!]'.ljust(width()))
                    print(' Preparing to Exit..'.ljust(width()))
                else:
                    print(colored('\n [','yellow',attrs=['bold'])
                        +colored('!','red',attrs=['bold'])
                        +colored(']','yellow',attrs=['bold'])+' Caught '
                        +colored('KeyboardInterrupt','yellow',attrs=['bold'])+'. '
                        +colored('[','yellow',attrs=['bold'])
                        +colored('!','red',attrs=['bold'])
                        +colored(']'.ljust(width()),'yellow',attrs=['bold']))
                    print(colored(' Preparing to Exit..'.ljust(width()),'red'))
                executor.shutdown(wait=False,cancel_futures=True)
                if state['no_color']:
                    print('\n [..] Cleaning up Running Threads '
                        'and Preparing Gathered Results..'.ljust(width()))
                else:
                    print(colored('\n [','red')+colored('.',rngColor())
                        +colored('.',rngColor())+colored(']','red')
                        +colored(' Cleaning up Running Threads '
                            'and Preparing Gathered Results..'.ljust(width()),rngColor()))  

        # After our threads are finished:
        reportResults(start_time)
    except KeyboardInterrupt:
        die(0)
    except Exception as err:
        if state['no_color']:
            print(f'\n [!] Unrecoverable Error [!]'.ljust(width()))
            raise err
        else:
            print(colored(' [','red')+colored('!','yellow')+colored(']','red')
                +colored(' Unrecoverable Error ','yellow')
                +colored(f'[','red')
                +colored('!','yellow')
                +colored(']'.ljust(width()),'red'))
            raise err


if zero_X(__author__):
    zenBuster()