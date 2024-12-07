import pyautogui
import argparse
import os

bin_folder = f"C:/Users/{os.getlogin()}/bin"

parser = argparse.ArgumentParser(description="")
parser.add_argument('option', type=str, help="None")
args = parser.parse_args()

if args.option == 'screenshot':
    screenshot = pyautogui.screenshot()
    filename = f'SCREENSHOT-{os.getlogin()}.png'
    screenshot.save(f'{bin_folder}/{filename}')
elif args.option == 'webcame':
    pass
