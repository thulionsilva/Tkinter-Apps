# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:01:14 2023

@author: thuli
"""


HEIGHT = 500
WIDTH = 400


import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
from tkinter import ttk


def peak_finder(Series):
        peak_1 = Series[0]
        time_1 = 0
        
        peak_2 = 0
        time_2 = 0
        
        diferenca1 = -1
        
        for i in range(Series.size-2):
            if abs(peak_1 - Series[i]) > diferenca1:
                diferenca1  = abs(peak_1 - Series[i])
            
            else:
                peak_1 = Series[i-1]
                time_1 = i-1
                diferenca1 = -1
                peak_2 = peak_1
                
                while i < (Series.size-2):
                    if abs(peak_2 - Series[i]) > diferenca1:
                        diferenca1  = abs(peak_2 - Series[i])
                    else:
                        peak_2 = Series[i-1]
                        time_2 = i-1
                        break
                    i+=1
                break
        
        return peak_1, time_1, peak_2, time_2

# class First_Screen:
#     def __init__(self, master):
#         self.master = master
#         self.size = tk.Canvas(self.master, height = HEIGHT, width = WIDTH)
#         self.size.pack()
#         self.frame = tk.Frame(self.master, bg = "#F0F0F0",highlightbackground="grey", highlightthickness=1)

#         self.frame.place(relx = 0.05, rely = 0.05, relheight = 0.9, relwidth = 0.9)
        
#         self.substance = ttk.Label(self.frame, bg = "#bdbdbd", font = 20, highlightbackground="grey", highlightthickness=1)
#         self.substance['text'] = "Enter substance molecular formula"
#         self.substance.place(anchor = "n", relx = 0.5, rely=0.01, relheight = 0.1, relwidth = 0.9)

#         self.substance_entry_box = ttk.Entry(self.frame, bg = "#bdbdbd", font = 40)
#         self.substance_entry_box.place(anchor = "n", relx = 0.5, rely=0.2, relheight = 0.1, relwidth = 0.25)
        
#         self.Screen1_buttonEnter = ttk.Button(self.frame, text = "Enter", font = 20, command = lambda: self.new_window())
#         self.Screen1_buttonEnter.place(anchor ="n", rely = 0.9, relx = 0.1, relwidth = 0.2, relheight = 0.1)

#     def new_window(self):
#         self.newWindow = ttk.Toplevel(self.master)
#         self.size = ttk.Canvas(self.newWindow, height = HEIGHT, width = WIDTH)
#         self.size.pack()
#         self.app = Second_Screen(self.newWindow,self.substance_entry_box.get())


class Second_Screen:
    def __init__(self, master):
        self.master = master
        self.size = tk.Canvas(self.master, height = HEIGHT, width = WIDTH)
        self.size.pack()
        s = ttk.Style()
        s.configure('TFrame', relief="groove", background="#F0F0F0")
        
        self.keys = ttk.Frame(self.master, style="TFrame")
        self.keys.place(relx = 0.05, rely = 0.05, relheight = 0.9, relwidth = 0.9)
        
        mover = 1.2
        space = 0.12
        
        
        ''' ---------------------  Label onde os dados serão exibidos -------------------------'''
        #Label para o período 
        Label_Output_X = 0.7
        
        Font_tuple = ("Calibri",15)
        

        s.configure('OUT.TLabel', font=('Calibri', 12))
        s.configure('OUT.TLabel', anchor='center')
        #s.configure('Red.TLabel', foreground ='red')
        s.configure('OUT.TLabel', background='#d4d4d4')
        s.configure('OUT.TLabel', highlightbackground="red")
        s.configure('OUT.TLabel', borderwidth = 0 , relief='groove')
        
        self.myLabelT = ttk.Label(self.keys, anchor="center", style="OUT.TLabel")
        #self.myLabelT = ttk.Label(self.keys, style = "TLabel", borderwidth=4)
        self.myLabelT.place(anchor = "n", relx = Label_Output_X, rely=space*2*mover, relheight = 0.1, relwidth = 0.3)
        
        #Label para a frequência
        self.myLabelF =ttk.Label(self.keys, anchor="center", style="OUT.TLabel")
        self.myLabelF.place(anchor = "n", relx = Label_Output_X, rely=space*3*mover, relheight = 0.1, relwidth = 0.3)
        
        #Label para o ganho
        self.myLabelG = ttk.Label(self.keys, anchor="center", style="OUT.TLabel")
        self.myLabelG.place(anchor = "n", relx = Label_Output_X, rely=space*4*mover, relheight = 0.1, relwidth = 0.3)
        
        #Label para a Fase
        self.myLabelP = ttk.Label(self.keys, anchor="center", style="OUT.TLabel")
        self.myLabelP.place(anchor = "n", relx = Label_Output_X, rely=space*5*mover, relheight = 0.1, relwidth = 0.3)
        



        '''=========================================================================='''


        '''--------------------- Label para a entrada de dados -----------------------------'''
        s.configure('W.TLabel', font=('Calibri', 12))
        s.configure('W.TLabel', background = "#F0F0F0")
        s.configure('W.TLabel', relief="flat")
        
        #self.Sample_time = ttk.Label(self.keys, bg = "#F0F0F0", font = Font_tuple, highlightbackground="grey", highlightthickness=0)
        self.Sample_time = ttk.Label(self.keys, style="W.TLabel")

        self.Sample_time['text'] = "Tempo amostra (ms): "
        self.Sample_time.place(anchor = "w", relx = 0.05, rely=0.05, relheight = 0.09, relwidth = 0.55)

        '''Caixa para a entrada do tempo de amostra dos dados '''
        
        s.configure('W.TEntry', font=('Calibri', 15))
        s.configure('W.TEntry', background = "#F0F0F0")
        self.Sample_time_entry_box = ttk.Entry(self.keys,style="W.TEntry")
        self.Sample_time_entry_box.place(anchor = "w", relx = 0.6, rely=0.05, relheight = 0.07, relwidth = 0.3)


        '''=========================================================================='''
        '''=========================================================================='''
        '''=========================================================================='''

        '''-------------------- Label com o nome do dados -----------------------------'''
        
        s.configure('NAME.TLabel',  font=('Calibri', 12))
        #s.configure('Red.TLabel', foreground ='red')
        s.configure('NAME.TLabel', anchor=tk.CENTER)
        s.configure('NAME.TLabel', background='#E5E5E5')
        s.configure('NAME.TLabel', anchor='center')
        s.configure('NAME.TLabel', borderwidth = 0 , relief='groove')
        
        Label_Title_Width = 0.47
        Label_Title_X = 0.54
        self.Periodo = ttk.Label(self.keys,anchor=tk.CENTER, style="NAME.TLabel",)
        self.Periodo['text'] = "Período (s): "
        self.Periodo.place(anchor = "ne", relx = Label_Title_X, rely=space*2*mover, relheight = 0.1, relwidth = Label_Title_Width)
        
        self.Frequencia = ttk.Label(self.keys,anchor=tk.CENTER, style="NAME.TLabel",)
        self.Frequencia['text'] = "Frequência (rad/s): "
        self.Frequencia.place(anchor = "ne", relx = Label_Title_X, rely=space*3*mover, relheight = 0.1, relwidth = Label_Title_Width)
        
        self.Ganho_dB = ttk.Label(self.keys,anchor=tk.CENTER, style="NAME.TLabel",)
        self.Ganho_dB['text'] = "Ganho (dB): "
        self.Ganho_dB.place(anchor = "ne", relx = Label_Title_X, rely=space*4*mover, relheight = 0.1, relwidth = Label_Title_Width)
        
        self.Phase = ttk.Label(self.keys,anchor=tk.CENTER, style="NAME.TLabel",)
        self.Phase['text'] = "Fase (º): "
        self.Phase.place(anchor = "ne", relx = Label_Title_X, rely=space*5*mover, relheight = 0.1, relwidth = Label_Title_Width)
        

        
        s.configure('TButton', font=('Calibri', 12))
        s.configure('TButton', foreground="blue")
        
        buttonEnter = ttk.Button(self.keys, text = "Enter", command = lambda: self.update_data())
        buttonEnter.place(anchor ="n", rely = 0.88, relx = 0.5, relwidth = 0.2, relheight = 0.1)
        
        buttonFile = ttk.Button(self.keys, text = "Browser File", command = lambda: self.get_file_adress())
        buttonFile.place(anchor ="n", rely = 0.14, relx = 0.5, relwidth = 0.4, relheight = 0.1)
        
        Quit_button = tk.Button(self.keys, text="Quit", fg='#f00', command=self.close_windows)
        #Quit_button.place(anchor ="n", rely = 0.88, relx = 0.2, relwidth = 0.2, relheight = 0.1)

    
    def update_data(self):
        self.DF = pd.read_csv(self.file_name)
        self.time_sample = float(self.Sample_time_entry_box.get())/1000
        self.peak_value_time()
        self.myLabelT['text'] = round(self.period,5)
        self.myLabelF['text'] = round(self.frequency,5)
        self.myLabelG['text'] = round(self.gain,5)
        self.myLabelP['text'] = round(self.phase,5)


        
    def peak_value_time(self):
        peak_Y = self.DF["Y"][0]
        time_Y = 0
        
        peak_Y2 = 0
        time_Y2 = 0
        
        peak_U = self.DF["U"][0]
        time_U = 0
        
        peak_U2 = 0
        time_U2 = 0
        diferenca1 = -1
        
        
        # Determina diferença de picos
        '''----------------------------------------------------------------'''
        
        for i in range(self.DF["Y"].size-2):
            if abs(peak_Y - self.DF["Y"][i]) > diferenca1:
                diferenca1  = abs(peak_Y - self.DF["Y"][i])
            
            else:
                peak_Y = self.DF["Y"][i-1]
                time_Y = i-1
                diferenca1 = -1
                peak_Y2 = peak_Y
                
                while i < (self.DF["Y"].size-2):
                    if abs(peak_Y2 - self.DF["Y"][i]) > diferenca1:
                        diferenca1  = abs(peak_Y2 - self.DF["Y"][i])
                    else:
                        peak_Y2 = self.DF["Y"][i-1]
                        time_Y2 = i-1
                        break
                    i+=1
                break
            
        '''----------------------------------------------------------------'''
        diferenca1 = -1
        for j in range(self.DF["U"].size-2):
            if abs(peak_U - self.DF["U"][j]) > diferenca1:
                diferenca1  = abs(peak_U - self.DF["U"][j])
            
            else:
                peak_U = self.DF["U"][j-1]
                time_U = j-1
                diferenca1 = -1
                peak_U2 = peak_U
                
                while j < (self.DF["U"].size-2):
                    if abs(peak_U2 - self.DF["U"][j]) > diferenca1:
                        diferenca1  = abs(peak_U2 - self.DF["U"][j])
                    else:
                        peak_U2 = self.DF["U"][j-1]
                        time_U2 = j-1
                        break
                    j+=1
                break
                    
        
        if peak_Y > peak_Y2:
            Y_Upper_Peak = peak_Y
            Y_Lower_Peak = peak_Y2
            Y_Upper_Peak_Time = time_Y
            Y_Lower_Peak_Time = time_Y2
        else:
            Y_Upper_Peak = peak_Y2
            Y_Lower_Peak = peak_Y
            Y_Upper_Peak_Time = time_Y2
            Y_Lower_Peak_Time = time_Y
        
        
        if peak_U > peak_U2:
            U_Upper_Peak = peak_U
            U_Lower_Peak = peak_U2
            U_Upper_Peak_Time = time_U
            U_Lower_Peak_Time = time_U2
        else:
            U_Upper_Peak = peak_U2
            U_Lower_Peak = peak_U
            U_Upper_Peak_Time = time_U2
            U_Lower_Peak_Time = time_U
        
            
        
                
        
        #self.period = time_U2
        self.gain = 20*np.log10(abs(Y_Upper_Peak - Y_Lower_Peak)/abs(U_Upper_Peak - U_Lower_Peak))
        
        self.period = 2*abs(Y_Upper_Peak_Time-Y_Lower_Peak_Time)*self.time_sample
        #self.period = time_Y
        
        self.phase = (360/self.period)*((U_Upper_Peak_Time - Y_Upper_Peak_Time)*self.time_sample)
        
        self.frequency = 2*np.pi/self.period




    def close_windows(self):
        self.master.destroy()
        self.master.quit()
    
    def get_file_adress(self):
        self.file_name = tk.filedialog.askopenfilename()




root = tk.Tk()


root.title("Análise resposta em frequência")
#root.iconbitmap('./Sine.ico')

clas = Second_Screen(root)

'''--------------------- Destroy window function -------------------------'''

'''-----------------------------------------------------------------------'''


root.mainloop()




#print("{}{}".format(nome,sobrenome))

