import scipy as sp
from scipy import optimize
import matplotlib.pyplot as plt
from abc import abstractstaticmethod
from google.protobuf.internal.python_message import _AddStaticMethods
import numpy as np
from orca.scripts import self_voicing

"""
Höyrynpaine luokan tehtävä on huolehtia tiedostojen lukemisesta...
"""
class Hoyrynpaine:
    
    """
    Lukee datan tekstitiedostosta stringiin
    @param tiedostopolku: Polku, josta luettava tekstitiedosto löytyy
    @return rivit: Palauttaa rivit listan, jossa jokainen listan alkio on yksi tekstitiedostonrivi
    """
    @staticmethod
    def lueDataTiedostosta(tiedostopolku):
        mode = 'r' #'r' = read, 'w' = write, 'a' = append
        with open(tiedostopolku, mode, encoding='utf8') as tiedosto:
            rivit = tiedosto.readlines() #read() lukee kokotiedoston stringiin #readline() lukee tiedoston riviriviltä ja palauttaa stringeinä #readlines() lukee kaikki rivit ja palauttaa string taulukkona
            return rivit
    
    """
    Konstruktori alustaa mittauksen tiedostopolusta löytyvien tiedostojen mukaan
    @param tiedostopolku: Pilku, josta luettavat tekstitiedostot löytyy
    """
    def __init__(self, tiedostopolku):
        self.tiedostopolku = tiedostopolku
        
        self.pallo
        self.__alustaEristePallo()
        
        self.vedenMassa = []
        
        self.astianMassa = []
        self.huoneenlämpötila = []
        
        self.vedenJaAstianMassa = []
        
        self.astianMassa = 0;
        self.vedenMassa = []
        self.vedenMassa_err = []
        
        self.wh_alussa = []
        self.wh_lopussa = []
        self.wh_kulutus = []
        self.wh_kulutus_err = []
        self.alustaSuoraMittaus()
        self.suoraMittaus = SuoraMittaus(self.vedenMassa, self.wh_kulutus)
        
        self.epaSuoraMittaus = EpasuoraMittaus()
    
    """
    Alustaa eristePallon, jonka tiedot on tekstitiedostossa suoraMittausEristePallo.txt. Alla tekstitiedoston esimerkki rakenne. Kaksi ekaa saraketta ovat ohjelman toiminnan kannalta oleellisia. Kolmas sarake on vain esimerkin vuoksi kertomassa mitä yksikköä tulisi käyttää.
        pullonTilavuus    4    l
        pullonTilavuus_err    0.1    l
        pullonYmparysMitta    10    cm
        pullonYmparysMitta_err 5    cm
    """    
    def __alustaEristePallo(self):
        data = self.lueDataTiedostosta(self.tiedostopolku + "suoraMittausEristePallo.txt")
        for rivi in data:
            rivi = rivi.split()
            
            match rivi[0]:
                case "pullonTilavuus":
                    pullonTilavuus = float(rivi[1])
                case "pullonTilavuus_err":
                    pullonTilavuus_err = float(rivi[1])
                case "pullonYmparysMitta":
                    pullonYmparysMitta = float(rivi[1])
                case "pullonYmparysMitta_err":
                    pullonYmparysMitta_err = float(rivi[1])
                case _:
                    print("Tiedostosta suoraMittausEristePallo.txt ylimääräinen rivi")
            
        self.pallo = EristePallo(pullonTilavuus, pullonTilavuus_err, pullonYmparysMitta, pullonYmparysMitta_err)
        
    def alustaSuoraMittaus(self):
        data = self.lueDataTiedostosta(self.tiedostopolku + "suoraMittaus.txt")
        for rivi in data:
            rivi = rivi.split()
            
            self.wh_alussa.append(float(rivi[0]))
            self.wh_lopussa.append(float(rivi[1]))
            self.wh_kulutus.append(float(rivi[1])-float(rivi[2]))
            
            self.vedenJaAstian_massa.append(float(rivi[2]))
                

"""
    Mittauksessa käytetyn eristepallon ominaisuudet
    @param pullonTilavuus: Pullon tilavuus litroina
    @param pullonTilavuus_err: Pullon tilavuuden virhe litroina
    @param pullonYmparysMitta: Pullon ympärysmitta senttimetreinä
    @param pullonYmparysMitta_err: Pullon ympärysmitan virhe senttimetreinä
"""
class EristePallo:
    def __init__(self, pullonTilavuus, pullonTilavuus_err, pullonYmparysMitta, pullonYmparysMitta_err):
        self.pullonTilavuus = pullonTilavuus
        self.pullonTilavuus_err = pullonTilavuus_err
        self.pullonYmparysMitta = pullonYmparysMitta
        self.pullonYmparysMitta_err = pullonYmparysMitta_err
        
        self.eristeenPaksuus = 

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

