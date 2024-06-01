# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:42:02 2024

@author: thuli
"""

import os
from PIL import Image

directory_string = "C:\\Users\\thuli\\OneDrive\\Área de Trabalho\WhatsApp\\Media\\WhatsApp Stickers\\GIF"
png_directory_string = "C:\\Users\\thuli\\OneDrive\\Área de Trabalho\WhatsApp\\Media\\WhatsApp Stickers\\GIF\\gif"
directory = os.fsencode(directory_string) #Conver to Bin
    
for file in os.listdir(directory):
    filename = os.fsdecode(file) #Convert to String
    if filename.endswith(".webp") or filename.endswith(".MP4"):
        
        #directory_string =  os.fsdecode(directory)
        filename_png = "{}.gif".format(filename.split(".")[0])     
        webp_path = os.path.join(directory_string, filename)
        
        path2 = os.path.join(directory, file)
        
        png_path = os.path.join(png_directory_string, filename_png)

        im = Image.open(webp_path)#.convert("RGB")
        im.info.pop('background', None)
        im.save(png_path,"gif",save_all=True)



    

#video = VideoFileClip(os.path.join("path","to","movie.mp4"))

#video.audio.write_audiofile(os.path.join("path", filename_mp3))