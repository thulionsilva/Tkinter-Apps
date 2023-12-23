# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:01:14 2023

@author: thuli
"""


HEIGHT = 500
WIDTH = 400
import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
from tkinter import ttk
from scipy.fft import fft, fftfreq


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
        #s.configure('TButton', background="white")

        # buttonPlotSignal = ttk.Button(self.keys, text = "Plot Sine", command = lambda: self.plot_signal())
        # buttonPlotSignal.place(anchor ="n", rely = 0.88, relx = 0.2, relwidth = 0.3, relheight = 0.1)
        
        
        buttonEnter = ttk.Button(self.keys, text = "Enter", command = lambda: self.update_data())
        buttonEnter.place(anchor ="n", rely = 0.88, relx = 0.5, relwidth = 0.2, relheight = 0.1)
        
        
        # buttonPlotFFT = ttk.Button(self.keys, text = "Plot Fourier", command = lambda: self.plot_fft())
        # buttonPlotFFT.place(anchor ="n", rely = 0.88, relx = 0.8, relwidth = 0.3, relheight = 0.1)
        
        
        buttonFile = ttk.Button(self.keys, text = "Browser File", command = lambda: self.get_file_adress(),style="TButton")
        buttonFile.place(anchor ="n", rely = 0.14, relx = 0.5, relwidth = 0.4, relheight = 0.1)
        
        Quit_button = tk.Button(self.keys, text="Quit", fg='#f00', command=self.close_windows)
        #Quit_button.place(anchor ="n", rely = 0.88, relx = 0.2, relwidth = 0.2, relheight = 0.1)

    
    def update_data(self):
        self.DF = pd.read_csv(self.file_name)
        origin, end = self.truncate()
        self.DF = self.DF.iloc[origin:end,:].reset_index()
        self.time_sample = float(self.Sample_time_entry_box.get())/1000
        self.peak_value_time()
        self.myLabelT['text'] = round(self.period,2)
        self.myLabelF['text'] = round(self.frequency,2)
        self.myLabelG['text'] = round(self.gain,2)
        self.myLabelP['text'] = round(self.phase,2)


        
    def peak_value_time(self):

        
        # Determina diferença de picos
        '''----------------------------------------------------------------'''
        #self.DF = self.DF.iloc[-500:,:]

        

        
        phase_U, frequency_U, amplitude_U = self.FF_transform(self.DF["Malha.U"].to_numpy())
        
        phase_Y, frequency_Y, amplitude_Y = self.FF_transform(self.DF["Malha.Y"].to_numpy())
        
        '''----------------------------------------------------------------'''
          

        self.frequency = frequency_U
        
        self.gain = 20*np.log10(amplitude_Y/amplitude_U)
        
        self.period = 2*np.pi/self.frequency
        
        self.phase = phase_Y - phase_U
        
        




    def close_windows(self):
        self.master.destroy()
        self.master.quit()
    
    def get_file_adress(self):
        self.file_name = tk.filedialog.askopenfilename()
        
    def plot_signal(self):
        fig, ax = plt.subplots(2,1)
        ax[0].plot(self.DF["Malha.Y"])
        ax[0].axhline(self.DF["Malha.Y"].max()*self.error)
        ax[0].set_title("malha.Y")
        ax[0].set_ylabel("RPM")
        ax[1].plot(self.DF["Malha.U"])
        ax[1].set_title("malha.U")
        ax[1].set_ylabel("Volts")

    
    def plot_fft(self):
        fig, ax = plt.subplots(2,1)
        x = (fftfreq(self.N, self.time_sample)[:self.N//2])*2*np.pi
        amplitude = 1.0/self.N * np.abs(self.yf[0:self.N//2])
        phase = np.angle(self.yf[0:self.N//2])*180/np.pi + 90
        ax[0].plot(x,amplitude)
        ax[0].set_ylabel("Amplitude")
        ax[1].plot(x,phase)
        ax[1].set_ylabel("Phase")
    
    
    def FF_transform(self, Series):

        self.N = len(Series)

        #calcula a tranformada
        self.yf = fft(Series)
        
        self.xf = (fftfreq(self.N, self.time_sample)[1:self.N//2])*2*np.pi
        
        amplitude=2/self.N*np.max(abs(self.yf[1:self.N//2])) 
        
        frequency_index=np.argmax(abs(self.yf[1:self.N//2])) 
        
        phase = np.angle(self.yf[1:self.N//2])*180/np.pi + 90
        
        phase = round(phase[frequency_index],3)
        
        frequency = self.xf[frequency_index]
        
            
        return phase, frequency, amplitude

    def truncate(self):
            
        self.error = 0.98
        origin_index = 0
        origin_value = 0
        
        while origin_value < self.DF["Malha.Y"].max()*self.error:
            origin_value = self.DF["Malha.Y"].iloc[origin_index]
            origin_index+=1
        
        end_index = -1
        end_value = 0
        
        while end_value < self.DF["Malha.Y"].max()*self.error:
            end_value = self.DF["Malha.Y"].iloc[end_index]
            end_index-=1
            

        return origin_index, end_index


root = tk.Tk()


root.title("Análise resposta em frequência")
#root.iconbitmap('./Sine.ico')

clas = Second_Screen(root)

'''--------------------- Destroy window function -------------------------'''

'''-----------------------------------------------------------------------'''


root.mainloop()




#print("{}{}".format(nome,sobrenome))

