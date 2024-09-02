# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:42:02 2024

@author: thuli
"""

import os
from moviepy.editor import *
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

HEIGHT = 500
WIDTH = 400

root = tk.Tk()
root.title("MP4 to MP3 converter")

def get_path(x):
    if x == 1:
        files_tuple = tk.filedialog.askopenfilenames()
        folder_path = None
    if x == 2:
        folder_path = tk.filedialog.askdirectory()
        files_tuple = None
    
def get_destiny_path():
        destiny_path = tk.filedialog.askdirectory()
        

path_type = tk.IntVar()
quit = 0
itag = tk.IntVar()
progress_value = tk.IntVar()
path_type.set(1)
itag.set(140)
progress_value.set(0)
size = tk.Canvas(root, height = HEIGHT, width = WIDTH)
size.pack()
s = ttk.Style()
s.configure('TFrame', relief="groove", background="#F0F0F0")


        
keys = ttk.Frame(root, style="TFrame")
keys.place(relx = 0.05, rely = 0.05, relheight = 0.9, relwidth = 0.9)
        

s.configure('NAME.TLabel',  font=('Calibri', 12))
        #s.configure('Red.TLabel', foreground ='red')
       # s.configure('NAME.TLabel', anchor=tk.CENTER)
s.configure('NAME.TLabel', background='#E5E5E5')
s.configure('NAME.TLabel', anchor='center')
s.configure('NAME.TLabel', borderwidth = 0 , relief='groove')
        
s.configure('TLabelframe',  font=('Calibri', 12))
        #s.configure('Red.TLabel', foreground ='red')
       # s.configure('NAME.TLabel', anchor=tk.CENTER)
s.configure('Labelframe', bordercolor='#black')
s.configure('TLabelframe', anchor='center')
s.configure('NAME.TLabelframe', relief='groove')
        
s.configure('TButton', font=('Calibri', 12))
s.configure('TButton', foreground="blue")

s.configure('OUT.TFrame', borderwidth = 0 , relief='groove')

'''--------------------- Label para a entrada de URL -----------------------------'''
s.configure('W.TLabel', font=('Calibri', 12))
s.configure('W.TLabel', background = "#F0F0F0")
s.configure('W.TLabel', relief="flat")

# URL_Label= ttk.Label(keys, style="W.TLabel")
# URL_Label['text'] = "URL: "
# URL_Label.place(anchor = "w", relx = 0.05, rely=0.09, relheight = 0.09, relwidth = 0.55)

'''----------------Caixa para a entrada para URL----------------'''

""" s.configure('W.TEntry', font=('Calibri', 15))
s.configure('W.TEntry', background = "#F0F0F0")
URL = ttk.Entry(keys,style="W.TEntry")
URL.place(anchor = "w", relx = 0.1, rely=0.09, relheight = 0.07, relwidth = 0.6) """

''' ---------------------  Label para escolher caminho de arquivos MP4 -------------------------'''
files_folder_selector_frame = ttk.LabelFrame(keys,style='TFrame',text="Playlist")
files_folder_selector_frame['text'] = "files or folder"
files_folder_selector_frame.place(anchor = "n", relx = 0.5, rely=0.05, relheight = 0.15, relwidth = 0.9)

""" files_radio_button = ttk.Radiobutton(files_folder_selector_frame,text="MP4 files", value = 1, variable = path_type)
files_radio_button.place(anchor = "nw", relx = 0.1, rely=0.15, relheight = 0.2, relwidth = 0.5)

folder_radio_button = ttk.Radiobutton(files_folder_selector_frame,text="MP4 folder",value = 2, variable = path_type)
folder_radio_button.place(anchor = "nw", relx = 0.1, rely=0.5, relheight = 0.2, relwidth = 0.5) """

MP4_file_Button = ttk.Button(files_folder_selector_frame, text = "MP4 files", command = lambda x=1: get_path(x))
MP4_file_Button.place(anchor ="center", rely = 0.5, relx = 0.25, relwidth = 0.3, relheight = 0.8)

MP4_folder_Button = ttk.Button(files_folder_selector_frame, text = "MP4 folder", command = lambda x=2: get_path(x))
MP4_folder_Button.place(anchor ="center", rely = 0.5, relx = 0.75, relwidth = 0.3, relheight = 0.8)

MP3_folder_Button = ttk.Button(keys, text = "MP3 destiny", command = lambda : get_destiny_path())
MP3_folder_Button.place(anchor ="center", rely = 0.3, relx = 0.5, relwidth = 0.3, relheight = 0.1)

''' ---------------------  Label para escolher qualidade -------------------------'''



#p720_radio_button = ttk.Radiobutton(quality_selector,text="720p Video", value = 22, variable = itag)
#p720_radio_button.place(anchor = "nw", relx = 0.1, rely=0.45, relheight = 0.2, relwidth = 0.5)

#p480_radio_button = ttk.Radiobutton(quality_selector,text="480p Video", value = 4, variable = itag)
#p480_radio_button.place(anchor = "nw", relx = 0.1, rely=0.6, relheight = 0.2, relwidth = 0.5)
'''=========================================================================='''



#Progress_info = ttk.LabelFrame(keys, text="Download Status",style='OUT.TFrame')
#myLabelT = ttk.Label(keys, style = "TLabel", borderwidth=4)
#Progress_info.place(anchor = "nw", relx = 0.37, rely=0.2, relheight = 0.52, relwidth = 0.6)

Output_info = tk.Text(keys, state = "disabled",borderwidth=1,relief='sunken')
Output_info.place(anchor="n", relx = 0.5, rely = 0.45, relheight = 0.5, relwidth = 0.9)

'''=========================================================================='''
'''=========================================================================='''


#buttonEnter = ttk.Button(keys, text = "Enter", command = lambda: start_download())
#buttonEnter.place(anchor ="center", rely = 0.92, relx = 0.5, relwidth = 0.2, relheight = 0.1)

#buttonFolder = ttk.Button(keys, text = "Download folder", command = lambda: get_folder_adress())
#buttonFolder.place(anchor ="w", rely = 0.09, relx = 0.75, relwidth = 0.2, relheight = 0.08)







'''==============================================================================================================='''
def convert():
    directory_string = "C:\\Users\\thuli\\Music\\Mano Walter - Maceió"
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


if __name__ == "__main__":
    convert()
    #root.mainloop()

#video = VideoFileClip(os.path.join("path","to","movie.mp4"))

#video.audio.write_audiofile(os.path.join("path", filename_mp3))
