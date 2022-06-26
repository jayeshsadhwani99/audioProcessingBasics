from pydub import AudioSegment

audio = AudioSegment.from_wav("test.wav")

# Increase volume by 6 dB
audio = audio + 6

# Double the audio
audio = audio * 2

# Fade in
audio = audio.fade_in(2000)

audio.export("test_mp3.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("test_mp3.mp3")
print("Done importing mp3")