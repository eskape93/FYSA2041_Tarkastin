'''
Created on May 18, 2023

@author: esa
'''

import tkinter as tk
from tkinter import *
from tkinter import ttk

def avaaSuoranMittauksenIkkuna(root1):
    suoramittausIkkuna = Toplevel(root1)
    #suoramittausIkkuna = Tk()
    suoramittausIkkuna.title("Suoran mittauksen data")
    
    mainframeSuoramittaus = ttk.Frame(suoramittausIkkuna, width=1600, height=800)
    mainframeSuoramittaus.grid(column=0, row=0)
    
    suoraMittausDataFrame = ttk.Frame(mainframeSuoramittaus, padding=(3,3,12,12))
    suoraMittausDataFrame.grid(column=0, row=0)
    
    suoramittausMuutFrame = ttk.Frame(mainframeSuoramittaus, padding=(3,3,12,12))
    suoramittausMuutFrame.grid(column=0, row=1)
    
    suoramittausPainikkeetFrame = ttk.Frame(mainframeSuoramittaus, padding=(3,3,12,12))
    suoramittausPainikkeetFrame.grid(column=0, row=2)
    
    kwhAlussa = []
    kwhAlussa_err = []
    kwhLopussa = []
    kwhLopussa_err = []
    vedenJaAstianMassa = []
    vedenJaAstianMassa_err = []
    #padding=(3,3,12,12)
    
    ttk.Label(suoraMittausDataFrame, text="Nr.").grid(column=0, row=0)
    ttk.Label(suoraMittausDataFrame, text="Wh-alussa").grid(column=1, row=0)
    ttk.Label(suoraMittausDataFrame, text="Virhe (wh)").grid(column=2, row=0)
    ttk.Label(suoraMittausDataFrame, text="Wh-lopussa").grid(column=3, row=0)
    ttk.Label(suoraMittausDataFrame, text="Virhe (wh)").grid(column=4, row=0)
    ttk.Label(suoraMittausDataFrame, text="Vesi + astia massa (g)").grid(column=5, row=0)
    ttk.Label(suoraMittausDataFrame, text="Virhe (g)").grid(column=6, row=0)
    
    
    for i in range(0, 9, 1):
        ttk.Label(suoraMittausDataFrame, text=str(i+1) + ".").grid(column=0, row=i+1)
        
        kwhAlussa.append(ttk.Entry(suoraMittausDataFrame, textvariable=StringVar()))
        kwhAlussa[i].grid(column=1, row=i+1)
        
        kwhAlussa_err.append(ttk.Entry(suoraMittausDataFrame, textvariable=StringVar()))
        kwhAlussa_err[i].grid(column=2, row=i+1)
        
        kwhLopussa.append(ttk.Entry(suoraMittausDataFrame, textvariable=StringVar()))
        kwhLopussa[i].grid(column=3, row=i+1)
        
        kwhLopussa_err.append(ttk.Entry(suoraMittausDataFrame, textvariable=StringVar()))
        kwhLopussa_err[i].grid(column=4, row=i+1)
        
        vedenJaAstianMassa.append(ttk.Entry(suoraMittausDataFrame, textvariable=StringVar()))
        vedenJaAstianMassa[i].grid(column=5, row=i+1)
        
        vedenJaAstianMassa_err.append(ttk.Entry(suoraMittausDataFrame, textvariable=StringVar()))
        vedenJaAstianMassa_err[i].grid(column=6, row=i+1)
        
    ttk.Label(suoramittausMuutFrame, text="Huoneenlämpötila (\u00B0C)").grid(column=0, row=0)
    ttk.Label(suoramittausMuutFrame, text="Virhe (\u00B0C)").grid(column=1, row=0)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=0, row=1)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=1, row=1)
    
    ttk.Label(suoramittausMuutFrame, text="Astian massa (g)").grid(column=0, row=2)
    ttk.Label(suoramittausMuutFrame, text="Virhe (g)").grid(column=1, row=2)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=0, row=3)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=1, row=3)
    
    ttk.Label(suoramittausMuutFrame, text="Aika (s)").grid(column=2, row=0)
    ttk.Label(suoramittausMuutFrame, text="Virhe (s)").grid(column=3, row=0)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=2, row=1)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=3, row=1)
    
    ttk.Label(suoramittausMuutFrame, text="Tilavuus (l)").grid(column=2, row=2, columnspan=2)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=2, row=3, columnspan=2)
    #ttk.Label(suoramittausMuutFrame, text="Huoneenlämpötila (\u00B0C)").grid(column=0, row=0)
    #ttk.Label(suoramittausMuutFrame, text="Virhe (\u00B0C)").grid(column=1, row=0)
    
    
    
    ttk.Label(suoramittausMuutFrame, text="Ympärysmitta (cm)").grid(column=5, row=0)
    
    ttk.Label(suoramittausMuutFrame, text="1.").grid(column=4, row=1, sticky=(E))
    ttk.Label(suoramittausMuutFrame, text="2.").grid(column=4, row=2, sticky=(E))
    ttk.Label(suoramittausMuutFrame, text="3.").grid(column=4, row=3, sticky=(E))
    
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=5, row=1)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=5, row=2)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=5, row=3)
    
    ttk.Label(suoramittausMuutFrame, text="Virhe (cm)").grid(column=6, row=0)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=6, row=1)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=6, row=2)
    ttk.Entry(suoramittausMuutFrame, textvariable=StringVar()).grid(column=6, row=3)
    
    ttk.Button(suoramittausPainikkeetFrame, text='Ok').grid(column=0, row=0)
    ttk.Button(suoramittausPainikkeetFrame, text='Peruuta').grid(column=1, row=0)
"""
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
"""
#Sets up main application windows
root = Tk()
root.title("Höyrynpaine")

#Mainframe widget
mainframe = ttk.Frame(root, width=1600, height=800)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#root.columnconfigure(0, weight=1)
#root.rowconfigure(0, weight=1)

suoramittausKuvaFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=300, height=300)
suoramittausKuvaFrame.grid(column=0, row=0)

epasuoramittausKuvaFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=300, height=300)
epasuoramittausKuvaFrame.grid(column=1, row=0)

suoramittausArvotFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=300, height=300)
suoramittausArvotFrame.grid(column=0, row=1)

epasuoramittausArvotFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge", width=300, height=300)
epasuoramittausArvotFrame.grid(column=1, row=1)

suoramittausDataButton = ttk.Button(mainframe, text="Suoran mittauksen data", command=lambda: avaaSuoranMittauksenIkkuna(root))
suoramittausDataButton.grid(column=0, row=2)

#suoramittausLabel = ttk.Label(mainframe, text='Suoramittaus', width=100)
#suoramittausLabel.grid(column=0, row=0, sticky=(N, W, E, S))

#epasuoramittausLabel = ttk.Label(mainframe, text='Epäsuoramittaus', width=100)
#epasuoramittausLabel.grid(column=1, row=0, sticky=(N, W, E, S))

#Create entry widget
#feet = StringVar()
#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

#Creating the remaining widgets
#meters = StringVar()
#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

#ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#for child in mainframe.winfo_children(): 
#    child.grid_configure(padx=5, pady=5)

#feet_entry.focus()
#root.bind("<Return>", calculate)


root.mainloop()