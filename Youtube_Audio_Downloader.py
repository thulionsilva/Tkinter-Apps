# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 11:34:36 2023

@author: thuli
"""

HEIGHT = 600
WIDTH = 800

import multiprocessing
import threading
import re
from pytube import Playlist
from pytube import YouTube
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog

def start_video_thread(URL,itag,Folder):
    p = threading.Thread(target = Download_Video,args = (URL,itag,Folder))
    p.start()
    return p

def Download_Video(URL,itag,Folder):

    video = URL
    try:
        audioStream = video.streams.get_by_itag(str(itag))
        audioStream.download(output_path=Folder)
    except:
      print("Age restricted video")
      
    return
             
class First_Screen:
    def __init__(self, master):
        self.URL_Type = tk.IntVar()
        self.quit = 0
        self.itag = tk.IntVar()
        self.progress_value = tk.IntVar()
        self.URL_Type.set(1)
        self.itag.set(140)
        #self.itag.set(251)
        self.progress_value.set(0)
        self.master = master
        self.size = tk.Canvas(self.master, height = HEIGHT, width = WIDTH)
        self.size.pack()
        s = ttk.Style()
        s.configure('TFrame', relief="groove", background="#F0F0F0")


        
        self.keys = ttk.Frame(self.master, style="TFrame")
        self.keys.place(relx = 0.05, rely = 0.05, relheight = 0.9, relwidth = 0.9)
        

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
        #s.configure('TButton', background="white")

        #s.configure('OUT.TLabel', font=('Calibri', 12))
        #s.configure('OUT.TLabel', anchor='center')
        #s.configure('Red.TLabel', foreground ='red')
        #s.configure('OUT.TLabel', background='#d4d4d4')
        #s.configure('OUT.TLabel', highlightbackground="red")
        s.configure('OUT.TFrame', borderwidth = 0 , relief='groove')

        '''--------------------- Label para a entrada de URL -----------------------------'''
        s.configure('W.TLabel', font=('Calibri', 12))
        s.configure('W.TLabel', background = "#F0F0F0")
        s.configure('W.TLabel', relief="flat")
        
        self.URL_Label= ttk.Label(self.keys, style="W.TLabel")
        self.URL_Label['text'] = "URL: "
        self.URL_Label.place(anchor = "w", relx = 0.05, rely=0.09, relheight = 0.09, relwidth = 0.55)

        '''----------------Caixa para a entrada para URL----------------'''
        
        s.configure('W.TEntry', font=('Calibri', 15))
        s.configure('W.TEntry', background = "#F0F0F0")
        self.URL = ttk.Entry(self.keys,style="W.TEntry")
        self.URL.place(anchor = "w", relx = 0.1, rely=0.09, relheight = 0.07, relwidth = 0.6)
        
        ''' ---------------------  Label para escolher playlist-video -------------------------'''
        self.video_playlist_selector_frame = ttk.LabelFrame(self.keys,style='TFrame',text="Playlist")
        self.video_playlist_selector_frame['text'] = "Select type "
        self.video_playlist_selector_frame.place(anchor = "nw", relx = 0.05, rely=0.2, relheight = 0.2, relwidth = 0.25)
        
        self.playlist_radio_button = ttk.Radiobutton(self.video_playlist_selector_frame,text="Playlist", value = 1, variable = self.URL_Type)
        self.playlist_radio_button.place(anchor = "nw", relx = 0.1, rely=0.15, relheight = 0.2, relwidth = 0.5)
        
        self.video_radio_button = ttk.Radiobutton(self.video_playlist_selector_frame,text="Single Video",value = 2, variable = self.URL_Type)
        self.video_radio_button.place(anchor = "nw", relx = 0.1, rely=0.5, relheight = 0.2, relwidth = 0.5)

        
        ''' ---------------------  Label para escolher qualidade -------------------------'''
        
        self.quality_selector = ttk.LabelFrame(self.keys, text="Quality",style='OUT.TFrame')
        #self.myLabelT = ttk.Label(self.keys, style = "TLabel", borderwidth=4)
        self.quality_selector.place(anchor = "nw", relx = 0.05, rely=0.42, relheight = 0.3, relwidth = 0.25)
        
        self.Audio_only_radio_button = ttk.Radiobutton(self.quality_selector,text="Audio Only", value = 140, variable = self.itag)
        self.Audio_only_radio_button.place(anchor = "nw", relx = 0.1, rely=0.15, relheight = 0.2, relwidth = 0.5)
        
        self.p1080_radio_button = ttk.Radiobutton(self.quality_selector,text="High Resolution", value = 137, variable = self.itag)
        self.p1080_radio_button.place(anchor = "nw", relx = 0.1, rely=0.3, relheight = 0.2, relwidth = 0.5)
        
        #self.p720_radio_button = ttk.Radiobutton(self.quality_selector,text="720p Video", value = 22, variable = self.itag)
        #self.p720_radio_button.place(anchor = "nw", relx = 0.1, rely=0.45, relheight = 0.2, relwidth = 0.5)

        #self.p480_radio_button = ttk.Radiobutton(self.quality_selector,text="480p Video", value = 4, variable = self.itag)
        #self.p480_radio_button.place(anchor = "nw", relx = 0.1, rely=0.6, relheight = 0.2, relwidth = 0.5)
        '''=========================================================================='''



        #self.Progress_info = ttk.LabelFrame(self.keys, text="Download Status",style='OUT.TFrame')
        #self.myLabelT = ttk.Label(self.keys, style = "TLabel", borderwidth=4)
        #self.Progress_info.place(anchor = "nw", relx = 0.37, rely=0.2, relheight = 0.52, relwidth = 0.6)
        
        self.Output_info = tk.Text(self.keys, state = "disabled",borderwidth=1,relief='sunken')
        self.Output_info.place(anchor="nw", relx = 0.32, rely = 0.215, relheight = 0.505, relwidth = 0.625)

        '''=========================================================================='''
        '''=========================================================================='''

        
        self.buttonEnter = ttk.Button(self.keys, text = "Enter", command = lambda: self.start_download())
        self.buttonEnter.place(anchor ="center", rely = 0.92, relx = 0.5, relwidth = 0.2, relheight = 0.1)
        
        self.buttonFolder = ttk.Button(self.keys, text = "Download folder", command = lambda: self.get_folder_adress())
        self.buttonFolder.place(anchor ="w", rely = 0.09, relx = 0.75, relwidth = 0.2, relheight = 0.08)

 
    def Download_Playlist(self):
        URL = self.URL.get()
        itag = self.itag.get()
        Folder = self.DOWNLOAD_DIR
        playlist = Playlist(URL)
    
        self.progress_value.set(0)
        self.download_count = 0
        self.Output_info.config(state="normal")
        self.Output_info.insert("end", "> Download started\n")
        self.Output_info.config(state="disabled")
        self.buttonEnter.config(state = "disabled")
        self.buttonFolder.config(state = "disabled")
       
        
        # this fixes the empty playlist.videos list
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        l = len(playlist)

        self.progress_bar = ttk.Progressbar(self.keys, maximum=l, variable = self.progress_value)
        self.progress_bar.place(anchor ="c", rely = 0.8, relx = 0.5, relwidth = 0.5, relheight = 0.05)
     
        # physically downloading the audio track
    
        for video in playlist.videos:
            if self.quit == 1:
                break
            try:
                self.download_count+=1
                self.progress_value.set(self.download_count)
                self.Output_info.config(state="normal")
                self.Output_info.insert("end", f"> {video.title} ({self.download_count}/{l})\n") 
                self.Output_info.config(state="disabled")
                #audioStream = video.streams.get_by_itag(str(itag))
                #audioStream = video.streams.get_highest_resolution() #Testando pegar video e não audio
                if itag == 140:
                    audioStream = video.streams.get_audio_only()
                if itag == 137:
                    audioStream = video.streams.get_highest_resolution()
                        
                audioStream.download(output_path=Folder)
            except:
              print("A error occurred")
             
        self.Output_info.config(state="normal")
        self.Output_info.insert("end", "> Download finished\n")
        self.Output_info.config(state="disabled")
        self.buttonEnter.config(state = "normal")
        self.buttonFolder.config(state = "normal")
        
        return

    def start_playlist_thread(self):
        p = threading.Thread(target = self.Download_Playlist)
        p.start()
        return p

    def start_download(self):
        self.p = self.start_playlist_thread()



    def call_download_video(self):
        self.download_count = 0
        self.download_count_previous = 0
        self.progress_value.set(0)
        self.Output_info.config(state="normal")
        self.Output_info.insert("end", "> Download started\n")
        self.Output_info.config(state="disabled")
        self.Download_Video()
        
    def Download_Video(self):
        URL = self.URL.get()
        self.playlist = Playlist(URL)
        self.playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        itag = self.itag.get()
        Folder = self.DOWNLOAD_DIR
        
        if self.download_count == self.download_count_previous:
            self.progress_bar = ttk.Progressbar(self.keys, maximum=len(self.playlist), variable = self.progress_value)
            self.progress_bar.place(anchor ="c", rely = 0.8, relx = 0.5, relwidth = 0.5, relheight = 0.05)
            self.video = self.playlist.videos[self.download_count]
            self.download_count+=1
            p = start_video_thread(self.video,itag,Folder)
            self.check_status(p)

        if self.download_count < len(self.playlist):
            self.master.after(500, self.Download_Video)
        
    def get_folder_adress(self):
        self.DOWNLOAD_DIR = tk.filedialog.askdirectory()
        self.Output_info.config(state="normal")
        self.Output_info.insert("end", f"> Folder path: {self.DOWNLOAD_DIR}\n")
        self.Output_info.config(state="disabled")
        
    def check_status(self,p):
        """ p is the multiprocessing.Process object """
        if p.is_alive(): # Then the process is still running
            self.buttonEnter.config(state = "disabled")
            self.buttonFolder.config(state = "disabled")
            self.master.after(500, lambda p=p: self.check_status(p)) # After 200 ms, it will check the status again.

        else:
            self.download_count_previous+=1
            self.progress_value.set(self.download_count_previous)
            l = len(self.playlist)
            self.Output_info.config(state="normal")
            self.Output_info.insert("end", f"> {self.video.title} ({self.download_count_previous}/{l})\n") 
            if self.download_count >= len(self.playlist):
                self.Output_info.insert("end", "> Download finished\n")
                self.buttonEnter.config(state = "normal")
                self.buttonFolder.config(state = "normal")
            
            self.Output_info.config(state="disabled")
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Youtube Video Download")
    clas = First_Screen(root)
    root.mainloop()
    clas.quit = 1
    





'''--------------------- Destroy window function -------------------------'''

'''-----------------------------------------------------------------------'''

