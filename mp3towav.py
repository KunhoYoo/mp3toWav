# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-

# Dependencies: ffmpeg
#               http://www.ffmpeg.org/

#kunho.yoo

import os
from pydub import AudioSegment
path = "./"

os.chdir(path)
audio_files = os.listdir()

for file in audio_files:

    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       mp3_sound.export("{0}.wav".format(name), format="wav")
