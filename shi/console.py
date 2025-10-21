import colorama
import threading

from pystyle import *
from datetime import datetime
from colorama import *

lock = threading.Lock()

class Ascii:
    def __init__(self):
        self.banner = None

    def _ascii(self):
        return f'''
             _      _           _ _ _     
__  ____   _| |__  (_)___    __| (_) |__  
\ \/ /\ \ / / '_ \ | / __|  / _` | | '_ \ 
 >  <  \ V /| | | || \__ \ | (_| | | | | |
/_/\_\  \_/ |_| |_|/ |___/  \__,_|_|_| |_|
                 |__/                     
        
'''

    def ascii(self):
        asc = self._ascii()
        self.banner = Colorate.Horizontal(Colors.blue_to_purple, asc, 1)
        return self.banner
    def ascii2(self, text):
        asc = self._ascii() + '\t' + text
        self.banner = Colorate.Horizontal(Colors.blue_to_purple, asc, 1)
        return self.banner


class Logging:
    def inp(action, msg):
        mg = f'''\n┏━[xvhjsdih@{action}] [{msg}]
┃
┃
┗━[xvhjs2@xvhjsdih]──$  '''
        lock.acquire()
        inp = input(Colorate.Horizontal(Colors.red_to_purple, mg, 1))
        lock.release()
        return inp
    
    def inp2(msg):
        lock.acquire()
        inp = input(Colorate.Horizontal(Colors.red_to_purple, 'xvhjs2@xvhjsdih >', 1) + " " + Fore.BLUE + 'INPUT ' + Colorate.Horizontal(Colors.red_to_blue, msg, 1))
        lock.release()
        return inp
    
    def success(msg):
        now = datetime.now()
        d = now.strftime('%H:%M:%S')

        lock.acquire()
        print(Colorate.Horizontal(Colors.red_to_purple, f'{d} >', 1) + " " + Fore.GREEN + 'SUCCESS ' + Colorate.Horizontal(Colors.red_to_blue, msg, 1))

        lock.release()
        return msg
    
    def fail(msg):
        now = datetime.now()
        d = now.strftime('%H:%M:%S')

        lock.acquire()
        print(Colorate.Horizontal(Colors.red_to_purple, f'{d} >', 1) + " " + Fore.RED + 'FAILED ' + Colorate.Horizontal(Colors.red_to_blue, msg, 1))
        lock.release()
        return msg
        
    def info(msg):
        now = datetime.now()
        d = now.strftime('%H:%M:%S')
        
        lock.acquire()
        print(Colorate.Horizontal(Colors.red_to_purple, f'{d} >', 1) + " " + Fore.YELLOW + 'INFO ' + Colorate.Horizontal(Colors.red_to_blue, msg, 1))
        lock.release()
        return msg
    

    
class Options:
    def options(self):
        self.opt = '''
            [01] Delete all channels            [07] Give admin
            [02] Edit the server                [21] Select a different server
            [03] Create channels                [41] Use a different bot
            [04] Spam messages                  [67] Classic nuke
            [05] Webhook spam                   [100] Exit
            [06] Create roles

        '''
        self.opti = Colorate.Horizontal(Colors.blue_to_purple, self.opt, 1)
        return self.opti

