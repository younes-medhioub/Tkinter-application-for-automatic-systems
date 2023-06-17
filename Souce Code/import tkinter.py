import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt
import control as Co
from scipy import signal
from scipy import ndimage
import numba as nb

def Bode(a,b):
        numstr = str(a)
        denumstr = str(b)
        numstrlist = numstr.split(",")
        denumstrlist = denumstr.split(",")
        numstrlist = [int(x) for x in numstrlist]
        denumstrlist = [int(x) for x in denumstrlist]
        sys = Co.tf(numstrlist,denumstrlist)
        m = str(sys)
        body = Co.bode(sys,dB=True, Hz = True)
        empty_label.config(text=m)
        plt.plot(body)
        plt.grid(True)
        plt.show()

def Impulse(a,b):
        
        numstr = str(a)
        denumstr = str(b)
        numstrlist = numstr.split(",")
        denumstrlist = denumstr.split(",")
        numstrlist = [int(x) for x in numstrlist]
        denumstrlist = [int(x) for x in denumstrlist]
        sys = Co.tf(numstrlist,denumstrlist)
        m = str(sys)
        empty_label.config(text=m)
        syst= (numstrlist,denumstrlist)
        temps,amplitude = signal.impulse(syst)
        plt.xlabel('Temps [s]')
        plt.ylabel('Amplitude')
        plt.title('Réponse impulsionnelle')
        plt.figure(1)
        plt.plot(temps,amplitude)
        plt.grid(True , which= 'both')
        plt.show()

def echlon(a,b):
        numstr = str(a)
        denumstr = str(b)
        numstrlist = numstr.split(",")
        denumstrlist = denumstr.split(",")
        numstrlist = [int(x) for x in numstrlist]
        denumstrlist = [int(x) for x in denumstrlist]
        sys = Co.tf(numstrlist,denumstrlist)
        m = str(sys)
        empty_label.config(text=m)
        syst= (numstrlist,denumstrlist)
        temps,amplitude = signal.step(syst)
        plt.xlabel('Temps [s]')
        plt.ylabel('Amplitude')
        plt.title('Réponse indicielle')
        plt.figure(1)
        plt.plot(temps,amplitude)
        plt.grid()
        plt.show()



def niquist(a,b):
        sampleTime = 0.001
        numstr = str(a)
        denumstr = str(b)
        numstrlist = numstr.split(",")
        denumstrlist = denumstr.split(",")
        numstrlist = [int(x) for x in numstrlist]
        denumstrlist = [int(x) for x in denumstrlist]
        sys = Co.tf(numstrlist,denumstrlist)
        mag = Co.nyquist(sys)
        plt.figure(1)
        plt.plot(mag)
        plt.grid()
        plt.show()

       
def Tracez():
        num = numerateur_entry.get()
        denum = denominateur_entry.get()
        nature = Nature_combobox.get()
        Type  = Type_combobox.get()

        if (nature == "Etude temporelle" and Type =="Réponse impulsionnelle"):
         Impulse(num,denum)
        elif(nature == "Etude temporelle"and Type == "Réponse indicielle"):
         echlon(num,denum)
        elif (nature == "Etude frequentielle" and Type =="Bode"):
         Bode(num,denum)
        elif (nature == "Etude frequentielle" and Type =="nyquist"):
          niquist (num,denum)



window = tkinter.Tk()
window.title("APP0")

frame = tkinter.Frame(window)
frame.pack()

# Les paramètres de la fonction de transfert
fonction_de_transfert =tkinter.LabelFrame(frame, text="Fonction de transfert")
fonction_de_transfert.grid(row= 0, column=0, padx=20, pady=10)

numerateur = tkinter.Label(fonction_de_transfert, text="Numérateur")
numerateur.grid(row=0, column=0)
denominateur = tkinter.Label(fonction_de_transfert, text="Dénominateur")
denominateur.grid(row=0, column=1)

numerateur_entry = tkinter.Entry(fonction_de_transfert)
denominateur_entry = tkinter.Entry(fonction_de_transfert)
numerateur_entry.grid(row=1, column=0)
denominateur_entry.grid(row=1, column=1)

Nature_label = tkinter.Label(fonction_de_transfert, text="Nature de l'etude")
Nature_combobox = ttk.Combobox(fonction_de_transfert, values=["Etude temporelle","Etude frequentielle"])
Nature_label.grid(row=2, column=0)
Nature_combobox.grid(row=3, column=0)

Type_label = tkinter.Label(fonction_de_transfert, text="Type de la réponse")
Type_combobox = ttk.Combobox(fonction_de_transfert, values=["Réponse impulsionnelle","Réponse indicielle","Bode","nyquist"])
Type_label.grid(row=2, column=1)
Type_combobox.grid(row=3, column=1)

empty_label0 = tkinter.Label(fonction_de_transfert,text="Votre fonction de transfert est :" )
empty_label0.grid(row= 0, column=2)
empty_label = tkinter.Label(fonction_de_transfert )
empty_label.grid(row= 1, column=2)




for widget in fonction_de_transfert.winfo_children():
    widget.grid_configure(padx=20, pady=15)

# Button
button = tkinter.Button(frame, text="Tracez la croube", command= Tracez)
button.grid(row=3, column=0, sticky="news", padx=5, pady=5)



 
window.mainloop()