"""
Luokka suoralle mittaukselle
"""     
class SuoraMittaus(Mittaus):
    
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
    def __init__(self, x, y, x_err, y_err):
        super().__init__(x, y, x_err, y_err, eristePallo, huoneenLampotila)
        
        self.popt_painottamaton, self.pcov_painottamaton = sp.optimize.curve_fit(SuoraMittaus.suoranykoordinaatti, x, y) #painottamaton sovitus
        self.popt_painotettu_suhteellinenVirhe, self.pcov_painotettu_suhteellinenVirhe = sp.optimize.curve_fit(SuoraMittaus.suoranykoordinaatti, x, y, sigma=y_err, absolute_sigma=False) #painotettu sovitus vain sigmojen suhteellisella suuruudella väliä
        self.popt_painotettu_absoluuttinenVirhe, self.pcov_painotettu_absoluuttinenVirhe = sp.optimize.curve_fit(SuoraMittaus.suoranykoordinaatti, x, y, sigma=y_err, absolute_sigma=True) #painotettu sovitus sigmojen absoluuttisella suuruudella väliä
    
        self.painottamatonKuvaaja = self.muodostaKuvaaja(self.popt_painottamaton[0], self.popt_painottamaton[1], np.sqrt(self.pcov_painottamaton[0][0]), np.sqrt(self.pcov_painottamaton[1][1]))
        self.painotettuKuvaaja_suhteellinenVirhe = self.muodostaKuvaaja(self.popt_painotettu_suhteellinenVirhe[0], self.popt_painotettu_suhteellinenVirhe[1], np.sqrt(self.pcov_painotettu_suhteellinenVirhe[0][0]), np.sqrt(self.pcov_painotettu_suhteellinenVirhe[1][1]))
        self.painotettuKuvaaja_absoluuttinenVirhe = self.muodostaKuvaaja(self.popt_painotettu_absoluuttinenVirhe[0], self.popt_painotettu_absoluuttinenVirhe[1], np.sqrt(self.pcov_painotettu_absoluuttinenVirhe[0][0]), np.sqrt(self.pcov_painotettu_absoluuttinenVirhe[1][1]))
        
    def muodostaKuvaaja(self, a, b, a_err, b_err):
        #def plottaaSuoraMittaus(x1_values, y1_values,a,b,a_err,b_err,kuvanPolku):
        kuvaaja = plt.figure()
        
        plt.errorbar(self.x, self.y, yerr=self.y_err, xerr=self.x_err, label="Mittauspisteet")
        
        x_line = np.arange(min(self.x), max(self.x), 0.0001)
        y_line = SuoraMittaus.suoranykoordinaatti(x_line, a, b)
        
        plt.plot(x_line, y_line, '-', color='red', label='Sovitetty käyrä:')
        
        plt.xlabel('Veden massa (kg)')
        plt.ylabel('Energia (kJ)')
        plt.title('Painotettu sovitus suhteellisilla virheillä:\nEnergia höyrystyneen veden massan funktiona.')
        #Plotataan tyhjä käyrä, jotta saadaan legend kuntoon
        plt.plot([], [], ' ', label=f"Q = L*m + Q\u2080\nL = {a:.5f} \u00B1 {a_err:.5f}\nQ\u2080 = {b:.5f} \u00B1 {b_err:.5f}")
        plt.legend()
        #plt.savefig(kuvanPolku)
        #plt.show()
        return kuvaaja
    
class EpasuoraMittaus(Mittaus):
    
    @staticmethod
    def epasuoranFunktionykoordinaatti(T, a, b):
        P_0=101.325 #TODO nämä olisi hyvä laittaa parametrina
        T_0=373.15 #TODO nämä olisi hyvä laittaa parametrina
        return P_0*(T/T_0)**b*e**(a*(1/T_0-1/T))
    
    """
    Epäsuoran mittauksen konstruktori
    @param x: Lista mittauksen x-koordinaateista
    @param y: Lista mittauksen y-koordinaateista
    @param x_err: Lista mittauksen x-koordinaatteihin liittyvistä virheistä
    @param y_err: Lista mittauksen y-koordinaatteihin liittyvistä virheistä  
    """
    def __init__(self, x, y, x_err, y_err):
        super().__init__(x, y, x_err, y_err)
        self.popt_painottamaton, self.pcov_painottamaton = sp.optimize.curve_fit(EpasuoraMittaus.epasuoranFunktionykoordinaatti, x, y) #painottamaton sovitus
        self.popt_painotettu_suhteellinenVirhe, self.pcov_painotettu_suhteellinenVirhe = sp.optimize.curve_fit(EpasuoraMittaus.epasuoranFunktionykoordinaatti, x, y, sigma=y_err, absolute_sigma=False) #painotettu sovitus vain sigmojen suhteellisella suuruudella väliä
        self.popt_painotettu_absoluuttinenVirhe, self.pcov_painetettu_absoluuttinenVirhe = sp.optimize.curve_fit(EpasuoraMittaus.epasuoranFunktionykoordinaatti, x, y, sigma=y_err, absolute_sigma=True) #painotettu sovitus sigmojen absoluuttisella suuruudella väliä
    """
    def sovitaSuora(self):
       """ 
"""        
class Kuvaaja:
    
    def __init__(self):
"""

print(f"Toimii ainakin vielä")
ekaMittaus = SuoraMittaus([0,1,2,3], [0,1,2,3], [0,0,0,0], [0.1,0.1,0.1,0.1])
plt.show()