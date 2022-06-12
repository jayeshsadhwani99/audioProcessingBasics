import wave

# Audio Signal parameters
# - number of channels
# - sample width
# - frame rate/sample rate
# - number of frames
# - values of each frame

obj = wave.open("test.wav", "rb")

obj_channels = obj.getnchannels()
obj_width = obj.getsampwidth()
obj_frame_rate = obj.getframerate()

print("Number of channels: ", obj_channels)
print("Sample width: ", obj_width)
print("Frame rate: ", obj_frame_rate)
print("Number of frames: ", obj.getnframes())
print("All parameters", obj.getparams())

time_audio = obj.getnframes() / obj.getframerate()
print("Time of audio", time_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))

# These are 4 times as that of number of frames,
# Cause we have 2 channels and the sample width is
# 2 bytes
print("Length of frames: ", len(frames))

# Close the file Object
obj.close()

obj_new = wave.open("test_new.wav", "wb")

obj_new.setnchannels(obj_channels)
obj_new.setsampwidth(obj_width)
obj_new.setframerate(obj_frame_rate)

obj_new.writeframes(frames)

obj_new.close()