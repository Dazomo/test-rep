import pyaudio
import wave
import os
import argparse
import cv2
import numpy as np
import pyautogui

bin_folder = f"C:/Users/{os.getlogin()}/bin"

parser = argparse.ArgumentParser(description="")
parser.add_argument('option', type=str, help="None")
args = parser.parse_args()

screen_width, screen_height = pyautogui.size()
resolution = (screen_width, screen_height)

def record_voice(duration=10):
    format = pyaudio.paInt16
    channels = 2
    rate = 44100
    chunk = 1024
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    frames = []
    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()
    file_name = f"RECORDED-{os.getlogin()}.wav"
    with wave.open(f"{bin_folder}/{file_name}", 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

def record_screen(duration=10):
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(f"{bin_folder}/SCREENVID-{os.getlogin()}.avi", fourcc, 20.0, resolution)
    end_time = pyautogui.time.time() + duration
    while pyautogui.time.time() < end_time:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

    # Libérer les ressources
    out.release()
    cv2.destroyAllWindows()

if args.option == 'voice':
    record_voice()
elif args.option == 'screen':
    record_screen()
