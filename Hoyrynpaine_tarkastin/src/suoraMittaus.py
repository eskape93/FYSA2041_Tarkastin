'''
Created on Mar 30, 2023

@author: esa
'''

import mittaus
import scipy as sp
from scipy import optimize
import numpy as np

"""
Luokka suoralle mittaukselle
"""     
class SuoraMittaus(mittaus.Mittaus):
    
    """
    Laskee suoran y-koordinaatin, kun suoran x-koordinaatti, kulmakerroin ja vakiotermi on annettu
    @param x: suoran x-koordinaatti
    @param a: suoran kulmakerroin
    @param b: suoran vakiotermi 
    @return suoran y-koordinaatti
    """
    @staticmethod
    def suoranykoordinaatti(x, a, b):
        return a * x + b
    
    """
    Suoran mittauksen konstruktori
    @param x: Lista mittauksen x-koordinaateista
    @param y: Lista mittauksen y-koordinaateista
    @param x_err: Lista mittauksen x-koordinaatteihin liittyvistä virheistä
    @param y_err: Lista mittauksen y-koordinaatteihin liittyvistä virheistä  
    """
    def __init__(self, x, y, x_err, y_err, eristePallo, huoneenLampotila):
        super().__init__(x, y, x_err, y_err)
        
        self.popt_painottamaton, self.pcov_painottamaton = sp.optimize.curve_fit(SuoraMittaus.suoranykoordinaatti, x, y) #painottamaton sovitus
        self.popt_painotettu_suhteellinenVirhe, self.pcov_painotettu_suhteellinenVirhe = sp.optimize.curve_fit(SuoraMittaus.suoranykoordinaatti, x, y, sigma=y_err, absolute_sigma=False) #painotettu sovitus vain sigmojen suhteellisella suuruudella väliä
        self.popt_painotettu_absoluuttinenVirhe, self.pcov_painotettu_absoluuttinenVirhe = sp.optimize.curve_fit(SuoraMittaus.suoranykoordinaatti, x, y, sigma=y_err, absolute_sigma=True) #painotettu sovitus sigmojen absoluuttisella suuruudella väliä
    
        self.painottamatonKuvaaja = self.muodostaKuvaaja(self.popt_painottamaton[0], self.popt_painottamaton[1], np.sqrt(self.pcov_painottamaton[0][0]), np.sqrt(self.pcov_painottamaton[1][1]))
        self.painotettuKuvaaja_suhteellinenVirhe = self.muodostaKuvaaja(self.popt_painotettu_suhteellinenVirhe[0], self.popt_painotettu_suhteellinenVirhe[1], np.sqrt(self.pcov_painotettu_suhteellinenVirhe[0][0]), np.sqrt(self.pcov_painotettu_suhteellinenVirhe[1][1]))
        self.painotettuKuvaaja_absoluuttinenVirhe = self.muodostaKuvaaja(self.popt_painotettu_absoluuttinenVirhe[0], self.popt_painotettu_absoluuttinenVirhe[1], np.sqrt(self.pcov_painotettu_absoluuttinenVirhe[0][0]), np.sqrt(self.pcov_painotettu_absoluuttinenVirhe[1][1]))