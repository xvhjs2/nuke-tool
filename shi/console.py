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
      ____     _____  ___  __      ___   ___  __ 
     6MXMMb\  6MMVMMb `MM 6MHb   6MMMMb  `MM 6MS 
    MD'    ` 6M'   `Mb MIM9 `Mb 8M'  `Hb  MM67 " 
    YM.      MM     MM MM'   MM     ,oMM  MM'    
     YMMMMb  MM     MM MM    MM ,6MMo'MM  MM     
         `Mb MM     MM MM    MM MM'   MM  MM     
    L    ,MM YM.   ,M9 MM    MM MM.  ,MM  MM     
    MYMMMM9   YMMMMM9 _MM_  _MM_`YMMMJ'Yb_MM_    
                                                
                                                     
'''

    def ascii(self):
        asc = self._ascii()
        self.banner = Colorate.Horizontal(Colors.blue_to_cyan, asc, 1)
        return self.banner
    
    def ascii2(self, text):
        asc = self._ascii() + '\t' + text
        self.banner = Colorate.Horizontal(Colors.blue_to_cyan, asc, 1)
        return self.banner


class Logging:
    def inp(action, msg):
        mg = f'''\n┏━[sonar@{action}] [{msg}]
┃
┃
┗━[sonar]──$  '''
        lock.acquire()
        inp = input(Colorate.Horizontal(Colors.cyan_to_blue, mg, 1))
        lock.release()
        return inp
    
    def inp2(msg):
        lock.acquire()
        inp = input(Colorate.Horizontal(Colors.cyan_to_blue, '[sonar]──$', 1) + " " + Fore.BLUE + 'INPUT ' + Colorate.Horizontal(Colors.red_to_blue, msg, 1))
        lock.release()
        return inp
    
    def success(msg):
        now = datetime.now()
        d = now.strftime('%H:%M:%S')

        lock.acquire()
        print(Colorate.Horizontal(Colors.cyan_to_blue, f'{d} >', 1) + " " + Fore.GREEN + 'SUCCESS ' + Colorate.Horizontal(Colors.red_to_blue, msg, 1))

        lock.release()
        return msg
    
    def fail(msg):
        now = datetime.now()
        d = now.strftime('%H:%M:%S')

        lock.acquire()
        print(Colorate.Horizontal(Colors.cyan_to_blue, f'{d} >', 1) + " " + Fore.RED + 'FAILED ' + Colorate.Horizontal(Colors.red_to_blue, msg, 1))
        lock.release()
        return msg
        
    def info(msg):
        now = datetime.now()
        d = now.strftime('%H:%M:%S')
        
        lock.acquire()
        print(Colorate.Horizontal(Colors.cyan_to_blue, f'{d} >', 1) + " " + Fore.YELLOW + 'INFO ' + Colorate.Horizontal(Colors.red_to_blue, msg, 1))
        lock.release()
        return msg
    

    
class Options:
    def options(self):
        self.opt = '''
            [01] Delete all channels            [11] DM everyone                    [21] Select a different server
            [02] Edit the server                [12] Time out everyone              [22] Rename bot
            [03] Create channels                [13] Disable community              [23] Change bot pfp
            [04] Spam messages                  [14] Mass nick                      [41] Use a different bot
            [05] Webhook spam                   [15] Unban user                     [61] Bypass anti nuke
            [06] Create roles                   [16] Unban all                      [67] Classic nuke
            [07] Give admin                     [17] Delete role                    [69] Custom nuke
            [08] Ban everyone                   [18] Delete roles                   [100] Exit
            [09] Kick everyone                  [19] Scrape members                              
            [10] Give everyone admin            [20] Delete emojis                 
        '''
        self.opti = Colorate.Horizontal(Colors.blue_to_purple, self.opt, 1)
        return self.opti


