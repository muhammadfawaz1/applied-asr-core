import soundfile as sf
from pathlib import Path

audio_path= Path(__file__).resolve().parents[2]/"data"/"test.flac"
data,samplerate=sf.read(audio_path)

print (f"{data}and the sample rate is {samplerate}")