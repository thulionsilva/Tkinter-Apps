# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:01:14 2023

pyinstaller --onefile --icon=Sine.ico Bode_Plot_Genarator.py -w
pyinstaller --icon=Sine.ico Bode_Plot_Genarator.py -w
path\\to\\pyinstaller.exe --onefile --paths path\\to\\venv\\Lib\\site-packages file.py

@author: thuli
"""


HEIGHT = 500
WIDTH = 900
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
from tkinter import ttk
from scipy.fft import fft, fftfreq

class Main_Screen:
    def __init__(self, master):
        
        self.Bode = pd.DataFrame(columns=["Frequency (rad/s)", "Gain (dB)", "Phase (º)"])
        self.folder_name = None
        self.master = master
        self.size = tk.Canvas(self.master, height = HEIGHT, width = WIDTH)
        self.size.pack()
        s = ttk.Style()
        s.configure('TFrame', relief="groove", background="#F0F0F0")


        
        self.keys = ttk.Frame(self.master, style="TFrame")
        self.keys.place(relx = 0.05, rely = 0.05, relheight = 0.755, relwidth = 0.35)

        self.progress = ttk.Frame(self.master, style="TFrame")
        self.progress.place(relx = 0.05, rely = 0.84, relheight = 0.1, relwidth = 0.9)
        
        self.data_frame = ttk.Frame(self.master, style="TFrame")
        self.data_frame.place(relx = 0.42, rely = 0.05, relheight = 0.755, relwidth = 0.53)

        self.Output_info = tk.Text(self.master, state = "disabled",borderwidth=1,relief="ridge")
        self.Output_info.place(anchor="nw", relx = 0.42, rely = 0.05, relheight = 0.755, relwidth = 0.53)



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
        
        self.Sample_time = ttk.Label(self.keys, style="W.TLabel")

        self.Sample_time['text'] = "Sampling Time (ms): "
        self.Sample_time.place(anchor = "w", relx = 0.05, rely=0.05, relheight = 0.09, relwidth = 0.55)

        '''Caixa para a entrada do tempo de amostra dos dados '''
        
        s.configure('W.TEntry', font=('Calibri', 15))
        s.configure('W.TEntry', background = "#F0F0F0",bd = 10)
        self.Sample_time_entry_box = ttk.Entry(self.keys,style="W.TEntry")
        self.Sample_time_entry_box.place(anchor = "w", relx = 0.6, rely=0.05, relheight = 0.07, relwidth = 0.3)


        '''=========================================================================='''
        '''=========================================================================='''
        '''=========================================================================='''

        '''-------------------- Label com o nome do dados -----------------------------'''
        
        s.configure('NAME.TLabel',  font=('Calibri', 12))
        s.configure('NAME.TLabel', anchor=tk.CENTER)
        s.configure('NAME.TLabel', background='#E5E5E5')
        s.configure('NAME.TLabel', anchor='center')
        s.configure('NAME.TLabel', borderwidth = 0 , relief='groove')
        
        Label_Title_Width = 0.47
        Label_Title_X = 0.54
        self.Periodo = ttk.Label(self.keys,anchor=tk.CENTER, style="NAME.TLabel",)
        self.Periodo['text'] = "Period (s): "
        self.Periodo.place(anchor = "ne", relx = Label_Title_X, rely=space*2*mover, relheight = 0.1, relwidth = Label_Title_Width)
        
        self.Frequencia = ttk.Label(self.keys,anchor=tk.CENTER, style="NAME.TLabel",)
        self.Frequencia['text'] = "Frequency (rad/s): "
        self.Frequencia.place(anchor = "ne", relx = Label_Title_X, rely=space*3*mover, relheight = 0.1, relwidth = Label_Title_Width)
        
        self.Ganho_dB = ttk.Label(self.keys,anchor=tk.CENTER, style="NAME.TLabel",)
        self.Ganho_dB['text'] = "Gain (dB): "
        self.Ganho_dB.place(anchor = "ne", relx = Label_Title_X, rely=space*4*mover, relheight = 0.1, relwidth = Label_Title_Width)
        
        self.Phase = ttk.Label(self.keys,anchor=tk.CENTER, style="NAME.TLabel",)
        self.Phase['text'] = "Phase (º): "
        self.Phase.place(anchor = "ne", relx = Label_Title_X, rely=space*5*mover, relheight = 0.1, relwidth = Label_Title_Width)
        

        s.configure('TButton', font=('Calibri', 12))
        s.configure('TButton', foreground="blue")

        #buttonPlotSignal = ttk.Button(self.progress, text = "Plot Sine", command = lambda: self.plot_signal())
        #buttonPlotSignal.place(anchor ="w", rely = 0.5, relx = 0.05, relwidth = 0.15, relheight = 0.7)
        
        
        buttonEnter = ttk.Button(self.keys, text = "Enter", command = lambda: self.update_data())
        buttonEnter.place(anchor ="n", rely = 0.867, relx = 0.5, relwidth = 0.25, relheight = 0.1)
        
        
        #buttonPlotFFT = ttk.Button(self.progress, text = "Plot Fourier", command = lambda: self.plot_fft())
        #buttonPlotFFT.place(anchor ="w", rely = 0.5, relx = 0.8, relwidth = 0.15, relheight = 0.7)

        buttonBodePlot = ttk.Button(self.progress, text = "Bode Plot", command = lambda: self.bode_plot())
        buttonBodePlot.place(anchor ="w", rely = 0.5, relx = 0.8, relwidth = 0.15, relheight = 0.7)
        
        
        buttonFile = ttk.Button(self.keys, text = "Input File", command = lambda: self.get_file_adress(),style="TButton")
        buttonFile.place(anchor ="n", rely = 0.14, relx = 0.3, relwidth = 0.4, relheight = 0.1)
        
        buttonFile = ttk.Button(self.keys, text = "Output Folder", command = lambda: self.get_folder_adress(),style="TButton")
        buttonFile.place(anchor ="n", rely = 0.14, relx = 0.7, relwidth = 0.4, relheight = 0.1)

        s.configure('R.TButton',foreground='red', bd = 10)

        Quit_button = ttk.Button(self.progress, text="Quit",style='R.TButton', command=self.close_windows)
        Quit_button.place(anchor ="center", rely = 0.5, relx = 0.5, relwidth = 0.15, relheight = 0.7)

        s.configure('G.TButton',foreground='green', bd = 10)
        Export_button = ttk.Button(self.progress, text="Export",style='G.TButton', command=self.export_Bode)
        Export_button.place(anchor ="w", rely = 0.5, relx = 0.05, relwidth = 0.15, relheight = 0.7)

    
    def update_data(self):
        
        if self.Sample_time_entry_box.get() != "":
            for file in self.file_names:
                self.DF = pd.read_csv(file)
                self.time_sample = float(self.Sample_time_entry_box.get())/1000
                origin, end = self.truncate()
                self.DF = self.DF.iloc[origin:end,:].reset_index()
                self.peak_value_time()
                self.myLabelT['text'] = round(self.period,2)
                self.myLabelF['text'] = round(self.frequency,2)
                self.myLabelG['text'] = round(self.gain,2)
                self.myLabelP['text'] = round(self.phase,2)
                self.concat()
        else:
            self.Output_info.config(state="normal")
            self.Output_info.insert("end", "Please type sampling time in miliseconds \n") 
            self.Output_info.config(state="disabled")
    
    def concat(self):
        
        if self.phase <= 0:
            self.Bode.loc[len(self.Bode)] = [round(self.frequency,2), round(self.gain,2), round(self.phase,2)]

            self.Bode.sort_values(by="Frequency (rad/s)", inplace=True)
            self.Output_info.config(state="normal")
            self.Output_info.delete("1.0","end")
            self.Output_info.insert("end", f"{self.Bode} \n") 
            self.Output_info.config(state="disabled")


        
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

    def export_Bode(self):
        if self.folder_name != None: #Only export if a folder is selected
            try:
                datatoexcel = pd.ExcelWriter('{}\\Bode_Plot.xlsx'.format(self.folder_name)) #Destiny file path

                self.Output_info.config(state="normal") 
                self.Output_info.insert("end", "Export Sucessful \n") 
                self.Output_info.insert("end", 'File path> {}\\Bode_Plot.xlsx \n'.format(self.folder_name)) 
                self.Output_info.config(state="disabled")
                self.Bode.to_excel(datatoexcel, index=False) 
                datatoexcel.close()
            except Exception as e:  
                self.Output_info.config(state="normal") 
                self.Output_info.insert("end", f"Export Failed {e}\n") 
                self.Output_info.config(state="disabled")

            self.Bode = pd.DataFrame(columns=["Frequency (rad/s)", "Gain (dB)", "Phase (º)"]) #Reset dataframe
        else:
            self.Output_info.config(state="normal") 
            self.Output_info.insert("end", "Please select a folder\n") 
            self.Output_info.config(state="disabled")

    
    def get_file_adress(self):
        self.file_names = tk.filedialog.askopenfilenames()
    
    def get_folder_adress(self):
        self.folder_name = tk.filedialog.askdirectory()
        self.Output_info.config(state="normal") 
        self.Output_info.insert("end", f"{self.folder_name} \n") 
        self.Output_info.config(state="disabled")
        
    def plot_signal(self):
        fig, ax = plt.subplots(2,1)
        ax[0].plot(self.DF["Malha.Y"])
        ax[0].axhline(self.DF["Malha.Y"].max()*self.error)
        ax[0].set_title("malha.Y")
        ax[0].set_ylabel("RPM")
        ax[1].plot(self.DF["Malha.U"])
        ax[1].set_title("malha.U")
        ax[1].set_ylabel("Volts")
        fig.tight_layout()
        #fig.subplots_adjust(wspace=2)
        toplevel = tk.Toplevel(self.master, height=600, width=800)
        canvas = FigureCanvasTkAgg(fig, master=toplevel)
        canvas.get_tk_widget().pack()
        canvas.draw()

    
    def plot_fft(self):
        fig, ax = plt.subplots(2,1,figsize=(10,7))
        x = (fftfreq(self.N, self.time_sample)[:self.N//2])*2*np.pi
        amplitude = 1.0/self.N * np.abs(self.yf[0:self.N//2])
        phase = np.angle(self.yf[0:self.N//2])*180/np.pi + 90
        ax[0].plot(x,amplitude)
        ax[0].set_ylabel("Amplitude")
        ax[0].set_xlabel("Frequency (rad/s)")
        ax[1].set_xlabel("Frequency (rad/s)")
        ax[1].plot(x,phase)
        ax[1].set_ylabel("Phase (º)")
        fig.tight_layout()

        toplevel = tk.Toplevel(self.master)
        canvas = FigureCanvasTkAgg(fig, master=toplevel)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, toplevel)
        toolbar.update()

    def bode_plot(self):
        #fig, ax = plt.subplots(2,1,figsize=(10,7))
        fig, ax = plt.subplots(2,1)
        fig.suptitle("Bode Diagram")
        x = self.Bode["Frequency (rad/s)"]
        gain = self.Bode["Gain (dB)"]
        phase = self.Bode["Phase (º)"]
        ax[0].plot(x,gain)
        ax[0].set_ylabel("Gain (dB)")
        ax[0].set_xscale('log')
        ax[0].set_xlabel("Frequency (rad/s)")
        ax[1].set_xlabel("Frequency (rad/s)")
        ax[1].plot(x,phase)
        ax[1].set_ylabel("Phase (º)")
        ax[1].set_xscale('log')
        fig.tight_layout()

        toplevel = tk.Toplevel(self.master)
        canvas = FigureCanvasTkAgg(fig, master=toplevel)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, toplevel)
        toolbar.update()

    
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


root.title("Bode Diagram Genarator")
root.iconbitmap('C:\\Users\\thuli\\OneDrive\\Área de Trabalho\\Tkinter Programs\\Sine.ico')

clas = Main_Screen(root)

root.mainloop()


