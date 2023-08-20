from moviepy.editor import *
import os 



def convert_to_mp3(filename):
    if len(filename.split('.')) == 2:
        name, type = filename.split('.')
        if type == "mp4":
            video = VideoFileClip(f"{name}.{type}")
            video.audio.write_audiofile(f"{name}.mp3")
os.chdir('../../Desktop/videos')
files = os.listdir()
for f in files:
    convert_to_mp3(f)
