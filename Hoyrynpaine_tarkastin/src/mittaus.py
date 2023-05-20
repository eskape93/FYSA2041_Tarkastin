'''
Created on Mar 30, 2023

@author: esa
'''

import matplotlib.pyplot as plt
from matplotlib.pyplot import legend

"""
    Yleinen mittausLuokka, jossa mitattu x ja y sekä niiden virheet
"""
class Mittaus:
    
    """
    Mittauksen konstruktori
    @param x: Lista mittauksen x-koordinaateista
    @param y: Lista mittauksen y-koordinaateista
    @param x_err: Lista mittauksen x-koordinaatteihin liittyvistä virheistä
    @param y_err: Lista mittauksen y-koordinaatteihin liittyvistä virheistä  
    """
    def __init__(self, x, y, x_err, y_err):
        if(len(x) != len(y) != len(x_err) != len(y_err)):
            raise ValueError(f"Listat eivät ole samankokoisia len(x) = {len(x)}, len(y) = {len(y)}, len(x_err) = {len(x_err)}, len(y_err) = {len(y_err)}")
        self.x = x
        self.y = y
        self.x_err = x_err
        self.y_err = y_err
        
        self.fig, self.ax = plt.subplots()
    
    """
    Muodostaa scatter-kuvaajan mittauspisteistä
    @param title: Kuvaajan otsikko (string)
    @param xlabel: x-akselin otsikko (string)
    @param ylabel: y-akselin otsikko (string)
    @param legend: Jos legendiin halutaan kirjottaa jotain ylimääräistä, voidaan se tehdä tämän parametrin avulla. (string)    
    """    
    def muodostaKuvaaja(self, title="Kuvaaja", xlabel="x-akseli", ylabel="y-akseli", legend = ""):
        self.ax.errorbar(self.x, self.y, yerr=self.y_err, xerr=self.x_err, label="Mittauspisteet")
        
        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel)
        self.ax.set_title(title)
        
        #Plotataan tyhjä käyrä, jotta saadaan legend kuntoon
        self.ax.plot([], [], ' ', label=legend)
        self.ax.legend()
    
    """
    """
    def lisaaKuvaajaanSovitettuKayra(self, x_line, y_line):
        self.ax.plot(x_line, y_line, '-', color='red', label='Sovitetty käyrä:')
        
def main():
    x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x_err=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    y_err=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    mittaus = Mittaus(x, y, x_err, y_err)
    mittaus.muodostaKuvaaja()
    plt.show()
    
main()
