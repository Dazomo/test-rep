# Version: 1.0

import pyaudio
import wave
import os

bin_folder = f"C:/Users/{os.getlogin()}/bin"

def record_voice(duration=15):
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

record_voice()
