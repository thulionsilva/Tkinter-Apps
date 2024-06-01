# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:42:02 2024

@author: thuli
"""

import os
from moviepy.editor import *
from moviepy.editor import VideoFileClip

directory_string = "C:\\Users\\thuli\\Music\\Tayronne Cigano - 20 Melhores"
directory = os.fsencode(directory_string)
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".mp4") or filename.endswith(".MP4"):
        
        #directory_string =  os.fsdecode(directory)
        filename_mp3 = "{}.mp3".format(filename.split(".")[0])     
        video_path = os.path.join(directory_string, filename)
        path2 = os.path.join(directory, file)
        
        video = AudioFileClip(video_path)
        mp3_path = os.path.join(directory_string, filename_mp3)
        video.write_audiofile(mp3_path)

    

#video = VideoFileClip(os.path.join("path","to","movie.mp4"))

#video.audio.write_audiofile(os.path.join("path", filename_mp3))